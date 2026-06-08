# 07. AI Infra 必读论文路线

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 论文路线 / 系统地图 |
| 难度 | 进阶到前沿 |
| 优先级 | P0 / Frontier / Survey |
| 状态 | 推荐 |
| 建议用途 | 建立 AI Infra 论文主线，连接训练、推理、算子和集群系统 |

---

> 目标：不是把所有论文列全，而是整理 AI Infra 最值得反复读的系统论文和技术报告。阅读时重点关注：**瓶颈是什么、系统边界在哪里、抽象如何设计、性能收益来自哪里、工程代价是什么**。

---

## 先看结论

AI Infra 的论文可以按四层理解：

```text
Kernel / Operator
  → FlashAttention / Triton / CUTLASS / TileLang / ThunderKittens

Single-node Runtime
  → CUDA Graph / memory planner / KV cache / quantization / compilation

Distributed Training & Serving
  → ZeRO / Megatron / GPipe / PipeDream / vLLM / SGLang / DistServe / Sarathi-Serve

Cluster-scale AI Systems
  → GSPMD / Alpa / MegaScale / Ray / Kubernetes / Slurm / fault tolerance / scheduling
```

建议优先建立两条主线：

1. **训练系统主线**：模型如何被切分、通信如何被隐藏、故障如何被恢复；
2. **推理系统主线**：KV Cache 如何管理、请求如何调度、prefill / decode 如何拆分、SLO 如何保证。

---

## 必读 Top 10

