# AI Infra 入门资料整理

> AI Infra（AI 基础设施）是支撑大模型训练、部署、运行的底层系统工程。
> 本系列覆盖从硬件体系结构到上层调度的完整知识栈，适合有一定编程基础的同学系统入门。

---

## 📚 子章节目录

| 章节 | 核心内容 | 关键词 |
|------|----------|--------|
| [01. 体系结构基础](01-architecture.md) | GPU 微架构、内存层次、Roofline Model、NVLink/IB 互联 | SM、Tensor Core、HBM、带宽 |
| [02. CUDA 与算子编程](02-cuda-kernels.md) | CUDA 编程模型、Triton、TileLang、FlashAttention | Kernel、Warp、Shared Memory |
| [03. 分布式训练](03-distributed-training.md) | DP/TP/PP/SP 并行策略、ZeRO、Megatron-LM、DeepSpeed | 3D Parallel、ZeRO-3、Pipeline Bubble |
| [04. LLM 推理系统](04-llm-inference.md) | vLLM、SGLang、KV Cache、量化、Speculative Decoding | PagedAttention、RadixAttention、TTFT |
| [05. 网络与存储](05-network-storage.md) | NCCL、InfiniBand、RDMA、JuiceFS、训练 I/O 优化 | AllReduce、RoCE、DataLoader |
| [06. 调度与编排](06-scheduling-orchestration.md) | Ray、Kubernetes、Volcano、Slurm、可观测性 | Gang Scheduling、Ray Serve、DCGM |

---

## 🗺️ 知识层次全景

```
用户请求 / 训练任务
      ↓
[ 调度与编排 ]  Ray · K8s · Volcano · Slurm
      ↓
[ 推理系统  ]  vLLM · SGLang · TensorRT-LLM
[ 训练框架  ]  Megatron-LM · DeepSpeed · FSDP
      ↓
[ 算子编程  ]  TileLang · Triton · FlashAttention · CUTLASS
      ↓
[ CUDA 软件栈 ]  CUDA Runtime · cuDNN · NCCL
      ↓
[ 体系结构  ]  GPU SM · Tensor Core · HBM · NVLink · IB
```

---

## 🚀 推荐入门顺序

```
第 1 个月：体系结构 → CUDA 基础 → 单机多卡 DDP
第 2 个月：分布式训练（TP/PP/ZeRO）→ FlashAttention 原理
第 3 个月：vLLM 源码精读 → SGLang RadixAttention → 量化实践
第 4 个月：TileLang Puzzles → Triton 自定义算子 → Nsight 性能分析
第 5-6 月：选方向深挖（训练 / 推理 / 算子）
```

---

## 🔗 核心资源速查

**论文：**
- [PagedAttention（vLLM）](https://arxiv.org/abs/2309.06180) · [FlashAttention-2](https://arxiv.org/abs/2307.08691) · [Megatron-LM](https://arxiv.org/abs/1909.08053) · [ZeRO](https://arxiv.org/abs/1910.02054) · [MegaScale](https://arxiv.org/abs/2402.15627)

**GitHub：**
- [vllm](https://github.com/vllm-project/vllm) · [sglang](https://github.com/sgl-project/sglang) · [tilelang](https://github.com/tile-ai/tilelang) · [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) · [DeepSpeed](https://github.com/microsoft/DeepSpeed) · [flash-attention](https://github.com/Dao-AILab/flash-attention)

**博客：**
- [Lilian Weng](https://lilianweng.github.io) · [LMSYS Blog](https://lmsys.org/blog/) · [vLLM Blog](https://blog.vllm.ai/) · [知乎 @BBuf](https://www.zhihu.com/people/bbuf)

