# Experiment Tracking

## 先看结论

工程实验要能回答三个问题：改了什么、指标变了多少、能不能复现。

```text
假设 → 实验设置 → 指标 → 结果 → 解释 → 决策
```

没有 baseline、没有固定输入、没有指标定义的实验，很难转化为可靠结论。

---

## 实验记录字段

| 字段 | 说明 |
|------|------|
| Hypothesis | 预期改动会改善什么，为什么？ |
| Baseline | 对照版本、commit、配置、数据集 |
| Change | 本次唯一改动或主要变量 |
| Metrics | 主要指标、护栏指标、采集方式 |
| Environment | 硬件、依赖版本、数据版本、随机种子 |
| Result | 数值、图表、日志、失败样例 |
| Decision | ship / rollback / retry / investigate |
| Follow-up | 后续问题和下一步实验 |

---

## 常见坑

- 只看平均值，不看 P95/P99、方差和失败样例；
- 同时改多个变量，无法解释结果；
- 没有固定随机种子或数据切分；
- benchmark 与真实 workload 不一致；
- 只记录成功实验，不记录失败实验；
- 没有把结论绑定到 commit、配置和数据版本。

---

## 复盘模板

```markdown
# Experiment Review

## Hypothesis
## Baseline
## Change
## Metrics
## Environment
## Result
## Interpretation
## Decision
## Follow-up
```
