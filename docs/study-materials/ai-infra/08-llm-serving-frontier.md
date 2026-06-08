# 08. LLM Serving 前沿系统

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 前沿 / 系统 / 实践 |
| 难度 | 进阶到前沿 |
| 优先级 | P0 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 系统理解 LLM serving 的前沿架构、调度、KV Cache 与工程实践 |

---

> 目标：集中整理 LLM Serving 的前沿系统问题。主线不是“哪个框架最快”，而是：**请求如何排队、KV Cache 如何管理、prefill / decode 如何隔离、SLO 如何稳定、长上下文和 MoE 如何服务**。

---

## 先看结论

LLM Serving 的核心矛盾可以压缩成一句话：

```text
在有限 GPU 显存、HBM 带宽和网络带宽下，同时优化 TTFT、TPOT、吞吐量、成本和稳定性。
```

现代推理系统大致沿着这些方向演进：

1. **Continuous Batching**：请求不再静态成批，而是 token-by-token 动态调度。
2. **Paged KV Cache**：把 KV Cache 当作显存页管理，减少碎片和浪费。
3. **Prefix / Radix Cache**：复用系统 prompt、RAG 前缀、多轮对话上下文。
4. **Chunked Prefill**：把长 prompt 的 prefill 切碎，减少对 decode 的阻塞。
5. **Prefill / Decode Disaggregation**：把 compute-bound 的 prefill 和 memory-bound 的 decode 分开部署。
6. **KV Cache Tiering / Offloading**：KV Cache 从 GPU 扩展到 CPU、DRAM、SSD、远端内存。
7. **Speculative Decoding**：用 draft 或多头预测减少大模型 decode 次数。
8. **Structured Decoding**：用 grammar / FSM 约束输出，服务 JSON、工具调用和 Agent。
9. **MoE Serving**：处理专家路由、expert parallel、负载均衡和跨节点通信。
10. **SLO-aware Scheduling**：调度目标从吞吐最大化转向 TTFT / ITL / cost 多目标优化。

---

## 核心指标

| 指标 | 含义 | 主要受什么影响 |
|------|------|----------------|
| TTFT | Time To First Token，首 token 延迟 | prefill 计算、排队、prefix cache 命中 |
| TPOT / ITL | Time Per Output Token / Inter-token Latency | decode 调度、HBM 带宽、KV Cache 大小 |
| Throughput | 单位时间输出 token 数 | batch size、调度、算子效率、并发 |
| KV Cache Hit Rate | 前缀缓存命中率 | prompt 复用、multi-turn、RAG、Agent 模板 |
| GPU Memory Utilization | 显存占用效率 | block size、fragmentation、cache eviction |
| SLO Violation Rate | 超过延迟目标的请求比例 | workload 波动、长短请求混部、抢占策略 |

---

## Serving 架构地图

```text
Client / Gateway
  ↓
Router / Load Balancer
  ↓
Scheduler
  ├─ admission control
  ├─ continuous batching
  ├─ priority / preemption
  ├─ chunked prefill
  └─ SLO-aware scheduling
  ↓
KV Cache Manager
  ├─ paged blocks
  ├─ prefix / radix tree
  ├─ eviction policy
  ├─ CPU / SSD offload
  └─ remote KV transfer
  ↓
Model Executor
  ├─ attention backend
  ├─ quantized kernels
  ├─ speculative decoding
  ├─ structured decoding
  └─ MoE expert routing
  ↓
GPU / Network / Storage
```

---

## 必读系统与论文

