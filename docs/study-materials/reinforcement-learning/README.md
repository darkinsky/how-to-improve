# Reinforcement Learning

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 索引 / 路线 |
| 难度 | 中级到前沿 |
| 优先级 | P0 / Survey / Frontier |
| 状态 | 推荐 |
| 建议用途 | 从经典 RL 进入 LLM / Agent RL |

---

这个目录整理强化学习进阶资料，以及 LLM / Agent 时代的 RL 前沿：RLHF、偏好优化、RLVR、Reasoning RL、Agentic RL、工具使用和自我改进。

---

## 先看结论

经典 RL 关注的是智能体在环境中通过 trial-and-error 最大化 reward；LLM / Agent 时代的 RL 则扩展出几条新主线：

```text
RLHF / Preference Optimization：从人类或 AI 偏好中学习对齐信号
RLVR / Reasoning RL：用可验证奖励提升数学、代码和逻辑推理
Agentic RL：把工具调用、网页操作、代码执行建模为长轨迹
Self-improvement：模型生成任务、解法、反思和偏好数据来自我提升
Inference-time Search：在推理阶段结合 verifier、搜索和工具反馈
```

如果目标是跟进 LLM reasoning 和 Agent 训练，建议先掌握基础 Deep RL，再重点看 RLHF、DPO、DeepSeekMath、DeepSeek-R1、ReAct、WebGPT、Toolformer、Agent Q / WebRL。

---

## 推荐学习顺序

1. [强化学习进阶学习资料与论文路线](advanced-rl.md)
2. [LLM / Agent 相关强化学习前沿论文](llm-agent-rl-frontier.md)

如果后续继续扩展，建议拆出：

```text
preference-optimization.md  # RLHF / DPO / KTO / ORPO
reasoning-rl.md             # RLVR / GRPO / verifier / reasoning models
agentic-rl.md               # Web agent / tool-use / long-horizon RL
```

---

## 必读 Top 10

1. **Sutton & Barto** — Reinforcement Learning: An Introduction
2. **DQN** — Human-level control through deep reinforcement learning
3. **Policy Gradient / Actor-Critic / PPO** — Deep RL 基础算法主线
4. **Deep RL from Human Preferences** — RLHF 思想源头之一
5. **InstructGPT** — SFT → Reward Model → PPO 的 LLM RLHF 主线
6. **DPO** — Direct Preference Optimization
7. **DeepSeekMath** — GRPO 与数学推理 RL 的重要前驱
8. **DeepSeek-R1** — RLVR / reasoning RL 的代表性工作
9. **ReAct / Toolformer / WebGPT** — LLM 工具使用和 Agent 轨迹建模
10. **Agent Q / WebRL** — Agentic RL 与网页任务训练

---

## 按目标选择

| 目标 | 建议路线 |
|------|----------|
| 补经典 RL | Sutton → DQN → Policy Gradient → PPO → SAC |
| 学 LLM 对齐 | RLHF → InstructGPT → DPO → KTO / ORPO |
| 学 Reasoning RL | DeepSeekMath → DeepSeek-R1 → GRPO → verifier / reward hacking |
| 学 Agentic RL | ReAct → WebGPT → Toolformer → Agent Q / WebRL |
| 学推理时搜索 | Tree of Thoughts → verifier → self-consistency → test-time scaling |

---

## 实践项目建议

- 在 Gymnasium 上实现 DQN / PPO；
- 用一个小模型和偏好数据跑 DPO；
- 为数学题或代码题设计 rule-based verifier；
- 对比 SFT、DPO、RLVR 在小任务上的差异；
- 跑一个简单 Web Agent / Tool-use Agent，记录轨迹、奖励和失败模式；
- 分析 DeepSeek-R1 类 RL 训练中的 reward hacking、长度偏置和格式奖励问题。

---

## 目前还值得补强的方向

- Reasoning RL / RLVR 单独成文；
- Agentic RL benchmark：SWE-bench、WebArena、Terminal-Bench、τ-bench；
- PPO、DPO、GRPO、REINFORCE++ 的对比；
- Process Reward Model / Outcome Reward Model；
- Tool-use RL 和 long-horizon credit assignment。
