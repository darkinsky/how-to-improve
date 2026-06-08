# 01. 体系结构基础

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 基础 / 系统 |
| 难度 | 中级 |
| 优先级 | P0 / Classic |
| 状态 | 可用 |
| 建议用途 | 理解 GPU、内存层次与性能分析基础 |

---

> 很多 AI Infra 的性能问题，本质是体系结构问题。理解硬件是写出高效代码的前提。

---

## GPU 微架构

### 整体架构层次

```
GPU
├── GPC（Graphics Processing Cluster）
│    └── SM（Streaming Multiprocessor）× N
│         ├── CUDA Core（FP32/INT32）
│         ├── Tensor Core（矩阵乘加单元，GEMM 加速核心）
│         ├── Warp Scheduler（每个 SM 4个，每周期调度 1 个 warp）
│         ├── Register File（每 SM 约 256KB，寄存器是最快存储）
│         ├── Shared Memory / L1 Cache（可配置，约 128-228KB）
│         └── Load/Store Unit
├── L2 Cache（全 GPU 共享，约 50-80MB on H100）
├── HBM（High Bandwidth Memory，显存，约 80GB on H100 SXM）
└── NVLink / PCIe（片间互联）
```

### NVIDIA GPU 代际演进

| 架构 | 代表产品 | Tensor Core 精度 | HBM 带宽 | 关键特性 |
|------|----------|-----------------|---------|----------|
| Volta（2017）| V100 | FP16 | 900 GB/s | 首代 Tensor Core |
| Ampere（2020）| A100 | BF16/TF32/INT8/FP64 | 2 TB/s | MIG、NVLink 3.0 |
| Hopper（2022）| H100 | FP8 | 3.35 TB/s | Transformer Engine、NVLink 4.0、TMA |
| Blackwell（2024）| B200 | FP4 | 8 TB/s | 2-chip 封装、NVLink 5.0 |

**关键概念：**
- **Tensor Core**：专为矩阵乘加（MMA）设计，D = A×B + C，一个时钟周期完成 4×4 矩阵乘。GEMM、Attention 计算的主力。
- **Warp**：32 个线程组成的执行单元，SIMT 执行，所有线程同一时刻执行同一条指令（分支时会序列化）
- **Occupancy**：SM 上活跃 warp 数 / 最大 warp 数，高 occupancy 有助于隐藏内存延迟

