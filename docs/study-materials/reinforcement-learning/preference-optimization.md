# Preference Optimization

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 专题 / 论文路线 / 实践 |
| 难度 | 进阶 |
| 优先级 | P0 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 理解 RLHF、DPO、KTO、ORPO、SimPO 等偏好优化方法 |

---

> Preference Optimization 的核心问题：**如何把“人类更喜欢 A 而不是 B”转成可训练的模型更新？**

---

## 先看结论

LLM 对齐最初的主线是 PPO-style RLHF：

```text
Prompt → SFT response → human preference → reward model → PPO optimize policy
```

但 PPO-style RLHF 训练复杂、成本高、稳定性差，所以后来出现了 DPO、IPO、KTO、ORPO、SimPO 等直接偏好优化方法：

```text
Prompt + chosen / rejected response → 直接优化 policy
```

可以粗略理解为：

| 路线 | 是否训练 Reward Model | 是否在线 RL | 优点 | 局限 |
|------|----------------------|-------------|------|------|
| PPO-style RLHF | 是 | 是 | 表达力强，可继续探索 | 复杂、贵、不稳定 |
| DPO / IPO / SimPO | 否 | 否 | 简单、稳定、易复现 | 依赖离线偏好数据，探索弱 |
| KTO | 否 | 否 | 可用单样本好/坏反馈 | 对数据分布和标注质量敏感 |
| ORPO / CPO | 否 | 否 | 可与 SFT 目标合并 | objective 选择影响较大 |
| Online DPO / iterative preference | 可选 | 半在线 | 能迭代采样和改进 | 需要 rollout 和数据刷新 |

---

## 知识地图

```text
Preference Optimization
├── RLHF 基础
│   ├── SFT
│   ├── Reward Model
│   ├── PPO
│   └── KL Penalty / Reference Model
├── Direct Preference Optimization
│   ├── DPO
│   ├── IPO
│   ├── CPO
│   ├── ORPO
│   ├── KTO
│   └── SimPO
├── 数据问题
│   ├── pairwise preference
│   ├── chosen / rejected quality
│   ├── length bias
│   ├── label noise
│   └── distribution shift
└── 实践问题
    ├── reference model
    ├── beta / margin
    ├── evaluation
    ├── reward hacking
    └── online iteration
```

---

## 必读 Top 10

