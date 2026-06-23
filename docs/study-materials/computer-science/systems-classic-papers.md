# Systems Classic Papers

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Computer Science / Systems / Distributed Systems / Databases / ML Systems |
| 材料类型 | 论文路线 / 经典系统 |
| 难度 | 中级到进阶 |
| 优先级 | P0 / Classic |
| 状态 | 推荐 |
| 建议用途 | 为 AI Infra、后端、分布式、数据库和系统研究补齐经典系统论文底座 |

---

## 先看结论

1. AI Infra 不是凭空出现的，很多设计来自分布式系统、数据库、调度、存储和数据流系统。
2. 必读主线：Lamport Clock / Paxos / Raft → GFS / MapReduce / Bigtable → Dynamo / Spanner → Borg / Kubernetes → TensorFlow / Ray / MLPerf。
3. 读系统论文时不要只记架构图，要问：问题定义、假设、瓶颈、核心机制、故障模型、评估指标、今天是否仍适用。

---

## 知识地图

```text
Distributed Systems Foundations
  → Storage / Data Processing
  → Databases / Transactions
  → Cluster Scheduling
  → Dataflow / Stream Processing
  → ML Systems / AI Infra
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | Time, Clocks, and the Ordering of Events | 论文 | Lamport clock，分布式系统时间与因果关系基础 |
| P0 | Paxos Made Simple | 论文 | 共识算法经典 |
| P0 | Raft | 论文 | 工程友好的共识算法 |
| P0 | Google File System / GFS | 论文 | 分布式文件系统经典 |
| P0 | MapReduce | 论文 | 大规模数据处理范式 |
| P0 | Bigtable | 论文 | 分布式结构化存储经典 |
| P0 | Dynamo | 论文 | eventual consistency 和 AP 系统代表 |
| P0 | Spanner | 论文 | 全球分布式事务和 TrueTime |
| P0 | Borg / Omega / Kubernetes | 论文 / 系统 | 集群调度和容器编排主线 |
| P1 | TensorFlow / Ray / MLPerf | 论文 / 系统 | ML Systems 和 AI Infra 入口 |

---

## 1. 分布式系统基础

- **Lamport Clock**：分布式事件排序和 happens-before。
- **Paxos / Raft**：共识、leader election、日志复制。
- **CAP / FLP**：理解一致性、可用性、分区容忍和不可能性边界。

---

## 2. 存储与数据处理

- **GFS**：chunk server、master、replication。
- **MapReduce**：map/shuffle/reduce，数据并行处理范式。
- **Bigtable**：tablet、SSTable、LSM-like 结构。
- **Dynamo**：consistent hashing、vector clock、quorum。
- **Spanner**：TrueTime、全球事务。

---

## 3. 数据库经典

- **System R**：关系数据库、优化器、SQL。
- **Volcano**：iterator model / query execution。
- **The Log-Structured Merge-Tree**：现代 KV / storage engine 基础。
- **C-Store / Column Stores**：列存和分析型数据库。
- **Calvin**：deterministic transaction processing。
- **FaRM**：RDMA database。

---

## 4. 调度与集群管理

- **Borg**：Google 大规模集群管理。
- **Omega**：shared-state scheduling。
- **Kubernetes**：容器编排生态。
- **Mesos**：two-level scheduling。
- **Sparrow / Firmament**：调度策略和低延迟任务。

---

## 5. ML Systems / AI Infra

| 材料 | 重点 |
|------|------|
| TensorFlow | dataflow graph 和 ML runtime |
| PyTorch design | eager execution 和动态图生态 |
| Ray | 分布式 Python / RL / serving |
| Horovod | 分布式训练工程化 |
| DeepSpeed / ZeRO | 大模型训练优化 |
| Megatron-LM | tensor parallelism |
| GShard / Switch Transformer | MoE 系统 |
| MLPerf | AI benchmark 方法论 |

---

## 读论文模板

每篇系统论文建议记录：

```markdown
## Problem
## Assumptions
## Key Idea
## Architecture
## Failure Model
## Evaluation
## Limitations
## What still matters today
```

---

## 实践项目 / 完成标准

### Project 1：System Paper Review Matrix

- 选择 10 篇系统论文。
- 用统一模板整理问题、机制、评估、局限。
- 完成标准：能画出这些系统之间的演化关系。

### Project 2：Mini MapReduce / KV Store

- 实现 toy MapReduce 或 replicated KV store。
- 加入故障恢复和简单 benchmark。
- 完成标准：能解释数据切分、调度、容错和吞吐瓶颈。

---

## 延伸资料

- CS 公开课：`open-courses.md`
- AI Infra：`../ai-infra/README.md`
- 分布式训练：`../ai-infra/03-distributed-training.md`
- 网络与存储：`../ai-infra/05-network-storage.md`

### 补充：Anna

- **Anna**：cloud-native key-value store，强调多一致性级别、弹性伸缩和 actor-style execution，可作为 Dynamo、Cassandra、FaRM 之后理解 elastic storage system 的补充材料。
