# Agent Engineering

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering |
| 材料类型 | 索引 / 路线 |
| 难度 | 中级到前沿 |
| 优先级 | P1 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 理解 Agent = Model + Harness 的工程主线 |

---

这个目录整理 LLM Agent 的工程与研究资料，重点关注 Agent Memory、Harness Engineering、Agent Benchmarks、工具系统、运行时约束、轨迹评估和自动演化。

---

## 先看结论

LLM Agent 的能力不只由模型决定，还强烈依赖模型外部的运行系统：

```text
Agent = Model + Harness
```

其中 Harness 包括：系统提示词、上下文选择、工具接口、文件系统、沙箱、状态管理、记忆、验证器、权限控制、调度编排和可观测性。

Agent 工程的核心问题不是“怎样写一个更长的 prompt”，而是：

- 模型应该看到什么？
- 能调用什么工具？
- 怎么记录状态和记忆？
- 怎么判断任务真的完成？
- 失败后如何恢复、重试或降级？
- 如何评估整条执行轨迹是否安全可靠？

---

## 推荐学习顺序

1. [Agent Memory](agent-memory.md)
2. [Harness Engineering](harness-engineering.md)
   - [Harness Engineering Cases](harness-engineering-cases.md)
   - [Harness Engineering Research](harness-engineering-research.md)
3. [Agent Benchmarks](agent-benchmarks.md)
4. [Code Agents / SWE Agents](code-agents.md)
5. [Agent Runtime Frameworks / Protocols](agent-runtime-frameworks.md)
6. [Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)

---

## 必读 Top 10

1. **ReAct** — Reasoning and Acting 的基础范式
2. **Toolformer** — 自监督工具使用
3. **WebGPT** — 浏览器辅助问答与轨迹式人类反馈
4. **Generative Agents** — Memory、Reflection、Planning 的经典 Agent 架构
5. **Voyager** — 终身学习与技能库
6. **Reflexion** — verbal reinforcement 与失败经验记忆
7. **Agent Benchmarks** — SWE-bench、Terminal-Bench、WebArena、GAIA 等评测系统
8. **Agent Memory 相关综述** — 记忆类型、检索和长期状态管理
9. **Natural-Language Agent Harnesses** — Harness 可表示化
10. **Agentic Harness Engineering / Harness Safety** — Harness 自动演化与轨迹级安全审计

---

## 按目标选择

| 目标 | 建议路线 |
|------|----------|
| 理解 Agent 基础 | ReAct → Toolformer → WebGPT → Reflexion |
| 学 Agent Memory | Generative Agents → Voyager → Agent Memory 文档 |
| 学工程化 Agent | Harness Engineering → Cases → Agent Runtime Frameworks → 工具系统 → 状态管理 → 验证与恢复 |
| 做 Code Agent / SWE Agent | Code Agents → SWE-bench / Terminal-Bench → mini SWE agent → trajectory replay |
| 跟进研究前沿 | Harness 2026 论文 → 自动演化 → 轨迹安全 → Harness optimizer |
| 做 Agent 评估 | SWE-bench / WebArena / Terminal-Bench / τ-bench / GAIA |

---

## 实践项目建议

- 实现一个 ReAct 风格的工具调用 Agent；
- 给 Agent 增加短期记忆、长期记忆和检索机制；
- 为一个代码 Agent 设计验证器：测试、lint、diff 检查、回滚；
- 记录 Agent 每次工具调用和状态变化，形成可审计轨迹；
- 设计一个简单 Harness：任务输入、上下文选择、工具限制、完成标准、失败恢复；
- 对比不同 Harness 下同一模型的任务成功率和 token 使用量。

---

## 一手资料优先级

后续维护时建议优先收录：

1. arXiv 论文；
2. OpenAI / Anthropic / LangChain / Google / Microsoft 等官方博客；
3. benchmark 官方仓库；
4. 主流 Agent 框架官方文档；
5. 中文二手解读和新闻报道。

二手资料可以保留，但最好标明它们是解读材料，不作为唯一依据。

---

## 目前还值得补强的方向

- Agent benchmarks：SWE-bench、Terminal-Bench、WebArena、OSWorld、GAIA、τ-bench；
- Agent safety：权限、信息泄漏、越权工具调用、轨迹审计；
- Agent runtime：LangGraph、AutoGen、OpenAI Agents SDK、Claude Code / Codex CLI；
- Harness optimizer 的直接评估；
- 多 Agent 协作中的共享状态、冲突和责任归因。
