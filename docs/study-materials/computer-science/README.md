# Computer Science

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Computer Science |
| 材料类型 | 索引 / 路线 |
| 难度 | 入门 |
| 优先级 | P0 / Classic / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 系统补齐 CS 基础 |

---

这个目录整理高质量 CS 公开课和计算机基础学习路线，适合系统补齐编程、算法、系统、数据库、网络、分布式和 AI 基础。

---

## 先看结论

如果目标是长期技术成长，不建议只追热点。最稳的路线是：

```text
编程抽象 → 数据结构 → 算法 → 计算机系统 → 操作系统 → 数据库 → 网络 / 分布式 → AI / ML 专题
```

公开课的价值不只在视频，更在 **作业、Lab、项目和课程资料**。能做完 Lab 的课程，优先级通常高于只看视频的课程。

课程选择原则：

| 类型 | 判断标准 |
|------|----------|
| 必读核心 | 能长期提升编程、系统、算法和工程能力 |
| 方向核心 | 和目标方向直接相关，如 AI Infra、数据库、安全、编译器 |
| 选择性专题 | 有兴趣或项目需要时再补，不必一开始全学 |

---

## 推荐学习路线

### 路线 A：CS 基础补全

适合目标：系统补齐 CS 本科核心能力。

1. Harvard CS50x 或 Berkeley CS61A
2. Berkeley CS61B
3. MIT 6.006
4. CMU 15-213 / CSAPP
5. MIT 6.S081 / Berkeley CS162
6. CMU 15-445 / Berkeley CS186
7. MIT 6.5840

完成标准：至少完成 3 门带 Lab 的课，而不是只看视频。

### 路线 B：AI Infra / LLM Systems

适合目标：进入大模型训练、推理、系统优化、AI Infra。

1. CMU 15-213 / CSAPP
2. Stanford CS149 或 Berkeley CS267
3. Stanford CS336
4. CMU 10-414 / 10-714 Deep Learning Systems
5. MIT 6.5840
6. CMU 15-445
7. Stanford CS144

完成标准：能理解 GPU / 并行计算、分布式训练、LLM 推理和存储网络瓶颈。

### 路线 C：后端 / 分布式 / 数据库

适合目标：后端基础设施、数据库、分布式系统、存储系统。

1. Berkeley CS61B
2. CMU 15-213 / CSAPP
3. MIT 6.S081 / Berkeley CS162
4. CMU 15-445 / Berkeley CS186
5. MIT 6.5840
6. Stanford CS144 / CMU 15-441

完成标准：能实现或解释一个 KV store、事务系统、Raft、TCP 基础组件。

### 路线 D：少而精压缩路线

如果时间有限，优先：

```text
CS61A / CS50x → CS61B → CSAPP → 6.S081 → 15-445 → 6.5840 → CS336 / CS149
```

---

## 如果只学 10 门

1. [Berkeley CS61A](https://cs61a.org/) — 编程抽象与 SICP 思想
2. [Berkeley CS61B](https://www.datastructur.es/) — 数据结构与工程化编程
3. [MIT 6.006](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/) — 算法基础
4. [CMU 15-213 / CSAPP](https://www.cs.cmu.edu/~213/) — 计算机系统
5. [MIT 6.S081 / 6.1810](https://pdos.csail.mit.edu/6.1810/) — 操作系统工程
6. [CMU 15-445](https://15445.courses.cs.cmu.edu/) — 数据库系统
7. [MIT 6.5840](https://pdos.csail.mit.edu/6.824/) — 分布式系统
8. [Stanford CS144](https://cs144.github.io/) — 计算机网络
9. [Stanford CS224n](https://web.stanford.edu/class/cs224n/) / [CS231n](http://cs231n.stanford.edu/) — 深度学习专题
10. [Stanford CS336](https://stanford-cs336.github.io/spring2025/) — Language Modeling from Scratch

---

## 详细课程清单

- [CS 公开课资源整理](open-courses.md)

---

## 完成标准

学完这个方向，不是“看过视频”，而是应该能做到：

- 用递归、抽象和数据结构写出清晰程序；
- 能分析常见算法复杂度；
- 能解释程序从源代码到执行的基本路径：编译、链接、内存、系统调用；
- 能实现或修改一个小型 OS / DB / Distributed System Lab；
- 能读懂现代 AI / Infra 课程对系统、网络、并发和性能的要求。

---

## 系统经典论文路线

- [Systems Classic Papers](systems-classic-papers.md)：Lamport Clock、Paxos、Raft、GFS、MapReduce、Bigtable、Dynamo、Spanner、Borg、TensorFlow、Ray、MLPerf。

---

## 经典书籍补充清单

| 优先级 | 书籍 | 方向 | 为什么重要 |
|--------|------|------|------------|
| P0 | CSAPP | 计算机系统 | 程序、内存、链接、并发、系统性能的共同底座 |
| P0 | SICP | 程序设计思想 | 抽象、解释器、语言设计和程序构造经典 |
| P0 | Designing Data-Intensive Applications / DDIA | 数据系统 | 分布式存储、数据流、一致性和系统设计入门经典 |
| P0 | OSTEP | 操作系统 | 进程、线程、虚拟内存、文件系统的可读教材 |
| P0 | CLRS | 算法 | 算法分析和经典算法参考书 |
| P1 | Computer Networking: A Top-Down Approach | 计算机网络 | 网络协议栈和互联网系统入门经典 |
| P1 | Database System Concepts | 数据库 | SQL、事务、优化器、存储和并发控制基础 |
| P1 | Compilers: Principles, Techniques, and Tools | 编译器 | 词法、语法、优化和代码生成经典教材 |
| P1 | The Datacenter as a Computer | 数据中心 | 数据中心硬件、网络、能耗和系统设计全局视角 |
| P1 | Site Reliability Engineering | SRE | 生产系统可靠性、SLO、事故复盘和运维工程经典 |
