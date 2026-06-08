# Agentic RL

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 专题 / 论文路线 / 实践 |
| 难度 | 前沿 |
| 优先级 | P1 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 理解工具调用、网页操作、代码执行和长任务 Agent 的 RL 训练 |

---

> Agentic RL 的核心问题：**如何用环境反馈训练 LLM Agent 完成多步任务，而不只是生成单个答案？**

---

## 先看结论

普通 LLM 训练多关注 prompt → response；Agentic RL 关注的是 trajectory：

```text
observation → thought / plan → action → tool result → new observation → ... → outcome
```

它和 RLHF / RLVR 的区别：

| 方向 | 训练对象 | Reward 来源 | 关键难点 |
|------|----------|-------------|----------|
| Preference Optimization | 单轮或短回答 | 人类 / AI 偏好 | 数据质量、长度偏差 |
| Reasoning RL | 推理解答 | verifier / 答案对错 | 稀疏奖励、reward hacking |
| Agentic RL | 多步行动轨迹 | 环境状态、工具结果、benchmark outcome | 长程 credit assignment、安全和可复现环境 |

Agentic RL 的代表场景：

- Coding Agent 修 bug；
- Web Agent 完成网站任务；
- Terminal Agent 执行命令行任务；
- Tool-use Agent 完成企业 workflow；
- GUI / OS Agent 操作软件；
- Research Agent 搜索、整理、验证资料。

---

## 知识地图

```text
Agentic RL
├── Agent 轨迹建模
│   ├── state / observation
│   ├── action / tool call
│   ├── tool result
│   ├── memory / context
│   └── terminal condition
├── Reward 来源
│   ├── unit tests / hidden tests
│   ├── web task success
│   ├── environment state
│   ├── human feedback
│   ├── trajectory verifier
│   └── safety constraints
├── 训练路线
│   ├── imitation learning
│   ├── rejection sampling
│   ├── offline RL from trajectories
│   ├── online RL in sandbox
│   └── self-evolving curriculum
├── 关键难题
│   ├── sparse reward
│   ├── long-horizon credit assignment
│   ├── exploration vs safety
│   ├── simulator fidelity
│   ├── tool-use safety
│   └── benchmark overfitting
└── 评测基准
    ├── SWE-bench / Terminal-Bench
    ├── WebArena / OSWorld
    ├── GAIA / τ-bench
    └── AgentBench / ToolBench
```

---

## 必读 Top 10

