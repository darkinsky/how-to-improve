# 强化学习进阶学习资料与论文路线

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 论文路线 / 课程 |
| 难度 | 进阶 |
| 优先级 | P0 / Classic / Frontier |
| 状态 | 推荐 |
| 建议用途 | 从经典 RL 进阶到 Deep RL、Offline RL、RLHF |

---

> 适用背景：已经学完 Sutton & Barto《Reinforcement Learning: An Introduction》，希望从经典 RL 进阶到 Deep RL、Offline RL、Model-Based RL、RLHF 与现代大模型/机器人相关方向。  
> 更新时间：2026-05-23  
> 资料原则：优先选择经典论文、可复现实验、公开课程和长期维护的资源。

---

## 总体路线图

```text
Sutton 基础
  ├─ Deep RL 基础：DQN / A2C / PPO / SAC / TD3
  ├─ 稳定性与表示：Distributional RL / Exploration / Hierarchy
  ├─ Model-Based RL：World Models / PETS / Dreamer
  ├─ Offline RL：BCQ / BEAR / CQL / IQL / Decision Transformer
  ├─ Preference Learning / RLHF：GAIL / Human Preferences / PPO-RLHF / DPO
  └─ 前沿方向：机器人、LLM reasoning、安全 RL、多智能体、泛化
```

如果只选一条最务实主线：

1. **PPO + SAC**：掌握现代 model-free RL 的工程稳定性。
2. **CQL + IQL + Decision Transformer**：掌握数据驱动/离线 RL。
3. **Dreamer 系列**：理解 world model 与 foundation agent 的连接。
4. **RLHF / DPO**：连接大模型训练与经典 RL。
5. **Safe RL / Evaluation**：避免只追 reward，不理解部署风险。

---

## 0. 从 Sutton 过渡到进阶 RL，需要补什么？

### 数学与理论

- Bellman operator、contraction、policy improvement 的证明要能自己写出来。
- 理解 on-policy vs off-policy、bootstrapping、function approximation 三者一起出现时为什么会不稳定。
- 补充 stochastic approximation、convex optimization、concentration bound 的基本直觉。
- 明确 bias / variance / sample efficiency / stability 这四个维度如何互相 trade-off。

### 工程与实验

- 会用 PyTorch/JAX 实现 DQN、PPO、SAC，能复现实验曲线而不只是跑通代码。
- 掌握 Gymnasium / MuJoCo / Brax / CleanRL / Stable-Baselines3 / RLlib 中至少一套工具链。
- 建立实验纪律：seed、日志、评估频率、ablation、超参表、失败案例记录。

---

## 1. Deep RL 基础算法主线

### Value-based / DQN 系列

- [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602) — DQN 开端，理解经验回放、target network、像素到动作。
- [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461) — Double DQN，解决 Q-learning 的过估计偏差。
- [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581) — 把 state value 与 advantage 分解。
- [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952) — 让 replay buffer 不只是均匀采样。
- [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298) — 把 DQN 系列 trick 组合成强 baseline。

### Actor-Critic / Policy Gradient