| 优先级 | 材料 | 方向 | 为什么重要 |
|--------|------|------|------------|
| P0 | [ZeRO](https://arxiv.org/abs/1910.02054) | 分布式训练 | 数据并行从“复制模型”走向“切分状态”的关键论文 |
| P0 | [Megatron-LM](https://arxiv.org/abs/1909.08053) | 张量并行 | 大模型 tensor parallel 的基础范式 |
| P0 | [GPipe](https://arxiv.org/abs/1811.06965) / [PipeDream](https://arxiv.org/abs/1806.03377) | 流水线并行 | 理解 pipeline bubble、micro-batch 和 1F1B 的基础 |
| P0 | [FlashAttention](https://arxiv.org/abs/2205.14135) / [FlashAttention-2](https://arxiv.org/abs/2307.08691) | Kernel | IO-aware 算子优化的代表，连接算法和 GPU memory hierarchy |
| P0 | [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180) | LLM Serving | 现代 LLM 推理系统的必读论文，核心是 KV Cache 分页管理 |
| P0 | [Orca](https://www.usenix.org/conference/osdi22/presentation/yu) | LLM Serving | Continuous batching / iteration-level scheduling 的系统代表 |
| P1 | GSPMD / Alpa | 自动并行 | 理解编译器和系统如何自动搜索并行策略 |
| P1 | [MegaScale](https://arxiv.org/abs/2402.15627) | 大规模训练 | 生产级万卡训练系统，重视故障恢复、调度和稳定性 |
| P1 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437) | MoE 训练 / 推理 | 连接 MoE、FP8、MLA、负载均衡和工程效率 |
| P1 | DistServe / Sarathi-Serve / Mooncake / LMCache | 推理前沿 | 代表 prefill-decode 分离、chunked prefill、KV cache 分层和复用 |

---

## 训练系统论文路线

### 1. 数据并行与状态切分

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| ZeRO | P0 | optimizer state、gradient、parameter 如何切分 |
| ZeRO-Offload / ZeRO-Infinity | P1 | CPU / NVMe offload 如何扩大可训练模型规模 |
| PyTorch FSDP 文档与源码 | P0 / Hands-on | ZeRO-3 在 PyTorch 生态中的工程实现 |

读的时候不要只记结论，要算清楚：

```text
参数显存 + 梯度显存 + 优化器状态 + 激活显存 + 通信 buffer
```

这比背诵 ZeRO-1/2/3 更重要。

### 2. Tensor / Pipeline / Sequence Parallelism

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| Megatron-LM | P0 | MLP 和 Attention 的列切分 / 行切分 |
| GPipe | P0 | pipeline bubble 与 micro-batch |
| PipeDream | P0 | 1F1B 调度、权重版本与吞吐延迟权衡 |
| Sequence Parallelism | P1 | 长序列下 activation / communication 的切分 |
| Ring Attention / Ulysses | P1 / Frontier | 超长上下文训练中的 context parallelism |

建议配合 `Megatron-LM` 或 `DeepSpeed` 源码读：

```text
megatron/core/tensor_parallel/
megatron/core/pipeline_parallel/
megatron/core/distributed/
```

### 3. 大规模训练系统

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| GSPMD | P1 | 张量切分和编译器并行抽象 |
| Alpa | P1 | inter-op / intra-op 并行搜索 |
| MegaScale | P1 / Frontier | 万卡训练中的稳定性、通信、checkpoint、调度 |
| DeepSeek-V3 Technical Report | P1 / Frontier | MoE、FP8、DualPipe、MLA、负载均衡 |

大规模训练系统论文要重点看：

- failure recovery：掉卡后怎么恢复？
- checkpoint：保存频率、异步写入、存储压力；
- communication overlap：通信和计算如何重叠；
- load balance：MoE expert 如何避免热点；
- observability：如何定位慢节点、坏卡、网络抖动。

---

## 推理系统论文路线

### 1. Serving 调度基础

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| Orca | P0 | iteration-level scheduling / continuous batching |
| vLLM / PagedAttention | P0 | KV Cache 分页与显存碎片治理 |
| SGLang / RadixAttention | P0 / Hands-on | 前缀复用、multi-turn / RAG / Agent 场景 |
| TensorRT-LLM | P1 / Hands-on | 高性能 kernel、quantization、production deployment |

### 2. Prefill / Decode 分离

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| Sarathi-Serve | P1 / Frontier | chunked prefill 如何减少 decode interference |
| DistServe | P1 / Frontier | prefill 和 decode 为什么要资源隔离 |
| Mooncake | P1 / Frontier | KV Cache centric disaggregated architecture |
| LMCache | P1 / Hands-on | KV Cache 复用、offloading、跨请求缓存 |

核心判断：

```text
Prefill: compute-bound, 影响 TTFT
Decode : memory-bandwidth-bound, 影响 TPOT / ITL
```

如果把两者混在一个队列里，通常会出现：长 prompt 抬高 TTFT，decode 被 prefill 阻塞，SLO 抖动变大。

### 3. Speculative / Structured / MoE Serving

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| SpecInfer / Medusa / EAGLE | P1 | 如何用 draft / heads / feature prediction 提升 decode |
| Outlines / Guidance / XGrammar | P1 | 结构化输出如何约束 decoding |
| DeepSeek-V3 / MLA / MoE serving | P1 / Frontier | MLA 减少 KV，MoE 引入 expert parallel 和 routing 问题 |

---

## Kernel 与编程模型路线

| 材料 | 优先级 | 重点问题 |
|------|--------|----------|
| FlashAttention / FlashAttention-2 / FlashAttention-3 | P0 | IO-aware tiling、online softmax、warp-level pipeline |
| Triton | P0 / Hands-on | Python DSL 如何表达高性能 GPU kernel |
| CUTLASS / CuTe | P1 | NVIDIA 官方 GEMM / tensor abstraction |
| TileLang | P1 / Hands-on | 面向 tile 的 kernel 编写和自动化 |
| ThunderKittens | P2 / Frontier | 更贴近硬件的数据移动和 warp group 编程 |

实践建议：

1. 先用 PyTorch 写 baseline attention；
2. 再用 Triton 写 tiled matmul / attention；
3. 用 Nsight Systems / Nsight Compute 看 kernel timeline、occupancy、memory throughput；
4. 对比 FlashAttention 的 IO 复杂度和真实吞吐。

---

## 推荐阅读顺序

### 第 1 阶段：训练系统基础

1. ZeRO
2. Megatron-LM
3. GPipe / PipeDream
4. PyTorch FSDP 文档

完成标准：能手算 7B / 70B 模型在 DDP、ZeRO-3、TP、PP 下的大致显存和通信量。

### 第 2 阶段：推理系统基础

1. Orca
2. vLLM / PagedAttention
3. SGLang / RadixAttention
4. TensorRT-LLM 文档

完成标准：能解释 TTFT、TPOT、KV Cache、continuous batching、prefix caching 的相互关系。

### 第 3 阶段：前沿系统

1. MegaScale
2. DeepSeek-V3 Technical Report
3. DistServe / Sarathi-Serve
4. Mooncake / LMCache
5. FlashAttention-3 / TileLang / ThunderKittens

完成标准：能画出一个训练集群和一个推理集群的系统架构，并说明主要瓶颈在哪里。

---

## 实践项目

1. **显存计算器**：输入模型参数量、层数、hidden size、context length、并行策略，估算训练和推理显存。
2. **Mini ZeRO**：用 PyTorch 实现 optimizer state / gradient sharding 的简化版本。
3. **Mini vLLM Scheduler**：模拟 continuous batching、block allocation、request preemption。
4. **Triton Kernel Lab**：实现 matmul、layernorm、attention block，并用 Nsight 分析。
5. **Serving Benchmark**：用 vLLM / SGLang 对比不同 prompt length、output length、并发数下的 TTFT / TPOT。

---

## 后续维护建议

本文件保持“论文地图”定位，不展开太多实现细节。具体专题应拆到：

- [03. 分布式训练](03-distributed-training.md)
- [04. LLM 推理系统](04-llm-inference.md)
- [08. LLM Serving 前沿系统](08-llm-serving-frontier.md)
