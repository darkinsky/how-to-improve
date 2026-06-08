# Agent Benchmarks

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering |
| 材料类型 | Benchmark / 评测路线 / 实践 |
| 难度 | 中级到前沿 |
| 优先级 | P0 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 系统理解 Agent 评测、轨迹评估、工具使用、安全和长任务能力 |

---

> Agent benchmark 的核心不是“模型会不会回答一道题”，而是：**模型 + harness + tools + memory + runtime** 组成的系统，能否在真实约束下持续完成任务。

---

## 先看结论

Agent 评测和传统 LLM 评测最大的不同：

1. **不能只看最终答案**：Agent 的工具调用、文件修改、网页操作、权限使用、错误恢复同样重要。
2. **评测对象是系统**：同一个模型放进不同 harness，结果可能差很多。
3. **长任务比短题更重要**：真实 Agent 任务通常包含规划、执行、验证、修复和交接。
4. **环境可复现很关键**：没有稳定 sandbox、初始状态和评分脚本，benchmark 很容易不可比较。
5. **轨迹级评估正在变重要**：不仅要知道“做对没”，还要知道“怎么做的、是否安全、是否浪费”。
6. **Agent benchmark 容易被过拟合**：公开任务集、固定测试和泄漏样例会让分数虚高。
7. **最好的评估方式通常是组合评测**：自动评分 + 轨迹审计 + 人工 spot check + 回归测试。

---

## Agent Benchmark 地图

```text
Agent Benchmarks
├── Coding Agent
│   ├── SWE-bench / SWE-bench Verified
│   ├── Terminal-Bench
│   ├── HumanEval / MBPP
│   └── RepoBench / repository-level tasks
├── Web / GUI Agent
│   ├── WebArena
│   ├── MiniWoB++
│   ├── OSWorld
│   └── AndroidWorld
├── Tool-use / Long-horizon Agent
│   ├── GAIA
│   ├── AgentBench
│   ├── ToolBench
│   ├── τ-bench
│   └── τ²-bench
├── Memory / Long-context Agent
│   ├── LongMemEval
│   ├── LoCoMo
│   └── RULER
└── Safety / Trajectory / Harness Audit
    ├── tool-use safety datasets
    ├── permission / exfiltration tests
    └── trajectory-level auditing
```

---

## 必读 Top 10

