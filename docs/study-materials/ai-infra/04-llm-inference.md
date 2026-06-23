# 04. LLM 推理系统

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 系统 / 实践 |
| 难度 | 进阶 |
| 优先级 | P0 / Hands-on / Frontier |
| 状态 | 需更新 |
| 建议用途 | 理解 LLM serving 与推理优化 |

---

> LLM 推理是 AI Infra 当前最热门的方向之一。如何在有限显存和算力下服务海量请求，是核心挑战。

> 延伸阅读：本文讲基础概念和主流框架；更系统的前沿 serving 架构见 [08. LLM Serving 前沿系统](08-llm-serving-frontier.md)。

---

## 先看结论

- LLM 推理系统的核心矛盾是：**显存有限、请求动态、序列长度不均、prefill/decode 资源需求不同**。
- Prefill 通常更 compute-bound，decode 通常更 memory-bound；优化 TTFT 和 TPOT 往往需要不同策略。
- KV Cache 是 serving 的中心资源：PagedAttention、prefix caching、RadixAttention、KV quantization、MLA 都围绕它展开。
- Continuous batching 解决吞吐，chunked prefill 平衡抢占和延迟，P/D 分离进一步把不同阶段拆到不同资源池。
- 评估 serving 不能只看 tokens/s，还要同时看 TTFT、TPOT、tail latency、显存占用、SLO violation 和成本。
- 完成标准：能解释一个请求从进入 vLLM / SGLang 到生成完成的生命周期，并能跑一组 benchmark 分析瓶颈。

---

## 推理系统核心概念

### 两个阶段

| 阶段 | 说明 | 计算特性 |
|------|------|----------|
| **Prefill（预填充）** | 处理输入 prompt，并行计算所有 token 的 KV，生成第一个 token | Compute-bound |
| **Decode（解码）** | 逐 token 自回归生成，每步只新增 1 个 token 但要读全部 KV Cache | Memory-bound |

### 关键指标

| 指标 | 全称 | 说明 |
|------|------|------|
| **TTFT** | Time To First Token | 首 token 延迟，取决于 prefill 速度 |
| **TPOT** | Time Per Output Token | 每个输出 token 延迟，取决于 decode 速度 |
| **吞吐量** | Throughput | 单位时间 token 数 / 并发请求数 |
| **MFU** | Model FLOP Utilization | 实际 FLOPS / 峰值 FLOPS，衡量 GPU 利用率 |

---

## KV Cache 管理

### 为什么需要 KV Cache

Decode 阶段每步都需要前面所有 token 的 K/V，不缓存则每步重算代价为 O(N²)。

### 显存估算（LLaMA-2 70B 为例）

```
KV per token = 2 × num_layers × num_kv_heads × head_dim × dtype_bytes
             = 2 × 80 × 8(GQA) × 128 × 2(FP16)
             ≈ 0.32 MB/token

4096 token 请求 ≈ 1.3 GB KV Cache
并发 64 个请求 ≈ 83 GB → 超出单卡显存
```

### KV Cache 优化技术

| 技术 | 说明 | 框架 |
|------|------|------|
| **PagedAttention** | 类 OS 分页管理 KV，物理不连续，消除碎片 | vLLM |
| **RadixAttention** | 前缀基数树，自动跨请求复用公共前缀 KV | SGLang |
| **Prefix Caching** | 系统 prompt 等公共前缀只算一次 | vLLM/SGLang |
| **MQA/GQA** | 多 Query 共享 KV head，减少 KV 大小 2-8x | 模型层面 |
| **KV 量化** | INT8/FP8 存储 KV，节省约 50% 显存 | vLLM/SGLang |
| **MLA（DeepSeek）** | 低秩压缩 KV，大幅减少 KV Cache 占用 | 模型层面 |

---

## 批处理策略

| 策略 | 说明 | 缺点 |
|------|------|------|
| **Static Batching** | 等一批请求凑齐再一起处理 | 延迟高，短请求等长请求 |
| **Continuous Batching** | 动态插入新请求、踢出已完成，不等齐 | 实现复杂 |
| **Chunked Prefill** | Prefill 按 chunk 切分，与 decode 混合调度 | 平衡 TTFT 和吞吐 |
| **Disaggregated Prefill** | Prefill 和 Decode 部署在不同实例 | 彻底隔离资源，运维成本高 |