- [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971) — DDPG，连续控制经典 off-policy actor-critic。
- [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783) — A3C/A2C，多 worker 异步 actor-critic。
- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347) — PPO，当前最常用 on-policy baseline，重点理解 clipped objective。
- [Addressing Function Approximation Error in Actor-Critic Methods](https://arxiv.org/abs/1802.09477) — TD3，针对 actor-critic 函数逼近误差的三个 trick。
- [Soft Actor-Critic](https://arxiv.org/abs/1801.01290) — SAC，最大熵 RL，现代连续控制核心算法。

### 大规模训练

- [IMPALA](https://arxiv.org/abs/1802.01561) — actor-learner 架构 + V-trace，适合理解大规模采样。
- [Distributed Prioritized Experience Replay](https://arxiv.org/abs/1803.00933) — Ape-X，大规模分布式 prioritized replay。
- [Recurrent Experience Replay in Distributed Reinforcement Learning](https://openreview.net/forum?id=r1lyTjAqYX) — R2D2，循环网络 + replay，处理部分可观测和长期记忆。

---

## 2. 表示、分布、探索与层次化

### Distributional RL

- [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887) — C51，学习 return distribution 而非只学期望。
- [Distributional Reinforcement Learning with Quantile Regression](https://arxiv.org/abs/1710.10044) — QR-DQN，把 distributional RL 推向更通用的分位数表示。

### Exploration

- [Deep Exploration via Bootstrapped DQN](https://arxiv.org/abs/1602.04621) — 用 bootstrapped heads 近似不确定性。
- [Curiosity-driven Exploration by Self-supervised Prediction](https://arxiv.org/abs/1705.05363) — curiosity / intrinsic reward 代表作。
- [Exploration by Random Network Distillation](https://arxiv.org/abs/1810.12894) — RND，用随机网络蒸馏构造探索奖励。

### Hierarchy / Skill Learning

- [The Option-Critic Architecture](https://arxiv.org/abs/1609.05140) — 自动学习 options。
- [Hierarchical Deep Reinforcement Learning](https://arxiv.org/abs/1604.06057) — h-DQN，把目标/子目标纳入深度 RL。
- [Diversity is All You Need](https://arxiv.org/abs/1802.06070) — DIAYN，无监督技能发现。

---

## 3. Model-Based RL 与 World Models

### 核心阅读

- [World Models](https://arxiv.org/abs/1803.10122) — 用潜变量世界模型做控制。
- [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://arxiv.org/abs/1805.12114) — PETS，probabilistic ensembles + trajectory sampling。
- [Dream to Control: Learning Behaviors by Latent Imagination](https://arxiv.org/abs/1912.01603) — Dreamer，在 latent dynamics 中做 actor-critic。
- [Mastering Atari with Discrete World Models](https://arxiv.org/abs/2010.02193) — DreamerV2，离散 latent + Atari。
- [Mastering Diverse Domains through World Models](https://arxiv.org/abs/2301.04104) — DreamerV3，统一配置跨多个 domain。

### 学习重点

- **model bias**：模型学错时，规划/策略会利用模型漏洞。
- **uncertainty**：ensemble、Bayesian、latent stochasticity 如何缓解过度自信。
- **planning vs policy learning**：MPC、CEM、latent imagination、actor-critic 的取舍。

---

## 4. Offline RL / Batch RL

### 为什么重要

真实系统里在线探索昂贵或危险：推荐、自动驾驶、医疗、机器人都更接近 offline setting。核心难点是 **distribution shift**：策略会选择数据集中没覆盖的动作，Q 函数容易外推过高。

### 必读论文

- [Batch-Constrained deep Q-learning](https://arxiv.org/abs/1812.02900) — BCQ，限制策略接近数据分布。
- [Stabilizing Off-Policy Q-Learning via Bootstrapping Error Reduction](https://arxiv.org/abs/1906.00949) — BEAR，通过 MMD 约束策略偏离行为策略。
- [Conservative Q-Learning for Offline Reinforcement Learning](https://arxiv.org/abs/2006.04779) — CQL，降低 OOD action 的 Q 值。
- [MOPO: Model-based Offline Policy Optimization](https://arxiv.org/abs/2005.13239) — 用模型不确定性惩罚做 offline model-based RL。
- [MOReL: Model-Based Offline Reinforcement Learning](https://arxiv.org/abs/2005.05951) — 构造 pessimistic MDP 处理模型不确定性。
- [Decision Transformer](https://arxiv.org/abs/2106.01345) — 把 offline RL 转成 return-conditioned sequence modeling。
- [Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169) — IQL，实用且强的 offline RL baseline。

### 资源

- [Offline RL Reading List - Stanford](https://web.stanford.edu/~mrifaki/offline-rl-readings.html)
- [awesome-offline-rl](https://github.com/hanjuku-kaso/awesome-offline-rl)
- [D4RL benchmark](https://github.com/Farama-Foundation/D4RL)

---

## 5. Sequence Modeling / Foundation Model 视角下的 RL

### 核心阅读

- [Decision Transformer](https://arxiv.org/abs/2106.01345) — return-conditioned behavior cloning。
- [Trajectory Transformer](https://arxiv.org/abs/2106.02039) — 用 transformer 做轨迹建模和规划。
- [Reinforcement Learning as One Big Sequence Modeling Problem](https://arxiv.org/abs/2106.02039) — 用序列建模视角重新理解 RL。
- [RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control](https://arxiv.org/abs/2307.15818) — VLA/机器人方向代表作。

### 学习重点

- 什么时候 RL 可以退化成 supervised sequence modeling？
- Return conditioning、advantage-weighted regression、behavior cloning 的边界在哪里？
- Foundation model 做 policy 时，环境反馈、数据覆盖和安全约束如何处理？

---

## 6. Imitation Learning / Preference Learning / RLHF

### 核心阅读

- [Generative Adversarial Imitation Learning](https://arxiv.org/abs/1606.03476) — GAIL，把 imitation learning 写成 occupancy measure matching。
- [Deep Reinforcement Learning from Human Preferences](https://arxiv.org/abs/1706.03741) — RLHF 经典源头之一。
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155) — InstructGPT，SFT + reward model + PPO。
- [Direct Preference Optimization](https://arxiv.org/abs/2305.18290) — DPO，绕过显式 RL 训练的偏好优化方法。
- [KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306) — 用 prospect theory 视角做偏好优化。

### 学习重点

- Preference model 学到的是 reward，还是人类选择偏差？
- PPO-RLHF、DPO、IPO/KTO/ORPO 等方法和经典 RL 的关系。
- Reward hacking、overoptimization、distribution shift 是 LLM/RLHF 的核心风险。

---

## 7. Safe RL / Robust RL / Generalization / Multi-Agent

### 核心阅读

- [Constrained Policy Optimization](https://arxiv.org/abs/1705.10528) — 安全约束 RL 经典。
- [Benchmarking Safe Exploration in Deep Reinforcement Learning](https://arxiv.org/abs/1910.01708) — Safety Gym 相关工作。
- [Multi-Agent Actor-Critic for Mixed Cooperative-Competitive Environments](https://arxiv.org/abs/1706.02275) — MADDPG，理解多智能体 credit assignment 和 non-stationarity。
- [QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485) — 多智能体 value decomposition 经典。

### 学习重点

- 约束 MDP、risk-sensitive objective、CVaR。
- OOD generalization：训练环境、测试环境、扰动和 domain randomization。
- 多智能体中的非平稳性、通信、协作/竞争。

---

## 课程与资料

- [Berkeley CS 285: Deep Reinforcement Learning](https://rail.eecs.berkeley.edu/deeprlcourse/) — 最推荐的 Deep RL 进阶课程，覆盖 policy gradient、actor-critic、model-based、offline RL。
- [Spinning Up in Deep RL](https://spinningup.openai.com/) — OpenAI 出品，适合把 PPO/SAC/DDPG/TD3 的公式和代码对上。
- [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit0/introduction) — 偏实践入门，但 bonus unit 可快速复习 MBRL、IL 等方向。
- [David Silver RL Course](https://www.davidsilver.uk/teaching/) — 经典 RL 到 Deep RL 的桥梁。
- [CleanRL](https://github.com/vwxyzjn/cleanrl) — 单文件实现，非常适合逐行理解算法。
- [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) — 工程使用和 baseline 对照。

---

## 12 周学习计划

- **第 1-2 周**：复现 DQN / Double DQN / Dueling / PER，在 Atari 或 CartPole/LunarLander 上对比曲线。
- **第 3-4 周**：实现 PPO 和 SAC，重点看 advantage normalization、entropy、target network、replay buffer。
- **第 5 周**：读 Distributional RL、RND、DIAYN，理解探索和表示为什么影响 sample efficiency。
- **第 6-7 周**：读 PETS、Dreamer 系列，做一个简单 latent dynamics 或 ensemble dynamics 实验。
- **第 8-9 周**：读 CQL、IQL、Decision Transformer，用 D4RL 做 offline RL baseline 对比。
- **第 10 周**：读 GAIL、Human Preferences、InstructGPT、DPO，梳理 RLHF 与经典 RL 的连接。
- **第 11 周**：选 safe RL / multi-agent / robotics / LLM reasoning 一个方向深挖。
- **第 12 周**：写一篇综述或复现实验报告，形成自己的 RL 进阶地图。

---

## 建议做的复现实验

- DQN ablation：去掉 target network / replay / Double Q，观察不稳定性。
- PPO clipping ablation：比较 clip ratio、KL penalty、entropy bonus 对性能的影响。
- SAC temperature：固定 alpha vs automatic entropy tuning。
- CQL vs IQL：在 D4RL medium / medium-replay / medium-expert 上比较。
- Decision Transformer：改变 return-to-go conditioning，看 sequence model 如何“选择”行为。
- Dreamer/PETS 小实验：比较 model-free 与 model-based 的 sample efficiency。

---

## 读论文的方法

- 第一遍只回答：问题是什么？为什么之前方法不够？核心 trick 是什么？
- 第二遍看公式：objective 从哪里来？近似在哪里？bias/variance trade-off 是什么？
- 第三遍看实验：baseline 是否公平？环境是否代表真实问题？ablation 是否支持结论？
- 最后做复现：哪怕只复现 toy setting，也比只读摘要有效。

---

## LLM / Agent 前沿补充

强化学习在 LLM reasoning、RLHF/RLVR、工具调用和 Agent 训练里正在快速升温。相关代表论文与学习路线见：

- [LLM / Agent 相关强化学习前沿论文](llm-agent-rl-frontier.md)

## 推荐主线

如果目标是工程/科研双向提升，我建议主线选：

1. **PPO + SAC**：掌握现代 model-free RL 的工程稳定性。
2. **IQL + CQL + Decision Transformer**：掌握数据驱动/离线 RL。
3. **DreamerV3**：理解 world model 和 foundation agent 的连接。
4. **RLHF / DPO**：连接大模型训练与经典 RL。
5. **Safe RL / evaluation**：避免只追 reward，不理解部署风险。
