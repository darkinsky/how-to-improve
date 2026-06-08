# CS 公开课资源整理

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Computer Science |
| 材料类型 | 课程 / 索引 |
| 难度 | 入门到进阶 |
| 优先级 | P0 / Classic / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 选择高质量 CS 公开课 |

---

> 面向自学计算机科学与 AI Infra / 大模型工程的公开课程清单。优先收录有官网、公开视频、公开讲义或公开 Lab 的课程。
>
> 使用建议：不要一次性全学。先根据目标选 1 条主线，把课程视频、作业 / Lab 和项目做完，比泛泛收藏更重要。

---

## 快速选课建议

| 目标 | 推荐优先级 |
|------|------------|
| 零基础入门 CS | CS50x → CS61A / CS106A → CS61B |
| 夯实算法与数据结构 | CS61B → MIT 6.006 → MIT 6.046 / Princeton Algorithms |
| 走系统 / 后端 / Infra | CSAPP → MIT 6.S081 / 6.1810 → CMU 15-445 → MIT 6.5840 |
| 走大模型 / AI Infra | CS229 → CS224n / CS231n → CS336 → CS149 / CS267 / Deep Learning Systems |
| 走安全 / 网络 / 编译器 | CS144 / 15-441 → CS155 / CS161 → CS143 |

---

## 1. 大模型 / 机器学习 / AI

### Stanford CS336 — Language Modeling from Scratch