| 优先级 | Benchmark | 类型 | 为什么重要 |
|--------|-----------|------|------------|
| P0 | [SWE-bench](https://www.swebench.com/) / SWE-bench Verified | Coding Agent | 真实 GitHub issue 修复，最能代表代码 Agent 的工程能力 |
| P0 | [Terminal-Bench](https://www.tbench.ai/) | Coding / Terminal Agent | 评估命令行环境中的长任务执行能力 |
| P0 | [WebArena](https://webarena.dev/) | Web Agent | 真实网站环境中的浏览、搜索、表单和多步骤任务 |
| P0 | [OSWorld](https://os-world.github.io/) | GUI / Desktop Agent | 桌面操作系统级 Agent 评测，接近真实软件使用 |
| P0 | [GAIA](https://huggingface.co/spaces/gaia-benchmark/leaderboard) | General Agent | 多工具、多步骤、真实世界问题，重视综合推理和执行 |
| P1 | [τ-bench](https://github.com/sierra-research/tau-bench) | Tool-use Agent | 面向真实业务流程的工具调用可靠性评估 |
| P1 | ToolBench | Tool-use Agent | 大规模工具学习与 API 调用能力评测 |
| P1 | [MiniWoB++](https://miniwob.farama.org/) | Web / UI Agent | 经典网页交互任务，适合快速实验和算法验证 |
| P1 | LongMemEval / LoCoMo | Memory Agent | 评估长程记忆、对话记忆和信息追踪能力 |
| P1 | RULER | Long-context | 长上下文检索、推理、信息保持能力的基础评测 |

---

## 1. Coding Agent Benchmarks

### SWE-bench / SWE-bench Verified

**评测对象**：给定真实 GitHub issue 和代码仓库，让 Agent 修改代码并通过测试。

为什么重要：

- 任务来自真实开源仓库，不是玩具题；
- 需要理解 repo、定位 bug、修改代码、运行测试；
- 强依赖 harness：上下文选择、工具调用、测试策略、patch 生成、失败恢复都会影响分数。

评测时重点看：

| 维度 | 问题 |
|------|------|
| Repo Understanding | Agent 是否能找到正确文件和相关上下文？ |
| Patch Quality | 是否只修目标问题，还是引入无关改动？ |
| Test Strategy | 是否能选择合适测试，而不是盲目跑全部？ |
| Regression Risk | 是否破坏已有行为？ |
| Trajectory Efficiency | 是否反复兜圈子、浪费 token 和工具调用？ |

### Terminal-Bench

**评测对象**：Agent 在终端环境中完成复杂任务，通常需要读文件、运行命令、调试、写脚本、验证结果。

适合关注：

- shell / filesystem / package manager 使用能力；
- 长任务计划和执行；
- 失败恢复与日志理解；
- sandbox 中的可复现评分。

### HumanEval / MBPP / RepoBench

这些更适合做 coding 能力的基础评测：

| Benchmark | 用途 | 局限 |
|-----------|------|------|
| HumanEval | 函数级代码生成 | 太短，不能代表 Agent 工程能力 |
| MBPP | 基础编程题 | 适合入门 sanity check |
| RepoBench | repository-level 代码理解 | 更接近真实仓库，但仍不等于完整 Agent 任务 |

建议：不要只用 HumanEval / MBPP 判断 coding agent。它们可以作为单元测试，不应作为最终评测。

---

## 2. Web / GUI Agent Benchmarks

### WebArena

WebArena 关注真实网站环境中的任务完成能力，例如购物、论坛、GitLab、地图、CMS 等。

重点评估：

- 页面理解；
- 多步骤导航；
- 表单填写；
- 状态跟踪；
- 错误页面恢复；
- 浏览器工具使用。

### MiniWoB++

MiniWoB++ 是更轻量的网页交互 benchmark，适合快速实验：

- button / form / list / drag / click 等基础交互；
- 环境简单，可重复性好；
- 适合调试 perception-action loop。

### OSWorld / AndroidWorld

这类 benchmark 更接近“真实软件操作”：

| Benchmark | 环境 | 关注点 |
|-----------|------|--------|
| OSWorld | Desktop OS | 文件、应用、GUI、跨应用任务 |
| AndroidWorld | Android | 移动端 UI、app 操作、系统状态 |

GUI benchmark 的难点不是单纯视觉识别，而是：

```text
观察 → 决策 → 操作 → 状态变化理解 → 失败恢复
```

---

## 3. Tool-use / Long-horizon Benchmarks

### GAIA

GAIA 评估通用 AI assistant 解决真实问题的能力，常需要搜索、计算、文件处理、多步推理和工具使用。

适合看：

- 多工具组合；
- 信息检索和交叉验证；
- 复杂问题拆解；
- 最终答案可验证性。

### AgentBench / ToolBench

| Benchmark | 重点 |
|-----------|------|
| AgentBench | 多环境 Agent 能力，包括 web、game、tool、OS 等 |
| ToolBench | 学习和调用大量 API / tools 的能力 |

### τ-bench / τ²-bench

τ-bench 系列更接近业务流程中的 tool-use：

- 工具调用必须遵守业务规则；
- 中间状态会变化；
- 不能只得到正确答案，还要按正确流程执行；
- 适合评估客服、订票、订单、企业 workflow 类 Agent。

---

## 4. Memory / Long-context Benchmarks

Agent memory 评测要区分：

| 类型 | 评估问题 |
|------|----------|
| Short-term Working Memory | 当前任务状态是否持续一致？ |
| Episodic Memory | 是否记得过去交互中的事件？ |
| Semantic Memory | 是否能沉淀稳定事实和偏好？ |
| Procedural Memory | 是否能复用过去成功流程？ |

代表 benchmark：

- **LongMemEval**：长程记忆问答和信息追踪；
- **LoCoMo**：长对话记忆；
- **RULER**：长上下文检索、聚合、多跳任务。

Agent memory 不应只看“能不能从长上下文里找答案”。更关键的是：

```text
写入什么 → 何时检索 → 如何压缩 → 是否遗忘 → 是否污染未来决策
```

---

## 5. Safety / Trajectory Benchmarks

Agent 安全评测要从“输出是否安全”扩展到“行为是否安全”。

### 轨迹级风险

| 风险 | 例子 |
|------|------|
| Tool Misuse | 不该调用 shell 却调用了 shell |
| Permission Escalation | 绕过权限限制访问敏感文件 |
| Data Exfiltration | 把本地 secret 发到外部服务 |
| Prompt Injection | 被网页或文档诱导执行恶意指令 |
| Reward Hacking | 只修改测试让分数通过，而不解决问题 |
| Hidden Side Effects | 为了完成任务偷偷改环境、删文件、改配置 |

### 轨迹审计应该记录什么

```text
task input
model messages
context selected
tool calls
arguments
tool outputs
file diffs
network requests
permission prompts
verification results
final answer
```

评估 Agent 安全时，建议至少做三类测试：

1. **权限边界测试**：无权限工具是否被阻断；
2. **注入抵抗测试**：网页 / 文件中的恶意指令是否覆盖系统规则；
3. **副作用审计**：是否产生不必要文件修改、网络请求或数据泄漏。

---

## Agent 评测设计原则

### 1. 固定环境

每个任务应明确：

- 初始文件系统；
- 可用工具；
- 网络是否开放；
- 时间限制；
- 最大 token / tool call budget；
- 评分脚本；
- 环境重置方式。

### 2. 区分 Outcome 与 Process

| 评估层级 | 问题 |
|----------|------|
| Outcome | 最终答案 / patch / 操作是否正确？ |
| Process | 是否用了合理工具和步骤？ |
| Safety | 是否越权、泄漏、破坏环境？ |
| Efficiency | token、时间、工具调用是否可接受？ |
| Robustness | 换模型、换 seed、换环境是否稳定？ |

### 3. 加入回归任务

Agent harness 每次修改后，都应该跑一组小而稳定的 regression tasks。不要只看 leaderboard 分数。

### 4. 记录完整轨迹

没有轨迹，就无法解释失败，也无法优化 harness。

---

## 实践项目

### 项目 1：Coding Agent Mini Eval

构建 10 个小型 repo bugfix 任务：

- 每个任务包含 issue 描述、初始仓库、隐藏测试；
- Agent 需要修改代码并提交 diff；
- 评分脚本运行测试并检查 diff 范围；
- 记录工具调用和失败轨迹。

完成标准：能比较两个 harness 在同一模型下的成功率、平均工具调用次数和失败类型。

### 项目 2：Tool-use Agent Eval

设计一个 mock business API：

```text
get_user
get_order
refund_order
update_address
send_email
```

给 Agent 20 个客服任务，检查：

- 是否调用正确工具；
- 是否遵守业务规则；
- 是否避免越权操作；
- 是否在不确定时请求确认。

### 项目 3：Trajectory Auditor

实现一个轨迹审计器，对每次 Agent run 输出：

- 工具调用序列；
- 可疑操作；
- 重复循环；
- 未验证完成；
- 权限风险；
- 最终评分。

---

## 推荐学习顺序

1. 先看 SWE-bench / Terminal-Bench，理解 coding agent 的真实任务结构；
2. 再看 WebArena / OSWorld，理解 web / GUI agent 的环境交互；
3. 然后看 GAIA / τ-bench，理解多工具和业务流程；
4. 补 LongMemEval / LoCoMo / RULER，理解 memory 和 long-context；
5. 最后做 trajectory audit，把评测从最终结果扩展到过程和安全。

---

## 和现有文档的关系

- [Agent Memory](agent-memory.md)：解释 memory 系统本身如何设计；本文关注 memory 如何被评测。
- [Harness Engineering](harness-engineering.md)：解释 agent runtime / harness 如何设计；本文关注 harness 如何被 benchmark 验证。
- [Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)：跟进 harness 自动演化和安全审计前沿。