| 优先级 | 材料 | 关键词 | 为什么重要 |
|--------|------|--------|------------|
| P0 | [ReAct](https://arxiv.org/abs/2210.03629) | thought-action loop | Agent 轨迹范式基础 |
| P0 | [WebGPT](https://arxiv.org/abs/2112.09332) | browser + human feedback | 早期 LLM Agent + RLHF 代表 |
| P0 | [Toolformer](https://arxiv.org/abs/2302.04761) | self-supervised tool use | 工具调用数据构造代表 |
| P0 | [Reflexion](https://arxiv.org/abs/2303.11366) | verbal reinforcement | 不改权重的轨迹改进 |
| P1 | [Agent Q](https://arxiv.org/abs/2408.07199) | MCTS / DPO / web agent | 网页 Agent RL 代表 |
| P1 | [WebRL](https://arxiv.org/abs/2411.02337) | self-evolving curriculum | 在线课程和网页任务 RL |
| P1 | [SWE-bench](https://www.swebench.com/) | coding outcome | 代码 Agent 真实任务评测 |
| P1 | [Terminal-Bench](https://www.tbench.ai/) | terminal tasks | 命令行长任务评测 |
| P1 | [τ-bench](https://github.com/sierra-research/tau-bench) | tool workflow | 业务流程工具调用评测 |
| P1 | [WebArena](https://webarena.dev/) / OSWorld | environment tasks | Web / GUI 环境交互评测 |

---

## 1. Agent 轨迹如何建模？

一个 Agent run 可以表示为：

```text
τ = (o0, a0, r0, o1, a1, r1, ..., oT, outcome)
```

其中：

| 元素 | LLM Agent 中的例子 |
|------|-------------------|
| observation | 用户任务、网页截图、文件内容、工具返回 |
| action | 调用 search、browser click、shell command、edit file |
| reward | 测试通过、网页状态达成、人工评分、规则检查 |
| state | 当前文件系统、浏览器状态、记忆、任务进度 |
| terminal | 任务完成、超时、失败、预算耗尽 |

难点是：LLM Agent 的 state 往往不是一个干净的向量，而是散落在上下文、文件系统、外部工具、记忆和环境状态里。

---

## 2. Reward 从哪里来？

| Reward 来源 | 示例 | 优点 | 风险 |
|-------------|------|------|------|
| Unit Tests | 代码修复后测试通过 | 自动、明确 | 公开测试可被投机 |
| Hidden Tests | SWE-bench 风格评分 | 更可靠 | 成本高，不透明 |
| Web State | 网页任务最终状态 | 接近真实操作 | 环境脆弱、难复现 |
| Tool Result | API 返回成功 | 适合 workflow | 只看结果可能忽略违规过程 |
| Human Feedback | 人评轨迹或结果 | 覆盖复杂偏好 | 昂贵、慢、不一致 |
| Judge Model | LLM-as-judge | 可扩展 | 偏差、可被迎合 |
| Trajectory Verifier | 检查工具调用和权限 | 过程安全 | 规则设计复杂 |

实践上经常需要组合 reward：

```text
final success reward
+ verification reward
- unsafe action penalty
- excessive tool calls penalty
- timeout / budget penalty
```

---

## 3. Agentic RL 的训练路线

### 3.1 Imitation Learning

先从人类轨迹、专家脚本或强模型轨迹做行为克隆：

```text
expert trajectory → supervised fine-tuning
```

优点：稳定、简单。缺点：不会主动探索，容易复制专家错误。

### 3.2 Rejection Sampling / Best-of-N

对同一任务采样多个轨迹，只保留成功轨迹：

```text
sample N trajectories → verifier score → keep successful trajectories → SFT / DPO
```

适合有自动评分器的任务，如 coding / math / web state。

### 3.3 Offline RL from Trajectories

用已有成功/失败轨迹学习策略或 reward model。关键是记录完整 trajectory，而不只是 final answer。

### 3.4 Online RL in Sandbox

让 Agent 在可重置 sandbox 中探索，并用环境反馈更新。

要求：

- 环境可快速重置；
- 工具权限受控；
- reward 自动计算；
- 失败不会产生真实副作用；
- 轨迹可回放和审计。

### 3.5 Self-evolving Curriculum

模型从失败中生成新任务或改写任务难度，逐步扩展训练分布。WebRL 类工作体现了这个方向。

---

## 4. 长程 Credit Assignment

Agentic RL 最难的是：任务失败时，错在哪里？

```text
第 1 步检索错了？
第 3 步工具参数错了？
第 6 步忘记验证？
第 9 步修改了无关文件？
最终答案格式错了？
```

缓解方式：

| 方法 | 思路 |
|------|------|
| Trajectory Annotation | 对关键步骤打标签 |
| Subgoal Reward | 把任务拆成可验证子目标 |
| Verifier at Each Step | 每步检查工具参数、权限、状态变化 |
| Replay Buffer | 收集失败轨迹并分类复用 |
| Reflection / Critique | 让模型生成失败分析，再转成训练数据 |
| Hierarchical Policy | 高层规划、低层执行分开训练 |

---

## 5. 安全问题

Agentic RL 不只是优化成功率，还必须约束行为。

典型风险：

- 为了通过测试修改测试本身；
- 为了完成任务删除报错文件；
- 向外部网络发送敏感信息；
- 绕过权限调用 shell；
- 被网页 prompt injection 控制；
- 产生不可逆真实副作用。

安全约束应该进入训练和评测：

```text
reward = task_success
       - unsafe_tool_use_penalty
       - data_exfiltration_penalty
       - unauthorized_file_change_penalty
       - no_verification_penalty
```

这和 [Agent Benchmarks](../agent-engineering/agent-benchmarks.md) 以及 [Harness Engineering](../agent-engineering/harness-engineering.md) 直接相关。

---

## 6. 实践项目

### 项目 1：Terminal Task Rejection Sampling

1. 构造 20 个小型终端任务；
2. 每个任务有明确评分脚本；
3. 对每个任务采样 N 条 Agent 轨迹；
4. 保留成功轨迹；
5. 比较 SFT 前后成功率。

完成标准：能分析失败轨迹属于工具错误、上下文错误、计划错误还是验证错误。

### 项目 2：Tool-use RL Sandbox

设计一个 mock enterprise workflow：

```text
get_user → get_order → update_address / refund_order → notify_user
```

给每个任务定义业务规则和 reward：

- 正确完成：+1；
- 未验证用户身份：-1；
- 错误退款：-2；
- 多余工具调用：-0.1；
- 未发送通知：-0.5。

### 项目 3：Trajectory Replay Buffer

实现一个 replay buffer，保存：

- task input；
- observations；
- actions；
- tool outputs；
- final reward；
- failure type；
- verifier logs。

完成标准：能从失败轨迹中自动生成 DPO / SFT / critique 数据。

---

## 推荐学习顺序

1. ReAct：理解 thought-action-observation loop；
2. WebGPT：理解浏览器轨迹和人类反馈；
3. Toolformer：理解工具调用数据构造；
4. Reflexion：理解 verbal feedback 和 memory-based improvement；
5. Agent Q / WebRL：理解在线 RL 和 self-evolving curriculum；
6. SWE-bench / WebArena / τ-bench：理解 Agent benchmark 如何给 reward；
7. 做一个可重置 sandbox 和 trajectory logger。

---

## 和现有文档的关系

- [Reasoning RL](reasoning-rl.md)：可验证奖励在数学、代码、逻辑题中的应用。
- [Preference Optimization](preference-optimization.md)：偏好优化适合单轮或短回答，Agentic RL 更关注长轨迹。
- [Agent Benchmarks](../agent-engineering/agent-benchmarks.md)：提供 Agent 评测和 reward 来源。
- [Harness Engineering](../agent-engineering/harness-engineering.md)：提供 runtime、tools、sandbox、verifier 和轨迹审计框架。
