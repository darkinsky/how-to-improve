# 03. 分布式训练

> 训练千亿参数模型需要数百甚至数千张 GPU 协同工作。分布式训练是 AI Infra 的核心挑战之一。

---

## 并行策略全景

```
单机单卡
  └─ 单机多卡（DDP）
       └─ 多机多卡
            ├─ 数据并行（DP / DDP / FSDP / ZeRO）
            ├─ 张量并行（TP）
            ├─ 流水线并行（PP）
            ├─ 序列并行（SP）
            └─ 混合并行（TP + PP + DP = 3D Parallel）
```

**选择原则：**
- 模型放得下单卡 → DDP 优先
- 模型放不下单卡但放得下单机 → FSDP 或 ZeRO-2/3
- 需要多机 → 机内 TP + 机间 PP + 数据并行 的 3D 混合

---

## 数据并行（Data Parallelism）

**原理**：每张卡持有完整模型副本，数据切分后各卡独立前向/后向，最后通过 AllReduce 同步梯度。

### 方案对比

| 方案 | 切分内容 | 通信量 | 显存节省 | 适用场景 |
|------|----------|--------|----------|----------|
| **DDP** | 无（每卡完整副本）| 梯度 AllReduce | 无 | 模型可放单卡 |
| **ZeRO-1** | optimizer state | 同 DDP | ~4x | 模型勉强放单卡 |
| **ZeRO-2** | optimizer state + gradient | 同 DDP | ~8x | 中等模型 |
| **ZeRO-3** | optimizer state + gradient + param | 更多 AllGather | ~64x | 超大模型 |
| **FSDP** | 同 ZeRO-3，PyTorch 原生实现 | 同 ZeRO-3 | ~64x | PyTorch 生态首选 |

### ZeRO 显存分析（以 7B 模型 FP16 为例）

```
参数量：7B × 2 bytes(FP16) = 14 GB
梯度：  7B × 2 bytes = 14 GB
优化器状态（Adam）：7B × 12 bytes(FP32 param + m + v) = 84 GB
总计：~112 GB（8卡 A100 单卡 80GB 放不下）

ZeRO-3 后（8卡）：
参数：14/8 = 1.75 GB/卡（用时 AllGather）
梯度：14/8 = 1.75 GB/卡（用时 ReduceScatter）
优化器：84/8 = 10.5 GB/卡
实际约 ~14 GB/卡 → 可放下
```

