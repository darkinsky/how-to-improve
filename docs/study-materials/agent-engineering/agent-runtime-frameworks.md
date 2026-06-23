# Agent Runtime Frameworks / Protocols

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering / Runtime / Protocols |
| 材料类型 | 系统 / 工程对比 / 实践 |
| 难度 | 中级到前沿 |
| 优先级 | P1 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 对比 Agent runtime、工具协议、workflow 框架和观测/评估能力 |

---

## 先看结论

1. Agent 框架的核心差异不是“能不能调用工具”，而是 state、tool interface、memory、observability、replay、evaluation、sandbox、deployment。
2. MCP、A2A、OpenAI Agents SDK、LangGraph、AutoGen、Semantic Kernel、LlamaIndex Workflows、DSPy 都代表不同抽象层。
3. 选框架前应先定义任务形态：single-agent tool use、multi-agent collaboration、workflow automation、coding agent、RAG agent、GUI agent。

---

## 知识地图

```text
Prompt / Tool Calling
  → Structured Output
  → Workflow Graph
  → Agent Runtime State
  → Memory / Context Protocol
  → Observability / Replay
  → Evaluation Harness
  → Deployment / Sandbox / Governance
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | ReAct | 论文 | reasoning + acting 的基本范式 |
| P0 | Toolformer | 论文 | 模型学习工具调用的早期代表 |
| P0 | Model Context Protocol / MCP | 协议 | tool/context 接入协议代表 |
| P1 | Agent2Agent / A2A | 协议 | agent interoperability 方向 |
| P1 | LangGraph | 框架 | graph/stateful workflow agent 代表 |
| P1 | AutoGen | 框架 | multi-agent conversation framework |
| P1 | Semantic Kernel | 框架 | enterprise agent orchestration |
| P1 | LlamaIndex Workflows | 框架 | RAG + workflow 结合 |
| P1 | DSPy | 框架 | programmatic prompting / optimizer |
| P1 | Guidance / Outlines / Instructor / PydanticAI | 工具 | structured generation 与 schema enforcement |

---

## 框架比较维度

| 维度 | 关键问题 |
|------|----------|
| State | 状态在哪里保存？能否恢复？ |
| Tool Interface | 工具 schema、权限、错误如何处理？ |
| Memory | 是否支持长期记忆、检索、摘要？ |
| Control Flow | 是自由 agent loop 还是显式 graph/workflow？ |
| Observability | 是否记录 prompt、tool call、latency、cost、diff？ |
| Replay | 失败轨迹能否复现？ |
| Evaluation | 是否支持 regression tasks / benchmark？ |
| Sandbox | 命令执行、文件访问、网络访问是否隔离？ |
| Deployment | 是否方便上线、扩缩容、权限治理？ |

---

## 学习路线

1. **先理解抽象层**：从 raw tool calling、structured output、workflow graph 到 stateful runtime。
2. **再比较协议**：重点理解 MCP 解决 tool/context 接入，A2A 解决 agent 间互操作。
3. **然后做框架对比**：用同一任务分别跑 LangGraph、AutoGen、Semantic Kernel / LlamaIndex Workflows。
4. **最后补工程治理**：加入 observability、replay、sandbox、evaluation harness 和 deployment policy。

完成后应能回答：同一任务为什么在不同 runtime 中成功率、可观测性和恢复能力不同。

---

## 实践项目 / 完成标准

### Project：Agent Runtime Bake-off

用同一个任务分别实现：

- raw tool calling；
- LangGraph；
- AutoGen；
- DSPy / structured output；
- MCP tool integration。

任务建议：

- RAG + tool use；
- coding task；
- research assistant；
- spreadsheet / document automation。

完成标准：

- 记录开发复杂度；
- 记录失败恢复能力；
- 比较 observability 和 replay；
- 给出适用场景结论。

---

## 延伸资料

- Harness Engineering：`harness-engineering.md`
- Agent Benchmarks：`agent-benchmarks.md`
- Code Agents：`code-agents.md`
- RAG：`../retrieval-rag/README.md`

### 补充：CrewAI

- **CrewAI**：多 Agent role-based workflow 框架，适合作为 AutoGen、LangGraph 之外的 multi-agent orchestration 对比对象。重点观察 role decomposition、task delegation、tool integration 和可观测性边界。

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
