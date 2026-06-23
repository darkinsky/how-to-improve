# Code Agents / SWE Agents

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering / Code Agents / SWE Agents |
| 材料类型 | 系统 / Benchmark / 实践 |
| 难度 | 中级到前沿 |
| 优先级 | P0 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 系统学习 coding agent、SWE agent、repo-level editing、测试驱动修复和代码轨迹评估 |

---

## 先看结论

1. Code Agent 不是“让 LLM 写代码”，而是 **repo understanding → edit planning → tool execution → test feedback → repair loop → trajectory logging** 的系统工程。
2. SWE-bench、Terminal-Bench、HumanEval/MBPP 分别覆盖不同层级：真实 issue、终端任务、函数级编程。
3. 评估 coding agent 时必须记录 trajectory、测试输出、失败分类，不能只看最终 demo。
4. 重点系统：SWE-agent、OpenHands、Aider、Cline、Claude Code、Codex CLI、Cursor Composer。

---

## 知识地图

```text
Function-level Coding
  → Repo-level Context Building
  → Patch Generation
  → Tool-use / Terminal Execution
  → Test-driven Repair Loop
  → SWE Benchmarks
  → Long-horizon Coding Agent
  → Agentic RL from Code Trajectories
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | HumanEval / MBPP | Benchmark | 函数级代码生成基础评测 |
| P0 | SWE-bench / SWE-bench Verified | Benchmark | repo-level issue fixing 事实标准 |
| P0 | Terminal-Bench | Benchmark | terminal tool-use 与长任务评估 |
| P0 | SWE-agent | 系统 | 早期代表性 SWE agent |
| P0 | OpenHands / OpenDevin | 系统 | 开源 coding agent runtime |
| P1 | Aider | 工具 | 实用型 pair programming agent |
| P1 | Cline | 工具 | IDE/agent 工程实践参考 |
| P1 | Claude Code | 产品 / 系统 | 现代 terminal coding agent 代表 |
| P1 | Codex CLI | 产品 / 系统 | coding agent CLI 代表 |
| Frontier | Devin / Cursor Composer | 产品 / 系统 | autonomous software engineering 方向参考 |

---

## 1. Code Agent 系统组成

一个可评估的 coding agent 至少包含：

```text
Issue / Task Parser
  → Repository Indexer
  → Context Builder
  → Planner
  → Editor / Patch Applier
  → Terminal Tool Runner
  → Test Runner
  → Verifier
  → Repair Loop
  → Trajectory Logger
```

关键工程问题：

- 如何选择相关文件；
- 如何避免上下文过载；
- 如何让模型安全地执行命令；
- 如何处理测试失败；
- 如何生成最小 diff；
- 如何记录可回放轨迹。

---

## 2. Benchmark 地图

| Benchmark | 评估对象 | 优点 | 局限 |
|-----------|----------|------|------|
| HumanEval | 函数级生成 | 简单快速 | 不能代表 repo-level coding |
| MBPP | 小函数编程 | 入门基线 | 任务较短 |
| RepoBench | repo context | 关注仓库理解 | 不完全代表真实修复 |
| SWE-bench | GitHub issue 修复 | 真实度高 | 环境和评分复杂 |
| SWE-bench Verified | 人工筛选子集 | 质量更高 | 覆盖较少 |
| Terminal-Bench | 终端长任务 | 更接近 tool-use agent | 任务设计影响大 |

---

## 3. 前沿问题

### Repo-level Context Building

不是把整个仓库塞进 context，而是建立：

- symbol index；
- dependency graph；
- search / grep / AST tools；
- failing test traces；
- recent edit history。

### Test-time Repair Loop

```text
generate patch → run tests → parse failure → locate error → revise patch → rerun
```

关键是 verifier 和日志，而不是 prompt 本身。

### Trajectory as Training Data

Code agent 轨迹可以用于：

- imitation learning；
- rejection sampling；
- verifier training；
- Agentic RL；
- failure taxonomy。

---

## 学习路线

1. **函数级代码生成**：先用 HumanEval / MBPP 理解 pass@k、单测和格式约束。
2. **仓库级理解**：学习 repo indexing、symbol search、dependency graph 和 failing test trace。
3. **真实 issue 修复**：阅读 SWE-bench / SWE-agent，理解 edit plan、patch、test feedback loop。
4. **长任务工具使用**：用 Terminal-Bench 观察 shell、文件、网络、环境配置中的失败模式。
5. **轨迹评估**：记录 tool calls、diff、test output、repair loop，建立 failure taxonomy。

完成后应能设计一个小型 coding-agent benchmark，而不是只写一个 demo。

---

## 实践项目 / 完成标准

### Project 1：Mini SWE Agent

功能要求：

- 输入一个 issue；
- 搜索相关文件；
- 生成 patch；
- 运行测试；
- 根据失败输出修复；
- 保存 trajectory。

完成标准：

- 在 10-20 个 toy repo issue 上运行；
- 统计 success rate；
- 给出失败分类：定位错误、修改错误、测试理解错误、环境错误。

### Project 2：Coding Agent Regression Suite

- 构建 20 个 terminal/coding tasks。
- 每次 prompt 或 harness 改动后跑回归。
- 记录通过率、平均 token、平均耗时、失败样例。

### Project 3：Trajectory Replay Viewer

- 把 agent 的 tool calls、文件 diff、测试输出记录成 JSONL。
- 支持回放和审计。

---

## 延伸资料

- Harness Engineering：`harness-engineering.md`
- Agent Benchmarks：`agent-benchmarks.md`
- Agentic RL：`../reinforcement-learning/agentic-rl.md`
- Foundation Models：`../foundation-models/README.md`

---

## 高质量外部引用

| 方向 | 资料 | 类型 | 链接 |
|------|------|------|------|
| 函数级代码生成 | HumanEval | 论文 / 代码 | https://arxiv.org/abs/2107.03374 / https://github.com/openai/human-eval |
| 仓库级修复 | SWE-bench | 论文 / 官网 / 代码 | https://arxiv.org/abs/2310.06770 / https://www.swebench.com/ / https://github.com/SWE-bench/SWE-bench |
| SWE Agent | SWE-agent | 论文 / 代码 | https://arxiv.org/abs/2405.15793 / https://github.com/SWE-agent/SWE-agent |
| 开源 runtime | OpenHands | 代码 | https://github.com/All-Hands-AI/OpenHands |
| 终端任务评估 | Terminal-Bench | 官网 / 代码 | https://www.tbench.ai/ / https://github.com/laude-institute/terminal-bench |
| 仓库上下文 | RepoBench | 论文 | https://arxiv.org/abs/2306.03091 |
| Code Agent 失败分析 | SWE-bench Verified | 论文 / 数据 | https://arxiv.org/abs/2408.03979 |

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