### Prefill / Decode 分离趋势

Prefill 和 Decode 的资源画像不同：Prefill 更偏 compute-bound，Decode 更偏 memory-bandwidth-bound。长 prompt 或 RAG 请求会让 prefill 占用大量计算，进而干扰 decode 的 inter-token latency。

常见演进路径：

```text
Static Batching
  → Continuous Batching
  → Chunked Prefill
  → Prefill / Decode Disaggregation
  → KV Cache-centric Serving
```

代表方向：

- **Sarathi-Serve**：把 prefill 切成 chunk，减少对 decode 的阻塞；
- **DistServe**：将 prefill 与 decode 分离部署，分别优化 TTFT 和 TPOT；
- **Mooncake / LMCache**：把 KV Cache 作为可复用、可迁移、可分层存储的核心资源；
- **Dynamo / llm-d**：面向云原生和集群级 serving 的系统化方案。

更多系统梳理见：[08. LLM Serving 前沿系统](08-llm-serving-frontier.md)。

---

## 推理加速技术

### 量化（Quantization）

| 方法 | 精度 | 特点 |
|------|------|------|
| **GPTQ** | INT4/INT8 | Post-training，精度损失小，需校准数据 |
| **AWQ** | INT4 | Activation-aware，保护重要权重通道，精度更好 |
| **FP8** | FP8 E4M3/E5M2 | H100/H800 原生支持，训练推理均可用 |
| **GGUF/llama.cpp** | INT4/Q8 | CPU 推理，端侧部署 |

### 推测解码（Speculative Decoding）

**原理**：
1. Draft Model（小模型）快速生成 k 个候选 token
2. Target Model（大模型）并行验证所有候选
3. 接受正确 token，拒绝时回退
4. 每次 Target Model 前向可接受多个 token，等效加速 2-4x

