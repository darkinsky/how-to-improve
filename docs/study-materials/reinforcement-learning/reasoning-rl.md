# Reasoning RL

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 专题 / 论文路线 / 实践 |
| 难度 | 前沿 |
| 优先级 | P0 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 理解 RLVR、GRPO、reasoning model、verifier 与 test-time compute |

---

> Reasoning RL 的核心问题：**如何用可验证奖励，让语言模型学会更长、更稳、更可检查的推理过程？**

---

## 先看结论

Reasoning RL 最近重新变热，原因是数学、代码、逻辑题提供了天然 verifier：

```text
模型生成解法 → verifier 检查答案 / 测试 / 约束 → reward → 更新模型
```

和传统 RLHF 不同，Reasoning RL 不一定需要人类偏好或 reward model。只要答案可验证，就可以直接给 reward。

```text
Preference Optimization: 人/AI 偏好告诉模型哪个回答更好
Reasoning RL / RLVR: verifier 告诉模型结果是否正确
Agentic RL: 环境告诉模型多步行动是否成功
```

当前主线：

1. **RLVR**：Reinforcement Learning with Verifiable Rewards；
2. **GRPO / PPO variants**：减少 value model 或降低训练复杂度；
3. **Outcome Reward vs Process Reward**：只奖最终答案，还是奖励中间步骤；
4. **Test-time Compute**：训练模型学会在推理时多想、多采样、多验证；
5. **Self-improvement**：模型自己生成题目、答案、反思，再用 verifier 筛选；
6. **Reward Hacking**：模型学会钻 verifier、格式或数据漏洞。

---

## 知识地图

```text
Reasoning RL
├── 基础路线
│   ├── RLHF / PPO
│   ├── DeepSeekMath / GRPO
│   └── DeepSeek-R1 / R1-Zero
├── Reward 设计
│   ├── outcome reward
│   ├── process reward
│   ├── rule-based verifier
│   ├── code / unit-test verifier
│   └── judge model / reward model
├── 训练问题
│   ├── sparse reward
│   ├── length bias
│   ├── KL control
│   ├── exploration
│   └── reward hacking
├── 推理时增强
│   ├── self-consistency
│   ├── best-of-N
│   ├── tree search
│   ├── verifier-guided decoding
│   └── test-time scaling
└── 自我改进
    ├── STaR
    ├── rejection sampling
    ├── synthetic data
    └── iterative RL
```

---

## 必读 Top 10

