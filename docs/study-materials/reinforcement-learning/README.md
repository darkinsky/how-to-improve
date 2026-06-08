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

1. [强化学习进阶学习资料与论文路线](advanced-rl.md)：补齐经典 RL、Deep RL、PPO、SAC 等基础。
2. [Preference Optimization](preference-optimization.md)：理解 RLHF、DPO、KTO、ORPO、SimPO 等偏好优化方法。
3. [Reasoning RL](reasoning-rl.md)：理解 RLVR、GRPO、verifier、process reward 与 test-time compute。
4. [Agentic RL](agentic-rl.md)：理解工具调用、网页操作、代码执行和长任务 Agent 的 RL 训练。
5. [LLM / Agent 相关强化学习前沿论文](llm-agent-rl-frontier.md)：作为总览页跟进前沿论文主线。

---

## 子专题

| 文档 | 主题 | 优先级 |
|------|------|--------|
| [advanced-rl.md](advanced-rl.md) | 经典 RL / Deep RL 进阶 | P0 / Classic |
| [preference-optimization.md](preference-optimization.md) | RLHF、DPO、KTO、ORPO、SimPO | P0 / Frontier / Hands-on |
| [reasoning-rl.md](reasoning-rl.md) | RLVR、GRPO、Reasoning Model、Verifier | P0 / Frontier / Hands-on |
| [agentic-rl.md](agentic-rl.md) | Tool-use、Web Agent、Coding Agent、long-horizon RL | P1 / Frontier / Hands-on |
| [llm-agent-rl-frontier.md](llm-agent-rl-frontier.md) | LLM / Agent RL 论文总览 | P0 / Frontier |

---

## 必读 Top 10

1. **Sutton & Barto** — Reinforcement Learning: An Introduction
2. **DQN** — Human-level control through deep reinforcement learning
3. **Policy Gradient / Actor-Critic / PPO** — Deep RL 基础算法主线
4. **InstructGPT** — SFT → Reward Model → PPO 的 LLM RLHF 主线
5. **DPO** — Direct Preference Optimization
6. **KTO / ORPO / SimPO** — 直接偏好优化家族
7. **DeepSeekMath** — GRPO 与数学推理 RL 的重要前驱
8. **DeepSeek-R1** — RLVR / reasoning RL 的代表性工作
9. **ReAct / Toolformer / WebGPT** — LLM 工具使用和 Agent 轨迹建模
10. **Agent Q / WebRL** — Agentic RL 与网页任务训练

---

## 按目标选择

| 目标 | 建议路线 |
|------|----------|
| 补经典 RL | Sutton → DQN → Policy Gradient → PPO → SAC |
| 学 LLM 对齐 | InstructGPT → [Preference Optimization](preference-optimization.md) → DPO / KTO / ORPO / SimPO |
| 学 Reasoning RL | DeepSeekMath → [Reasoning RL](reasoning-rl.md) → DeepSeek-R1 → verifier / reward hacking |
| 学 Agentic RL | ReAct → WebGPT → Toolformer → [Agentic RL](agentic-rl.md) → Agent Q / WebRL |
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

- PPO、DPO、GRPO、REINFORCE++ 的更细公式对比；
- Process Reward Model / Outcome Reward Model 专题；
- Tool-use RL 和 long-horizon credit assignment；
- Self-improvement / synthetic data / inference-time search 单独成文；
- Agentic RL benchmark 与 [Agent Benchmarks](../agent-engineering/agent-benchmarks.md) 的联动。
