# Study Materials Learning Paths

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 全局路线 / 导航 |
| 难度 | 入门到前沿 |
| 优先级 | P0 / Survey |
| 状态 | 推荐 |
| 建议用途 | 按目标选择学习路线，避免在大量材料中迷路 |

---

## 先看结论

如果只想快速进入这个知识库，不要从所有文档逐个看起。优先按目标选择一条主线：

| 目标 | 路线入口 | 适合人群 |
|------|----------|----------|
| 补 CS 基础 | [Computer Science](computer-science/README.md) | 转专业、基础不系统、想补长期技术底座 |
| 做 AI Infra / LLM Systems | [AI Infra](ai-infra/README.md) | 训练系统、推理系统、GPU / CUDA、集群调度方向 |
| 做 LLM / Agent 工程 | [Agent Engineering](agent-engineering/README.md) | Agent runtime、tool use、evaluation、harness 方向 |
| 跟进 LLM / Agent RL | [Reinforcement Learning](reinforcement-learning/README.md) | RLHF、DPO、RLVR、Reasoning RL、Agentic RL 方向 |
| 学生成模型 | [Generative Models](generative-models/README.md) | Diffusion、Flow Matching、DiT、图像 / 视频生成方向 |

建议顺序：

```text
先选一条主线 → 完成 2-3 个核心文档 → 做 1 个实践项目 → 再扩展到相邻方向
```

---

## 路线 A：AI Infra / LLM Systems

### 适合谁

- 想做大模型训练系统、推理系统、GPU 性能优化；
- 想理解 vLLM、SGLang、TensorRT-LLM、FlashAttention、NCCL、RDMA；
- 已经会写代码，但系统基础、并行计算或分布式训练不够系统。

### 推荐路线

```text
Computer Science 基础
  → AI Infra README
  → 体系结构 / CUDA / 分布式训练
  → AI Infra 必读论文路线
  → LLM Serving Frontier
  → 读源码 / 做 benchmark
```

### 必读入口

1. [Computer Science](computer-science/README.md)
2. [AI Infra 入门资料整理](ai-infra/README.md)
3. [01. 体系结构基础](ai-infra/01-architecture.md)
4. [02. CUDA 与算子编程](ai-infra/02-cuda-kernels.md)
5. [03. 分布式训练](ai-infra/03-distributed-training.md)
6. [04. LLM 推理系统](ai-infra/04-llm-inference.md)
7. [AI Infra 必读论文路线](ai-infra/07-ai-infra-papers.md)
8. [LLM Serving 前沿系统](ai-infra/08-llm-serving-frontier.md)

### 可以先跳过什么

- 如果目标是推理系统，可以先跳过过深的训练并行细节；
- 如果目标是训练系统，可以先不深入 Agent / RL；
- 如果系统基础薄弱，不要直接从最新 serving 论文开始。

### 完成标准

- 能解释 GPU kernel、memory hierarchy、batching、KV cache、parallelism 的基本关系；
- 能读懂 vLLM / SGLang / FlashAttention / NCCL 相关设计；
- 能搭建一个简单 LLM serving benchmark，并分析 TTFT、TPOT、吞吐、显存。

### 推荐实践项目

- 实现一个 naive attention，再对比 FlashAttention 思路；
- 跑 vLLM / SGLang benchmark，记录不同 batch size、sequence length、KV cache 策略下的指标；
- 阅读一个 serving 系统源码模块，写出 request lifecycle。

---

## 路线 B：LLM / Agent Engineering

### 适合谁

- 想做 Agent 框架、工具调用、长任务执行、轨迹评估；
- 想理解 Agent 为什么不是 prompt engineering 的简单扩展；
- 想搭建可测试、可审计、可回放的 Agent runtime。

### 推荐路线

```text
LLM / Transformer 基础
  → Preference Optimization / Reasoning RL
  → Agent Memory
  → Harness Engineering
  → Agent Benchmarks
  → Agentic RL
```

### 必读入口

1. [Preference Optimization](reinforcement-learning/preference-optimization.md)
2. [Reasoning RL](reinforcement-learning/reasoning-rl.md)
3. [Agent Memory](agent-engineering/agent-memory.md)
4. [Harness Engineering](agent-engineering/harness-engineering.md)
5. [Agent Benchmarks](agent-engineering/agent-benchmarks.md)
6. [Agentic RL](reinforcement-learning/agentic-rl.md)
7. [Harness Engineering 最新论文速读（2026）](agent-engineering/harness-engineering-papers-2026.md)

### 可以先跳过什么

- 如果目标是工程落地，可以先跳过 RL 公式推导，先做 harness / benchmark；
- 如果目标是研究，可以重点看 trajectory、credit assignment、Agentic RL；
- 如果没有系统基础，不要直接做高权限 tool-use agent。

### 完成标准

- 能画出 Agent runtime：context builder、planner、tool router、sandbox、memory、verifier、logger；
- 能用 benchmark 或 regression tasks 评估 agent，而不是只看 demo；
- 能记录、回放和审计一次完整 agent trajectory。

### 推荐实践项目

- 做一个小型 coding agent harness，用单元测试作为 verifier；
- 构建 20 个 terminal tasks，记录 agent success rate 和失败模式；
- 给 agent 增加 trajectory logger，并做一次失败案例审计。

---

## 路线 C：LLM / Agent RL

### 适合谁

