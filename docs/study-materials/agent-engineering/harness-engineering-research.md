# Harness Engineering Research

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering / Harness Engineering |
| 材料类型 | 研究前沿 / 论文路线 |
| 难度 | 前沿 |
| 优先级 | P1 / Frontier |
| 状态 | 推荐 |
| 建议用途 | 跟踪 harness 表示化、自动演化、运行时适配和轨迹安全研究 |

---

## 先看结论

- Harness 研究正在从经验工程走向可表示、可搜索、可优化和可审计的系统对象。
- 关键方向包括：Meta-Harness、Natural-Language Agent Harnesses、Agentic Harness Engineering、轨迹安全、领域专用 harness。
- 研究阅读不要只看 benchmark 提升，还要看可复现性、任务边界、harness 是否过拟合模型或环境。

---

## 三、前沿研究

### 3.1 Meta-Harness：自动优化 Harness 代码

- **arXiv**: https://arxiv.org/abs/2603.28052
- **作者**: Yoonho Lee 等（Stanford University）
- **核心思想**：引入一个**外循环系统**，在 Harness 代码空间中进行搜索优化
- **关键结果**：
  - 在线文本分类：比 SOTA 系统提升 7.7 分，同时使用 4 倍更少的上下文 token
  - 数学推理：单个 Harness 使 5 个保留模型在 200 道 IMO 级问题上平均提升 4.7 分
  - Agentic Coding：在 TerminalBench-2 上超越手工基线
- **启示**：Harness 的优化正在走向自动化，无需修改模型权重

### 3.2 CMU/耶鲁/亚马逊联合综述（2026.05）

- **来源**: https://news.qq.com/rain/a/20260522A04EVA00
- **核心发现**：同一个大模型塞进不同 Agent 框架系统，表现\"判若两模\"
- **结论**：决定 Agent 在真实世界表现的，不是模型本身，而是包在模型外面的 Harness

### 3.3 上海交通大学 Harness 综述（2026.04）

- **来源**: https://news.qq.com/rain/a/20260414A01KTO00
- **框架**：系统梳理了 Harness 作为 Agent 时代基座的理论体系
- **定位**：Harness 是\"Agent 时代统管一切的基座\"

### 3.4 LangChain Terminal Bench 2.0 实验

- **实验设计**：固定模型为 gpt-5.2-codex，只改 Harness（系统提示词结构、工具描述方式、中间件）
- **结果**：得分从 52.8% → 66.5%，全球排名从第 30 → 第 5
- **关键改进**：
  1. 系统提示词强制\"构建-验证\"循环
  2. 工具上下文直接注入而非让 Agent 探索
  3. \"推理三明治\"策略：规划+验证用 xhigh，中间用 high
  4. LoopDetectionMiddleware 检测 Doom Loop

### 3.5 Hashline 协议：零成本大幅提升

- **来源**: https://can.ac （安全研究员 Can Boluk）
- **核心思想**：每行代码附带基于内容的哈希标签（2-3 字符），编辑时引用标签而非整行原文，写入时校验哈希一致性
- **实验结果**：
  - Grok Code Fast 1 成功率：6.7% → 68.3%（10 倍）
  - Gemini 成功率提升 8%（比大多数模型升级还大，且训练成本为零）
  - Grok 4 Fast 输出 token 下降 61%

---

---

## 最新论文与研究进展（2026）

Harness Engineering 已经从工程经验进入研究阶段，近期论文主要围绕：

- **Harness 表示化**：例如 Natural-Language Agent Harnesses，将 harness 政策抽象成可编辑、可检查、可迁移的自然语言对象。
- **Harness 自动演化**：例如 Agentic Harness Engineering，通过组件/经验/决策可观测性，让 coding-agent harness 自动改进。
- **运行时适配与推理时对齐**：不改模型参数，而通过接口、工具、轨迹控制和验证门控改善稳定性。
- **安全审计**：从答案安全扩展到轨迹安全，检查工具调用、资源访问和上下文泄漏。
- **领域专用 Harness**：科研、算法发现、可视化、仿真、搜索等任务正在出现垂直 harness。

完整论文清单与阅读顺序见：

- [Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)

---

## 推荐阅读顺序

1. 先读 Meta-Harness，理解 harness 代码空间搜索。
2. 再读 Natural-Language Agent Harnesses，理解 harness policy 如何被表示、编辑和迁移。
3. 然后读 Agentic Harness Engineering，关注组件、经验、决策可观测性如何驱动自动改进。
4. 最后读 Harness Safety，把评估从答案安全扩展到轨迹安全、工具安全和上下文安全。

## 实践项目 / 完成标准

- 选择一个固定 coding-agent benchmark；
- 修改 harness 的 context builder、tool policy、verifier、loop detection 四个组件；
- 记录 success rate、tool calls、token cost、失败类型和轨迹安全问题；
- 输出一份 harness ablation report。