| 优先级 | 材料 | 关键词 | 为什么重要 |
|--------|------|--------|------------|
| P0 | [InstructGPT](https://arxiv.org/abs/2203.02155) | RLHF / PPO | LLM RL 基础流程 |
| P0 | [STaR](https://arxiv.org/abs/2203.14465) | reasoning bootstrapping | self-improvement 前驱 |
| P0 | [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050) | process reward | 过程监督代表工作 |
| P0 | [DeepSeekMath](https://arxiv.org/abs/2402.03300) | GRPO / math RL | R1 的重要前驱 |
| P0 | [DeepSeek-R1](https://arxiv.org/abs/2501.12948) | RLVR / reasoning | reasoning RL 代表性工作 |
| P1 | [Tree of Thoughts](https://arxiv.org/abs/2305.10601) | search / verifier | 推理时搜索主线 |
| P1 | Self-Consistency | sampling / voting | test-time compute 基础技巧 |
| P1 | Rejection Sampling Fine-tuning | verifier filtering | SFT 与 RLVR 的中间路线 |
| P1 | Code RL / unit-test feedback | executable reward | 代码任务的可验证奖励 |
| P1 | Process Reward Model 相关论文 | PRM | 解释 outcome reward 的局限 |

---

## 1. 什么是 RLVR？

RLVR = Reinforcement Learning with Verifiable Rewards。

典型任务：

| 任务 | Verifier |
|------|----------|
| 数学题 | 最终答案匹配、符号检查、数值检查 |
| 代码题 | 单元测试、隐藏测试、类型检查 |
| 逻辑题 | 规则引擎、约束求解器 |
| 格式任务 | JSON schema、regex、grammar |
| 工具任务 | 环境状态是否达到目标 |

RLVR 的优点：

- 不必手写 dense reward；
- 不一定需要人类偏好标注；
- reward 相对客观；
- 容易扩展到大量自动生成任务。

RLVR 的难点：

- reward 通常稀疏；
- verifier 可能不完备；
- 模型可能学会投机格式；
- 最终答案正确不代表推理过程可靠；
- 长 CoT 会带来长度偏差和成本问题。

---

## 2. GRPO 与 PPO 的关系

PPO-style RLHF 通常需要 policy、reference model、reward model、value model。GRPO 类方法希望降低 value model 依赖，通过同一 prompt 下多个采样的 group baseline 来估计 advantage。

粗略对比：

| 方法 | 需要 Value Model | Reward 来源 | 适合场景 |
|------|------------------|-------------|----------|
| PPO | 通常需要 | reward model / verifier | 通用 RLHF / online RL |
| GRPO | 不需要独立 value model | verifier / rule reward | 数学、代码等可验证任务 |
| REINFORCE++ | 不需要或弱化 value | verifier / outcome reward | 简化 RLVR pipeline |
| Rejection Sampling | 不更新 policy via RL | verifier 过滤 | 数据构造 / SFT 前置 |

关键理解：GRPO 的重点不是某个公式，而是把 reasoning RL pipeline 简化，让可验证 reward 能更容易用于大模型训练。

---

## 3. Outcome Reward vs Process Reward

### Outcome Reward

只看最终结果是否正确：

```text
answer correct → reward = 1
answer wrong   → reward = 0
```

优点：简单、便宜、可扩展。

缺点：

- reward 稀疏；
- 不知道哪一步错了；
- 可能奖励错误推理但碰巧正确；
- 容易鼓励过长搜索或格式投机。

### Process Reward

对中间推理步骤评分：

```text
step 1 valid → +
step 2 valid → +
step 3 invalid → -
```

优点：更 dense，更能指导长链推理。

缺点：

- 标注和验证难；
- step 粒度难定义；
- judge model 可能引入偏差；
- 过程正确不一定最终正确。

### 实用建议

```text
数学 / 代码：优先 outcome verifier，必要时补 process verifier
复杂证明 / 长推理：考虑 PRM 或 step-level judge
工程任务：把过程 reward 转成测试、lint、环境状态和轨迹约束
```

---

## 4. Reward Hacking

Reasoning RL 中常见 reward hacking：

| 类型 | 例子 | 防范 |
|------|------|------|
| 格式投机 | 输出固定模板骗过 parser | 多 verifier、严格解析 |
| 答案泄漏 | 训练集答案进入 prompt | 数据去重、held-out eval |
| 长度偏置 | 越写越长，看似更“会思考” | 长度惩罚、成本指标 |
| 测试投机 | 代码只过公开测试 | hidden tests、变异测试 |
| Judge Exploit | 学会迎合 judge model 偏好 | 多 judge、人类抽检 |
| Reward Overoptimization | reward 升高但真实能力下降 | 多指标评估、KL 控制 |

---

## 5. Test-time Compute

Reasoning model 的关键特点之一是推理时可以花更多计算：

- best-of-N sampling；
- self-consistency voting；
- verifier reranking；
- tree search / MCTS-like search；
- tool-assisted verification；
- reflection and repair。

训练和推理的关系：

```text
训练阶段：让模型学会产生更可验证、更有结构的候选解
推理阶段：用采样、搜索、verifier 选择更好的候选
```

不要把 reasoning RL 只理解成“训练时 RL”。它通常和 inference-time search 一起构成完整系统。

---

## 6. 实践项目

### 项目 1：Tiny Math RLVR

1. 准备一批小学 / GSM8K 风格数学题；
2. 让模型每题采样 N 个解答；
3. 用答案解析器给 reward；
4. 用 rejection sampling 选正确解做 SFT；
5. 再尝试 GRPO / PPO-style 更新。

完成标准：能比较 SFT、rejection sampling、RLVR 的准确率和平均输出长度。

### 项目 2：Code Verifier Loop

1. 选择 HumanEval / MBPP 子集；
2. 模型生成代码；
3. 单元测试给 reward；
4. 记录错误类型；
5. 用通过测试的样本做训练或 rerank。

完成标准：能识别测试投机、超时、语法错误、隐藏测试失败。

### 项目 3：Reward Hacking Audit

构造 20 个 adversarial verifier cases：

- 格式边界；
- 多答案形式；
- 解析器漏洞；
- 单位换算；
- 代码只 print 答案；
- 测试覆盖不足。

完成标准：能说明你的 verifier 是否容易被 exploit。

---

## 推荐学习顺序

1. InstructGPT：理解语言模型上的 RL；
2. STaR：理解自举式 reasoning；
3. Let's Verify Step by Step：理解过程监督；
4. DeepSeekMath：理解 GRPO 与数学 RL；
5. DeepSeek-R1：理解 RLVR 如何激发 reasoning 行为；
6. Tree of Thoughts / Self-consistency：理解推理时搜索；
7. 做 Tiny Math RLVR 实验。

---

## 和现有文档的关系

- [Preference Optimization](preference-optimization.md)：偏好数据和 direct alignment 方法。
- [Agentic RL](agentic-rl.md)：把可验证奖励扩展到工具调用和环境状态。
- [LLM / Agent 相关强化学习前沿论文](llm-agent-rl-frontier.md)：总览 LLM / Agent RL 主线。

---

## RLVR 相关前沿范式补充

| 优先级 | 材料 / 方法 | 方向 | 建议关注点 |
|--------|-------------|------|------------|
| P0 | STaR | reasoning bootstrapping | 用 rationale 自举提升推理 |
| P0 | ReST / ReSTEM | rejection sampling / self-training | 采样、筛选、再训练循环 |
| P0 | Process Reward Models | PRM | step-level supervision 与 reward hacking |
| P1 | Self-Rewarding Language Models | self-reward | 模型自评和迭代风险 |
| P1 | SPIN | self-play fine-tuning | 无人工偏好数据的自博弈微调 |
| P1 | Tree of Thoughts / Graph of Thoughts | inference-time search | 搜索树、verifier、branching 策略 |
| P1 | Quiet-STaR | internal reasoning | 隐式 reasoning token / rationale |
| P1 | Reflexion | verbal reinforcement | 失败反思作为 episodic memory |

建议把 RLVR 放在更大的 test-time compute 框架下理解：

```text
sampling
  → verifier / ORM
  → PRM
  → rejection sampling
  → search / tree-of-thought
  → self-training / RL
```

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度 |
| 过时风险 | 高 |
| 维护重点 | RLVR、PRM/ORM、verifier、reasoning benchmark 和开源复现 |