**变体：**
- [Medusa](https://github.com/FasterDecoding/Medusa)：多个解码头并行猜测，无需单独 draft 模型
- [Eagle](https://github.com/SafeAILab/EAGLE)：特征级预测，更高接受率
- [SpecInfer](https://arxiv.org/abs/2305.09781)：多 draft 模型树状验证

### 稀疏注意力 / 长上下文优化

- **FlashAttention-3**：H100 专项，TMA + warpgroup 异步 pipeline，FP8 支持
- **MLA**（DeepSeek-V2/V3）：Multi-head Latent Attention，低秩 KV 压缩
- **Sparse Attention**：只计算重要位置的 attention

---

## 主流框架详解

### vLLM

- **GitHub**：https://github.com/vllm-project/vllm
- **文档**：https://docs.vllm.ai
- **论文**：[PagedAttention](https://arxiv.org/abs/2309.06180)
- **Blog**：https://blog.vllm.ai

**核心技术：**
- PagedAttention：KV Cache 物理分页，消除显存碎片
- Continuous Batching：动态请求队列管理
- Chunked Prefill：prefill 分 chunk 与 decode 混跑
- 多硬件：NVIDIA / AMD / Intel / TPU / Ascend

**源码阅读顺序：**
```
LLMEngine（整体入口）
  → Scheduler（请求调度，核心逻辑）
  → BlockManager（KV Cache 物理块分配）
  → Worker（单卡执行单元）
  → ModelRunner（模型前向 + CUDAGraph）
  → Attention Backend（PagedAttention kernel）
```

**快速上手：**
```bash
pip install vllm
python -c "
from vllm import LLM, SamplingParams
llm = LLM(model='Qwen/Qwen2.5-7B-Instruct')
outputs = llm.generate(['你好，介绍一下自己'], SamplingParams(max_tokens=200))
print(outputs[0].outputs[0].text)
"
```

### SGLang

- **GitHub**：https://github.com/sgl-project/sglang
- **文档**：https://docs.sglang.io/
- **学习材料**：https://github.com/sgl-project/sgl-learning-materials
- **Blog**：https://lmsys.org/blog/

**核心技术：**
- **RadixAttention**：基数树管理 KV Cache，跨请求自动复用公共前缀，multi-turn/RAG 场景命中率极高
- **Compressed State Machine**：结构化输出（JSON/regex）用有限状态机约束解码，比 Outlines 快
- **Overlap Scheduler**：CPU 调度与 GPU 计算重叠，减少空泡
- **Large-scale EP**：MoE 模型专家并行，DeepSeek-V3 等模型专项优化
- **SGLang Diffusion**：扩展到图像/视频生成模型（2026/01）
- **TPU/JAX Backend**：原生 TPU 支持（2025/10）

**源码阅读顺序：**
```
sglang/srt/server.py（HTTP 服务入口）
  → managers/router_manager.py（请求路由）
  → managers/scheduler.py（调度 + RadixAttention tree 管理）
  → model_executor/（模型执行）
  → layers/attention/（Attention 实现，含 RadixAttention）
```

### vLLM vs SGLang 对比

| 维度 | vLLM | SGLang |
|------|------|--------|
| 生态成熟度 | ✅ 更广泛 | 快速增长 |
| KV Cache 复用 | 基础 prefix caching | ✅ RadixAttention 更强 |
| 结构化输出 | 有限支持 | ✅ 原生高效 |
| MoE/EP 支持 | 支持 | ✅ 专项优化 |
| 多模态/Diffusion | 支持 | ✅ Diffusion 支持 |
| 代码可读性 | ✅ 更适合入门 | 中等 |
| Chunked Prefill | ✅ 支持 | ✅ 支持 |

### TensorRT-LLM

- **GitHub**：https://github.com/NVIDIA/TensorRT-LLM
- NVIDIA 官方，FP8/INT4/INT8 量化、Spec Decoding、MoE 全支持
- 极致性能，适合生产部署最后一公里
- 学习曲线较陡，建议先掌握 vLLM/SGLang 后再接触

---

## 推理学习路径

```
第一步：概念建立（1周）
  读 PagedAttention 论文（arxiv 2309.06180）
  读 vLLM Blog: https://blog.vllm.ai/2023/06/20/vllm.html
  理解 KV Cache / Continuous Batching / TTFT/TPOT

第二步：动手跑通（3天）
  pip install vllm
  跑 offline inference（LLaMA/Qwen）
  跑 OpenAI-compatible server + benchmark

第三步：源码精读（2-3周）
  vLLM：Scheduler + BlockManager
  SGLang：scheduler.py 中 RadixAttention 实现

第四步：进阶（1个月）
  量化实践（AWQ/GPTQ/FP8）
  Speculative Decoding 原理与实验
  Disaggregated Prefill（P/D 分离部署）
  自己实现一个简化推理引擎
```

---

## 推理系统前沿补充清单

| 优先级 | 系统 / 方法 | 方向 | 解决的问题 |
|--------|-------------|------|------------|
| P0 | Orca | continuous batching | decode 阶段动态 batch，提高 GPU 利用率 |
| P0 | vLLM / PagedAttention | KV cache 管理 | 降低 KV cache 碎片，提高吞吐 |
| P0 | SGLang / RadixAttention | prefix cache / structured generation | 多轮和结构化 workload 优化 |
| P1 | Sarathi / Sarathi-Serve | chunked prefill | prefill/decode 干扰和调度 |
| P1 | DistServe | prefill-decode disaggregation | 不同阶段资源解耦 |
| P1 | Mooncake | KV cache-centric serving | disaggregated serving 与 KV cache 传输 |
| P1 | Splitwise | disaggregated inference | prefill/decode 分离部署 |
| P1 | FlashInfer | inference kernel | attention / sampling / decode kernel 优化 |
| P1 | Medusa / EAGLE / EAGLE-2 | speculative decoding | 减少 decode latency |
| P2 | SpecInfer / Lookahead Decoding | speculative inference | 并行验证和候选生成 |

读这些系统时建议统一记录：

```markdown
## Workload Assumption
## Bottleneck
## Scheduling Policy
## KV Cache Strategy
## Kernel Dependency
## Evaluation Metrics: TTFT / TPOT / Throughput / P99 / Cost
```

### 补充：Serving 调度系统

| 材料 / 系统 | 方向 | 为什么值得补 |
|-------------|------|--------------|
| TetriInfer | serving scheduling | 面向 LLM 推理的调度和资源利用优化，可作为 P/D 分离、chunked prefill 之外的前沿系统补充 |
| NanoFlow | serving / pipeline | 面向细粒度推理流水线和资源调度的前沿系统，适合与 DistServe、Mooncake 对比 |
| Dynamo-style serving architecture | disaggregated serving | 不是单一论文条目，而是总结 KV cache、prefill/decode、scheduler、worker 解耦的服务架构风格 |
