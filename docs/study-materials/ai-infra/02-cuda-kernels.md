# 02. CUDA 与算子编程

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 实践 / 系统 |
| 难度 | 中级到进阶 |
| 优先级 | P0 / Hands-on |
| 状态 | 可用 |
| 建议用途 | 学习 CUDA、Triton 与算子优化 |

---

> 算子是 AI Infra 的最小计算单元。理解如何在 GPU 上高效实现算子，是优化训练和推理性能的基础。

---

## 先看结论

- 算子优化的核心是让数据搬运、线程组织和 Tensor Core 计算匹配起来，而不是只把 Python 改成 CUDA。
- CUDA 适合理解底层执行模型；Triton / TileLang 更适合快速写高性能 fused kernel 和验证想法。
- 入门顺序建议：vector add → matmul → reduction → softmax → attention，而不是直接手写复杂 Transformer kernel。
- 关键概念必须掌握：thread/block/grid、warp、shared memory、coalescing、bank conflict、occupancy、Tensor Core。
- 真正的完成标准是会 profiling：能用 Nsight / benchmark 定位是 memory-bound、compute-bound 还是 launch overhead。
- 和 LLM 推理最相关的算子包括 attention、RMSNorm / LayerNorm、SwiGLU、sampling、quantized GEMM。

---

## CUDA 编程基础

### 核心概念掌握路径

```
Thread/Block/Grid（线程层次结构）
  → Shared Memory（共享内存，片上高速缓存）
  → Warp Divergence（分支导致 warp 内线程序列化）
  → Memory Coalescing（合并内存访问，最大化带宽）
  → Bank Conflict（Shared Memory bank 冲突）
  → Async Copy（cp.async，异步数据搬运）
  → Tensor Core / WMMA（矩阵乘加加速单元）
  → CuTe（CUTLASS 现代 C++ 抽象层）
```

### 推荐资料

