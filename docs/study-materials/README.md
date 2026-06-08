# Study Materials

这里收录 AI、CS、工程与研究方向的公开学习资料。原则是：**优先整理最重要的课程、论文、代码和实践路线，而不是无限堆链接**。

> 注意：本目录只迁移和整理可公开分享的学习资料；不包含公司内网链接、内部文档、聊天记录或其它私人内容。

---

## 按目标选择路线

| 目标 | 推荐入口 | 建议路线 |
|------|----------|----------|
| 系统补 CS 基础 | [Computer Science](computer-science/README.md) | CS61A / CS50x → CS61B → MIT 6.006 → CSAPP → OS / DB / Distributed Systems |
| 进入 AI Infra / LLM Systems | [AI Infra](ai-infra/README.md) | 体系结构 → CUDA / Triton → 分布式训练 → LLM 推理 → 网络存储 → 调度编排 |
| 学现代生成模型 | [Generative Models](generative-models/README.md) | VAE / GAN / Flow → Diffusion → Flow Matching → 图像/视频生成 |
| 跟进 LLM / Agent RL | [Reinforcement Learning](reinforcement-learning/README.md) | Deep RL → RLHF / DPO → RLVR / Reasoning RL → Agentic RL |
| 学 Agent 工程 | [Agent Engineering](agent-engineering/README.md) | Agent Memory → Harness Engineering → 轨迹评估 / 安全 / 自动演化 |
| 学元学习与学习系统 | [Learning Systems](learning-systems/meta-learning.md) | Meta-learning 基础 → few-shot / optimization-based / model-based 方法 |

---

## 必读入口

如果只想先抓主线，建议从这些文档开始：

1. [CS 公开课资源整理](computer-science/open-courses.md)
2. [AI Infra 入门资料整理](ai-infra/README.md)
3. [04. LLM 推理系统](ai-infra/04-llm-inference.md)
4. [Diffusion Model 学习计划与资料汇总](generative-models/diffusion-model.md)
5. [Flow Matching 学习计划与资料汇总](generative-models/flow-matching.md)
6. [图像与视频生成模型学习计划](generative-models/image-video-generation.md)
7. [强化学习进阶学习资料与论文路线](reinforcement-learning/advanced-rl.md)
8. [LLM / Agent 相关强化学习前沿论文](reinforcement-learning/llm-agent-rl-frontier.md)
9. [Agent Memory 学习计划与资料汇总](agent-engineering/agent-memory.md)
10. [Harness Engineering 学习资料](agent-engineering/harness-engineering.md)

---

## Computer Science

- [Computer Science 学习入口](computer-science/README.md)
- [CS 公开课资源整理](computer-science/open-courses.md)

## AI Infra

- [AI Infra 入门资料整理](ai-infra/README.md)
- [01. 体系结构基础](ai-infra/01-architecture.md)
- [02. CUDA 与算子编程](ai-infra/02-cuda-kernels.md)
- [03. 分布式训练](ai-infra/03-distributed-training.md)
- [04. LLM 推理系统](ai-infra/04-llm-inference.md)
- [05. 网络与存储](ai-infra/05-network-storage.md)
- [06. 调度与编排](ai-infra/06-scheduling-orchestration.md)

## Generative Models

- [Generative Models 学习入口](generative-models/README.md)
- [AutoEncoder & VAE](generative-models/autoencoder-vae.md)
- [Diffusion Model](generative-models/diffusion-model.md)
- [GAN](generative-models/gan.md)
- [Flow-based Models](generative-models/flow-based-models.md)
- [Flow Matching](generative-models/flow-matching.md)
- [Image & Video Generation](generative-models/image-video-generation.md)

## Reinforcement Learning

- [Reinforcement Learning 学习入口](reinforcement-learning/README.md)
- [强化学习进阶学习资料与论文路线](reinforcement-learning/advanced-rl.md)
- [LLM / Agent 相关强化学习前沿论文](reinforcement-learning/llm-agent-rl-frontier.md)

## Agent Engineering

- [Agent Engineering 学习入口](agent-engineering/README.md)
- [Agent Memory](agent-engineering/agent-memory.md)
- [Harness Engineering](agent-engineering/harness-engineering.md)
- [Harness Engineering 最新论文速读（2026）](agent-engineering/harness-engineering-papers-2026.md)

## Learning Systems

- [Meta-Learning](learning-systems/meta-learning.md)

---

## 文档维护建议

每个方向后续尽量保持统一结构：

```markdown
# 主题

## 先看结论
## 知识地图
## 必读 Top 10
## 学习路线
## 实践项目 / 完成标准
## 最新进展
## 延伸资料
```

其中 **Top 10、实践项目、完成标准** 是后续最值得补强的部分。
