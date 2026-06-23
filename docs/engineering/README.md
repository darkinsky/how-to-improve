# Engineering

记录工程实践相关的改进：开发效率、代码质量、架构设计、调试方法、自动化、工具链等。

---

## 先看结论

Engineering 目录不只记录“做了什么”，更要沉淀可复用的工程判断：

```text
问题定义 → 约束澄清 → 方案设计 → 实施验证 → 复盘沉淀
```

每篇内容尽量回答：为什么做、有哪些约束、如何验证、失败时怎么恢复、下次如何更快。

---

## 方法论索引

| 文档 | 适用场景 | 输出物 |
|------|----------|--------|
| [Debugging Playbook](debugging-playbook.md) | 线上问题、测试失败、性能异常、复杂 bug | 假设树、证据链、最小复现、修复记录 |
| [Code Review Checklist](code-review-checklist.md) | PR review、自查、重构前后对比 | review 结论、风险点、必须修改项 |
| [System Design Review](system-design-review.md) | 新系统设计、架构升级、技术选型 | 设计评审记录、权衡表、风险清单 |
| [Experiment Tracking](experiment-tracking.md) | 性能优化、模型实验、A/B 测试、工程试验 | 实验记录、指标对比、结论与复盘 |

---

## 每篇工程笔记建议包含

- 背景问题；
- 约束条件；
- 尝试方案；
- 效果评估；
- 可复用经验；
- 下次遇到同类问题的检查清单。
