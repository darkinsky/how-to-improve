# Evaluation / Benchmarking

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Evaluation / Benchmarking / Reliability |
| 材料类型 | 方法论 / Benchmark / 实践 |
| 难度 | 入门到进阶 |
| 优先级 | P0 / Hands-on / Survey |
| 状态 | 推荐 |
| 建议用途 | 建立跨 LLM、RAG、Agent、Generative、Serving 的评估和 benchmark 方法论 |

---

## 先看结论

1. 没有 eval harness 的 AI 系统无法持续改进，只能靠 demo 感觉。
2. Benchmark 要同时衡量能力、稳定性、成本、延迟、安全和失败模式。
3. 对 Agent/RAG/生成模型，平均分不够；必须记录 trajectory、citation、failure taxonomy 和回归测试。
4. 评估本身需要防止数据泄漏、benchmark contamination、过拟合和不可复现。

---

## 知识地图

```text
Task Definition
  → Dataset / Test Case Design
  → Metrics
  → Harness / Runner
  → Logging / Tracing
  → Error Analysis
  → Regression Suite
  → Benchmark Governance
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | HELM | Benchmark / 方法论 | LLM 综合评估框架 |
| P0 | MMLU / BIG-bench / BIG-bench Hard | Benchmark | 通用知识和推理评估经典 |
| P0 | GSM8K / MATH / GPQA | Benchmark | 数学和高难推理评估 |
| P0 | HumanEval / MBPP | Benchmark | 函数级代码生成 |
| P0 | SWE-bench | Benchmark | repo-level software engineering |
| P0 | WebArena / OSWorld / Terminal-Bench | Benchmark | Agent 长任务与工具使用 |
| P1 | RAGAS / TruLens / DeepEval | 工具 | RAG evaluation |
| P1 | FID / IS / CLIPScore / FVD / VBench | 指标 | 图像/视频生成评估 |
| P1 | MLPerf | Benchmark | AI systems benchmark 方法论 |
| P1 | HarmBench / AdvBench / red-teaming reports | Safety eval | 安全和鲁棒性评估 |

---

## Benchmark Card 模板

```markdown
# Benchmark Card

## Task Definition
## Input / Output Format
## Dataset Source
## Leakage / Contamination Risk
## Metrics
## Baselines
## Cost / Latency Measurement
## Failure Taxonomy
## Human Review Policy
## Versioning / Change Log
```

---

## 各方向评估重点

| 方向 | 重点指标 |
|------|----------|
| LLM | accuracy、calibration、format following、cost/token |
| Reasoning | pass@k、verifier accuracy、reward hacking、solution diversity |
| Code Agent | resolved rate、test pass、diff size、trajectory length、repair loop success |
| RAG | recall@k、faithfulness、citation correctness、answer correctness、latency |
| VLM | OCR、grounding、chart QA、visual hallucination |
| Generative | FID、CLIPScore、FVD、human preference、safety |
| Serving | TTFT、TPOT、throughput、P95/P99 latency、GPU utilization、cost |

---

## 实践项目 / 完成标准

### Project 1：Unified Eval Harness

- 选择一个小任务集合。
- 支持多模型运行。
- 输出 JSONL traces。
- 自动生成 summary report。

### Project 2：Failure Taxonomy Report

- 对 100 个失败样例分类。
- 至少区分 model failure、retrieval failure、tool failure、environment failure、eval failure。
- 输出改进优先级。

### Project 3：Regression Suite

- 将高频失败样例固化成回归测试。
- 每次 prompt / harness / model 更新后跑一次。

---

## 延伸资料

- Agent Benchmarks：`agent-engineering/agent-benchmarks.md`
- RAG：`retrieval-rag/README.md`
- AI Infra Serving：`ai-infra/08-llm-serving-frontier.md`
- Generative Models：`generative-models/README.md`

### 补充：ARC-AGI

- **ARC-AGI**：强调抽象推理、少样本归纳和泛化能力的 benchmark。适合作为 MMLU / GSM8K / MATH / GPQA 之外，观察模型是否具备组合泛化和任务外推能力的评估材料。

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度 |
| 过时风险 | 高 |
| 维护重点 | LLM/RAG/Agent/生成模型 benchmark、leaderboard 污染和评估协议变化 |
