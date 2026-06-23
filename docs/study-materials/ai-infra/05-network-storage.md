# 05. 网络与存储

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | AI Infra |
| 材料类型 | 系统 / 工程实践 |
| 难度 | 进阶 |
| 优先级 | P1 / Hands-on |
| 状态 | 可用 |
| 建议用途 | 理解训练和推理中的网络与存储瓶颈 |

---

> 分布式训练中，网络通信和存储 I/O 往往是隐藏的性能瓶颈。GPU 算力提升的同时，通信和 I/O 能力跟上了吗？

---

## 先看结论

- 网络与存储是大规模训练 / 推理中最容易被低估的瓶颈：GPU 空转往往不是算子问题，而是通信或 I/O 跟不上。
- 训练侧重点是 collective communication：AllReduce、ReduceScatter、AllGather、AllToAll 决定 DP、ZeRO、TP、MoE 的效率。
- 拓扑很关键：NVLink、PCIe、InfiniBand、RoCE 的带宽和延迟差异会直接改变并行策略选择。
- 存储侧重点是数据供给：dataset sharding、prefetch、cache、checkpoint 读写、对象存储和并行文件系统都会影响吞吐。
- 调试优先看 NCCL 日志、拓扑、带宽测试、GPU utilization、dataloader wait time 和 checkpoint 时间。
- 完成标准：能解释一次多机训练中的梯度同步路径，并定位是网络、存储还是计算导致 GPU 利用率下降。

---

## 集合通信（Collective Communication）

### 核心操作

| 操作 | 说明 | 常见用途 |
|------|------|----------|
| **AllReduce** | 所有卡的数据求和/求均值，结果广播到所有卡 | DDP 梯度同步 |
| **AllGather** | 每卡贡献一份数据，所有卡得到完整拼接 | ZeRO-3 参数收集、TP |
| **ReduceScatter** | AllReduce 的分解步骤，每卡只保留部分结果 | ZeRO 梯度切分 |
| **Broadcast** | 一张卡的数据发送给所有卡 | 初始化参数同步 |
| **AllToAll** | 每卡向每张卡发送不同数据 | MoE 专家路由 |

### NCCL

- **GitHub**：https://github.com/NVIDIA/nccl
- **文档**：https://docs.nvidia.com/deeplearning/nccl/user-guide/
- NVIDIA 集合通信库，PyTorch distributed 默认后端
- 自动检测拓扑，优先 NVLink > NVLink + PCIe > 网络

**常用调试环境变量：**
```bash
NCCL_DEBUG=INFO          # 打印 NCCL 初始化和拓扑信息
NCCL_TOPO_DUMP_FILE=topo.xml  # 导出拓扑图
NCCL_ALGO=Ring           # 强制使用 Ring AllReduce
NCCL_PROTO=Simple        # 协议选择
NCCL_IB_DISABLE=1        # 禁用 InfiniBand（调试用）
```

### 通信拓扑与带宽

```
机内通信（同一台机器内）：
  NVLink 4.0（H100 SXM）：900 GB/s 双向/卡
  NVLink 3.0（A100 SXM）：600 GB/s 双向/卡
  PCIe 5.0：              ~128 GB/s 双向（比 NVLink 慢 ~7x）

机间通信（跨节点）：
  InfiniBand NDR：        400 Gb/s ≈ 50 GB/s 单端口
  InfiniBand HDR：        200 Gb/s ≈ 25 GB/s 单端口
  RoCE v2（以太网 RDMA）：带宽近似 IB，延迟略高
```

### 通信性能分析

**AllReduce 理论时延（Ring 算法）：**
```
Time = 2 × (N-1)/N × Data_Size / Bandwidth
N = GPU 数量

示例：8 卡 A100，同步 7B 模型梯度（14GB）
Time = 2 × 7/8 × 14GB / 600GB/s ≈ 40ms
```