- 想理解 RLHF、DPO、RLVR、GRPO、Reasoning RL；
- 想研究 test-time compute、verifier、process reward、self-improvement；
- 想把 RL 和 Agent benchmark / tool-use environment 连接起来。

### 推荐路线

```text
Advanced RL
  → Preference Optimization
  → Reasoning RL / RLVR
  → Agentic RL
  → LLM / Agent RL Frontier
```

### 必读入口

1. [强化学习进阶学习资料与论文路线](reinforcement-learning/advanced-rl.md)
2. [Preference Optimization](reinforcement-learning/preference-optimization.md)
3. [Reasoning RL](reinforcement-learning/reasoning-rl.md)
4. [Agentic RL](reinforcement-learning/agentic-rl.md)
5. [LLM / Agent 相关强化学习前沿论文](reinforcement-learning/llm-agent-rl-frontier.md)

### 可以先跳过什么

- 如果只是想用 DPO，不必先完整实现 PPO-style RLHF；
- 如果数学基础薄弱，可以先从 verifier + rejection sampling 做实践；
- 如果没有 agent runtime，不要直接做 online agent RL。

### 完成标准

- 能解释 SFT、RLHF、DPO、RLVR、Agentic RL 的差异；
- 能区分 outcome reward、process reward、preference reward 和 environment reward；
- 能实现一个 tiny verifier loop，并分析 reward hacking。

### 推荐实践项目

- 用数学题或代码题做一个 tiny RLVR / rejection sampling pipeline；
- 构建 chosen / rejected 数据集，跑一次 DPO 实验；
- 用 terminal benchmark 的任务结果构建 reward signal。

---

## 路线 D：Generative AI / Image & Video Generation

### 适合谁

- 想系统理解 Diffusion、Flow Matching、DiT、图像生成、视频生成；
- 想跟进 Sora、Veo、Movie Gen、Wan、CogVideoX、FLUX 等方向；
- 想做生成模型实验、评估或推理优化。

### 推荐路线

```text
Generative Models 2026
  → Diffusion Model
  → Flow Matching
  → Image & Video Generation
  → 实践：sampler / LoRA / video evaluation
```

### 必读入口

1. [Generative Models 2026](generative-models/generative-models-2026.md)
2. [AutoEncoder & VAE](generative-models/autoencoder-vae.md)
3. [Diffusion Model](generative-models/diffusion-model.md)
4. [Flow Matching](generative-models/flow-matching.md)
5. [Image & Video Generation](generative-models/image-video-generation.md)

### 可以先跳过什么

- 如果目标是现代图像生成，可以先略读 GAN；
- 如果目标是视频生成，不要跳过 Diffusion / Flow Matching；
- 如果目标是系统优化，要关注 sampler、batching、显存、延迟，而不只是模型效果。

### 完成标准

- 能解释 DDPM、DDIM、Score SDE、CFG、LDM、DiT、Flow Matching 的关系；
- 能跑一个 diffusion pipeline，并比较 scheduler / steps / guidance scale；
- 能说明视频生成的 temporal consistency、motion control、long video memory 难点。

### 推荐实践项目

- 比较不同 sampler 和 step 数对图像质量 / 延迟的影响；
- 用 LoRA 或 ControlNet 做一个小型可控生成实验；
- 对视频生成结果做 VBench / human preference 风格的人工评估表。

---

## 路线 E：CS 基础补全

### 适合谁

- 转专业或自学 CS，基础不系统；
- 做 AI / Infra / Agent 时发现系统、算法、网络、数据库薄弱；
- 想长期提升工程能力，而不是只学框架 API。

### 推荐路线

```text
CS61A / CS50x
  → CS61B
  → MIT 6.006
  → CSAPP
  → MIT 6.S081 / CS162
  → CMU 15-445 / CS186
  → MIT 6.5840
```

### 必读入口

1. [Computer Science](computer-science/README.md)
2. [CS 公开课资源整理](computer-science/open-courses.md)

### 可以先跳过什么

- 不做安全 / 编译器方向时，可以先不学 CS155 / CS143；
- 不做算法竞赛时，不必一开始就学很深的高级算法；
- 不做前端 / 全栈时，Web 课程可以后置。

### 完成标准

- 能写清晰程序并分析复杂度；
- 能解释编译、链接、内存、系统调用、网络请求的基本路径；
- 能完成至少一个 OS / DB / Distributed System Lab。

### 推荐实践项目

- 完成 CS61B 的一个大型项目；
- 做 CSAPP datalab / bomblab / malloclab 中至少两个；
- 完成 MIT 6.S081 的 2-3 个核心 lab；
- 实现一个 mini KV store 或 mini database component。

---

## 如何组合路线

| 组合目标 | 推荐组合 |
|----------|----------|
| AI Infra 工程师 | CS 基础补全 + AI Infra / LLM Systems |
| Agent 工程师 | CS 基础补全 + LLM / Agent Engineering + Agentic RL |
| LLM RL 研究 | Advanced RL + Preference Optimization + Reasoning RL + Agentic RL |
| 生成模型研究 | Generative AI + AI Infra 基础 |
| 后端 / 分布式工程师 | CS 基础补全 + 数据库 / 分布式 / 网络 |

---

## 维护说明

这个文档是全局导航页，不追求覆盖所有材料。新增专题时，只有满足以下条件才加入这里：

- 该专题已形成独立学习路线；
- 有明确入口文档；
- 能和至少一条主路线连接；
- 有实践项目或完成标准。

维护规则见：[Study Materials 维护机制](maintenance-guide.md)。