| 资料 | 说明 |
|------|------|
| [NVIDIA CUDA 官方文档](https://docs.nvidia.com/cuda/) | 权威参考，必备 |
| [CUDA C++ Programming Guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/) | 必读，理解底层执行模型 |
| 《Programming Massively Parallel Processors》（PMPP）| 公认 CUDA 入门圣经 |
| [CUDA Mode（GitHub）](https://github.com/cuda-mode) | 实战讲座，含 FlashAttention、Triton 等专题 |
| [How to Optimize a CUDA Matmul Kernel](https://siboehm.com/articles/22/CUDA-MMM) | GEMM 优化从 naive 到 Tensor Core 全过程，必读 |

### 入门动手练习顺序

```bash
# 1. 向量加法（理解 thread/block/grid）
# 2. 矩阵乘法（共享内存 tiling）
# 3. Reduction（warp shuffle、AllReduce）
# 4. Softmax（online softmax，理解 memory-bound 优化）
# 5. 自己实现一个简单 Attention
```

---

## Triton（高层 GPU 编程）

> OpenAI 出品的 Python DSL，是 vLLM/SGLang 中大量自定义算子的实现语言。

- **官方文档**：https://triton-lang.org/
- **入门教程**：https://triton-lang.org/main/getting-started/tutorials/
- **GitHub**：https://github.com/triton-lang/triton

**与 CUDA 的关系：**
- Triton 屏蔽了 warp/thread 级别的细节，以 tile（块）为编程单位
- 自动处理内存合并、向量化，适合快速实现 fused kernel
- 性能接近手写 CUDA，开发效率高很多

**适合场景：**
- 实现自定义激活函数融合（如 SwiGLU）
- fused LayerNorm、RMSNorm
- 自定义 Attention 变体
- vLLM/SGLang 中的 paged attention kernel

**学习路径：**
```
官方 Tutorial（向量加法 → 矩阵乘法 → Softmax → FlashAttention）
  → 读 vLLM 中的 Triton kernel（vllm/attention/ops/）
  → 自己实现一个 fused kernel
```

---

## TileLang

> 国产算子编程 DSL，tile-ai 团队开发，定位于 Triton 和 CUTLASS 之间，兼顾易用性和极致性能。

- **GitHub**：https://github.com/tile-ai/tilelang
- **官方文档**：https://tilelang.tile-ai.cn/
- **论文**：[TileLang: A Composable Tiled Programming Model for AI Systems](https://arxiv.org/abs/2504.17577)
- **互动学习**：[TileLang Puzzles](https://github.com/tile-ai/tilelang-puzzles) — 10 个由浅入深的编程谜题，强烈推荐

### 核心特点

- Python 语法 + 底层 TVM 编译器基础设施
- 支持 GEMM、Dequant GEMM、FlashAttention、LinearAttention、MLA 等关键算子
- 支持硬件：NVIDIA GPU、AMD GPU、Huawei Ascend、Apple Metal
- 2025/12 新增 CuTe DSL backend，可编译到 NVIDIA CUTLASS CuTe

### 与 Triton 的区别

| 对比 | Triton | TileLang |
|------|--------|----------|
| 编程粒度 | tile 级别 | tile 级别，更细粒度控制 |
| Layout 控制 | 有限 | ✅ 显式 layout 管理 |
| 硬件支持 | NVIDIA/AMD | ✅ 更多硬件（Ascend/Metal）|
| TMA/异步拷贝 | 部分支持 | ✅ 原生支持 |
| 后端 | LLVM IR | TVM + CuTe DSL |

### 入门路径

```bash
pip install tilelang
# 1. 跑通官方 GEMM 示例
# 2. 完成 TileLang Puzzles（10个由浅入深）
# 3. 实现 FlashAttention
# 4. 实现 MLA（Multi-head Latent Attention）
```

**知乎参考**：[TileLang: 80行Python代码实现FlashMLA](https://zhuanlan.zhihu.com/p/27965825936)

---

## FlashAttention

> 目前大模型训练和推理中最重要的算子优化之一。

- **FlashAttention-1 论文**：[FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- **FlashAttention-2 论文**：[FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)
- **FlashAttention-3 论文**：[FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision](https://arxiv.org/abs/2407.08608)
- **GitHub**：https://github.com/Dao-AILab/flash-attention

### 核心思路

**问题**：标准 Attention 需要将 N×N 的注意力矩阵写回 HBM，对长序列是 O(N²) 显存，且 I/O 是瓶颈。

**解法**：
1. **Tiling**：将 Q/K/V 分块，每块放进 Shared Memory，避免 HBM 大矩阵读写
2. **Online Softmax**：不需要提前知道全局最大值，流式计算 softmax
3. **Recomputation**：反向传播时重新计算 attention，不存 N×N 中间矩阵（省显存）

**效果**：
- 显存从 O(N²) 降到 O(N)
- HBM I/O 减少 5-20x
- 实际训练速度提升 2-4x

### 版本演进

| 版本 | 关键改进 |
|------|----------|
| FA-1 | 基础 tiling + online softmax |
| FA-2 | 更好的并行划分（Q 并行），减少非矩阵计算 |
| FA-3 | H100 专项，利用 TMA + warpgroup + FP8，异步 pipeline |

---

## CUTLASS / CuTe

> NVIDIA 官方 GEMM 模板库，极致性能但学习曲线较陡。

- **GitHub**：https://github.com/NVIDIA/cutlass
- CuTe 是 CUTLASS 3.x 的核心抽象层，用 Layout 描述 tensor 的内存排布
- 适合需要极限性能的生产场景
- 入门推荐先掌握 Triton/TileLang，再回头看 CUTLASS

---

## 学习路线建议

```
入门阶段（1-2个月）：
  CUDA 基础 → Triton Tutorial → 实现 Softmax/Reduction

进阶阶段（1个月）：
  TileLang Puzzles → 实现 GEMM → 精读 FlashAttention 论文

高阶阶段：
  FA-3 源码 → CUTLASS/CuTe → 自定义硬件 kernel
```