**推荐阅读：**
- [NVIDIA Hopper Architecture 白皮书](https://resources.nvidia.com/en-us-tensor-core/gtc22-whitepaper-hopper)
- [NVIDIA GPU 架构系列（知乎 @BBuf）](https://zhuanlan.zhihu.com/p/654012273)
- [Dissecting the NVIDIA Volta GPU Architecture](https://arxiv.org/abs/1804.06826)

---

## 内存层次与带宽

```
速度（快→慢）        容量（小→大）         延迟参考（H100）

Register File        ~256KB/SM             ~1 cycle
Shared Memory/L1     ~228KB/SM             ~30 cycles
L2 Cache             ~50MB                 ~200 cycles
HBM（显存）          80GB                  ~500 cycles，带宽 3.35 TB/s
NVLink（GPU间）      -                     μs 级，带宽 900 GB/s (H100)
InfiniBand（节点间） -                     μs 级，带宽 400 Gb/s
DRAM（主机内存）     ~TB 级                ~200 ns
```

### Roofline Model（屋顶线模型）

判断一个算子是 Compute-bound 还是 Memory-bound 的核心工具：
- **算术强度（Arithmetic Intensity）** = FLOPs / Bytes（计算量/内存访问量）
- 算术强度高（如 GEMM）→ Compute-bound
- 算术强度低（如 LayerNorm、Softmax）→ Memory-bound
- FlashAttention 的核心思路就是通过 tiling 提高 Attention 的算术强度

**必读**：[EfficientML Roofline Model 讲解](https://efficientml.ai/)

---

## 内存访问优化

| 概念 | 说明 |
|------|------|
| **Coalesced Access（合并访问）** | 同一 warp 内线程访问连续内存地址，合并为一次事务，带宽最优 |
| **Bank Conflict** | Shared Memory 分 32 个 bank，同一 warp 多线程访问同一 bank 会序列化 |
| **cp.async（异步拷贝）** | 数据从 HBM 直接异步搬到 Shared Memory，不占寄存器，隐藏延迟 |
| **TMA（Tensor Memory Accelerator）** | H100 新增，硬件直接搬运多维 tensor，减少 SM 开销 |
| **Double Buffering** | 预取下一块数据的同时计算当前块，隐藏内存延迟 |

---

## Tensor Core 与 GEMM

**GEMM 优化层次（从高到低）：**
```
cuBLAS（NVIDIA 官方库，大多数场景够用）
  ↓
CUTLASS / CuTe（更灵活，可定制 tile 大小、epilogue）
  ↓
TileLang / Triton（Python DSL，快速实现自定义 GEMM 变体）
  ↓
PTX / SASS（汇编级，极限调优）
```

**必读**：
- [How to Optimize a CUDA Matmul Kernel（Simon Boehm）](https://siboehm.com/articles/22/CUDA-MMM)
- [CUTLASS 文档](https://github.com/NVIDIA/cutlass)

---

## GPU 互联拓扑

### 机内互联（NVLink / NVSwitch）

| 产品 | 互联方式 | 带宽 |
|------|----------|------|
| A100 SXM（8卡）| NVLink 3.0 + NVSwitch | 600 GB/s 双向/卡 |
| H100 SXM（8卡）| NVLink 4.0 + NVSwitch | 900 GB/s 双向/卡 |
| B200 NVL72 | NVLink 5.0 全互联 | 1.8 TB/s 双向/卡 |

- NVSwitch 实现全连接拓扑，任意两卡直接通信，无需经过 PCIe
- PCIe 带宽（~64 GB/s 双向）远低于 NVLink，是 CPU-GPU 数据传输瓶颈

### 机间互联（InfiniBand / RoCE）

| 技术 | 带宽 | 特点 |
|------|------|------|
| InfiniBand HDR | 200 Gb/s/端口 | 低延迟，AI 训练首选 |
| InfiniBand NDR | 400 Gb/s/端口 | 当前主流 |
| RoCE v2 | 取决于以太网 | 成本低，延迟略高 |

- NCCL 自动检测拓扑，优先走 NVLink，其次 PCIe，最后网络

---

## 其他加速器架构简介

| 加速器 | 厂商 | 特点 |
|--------|------|------|
| **TPU v5** | Google | 脉动阵列（Systolic Array），JAX 原生 |
| **Ascend 910B** | Huawei | 达芬奇架构，CANN 软件栈 |
| **AMD MI300X** | AMD | HBM3，192GB 超大显存，ROCm 软件栈 |
| **Gaudi 3** | Intel | Habana SynapseAI 框架 |

**必读**：[TPU v1 论文](https://arxiv.org/abs/1704.04760)

---

## 性能分析工具

| 工具 | 用途 |
|------|------|
| **Nsight Compute（ncu）** | Kernel 级，显示 SM 利用率、内存带宽、Tensor Core 利用率 |
| **Nsight Systems（nsys）** | 系统级 timeline，看 CPU-GPU overlap、NCCL 通信 |
| **PyTorch Profiler** | Python 层分析，`torch.profiler.profile()` |

```bash
ncu --metrics sm__throughput.avg,dram__throughput.avg \
    --target-processes all python your_kernel.py
```

---

## 推荐学习资源

| 资料 | 说明 |
|------|------|
| 《Computer Architecture: A Quantitative Approach》 | 体系结构经典教材（Hennessy & Patterson）|
| [CMU 15-418 / Stanford CS149](http://cs149.stanford.edu/fall21/) | 并行计算课程，含 GPU 编程模型 |
| [MIT 6.5930: Hardware Architecture for Deep Learning](https://www.eecs.mit.edu/) | 深度学习硬件专项 |
| [GPU MODE（CUDA Mode）](https://github.com/cuda-mode) | 实战向 GPU 编程讲座 |
| [How GPU Computing Works（GTC 2021）](https://www.nvidia.com/en-us/on-demand/session/gtcspring21-s31151/) | NVIDIA 官方入门讲座 |