**必读**：
- [ZeRO 论文](https://arxiv.org/abs/1910.02054)
- [FSDP Tutorial](https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html)
- [DeepSpeed ZeRO 文档](https://www.deepspeed.ai/tutorials/zero/)

---

## 张量并行（Tensor Parallelism）

**原理**：将单个权重矩阵按行/列切分到多卡，每张卡只持有矩阵的一部分。

### MLP 切分方式（Megatron 风格）

```
Input X [B, S, H]
  ↓
Linear1（列切分）：每卡持有 W1 的 1/N 列，输出 [B, S, H/N]
  ↓（无需通信，各卡独立计算）
GELU（逐元素，各卡独立）
  ↓
Linear2（行切分）：每卡持有 W2 的 1/N 行，输出 [B, S, H]
  ↓
AllReduce（各卡结果求和，得到完整输出）
```

### Attention 切分方式

- Q/K/V 投影矩阵按 head 切分，每卡负责 num_heads/N 个头
- Output 投影按行切分，之后 AllReduce

**注意事项：**
- TP 机内 NVLink 效率好，机间不推荐（带宽差 10x+）
- 一般 TP=4 或 TP=8（机内 8 卡全 NVLink）

**必读**：
- [Megatron-LM 论文](https://arxiv.org/abs/1909.08053)
- [Megatron-LM GitHub](https://github.com/NVIDIA/Megatron-LM)

---

## 流水线并行（Pipeline Parallelism）

**原理**：将模型按层切分，每台机器负责若干层，数据以 micro-batch 流水方式流过各阶段。

### Pipeline Bubble 问题

```
朴素流水线（F=前向，B=后向）：
阶段1：F1 F2 F3 F4 [bubble] B4 B3 B2 B1
阶段2：   F1 F2 F3 F4 [bubble] B4 B3 B2 B1
...
bubble ratio = (p-1)/(m+p-1)，p=流水线段数，m=micro-batch数
```

### 调度优化

| 调度方式 | 说明 | bubble ratio |
|----------|------|------------|
| **GPipe** | 全部 F 完成后再全部 B | (p-1)/(m+p-1) |
| **1F1B** | 每完成一个 F 立即做对应 B | 同 GPipe，但显存省 |
| **Interleaved 1F1B** | 每卡持有多个非连续 layer chunk | (p-1)/(m×v+p-1)，v=chunk数 |

**必读**：
- [GPipe 论文](https://arxiv.org/abs/1811.06965)
- [PipeDream 论文](https://arxiv.org/abs/1806.03377)
- [Efficient Large Scale LM Training（3D Parallel）](https://arxiv.org/abs/2104.04473)

---

## 序列并行（Sequence Parallelism）

**原理**：将序列维度（token 维度）切分到多卡，配合 TP 使用，解决长序列 Attention 显存瓶颈。

- TP 组内用 AllGather/ReduceScatter 同步序列维度
- 超长序列训练（128K+ context）几乎必用

**Ring Attention**（更激进）：将 Attention 计算本身也分布式化，每卡只负责部分 KV，token 在 ring 上传递。

**必读**：
- [Sequence Parallelism 论文](https://arxiv.org/abs/2205.05198)
- [Ring Attention](https://arxiv.org/abs/2310.01889)

---

## 训练优化技术

| 技术 | 说明 | 收益 |
|------|------|------|
| **混合精度（AMP）** | FP16/BF16 前向，FP32 梯度累积 | 显存减半，速度 2x |
| **梯度累积** | 多个 micro-batch 累积后再更新 | 等效增大 batch size |
| **Activation Recomputation** | 不存中间激活，反向时重算 | 省 ~60% 激活显存 |
| **FlashAttention** | I/O-Aware Attention tiling | 速度 2-4x，显存 O(N)→O(√N) |
| **torch.compile** | JIT 编译计算图 | 减少 Python overhead，提速 10-30% |
| **CUDA Graph** | 录制静态 kernel 序列 | 消除 launch overhead，对小 batch 效果显著 |

---

## 框架速查

| 框架 | 定位 | 链接 |
|------|------|------|
| **Megatron-LM** | 工业级，TP/PP/SP 全支持，NVIDIA 维护 | https://github.com/NVIDIA/Megatron-LM |
| **DeepSpeed** | ZeRO 系列 + pipeline engine，微软维护 | https://github.com/microsoft/DeepSpeed |
| **PyTorch FSDP** | PyTorch 原生，ZeRO-3 等价实现 | https://pytorch.org/tutorials/intermediate/FSDP_tutorial.html |
| **Megatron-DeepSpeed** | 两者结合 | https://github.com/microsoft/Megatron-DeepSpeed |

---

## 学习路线

```
第一步：单机多卡 DDP
  torch.nn.parallel.DistributedDataParallel
  → 跑通 2 卡训练 GPT-2

第二步：ZeRO 显存优化
  DeepSpeed ZeRO-2/3 配置实验
  → 对比显存占用变化

第三步：张量并行
  读 Megatron-LM 论文 + 代码（megatron/core/tensor_parallel/）
  → 理解列并行/行并行 Linear 实现

第四步：流水线并行
  读 GPipe + 1F1B 论文
  → 在 Megatron-LM 上跑 PP 实验，观察 bubble

第五步：3D 并行
  结合 TP+PP+DP 跑 LLaMA-7B 训练
  → 调整并行配置观察吞吐量变化
```

