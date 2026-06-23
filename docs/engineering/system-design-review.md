# System Design Review

## 先看结论

系统设计评审的目标不是证明方案完美，而是把关键权衡显性化：

```text
需求 → 约束 → 方案 → 权衡 → 风险 → 验证 → 演进路径
```

如果一个设计不能说明如何失败、如何观测、如何回滚，就还不够完整。

---

## 评审结构

1. **问题定义**：用户、场景、非目标、成功指标。
2. **约束**：流量、延迟、成本、团队、人力、兼容性、合规。
3. **核心设计**：组件、数据流、接口、状态、依赖。
4. **关键权衡**：一致性 vs 可用性、性能 vs 成本、通用性 vs 简洁性。
5. **失败模式**：超时、重试风暴、数据不一致、下游不可用、资源耗尽。
6. **可观测性**：日志、指标、trace、dashboard、alert。
7. **上线计划**：灰度、回滚、数据迁移、验证门槛。

---

## 设计评审表

| 维度 | 问题 |
|------|------|
| Scope | 这个方案明确不解决什么？ |
| SLA | P50/P95/P99、错误率、可用性目标是什么？ |
| Data | 数据模型、生命周期、备份、删除策略是什么？ |
| API | 接口契约、版本兼容、错误处理是否明确？ |
| Dependency | 关键外部依赖失败时怎么办？ |
| Capacity | 峰值容量、扩容方式、成本上限是什么？ |
| Security | 鉴权、审计、敏感数据、权限边界是什么？ |
| Operations | 如何部署、监控、告警、回滚？ |

---

## 输出模板

```markdown
# System Design Review

## Context
## Goals / Non-goals
## Constraints
## Proposed Design
## Alternatives Considered
## Failure Modes
## Observability
## Rollout / Rollback
## Open Questions
```