| 优先级 | 材料 | 关键词 | 为什么重要 |
|--------|------|--------|------------|
| P0 | [Deep RL from Human Preferences](https://arxiv.org/abs/1706.03741) | preference reward | RLHF 思想源头之一 |
| P0 | [InstructGPT](https://arxiv.org/abs/2203.02155) | SFT / RM / PPO | LLM RLHF 标准流程 |
| P0 | [DPO](https://arxiv.org/abs/2305.18290) | direct preference | 偏好优化最重要 baseline |
| P1 | [Constitutional AI](https://arxiv.org/abs/2212.08073) | RLAIF | AI feedback 与规则化偏好 |
| P1 | [IPO](https://arxiv.org/abs/2310.12036) | implicit preference | DPO 目标修正与理论分析 |
| P1 | [KTO](https://arxiv.org/abs/2402.01306) | binary feedback | 不需要成对偏好数据 |
| P1 | [ORPO](https://arxiv.org/abs/2403.07691) | odds ratio | 合并 SFT 与 preference objective |
| P1 | [SimPO](https://arxiv.org/abs/2405.14734) | reference-free | 简化 reference model 依赖 |
| P1 | RLCD / RLAIF 相关工作 | AI feedback | 用 AI 反馈扩展偏好数据 |
| P2 | Online / Iterative DPO | data refresh | 连接离线偏好优化和在线 RL |

---

## 1. PPO-style RLHF

### 组成部分

| 组件 | 作用 |
|------|------|
| SFT Model | 初始策略，先学会基本指令跟随 |
| Reward Model | 根据 prompt + response 输出偏好分数 |
| Reference Model | 防止 policy 偏离原始模型太远 |
| PPO Optimizer | 用 reward 和 KL penalty 更新 policy |
| KL Penalty | 约束模型不要 reward hacking 或语言退化 |

典型目标：

```text
maximize: reward_model(prompt, response) - beta * KL(policy || reference)
```

为什么复杂：

- 需要训练和维护 reward model；
- PPO 对超参敏感；
- rollout 成本高；
- reward model 可能被 policy exploit；
- 训练中 response 分布不断变化，评估困难。

---

## 2. Direct Preference Optimization

DPO 的核心洞察：在 KL-constrained RLHF 目标下，最优 policy 与 reward function 存在解析关系，因此可以直接用偏好对训练 policy，而不显式训练 reward model。

数据格式：

```json
{
  "prompt": "...",
  "chosen": "更好的回答",
  "rejected": "较差的回答"
}
```

DPO 学到的是：

```text
让 policy 相对 reference 更偏向 chosen，而不是 rejected。
```

### 什么时候适合 DPO？

适合：

- 有高质量 pairwise preference 数据；
- 希望快速稳定地提升 instruction following / style / helpfulness；
- 不想维护 PPO 和 reward model；
- 任务主要是离线偏好，不需要大量探索。

不适合：

- 需要在线探索的任务；
- reward 来自环境长期反馈；
- chosen/rejected 差异很小或标注噪音大；
- 目标能力无法通过静态偏好对覆盖。

---

## 3. DPO 家族方法

| 方法 | 核心思想 | 适合场景 | 注意点 |
|------|----------|----------|--------|
| DPO | 从 KL-constrained RLHF 推导直接偏好目标 | 通用 pairwise preference | beta 很关键 |
| IPO | 修正 DPO 在 deterministic preference 下的问题 | 理论更稳健 | 实践收益依任务而定 |
| KTO | 用好/坏单样本反馈训练 | 没有 pairwise 数据时 | 数据比例和阈值敏感 |
| ORPO | SFT loss + odds ratio preference | SFT 阶段直接合并偏好 | 可能不如分阶段灵活 |
| SimPO | reference-free，使用 length-normalized reward | 简化训练管线 | 需要控制长度偏差 |
| CPO | Contrastive preference objective | 对比式偏好学习 | 依赖负样本质量 |

---

## 4. 数据质量比算法更重要

偏好优化最常见的问题来自数据，而不是公式。

### 4.1 Chosen 不一定真的好

如果 chosen 只是“比 rejected 好一点”，模型会学到很弱的偏好信号。

建议：

- chosen 应明显更正确、更安全或更符合要求；
- rejected 应覆盖真实失败模式；
- 不要把两个都很差的样本强行配对。

### 4.2 Length Bias

人类和 reward model 往往偏好更长、更啰嗦的答案。DPO 类方法也容易学到长度偏差。

处理方式：

- 使用 length-normalized objective；
- 在 eval 中加入简洁性指标；
- 构造“短但正确”胜过“长但空泛”的偏好对。

### 4.3 Distribution Shift

离线偏好数据来自旧模型，而训练后 policy 会生成新类型回答。旧偏好数据未必覆盖新错误。

解决路线：

```text
train policy → sample new responses → label preferences → train again
```

这就是 online / iterative preference optimization 的动机。

---

## 5. 和 RLVR / Agentic RL 的区别

| 方向 | Reward 来源 | 典型数据 | 是否需要环境 |
|------|-------------|----------|--------------|
| Preference Optimization | 人类 / AI 偏好 | chosen / rejected | 通常不需要 |
| RLVR / Reasoning RL | verifier 可验证结果 | math/code attempts | 需要 verifier |
| Agentic RL | 工具执行 / 环境状态 / benchmark outcome | trajectories | 需要 sandbox / environment |

Preference Optimization 更适合对齐风格、偏好和一般 helpfulness；RLVR 更适合有明确对错的推理；Agentic RL 更适合多步工具执行。

---

## 实践项目

### 项目 1：Tiny DPO

1. 选一个小模型；
2. 构造 500-2000 条 prompt/chosen/rejected 数据；
3. 跑 SFT baseline；
4. 跑 DPO；
5. 比较 win rate、长度、格式遵循、拒答质量。

完成标准：能解释 DPO 改善了什么，以及是否引入长度偏差。

### 项目 2：Preference Data Audit

写脚本检查偏好数据：

- chosen / rejected 长度分布；
- 重复 prompt；
- chosen 是否包含标准答案；
- rejected 是否只是格式不同；
- 是否存在明显标注反转。

### 项目 3：DPO vs KTO / ORPO

在同一小数据集上对比：

```text
SFT → DPO → KTO → ORPO / SimPO
```

记录：训练稳定性、最终 win rate、回答长度和失败案例。

---

## 推荐学习顺序

1. InstructGPT：先理解 SFT → RM → PPO；
2. Deep RL from Human Preferences：理解偏好如何变成 reward；
3. DPO：理解为什么可以绕过 reward model；
4. IPO / KTO / ORPO / SimPO：理解 DPO 家族差异；
5. Online preference optimization：理解为什么离线偏好数据不够。

---

## 和现有文档的关系

- [LLM / Agent 相关强化学习前沿论文](llm-agent-rl-frontier.md)：总览 LLM / Agent RL 主线。
- [Reasoning RL](reasoning-rl.md)：可验证奖励和推理模型训练。
- [Agentic RL](agentic-rl.md)：多步工具使用、环境反馈和长轨迹训练。
