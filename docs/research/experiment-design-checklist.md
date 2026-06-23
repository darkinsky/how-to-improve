# Experiment Design Checklist

## 先看结论

研究实验的核心是检验假设，而不是堆结果。一个实验计划至少要说明：变量、对照、指标、预期和失败解释。

---

## 实验设计字段

| 字段 | 问题 |
|------|------|
| Hypothesis | 你要验证什么机制或因果关系？ |
| Independent Variables | 主动改变哪些变量？ |
| Controlled Variables | 哪些条件必须固定？ |
| Baseline | 和谁比较才有意义？ |
| Metrics | 主指标、辅助指标、护栏指标是什么？ |
| Dataset / Task | 数据是否覆盖目标场景？ |
| Budget | 计算、时间、样本、人力成本是多少？ |
| Expected Result | 如果假设成立，应该看到什么？ |
| Failure Interpretation | 如果不成立，可能说明什么？ |

---

## Ablation Checklist

- 去掉核心模块是否下降？
- 替换为简单 baseline 是否仍有效？
- 调参收益是否大于方法收益？
- 结果是否对随机种子敏感？
- 是否存在数据泄漏或 benchmark overfitting？
- 是否报告方差、置信区间或多次运行结果？

---

## 实验计划模板

```markdown
# Experiment Plan

## Hypothesis
## Baseline
## Variables
## Metrics
## Dataset
## Protocol
## Expected Outcome
## Risks
## Decision Rule
```