- 学校：Stanford
- 主页：[CS336: Language Modeling from Scratch](https://stanford-cs336.github.io/spring2025/)
- 主题：LLM 数据、Tokenizer、Transformer、训练、推理、评测、Scaling Laws
- 适合：想理解大模型从零训练链路、LLM Infra、训练系统的学习者
- 难度：★★★★☆
- 前置：Python、PyTorch、深度学习基础、一定系统基础
- 推荐理由：非常贴近现代 LLM 工程实践，不只是讲模型结构，也覆盖数据、训练与推理系统。

### Stanford CS229 — Machine Learning

- 学校：Stanford
- 主页：[CS229: Machine Learning](https://cs229.stanford.edu/)
- 主题：监督学习、生成模型、SVM、EM、强化学习基础、泛化理论
- 适合：系统补机器学习理论基础
- 难度：★★★★☆
- 前置：线性代数、概率论、微积分、基础编程
- 推荐理由：经典 ML 课程，适合作为深度学习和 LLM 课程之前的理论底座。

### Stanford CS224n — Natural Language Processing with Deep Learning

- 学校：Stanford
- 主页：[CS224n](https://web.stanford.edu/class/cs224n/)
- 主题：词向量、RNN、Seq2Seq、Attention、Transformer、预训练语言模型
- 适合：NLP、Transformer、LLM 应用与研究入门
- 难度：★★★★☆
- 前置：Python、PyTorch、机器学习基础
- 推荐理由：NLP 深度学习经典课，和 CS336 互补。

### Stanford CS231n — Deep Learning for Computer Vision

- 学校：Stanford
- 主页：[CS231n](http://cs231n.stanford.edu/)
- 主题：CNN、反向传播、优化、视觉模型、深度学习实践
- 适合：深度学习入门到中级，尤其是视觉方向
- 难度：★★★☆☆
- 前置：Python、NumPy、基础机器学习
- 推荐理由：虽然主题是 CV，但对理解深度学习训练、优化、反向传播很有帮助。

### Berkeley CS285 — Deep Reinforcement Learning

- 学校：UC Berkeley
- 主页：[CS285: Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/)
- 主题：Policy Gradient、Actor-Critic、Model-Based RL、Offline RL
- 适合：强化学习方向深入学习
- 难度：★★★★★
- 前置：深度学习、概率、优化、PyTorch
- 推荐理由：深度强化学习代表性课程，适合已有 ML / DL 基础后深入。

### MIT 6.S191 — Introduction to Deep Learning

- 学校：MIT
- 主页：[MIT 6.S191](http://introtodeeplearning.com/)
- 主题：深度学习基础、CNN、RNN、生成模型、强化学习、AI 应用
- 适合：快速入门深度学习
- 难度：★★☆☆☆
- 前置：Python 基础、机器学习基础更佳
- 推荐理由：短小精悍，适合快速建立全局认知。

### CMU 10-414 / 10-714 — Deep Learning Systems

- 学校：Carnegie Mellon University
- 主页：[Deep Learning Systems](https://dlsyscourse.org/)
- 主题：自动微分、张量库、深度学习框架、模型训练系统
- 适合：想理解 PyTorch / TensorFlow 这类框架底层的人
- 难度：★★★★★
- 前置：深度学习、系统编程、C++ / Python
- 推荐理由：连接深度学习算法与系统实现，非常适合 AI Infra 方向。

---

## 2. 编程基础 / CS 入门

### Harvard CS50x — Introduction to Computer Science

- 学校：Harvard
- 主页：[CS50x](https://cs50.harvard.edu/x/)
- 主题：C、Python、SQL、Web、算法、数据结构、计算机科学导论
- 适合：零基础或需要补 CS 入门的人
- 难度：★★☆☆☆
- 前置：无
- 推荐理由：制作精良、作业有趣，是最适合入门的公开课之一。

### Berkeley CS61A — Structure and Interpretation of Computer Programs

- 学校：UC Berkeley
- 主页：[CS61A](https://cs61a.org/)
- 主题：Python、递归、高阶函数、解释器、抽象、Scheme
- 适合：想建立扎实编程思想的人
- 难度：★★★☆☆
- 前置：基础编程经验更佳
- 推荐理由：不只是学 Python，而是学习抽象、递归、解释器等核心思想。

### Stanford CS106A / CS106B

- 学校：Stanford
- 主页：[CS106A](https://web.stanford.edu/class/cs106a/) / [CS106B](https://web.stanford.edu/class/cs106b/)
- 主题：编程入门、抽象、递归、数据结构、C++
- 适合：偏传统大学 CS 入门路径的学习者
- 难度：CS106A ★★☆☆☆，CS106B ★★★☆☆
- 前置：CS106A 基本无；CS106B 需要基础编程
- 推荐理由：课程体系成熟，适合循序渐进建立编程能力。

---

## 3. 数据结构 / 算法

### Berkeley CS61B — Data Structures

- 学校：UC Berkeley
- 主页：[CS61B](https://www.datastructur.es/)
- 主题：Java、链表、树、图、哈希表、排序、复杂度、软件工程
- 适合：从“会写代码”进阶到“会组织程序”的学习者
- 难度：★★★☆☆
- 前置：基础编程、最好学过 CS61A 或同等内容
- 推荐理由：数据结构与工程实践结合得很好，项目质量高。

### Princeton Algorithms I & II

- 学校：Princeton
- 主页：[Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/)
- Coursera：[Algorithms Part I](https://www.coursera.org/learn/algorithms-part1) / [Algorithms Part II](https://www.coursera.org/learn/algorithms-part2)
- 主题：排序、查找、图算法、字符串算法、最短路、最大流
- 适合：算法入门到中级
- 难度：★★★☆☆
- 前置：Java 基础、离散数学基础更佳
- 推荐理由：Robert Sedgewick 经典算法课，讲解清晰、配套资料完整。

### MIT 6.006 — Introduction to Algorithms

- 学校：MIT
- 主页：[MIT 6.006 on OCW](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)
- 主题：复杂度、排序、哈希、树、图、动态规划
- 适合：系统学习算法基础
- 难度：★★★★☆
- 前置：数据结构、离散数学、Python
- 推荐理由：MIT 经典算法入门课，理论与实现兼顾。

### MIT 6.046 — Design and Analysis of Algorithms

- 学校：MIT
- 主页：[MIT 6.046J on OCW](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/)
- 主题：高级数据结构、图算法、随机算法、近似算法、NP 完全性
- 适合：算法进阶
- 难度：★★★★★
- 前置：MIT 6.006 或同等算法基础
- 推荐理由：适合从会用算法提升到理解算法设计与分析。

---

## 4. 计算机系统 / 操作系统 / 底层

### CMU 15-213 / CSAPP — Introduction to Computer Systems

- 学校：Carnegie Mellon University
- 主页：[15-213: Introduction to Computer Systems](https://www.cs.cmu.edu/~213/)
- 书籍主页：[Computer Systems: A Programmer's Perspective](https://csapp.cs.cmu.edu/)
- 主题：数据表示、汇编、链接、异常控制流、虚拟内存、并发、网络编程
- 适合：所有想补系统基础的程序员
- 难度：★★★★☆
- 前置：C 语言、基础数据结构
- 推荐理由：系统方向神课。学完会明显提升对程序运行机制、性能和调试的理解。

### MIT 6.S081 / 6.1810 — Operating System Engineering

- 学校：MIT
- 主页：[6.S081 / 6.1810](https://pdos.csail.mit.edu/6.1810/)
- 主题：xv6、系统调用、页表、进程、文件系统、锁、并发
- 适合：想通过 Lab 真正理解 OS 内核的人
- 难度：★★★★★
- 前置：C、RISC-V / 汇编基础、计算机系统基础
- 推荐理由：Lab 非常经典，是操作系统动手学习的高质量路径。

### Berkeley CS162 — Operating Systems and Systems Programming

- 学校：UC Berkeley
- 主页：[CS162](https://cs162.org/)
- 主题：进程、线程、调度、内存、文件系统、网络、分布式系统基础
- 适合：系统学习操作系统理论与实践
- 难度：★★★★★
- 前置：数据结构、计算机系统基础、C/C++
- 推荐理由：内容覆盖面广，适合作为 OS 系统课主线。

### Stanford CS149 — Parallel Computing

- 学校：Stanford
- 主页：[CS149: Parallel Computing](https://gfxcourses.stanford.edu/cs149/fall23/)
- 主题：并行编程、SIMD、多线程、GPU、性能优化
- 适合：AI Infra、HPC、系统性能优化方向
- 难度：★★★★☆
- 前置：C/C++、计算机系统、基础并发
- 推荐理由：对理解 GPU / 并行计算 / 性能优化非常有帮助。

### Berkeley CS267 — Applications of Parallel Computers

- 学校：UC Berkeley
- 主页：[CS267](https://sites.google.com/lbl.gov/cs267-spr2024/)
- 主题：并行计算、数值计算、通信优化、HPC 应用
- 适合：HPC、科学计算、训练系统性能方向
- 难度：★★★★★
- 前置：系统基础、算法、线性代数、并行编程经验
- 推荐理由：比 CS149 更偏 HPC 与大规模并行应用。

---

## 5. 数据库 / 分布式系统 / 后端核心

### CMU 15-445 / 15-645 — Database Systems

- 学校：Carnegie Mellon University
- 主页：[CMU Database Systems](https://15445.courses.cs.cmu.edu/)
- 主题：存储、索引、查询执行、优化器、事务、并发控制、恢复
- 适合：后端、数据库内核、存储系统方向
- 难度：★★★★☆
- 前置：C++、数据结构、操作系统基础
- 推荐理由：Andy Pavlo 的数据库系统课，配套 BusTub 项目含金量很高。

### Berkeley CS186 — Introduction to Database Systems

- 学校：UC Berkeley
- 主页：[CS186](https://cs186berkeley.net/)
- 主题：关系模型、SQL、索引、查询优化、事务、恢复
- 适合：数据库系统入门
- 难度：★★★☆☆
- 前置：数据结构、基础编程
- 推荐理由：比 CMU 15-445 更本科友好，适合先建立数据库系统全局观。

### MIT 6.824 / 6.5840 — Distributed Systems

- 学校：MIT
- 主页：[6.5840: Distributed Systems](https://pdos.csail.mit.edu/6.824/)
- 主题：MapReduce、Raft、KV Store、复制、容错、一致性、事务
- 适合：分布式系统、后端基础设施方向
- 难度：★★★★★
- 前置：Go、操作系统、网络、并发编程
- 推荐理由：分布式系统神课，Lab 经典但难度较高。

---

## 6. 计算机网络

### Stanford CS144 — Introduction to Computer Networking

- 学校：Stanford
- 主页：[CS144](https://cs144.github.io/)
- 主题：TCP/IP、可靠传输、路由、拥塞控制、应用层协议
- 适合：系统学习网络协议栈
- 难度：★★★★☆
- 前置：C++、计算机系统基础
- 推荐理由：Lab 通常会实现网络协议栈关键组件，动手价值高。

### CMU 15-441 / 15-641 — Computer Networks

- 学校：Carnegie Mellon University
- 主页：[15-441/641 Computer Networks](https://computer-networks.github.io/fa23/)
- 主题：互联网架构、传输层、路由、P2P、CDN、网络应用
- 适合：网络系统方向
- 难度：★★★★☆
- 前置：系统编程、数据结构、基础网络知识
- 推荐理由：网络系统经典课，适合进一步理解互联网基础设施。

---

## 7. 编译原理 / 程序语言

### Stanford CS143 — Compilers

- 学校：Stanford
- 主页：[CS143: Compilers](https://web.stanford.edu/class/cs143/)
- 主题：词法分析、语法分析、语义分析、类型检查、中间表示、代码生成
- 适合：编译器、程序语言、系统工具链方向
- 难度：★★★★☆
- 前置：数据结构、离散数学、C++ / Java 基础
- 推荐理由：经典编译原理课程，适合系统学习编译器 pipeline。

### Berkeley CS164 — Programming Languages and Compilers

- 学校：UC Berkeley
- 主页：[CS164](https://cs164berkeley.github.io/)
- 主题：程序语言、解释器、编译器、类型系统
- 适合：想从 PL 视角理解语言实现的人
- 难度：★★★★☆
- 前置：CS61A / CS61B 或同等基础
- 推荐理由：把语言设计与编译实现结合起来。

### UW CSE 341 — Programming Languages

- 学校：University of Washington
- 主页：[CSE 341](https://courses.cs.washington.edu/courses/cse341/)
- 主题：函数式编程、ML、Racket、Ruby、语言抽象、类型系统
- 适合：想提升编程范式和语言理解的人
- 难度：★★★☆☆
- 前置：数据结构、基础编程
- 推荐理由：对理解函数式编程、抽象和语言设计很有帮助。

---

## 8. 安全 / 密码学

### Stanford CS155 — Computer and Network Security

- 学校：Stanford
- 主页：[CS155](https://cs155.stanford.edu/)
- 主题：系统安全、Web 安全、网络安全、认证、隔离、安全协议
- 适合：安全方向入门到中级
- 难度：★★★★☆
- 前置：操作系统、网络、C/C++ 基础
- 推荐理由：覆盖系统安全与网络安全核心问题。

### Berkeley CS161 — Computer Security

- 学校：UC Berkeley
- 主页：[CS161](https://cs161.org/)
- 主题：内存安全、Web 安全、密码学应用、网络安全
- 适合：计算机安全入门
- 难度：★★★★☆
- 前置：数据结构、系统基础、基础密码学更佳
- 推荐理由：体系完整，适合作为安全方向第一门系统课。

### Stanford CS255 — Cryptography

- 学校：Stanford
- 主页：[CS255: Cryptography](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/)
- 主题：对称加密、公钥加密、数字签名、协议、安全证明
- 适合：密码学理论与应用入门
- 难度：★★★★☆
- 前置：离散数学、概率论、算法基础
- 推荐理由：Dan Boneh 的经典密码学课程。

---

## 9. 软件工程 / Web / 工程实践

### MIT 6.031 — Software Construction

- 学校：MIT
- 主页：[6.031: Software Construction](https://web.mit.edu/6.031/www/sp21/)
- 主题：规格、测试、不可变性、并发、设计、代码质量
- 适合：从“能写代码”进阶到“写可靠代码”的学习者
- 难度：★★★☆☆
- 前置：基础编程、数据结构
- 推荐理由：非常适合补软件工程基本功。

### Berkeley CS169 — Software Engineering

- 学校：UC Berkeley
- 主页：[CS169](https://saasbook.info/)
- 主题：SaaS、敏捷开发、测试、软件工程、团队协作
- 适合：软件工程、Web 应用、团队项目实践
- 难度：★★★☆☆
- 前置：Web 基础、编程经验
- 推荐理由：偏工程实践，适合补团队协作和项目开发方法。

### Harvard CS50W — Web Programming with Python and JavaScript

- 学校：Harvard
- 主页：[CS50W](https://cs50.harvard.edu/web/)
- 主题：Django、SQL、JavaScript、React、测试、CI/CD 基础
- 适合：Web 后端 / 全栈入门
- 难度：★★★☆☆
- 前置：Python、HTML/CSS、基础数据库
- 推荐理由：适合快速建立 Web 开发完整流程认知。

---

## 建议学习路线

### 路线 A：CS 基础补全

1. CS50x 或 CS61A
2. CS61B
3. MIT 6.006
4. CSAPP
5. MIT 6.S081 / 6.1810
6. CMU 15-445
7. MIT 6.5840

### 路线 B：大模型 / AI Infra

1. CS229
2. CS231n 或 CS224n
3. CS336
4. CSAPP
5. CS149
6. CMU 10-414 / 10-714
7. MIT 6.5840 或 CMU 15-445

### 路线 C：后端 / 分布式 / 数据库

1. CS61B
2. CSAPP
3. MIT 6.S081 / Berkeley CS162
4. CMU 15-445 / Berkeley CS186
5. MIT 6.5840
6. Stanford CS144 / CMU 15-441

---

## 维护原则

- 优先链接官方课程主页，避免只贴二次搬运链接。
- 对于年份滚动的课程，优先选择页面稳定、资料完整的一期。
- 如果课程官网失效，可补充 OCW、YouTube、B站或 GitHub 镜像作为备用。
- 标注难度仅作为自学参考：★★★★★ 表示作业 / Lab 强度高，不代表不适合学习。