**通信计算 overlap：**
- DDP/ZeRO 支持 bucket 级别梯度通信与反向计算重叠
- Megatron-LM 中 TP 的 AllReduce 与下一层计算重叠
- 用 Nsight Systems 可视化 overlap 程度

### 推荐资料

- [NCCL User Guide](https://docs.nvidia.com/deeplearning/nccl/user-guide/) 与 [NVIDIA NCCL GitHub](https://github.com/NVIDIA/nccl)
- [NCCL 算法原理（知乎，中文补充）](https://zhuanlan.zhihu.com/p/364816069)
- [Bandwidth Optimal All-reduce Algorithms（Ring AllReduce 原论文）](https://arxiv.org/abs/1811.05233)
- [MegaScale: Scaling LLM Training to 10,000 GPUs](https://arxiv.org/abs/2402.15627) — 万卡训练网络挑战实战

---

## InfiniBand 与 RDMA

### 为什么用 InfiniBand

| 对比维度 | 普通以太网 TCP | InfiniBand RDMA |
|----------|--------------|------------------|
| 延迟 | ~100 μs | ~1 μs |
| CPU 开销 | 高（内核协议栈）| 极低（零拷贝）|
| 带宽利用率 | ~60-70% | ~95%+ |

### RDMA 核心概念

- **RDMA（Remote Direct Memory Access）**：一台机器直接读写另一台机器内存，不经过 CPU
- **零拷贝**：数据不经过用户态/内核态拷贝，直接 DMA 传输
- **RoCE（RDMA over Converged Ethernet）**：在以太网上实现 RDMA，成本低于 IB，延迟略高

### 常见问题排查

```bash
# 查看 IB 设备
ibstat
ibstatus

# 测试 IB 带宽
ib_write_bw -d mlx5_0 -i 1

# 查看 NCCL 是否用上 IB
export NCCL_DEBUG=INFO
# 日志中看到 NET/IB 表示用了 IB
```

---

## 训练数据存储

### 存储选型

| 存储类型 | 代表产品 | 适用场景 | 注意事项 |
|----------|----------|----------|----------|
| **本地 NVMe SSD** | - | 单机训练，最快 | 无法跨节点共享 |
| **分布式文件系统** | Lustre、GPFS | HPC 集群标配 | 配置复杂 |
| **对象存储** | S3、COS、OSS | 云环境数据湖 | 随机读性能差 |
| **云原生分布式 FS** | JuiceFS、CubeFS | 云环境训练 | 兼顾性能与弹性 |

### JuiceFS

- **GitHub**：https://github.com/juicedata/juicefs
- 元数据存 Redis/TiKV，数据存对象存储（S3/COS）
- 支持 POSIX 接口，对训练框架透明
- 适合云上大规模训练数据共享

### 训练 I/O 优化

```
常见 I/O 瓶颈排查路径：

1. GPU 等待数据？
   → 看 DataLoader 是否瓶颈
   → 增加 num_workers，使用 pin_memory=True

2. DataLoader 够快但存储慢？
   → 用 iostat/iotop 观察磁盘带宽
   → 考虑本地缓存或换更快存储

3. 数据已在内存但还慢？
   → 看预处理是否 CPU 瓶颈
   → 使用 webdataset 等流式格式
```

**推荐数据格式：**
- **WebDataset**：tar 打包流式读取，适合大规模图文数据
- **MosaicML StreamingDataset**：支持随机 shuffle 的流式数据集
- **tfrecord / Arrow（HuggingFace datasets）**：NLP 训练常用

---

## 推荐资料

| 资料 | 说明 |
|------|------|
| [NCCL 文档](https://docs.nvidia.com/deeplearning/nccl/user-guide/) | 官方必读 |
| [MegaScale 论文](https://arxiv.org/abs/2402.15627) | 字节万卡训练经验，网络章节精彩 |
| [Efficient Large-Scale LLM Training on GPU Clusters](https://arxiv.org/abs/2104.04473) | 通信优化实战 |
| [JuiceFS 文档](https://juicefs.com/docs/zh/community/introduction/) | 云原生分布式存储 |