| 优先级 | 系统 / 论文 | 关键词 | 为什么重要 |
|--------|-------------|--------|------------|
| P0 | Orca | iteration-level scheduling | continuous batching 的代表系统 |
| P0 | [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180) | paged KV cache | 现代 LLM serving 的基础论文 |
| P0 | [SGLang](https://github.com/sgl-project/sglang) | RadixAttention / structured output | multi-turn、RAG、Agent 场景很重要 |
| P1 | TensorRT-LLM | NVIDIA kernels / quantization | 生产部署和极致性能参考 |
| P1 | Sarathi-Serve | chunked prefill | 平衡 prefill 与 decode 干扰 |
| P1 | DistServe | prefill-decode disaggregation | P/D 分离的代表系统 |
| P1 | Mooncake | KVCache-centric disaggregation | 把 KV Cache 作为系统核心资源管理 |
| P1 | LMCache | KV reuse / offloading | 长上下文和重复前缀场景的实用方向 |
| P1 | Medusa / EAGLE / SpecInfer | speculative decoding | decode 加速的重要路线 |
| P1 | XGrammar / Outlines / Guidance | structured decoding | Agent tool call / JSON 输出的关键工程能力 |
| P1 | Dynamo / llm-d | cloud-native serving | 面向 Kubernetes / 云原生部署的系统化方案 |

---

## 1. Continuous Batching

传统 static batching 会遇到两个问题：

- 长请求拖慢短请求；
- batch 内请求结束时间不同，GPU 空槽无法及时复用。

Continuous batching 的做法是：每一步 decode 后都可以把完成的请求移出，把新请求插入。调度粒度从“请求级”变成“token 级”。

```text
Static batch:       [req1 req2 req3 req4] 一起开始，一起等待
Continuous batch:   每个 decoding step 动态加入 / 移除请求
```

重点理解：

- admission control：什么时候允许新请求进 batch；
- preemption：显存不够时是否抢占请求；
- fairness：长输出请求是否会长期占用 KV；
- priority：交互式请求和批处理请求是否区别调度。

---

## 2. KV Cache 管理

### 2.1 PagedAttention

PagedAttention 的关键思想是把每个 sequence 的 KV Cache 切成 block，物理上不要求连续。

收益：

- 减少显存碎片；
- 支持更大的 effective batch size；
- 支持 copy-on-write 和 prefix sharing；
- 让调度器能像 OS 管页表一样管理 KV。

### 2.2 Prefix / Radix Cache

Agent、RAG、多轮对话、system prompt 模板会反复出现公共前缀。Prefix cache / RadixAttention 的目标是：

```text
相同前缀只 prefill 一次，后续请求复用已有 KV。
```

适合场景：

- 固定 system prompt；
- 同一文档上的多轮问答；
- Agent 工具说明和环境说明较长；
- batch 内 prompt 有公共模板。

### 2.3 KV Cache Offloading / Tiering

当 context length 和并发数继续增大，KV Cache 可能比模型权重更难管理。

典型层级：

```text
HBM GPU memory
  → CPU DRAM
  → Local SSD
  → Remote memory / KV service
```

关键问题：

- eviction policy：淘汰哪个 prefix / block；
- transfer overlap：KV 迁移能否和计算重叠；
- cache admission：哪些 KV 值得缓存；
- consistency：多副本 KV 如何管理；
- network bottleneck：远端 KV 是否会拖慢 decode。

---

## 3. Prefill / Decode 分离

Prefill 和 Decode 的硬件特性不同：

| 阶段 | 主要瓶颈 | 特征 | SLO 影响 |
|------|----------|------|----------|
| Prefill | 计算 | prompt tokens 可并行处理，矩阵乘密集 | TTFT |
| Decode | HBM 带宽 / KV 读取 | 每步生成 1 token，读历史 KV | TPOT / ITL |

### 为什么要分离？

混部会造成：

- 长 prompt prefill 阻塞 decode；
- decode 的 inter-token latency 抖动；
- GPU batch 组成不稳定，吞吐难预测；
- SLO 调优困难。

P/D 分离后，可以分别扩缩容：

```text
Prefill Pool: 处理长 prompt，优化 TTFT
Decode Pool : 持续生成 token，优化 TPOT / ITL
KV Transfer : prefill 完的 KV 从 P 节点传给 D 节点
```

### 代表系统

| 系统 | 核心思想 | 适合关注点 |
|------|----------|------------|
| Sarathi-Serve | chunked prefill，把 prefill 切成小块与 decode 混跑 | 不完全拆分时如何降低干扰 |
| DistServe | disaggregated prefill / decode | P/D 资源隔离与 SLO |
| Mooncake | KVCache-centric disaggregated architecture | KV 作为一等资源，跨节点复用和管理 |
| Dynamo / llm-d | 云原生 serving，面向 K8s / 多实例部署 | 生产部署、扩缩容、路由 |

---

## 4. Speculative Decoding

Decode 阶段通常 memory-bound，且每次只生成一个 token。Speculative decoding 的核心是：

```text
用便宜模型或额外预测头先猜多个 token，再用目标模型一次性验证。
```

| 方法 | 思路 | 适合场景 |
|------|------|----------|
| Draft model | 小模型生成候选，大模型验证 | 有高质量小模型时 |
| Medusa | 在大模型上加多个预测头 | 不想维护额外 draft 模型 |
| EAGLE | 在 feature space 预测候选 | 接受率更高，工程复杂度更高 |
| SpecInfer | 树状候选验证 | 多候选、多 draft 场景 |

注意：spec decoding 不一定总是加速。它依赖：

- draft token 接受率；
- target model batch 形状；
- 额外显存和 kernel 开销；
- 是否破坏 continuous batching。

---

## 5. Structured Decoding

Agent 和应用系统常要求输出 JSON、函数调用参数或 DSL。Structured decoding 的目标是：

```text
在解码过程中限制 token 选择，使输出满足 grammar / regex / JSON schema。
```

| 工具 | 关键词 | 关注点 |
|------|--------|--------|
| Outlines | regex / JSON schema | 易用，适合应用层约束 |
| Guidance | constrained generation | 模板和生成流程结合 |
| XGrammar | grammar compiler | 高性能结构化解码 |
| SGLang FSM | compressed finite state machine | serving 框架内置结构化输出优化 |

工程上要关注：

- grammar 编译开销；
- 每步 token mask 成本；
- 和 batch / speculative decoding 的兼容性；
- schema 很复杂时的失败恢复。

---

## 6. MoE Serving

MoE 模型把 FFN 替换成多个 expert，每个 token 只路由到少数 expert。推理系统新增几个问题：

- expert parallel：expert 放在哪些 GPU / 节点；
- routing skew：热门 expert 导致负载不均；
- all-to-all：token dispatch / combine 的通信开销；
- cache locality：同一 expert 的 token 是否能聚合；
- failover：某个 expert 节点失败如何处理。

DeepSeek-V3 / Mixtral / Qwen-MoE 等模型让 MoE serving 从研究问题变成工程问题。后续阅读时要把 MoE 和以下主题一起看：

- FP8 inference；
- expert parallelism；
- MLA / GQA 对 KV Cache 的影响；
- P/D 分离下 expert placement；
- router 和 load balancer 协同。

---

## 7. 实践路线

### 入门实验：跑通 serving benchmark

1. 用 vLLM 启动 OpenAI-compatible server；
2. 用不同输入长度 / 输出长度 / 并发数压测；
3. 记录 TTFT、TPOT、吞吐、显存占用；
4. 打开 / 关闭 prefix caching、chunked prefill，对比曲线。

### 进阶实验：实现 mini scheduler

实现一个简化模拟器：

```text
Request(id, prompt_len, output_len, arrival_time, priority)
KVBlockManager(num_blocks, block_size)
Scheduler(policy = continuous_batching / priority / preemptive)
Metrics(TTFT, TPOT, throughput, eviction_count)
```

完成标准：能模拟长短请求混部、KV block 不足、抢占和 prefix 命中。

### 前沿实验：P/D 分离原型

1. 一个 prefill worker 负责 prompt 计算；
2. 一个 decode worker 负责 token streaming；
3. 中间用本地内存或文件模拟 KV transfer；
4. 对比 mixed serving 与 P/D serving 的 TTFT / TPOT。

---

## 推荐阅读顺序

1. Orca：先理解 iteration-level scheduling；
2. vLLM / PagedAttention：理解 KV block 和 continuous batching；
3. SGLang / RadixAttention：理解 prefix reuse 和 Agent/RAG 场景；
4. Sarathi-Serve：理解 chunked prefill；
5. DistServe：理解 P/D 分离；
6. Mooncake / LMCache：理解 KV Cache 作为跨请求、跨节点资源；
7. Medusa / EAGLE：理解 speculative decoding；
8. XGrammar / Outlines：理解 structured decoding；
9. TensorRT-LLM：理解生产级 kernel 和部署优化；
10. Dynamo / llm-d：理解云原生和集群级 serving。

---

## 和现有文档的关系

- [04. LLM 推理系统](04-llm-inference.md)：基础概念、vLLM / SGLang / TensorRT-LLM 入门。
- [07. AI Infra 必读论文路线](07-ai-infra-papers.md)：训练、推理、算子和集群系统的论文地图。
- 本文：专注 LLM serving 前沿系统和工程取舍。
