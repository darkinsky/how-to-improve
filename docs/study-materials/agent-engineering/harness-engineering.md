# Harness Engineering（驭缰工程）学习资料

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering |
| 材料类型 | 专题 / 工程实践 |
| 难度 | 进阶 |
| 优先级 | P1 / Frontier / Hands-on |
| 状态 | 需更新 |
| 建议用途 | 理解 Agent harness、runtime、tools 与评估 |

---

> 综合来源：OpenAI、Anthropic、Stripe、LangChain、Mitchell Hashimoto、ThoughtWorks、CMU/耶鲁/斯坦福等
> 采集时间：2026-05-23
> 说明：本文档仅收录外网资料链接，不包含公司内网链接

> **研究进展补充**：2026 年 3-5 月 Harness Engineering 方向论文明显增多，已整理为：[Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)。建议把本文作为概念/工程实践主线，把论文速读作为研究前沿补充阅读。

> **评测补充**：Agent 不能只看最终答案，benchmark 和轨迹审计同样关键。评测路线见：[Agent Benchmarks](agent-benchmarks.md)。

---

## 先看结论

- Harness Engineering 的核心判断是：Agent 的可靠性不仅取决于模型，更取决于模型外部的运行系统。
- Prompt Engineering 解决“怎么问”，Context Engineering 解决“给什么信息”，Harness Engineering 解决“环境如何约束、执行、验证和恢复”。
- 一个成熟 harness 至少要包含：context builder、tool router、sandbox、memory/state、verifier、trajectory logger。
- 生产级 Agent 不能只看最终答案，必须记录轨迹、支持 replay、做 regression benchmark 和安全审计。
- 失败模式通常来自环境缺陷：权限过大、目标不清、状态丢失、工具反馈差、没有独立验证器。
- 完成标准：能设计一个可测试、可回放、可审计的 coding / terminal agent harness。

---

## 一、背景与起源

### 1.1 三代 AI 工程范式的演进

| 阶段 | 核心问题 | 工程师角色 |
|------|---------|-----------|
| **Prompt Engineering** (2023-2024) | 该怎么问模型？ | 写指令的人 |
| **Context Engineering** (2025 中) | 该让模型看到什么？ | 搭信息环境的人 |
| **Harness Engineering** (2026.2) | 整个环境该怎么运作？ | 设计运行系统的人 |

### 1.2 关键时间线

- **2025 年 8 月**：OpenAI 三名工程师开始 Codex Agent 实验项目，零手写代码
- **2025 年 11 月**：Anthropic 发布博客《Effective Harnesses for Long-Running Agents》，首次系统讨论长期 Agent 的约束设计
- **2026 年 2 月 5 日**：HashiCorp 联合创始人 Mitchell Hashimoto 在博客《My AI Adoption Journey》中正式命名 \"Harness Engineering\"
- **2026 年 2 月 11 日**：OpenAI 发布官方博客《Harness Engineering: Leveraging Codex in an Agent-First World》，披露 100 万行代码实验
- **2026 年 3-5 月**：LangChain、Anthropic、ThoughtWorks、Stripe 等团队陆续发布实践报告；CMU/耶鲁/斯坦福发布学术综述

### 1.3 核心公式

```
Agent = Model + Harness
```

- **Model**：负责推理与生成
- **Harness**：模型之外的一切 —— 系统提示词、工具调用、文件系统、沙箱、编排逻辑、中间件、反馈回路、约束机制、可观测性

类比：**LLM 是 CPU，Harness 是操作系统**。CPU 再强，OS 频繁崩溃也没用。

### 1.4 为什么现在需要 Harness Engineering？

当 AI Agent 进入生产环境、执行跨步骤的长期任务时，出现四类典型失败：

1. **试图一步到位**：Agent 倾向于一个会话做完所有事，上下文窗口被撑爆
2. **过早宣布胜利**：部分功能完成就标记\"完成\"，不管还有大量未实现
3. **过早标记功能完成**：单测跑通就停止，不检查端到端测试和联调
4. **模式复制**：Agent 忠实复制代码库中的\"坏模式\"，占比超过 5% 时新代码采用概率 > 70%

**这些问题的根因不是\"模型不够聪明\"，而是运行环境缺乏结构化约束。**

---

## 二、核心概念与六层架构

### 2.1 什么是 Harness？

一个成熟的 Agent Harness 通常包含六层架构：

| 层级 | 名称 | 解决什么问题 | 关键设计 |
|------|------|-------------|---------|
| **L1** | 信息边界层 | Agent 该知道什么、不该知道什么 | 定义角色目标，裁剪无关信息，结构化任务状态 |
| **L2** | 工具系统层 | Agent 怎么和外部世界交互 | 工具选择、调用时机控制、结果提炼反馈 |
| **L3** | 执行编排层 | 多步骤任务怎么串联 | 理解-判断-分析-生成-检查的轨道推进 |
| **L4** | 记忆与状态层 | 长任务中间结果管理 | 独立管理任务状态、中间产物和长期记忆 |
| **L5** | 评估与观测层 | Agent 怎么验证对错 | 独立于生成过程的验证机制 |
| **L6** | 约束校验恢复层 | 出错了怎么办 | 预设规则拦截，失败时重试、回滚或降级 |

> 不要一上来就想搭齐六层。更务实的做法：**先做 L1 + L6**（信息边界 + 约束恢复），投入最低但最易见效。

### 2.2 Agent Runtime 分层

从工程实现看，Harness 可以拆成一个可观测、可测试、可替换的 runtime：

```text
Task Input
  ↓
Context Builder
  ↓
Planner / Controller
  ↓
Tool Router / Permission Gate
  ↓
Executor / Sandbox
  ↓
Memory Manager / State Store
  ↓
Verifier / Evaluator
  ↓
Trajectory Logger / Auditor
```

| 层级 | 职责 | 常见失败 |
|------|------|----------|
| Context Builder | 选择模型应该看到的文件、历史、状态 | 上下文过载、遗漏关键事实 |
| Planner / Controller | 拆任务、决定下一步、管理循环 | 过度规划、兜圈子、提前收工 |
| Tool Router | 决定可用工具、参数校验、权限控制 | 越权调用、不必要副作用 |
| Sandbox / Executor | 隔离执行命令、浏览器、文件操作 | 环境污染、不可复现 |
| Memory / State Store | 保存任务状态、长期记忆和中间产物 | 记忆污染、状态不一致 |
| Verifier | 用测试、lint、规则或外部评估验证结果 | 自我评价偏差、成功幻觉 |
| Trajectory Logger | 记录消息、工具调用、diff、验证结果 | 失败不可解释、无法回放 |

一个好的 Agent runtime 不是让模型更自由，而是让模型在**明确边界、可验证反馈和可回放轨迹**中行动。

### 2.3 Harness、Prompt Engineering、Context Engineering 的区别

| 范式 | 核心问题 | 主要产物 | 局限 |
|------|----------|----------|------|
| Prompt Engineering | 该怎么问模型？ | 指令、few-shot、输出格式 | 主要约束单轮生成 |
| Context Engineering | 该让模型看到什么？ | 检索、摘要、上下文窗口管理 | 仍偏信息供给，不管执行闭环 |
| Harness Engineering | 整个运行环境该如何运作？ | runtime、tools、state、verifier、sandbox、audit | 工程复杂度更高，需要评测闭环 |

可以粗略理解为：

```text
Prompt = 指令
Context = 信息环境
Harness = 可执行、可约束、可观测的运行系统
```

### 2.4 Agent 常见失败模式

| 失败模式 | 现象 | 根因 |
|---------|------|------|
| 上下文焦虑 | 上下文快满时犹豫不决或提前收工 | 长期运行缺乏 Context Reset |
| 兜圈子（Doom Loop） | 同一文件反复修改 10+ 次 | 缺乏循环检测和视角切换 |
| 自我评价偏差 | Agent 自信地说做完了，实际质量一般 | 生成和评估用同一模型 |
| 成功幻觉 | 读到通过测试的输出就以为自己实现了功能 | 反馈噪声淹没信号 |

---

---

## 三、延伸阅读：案例与研究

本文保留 harness 的核心概念、架构、评测和学习路线。为降低单篇长度，案例和研究前沿拆到两个附录：

- [Harness Engineering Cases](harness-engineering-cases.md)：OpenAI、Anthropic、Stripe、LangChain、HumanLayer 等工程案例。
- [Harness Engineering Research](harness-engineering-research.md)：Meta-Harness、自动演化、轨迹安全和领域专用 harness 研究。
- [Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)：论文清单与速读顺序。

---

## 四、评测、审计与安全闭环

Harness 的质量不能靠主观感觉判断，必须用 benchmark、轨迹审计和回归任务验证。完整 benchmark 路线见：[Agent Benchmarks](agent-benchmarks.md)。

### 5.1 Harness 评测指标

| 指标 | 说明 |
|------|------|
| Task Success Rate | 最终任务是否完成 |
| Verification Pass Rate | 测试、lint、规则检查是否通过 |
| Tool Call Efficiency | 工具调用次数是否合理 |
| Context Efficiency | token 使用是否可控，是否重复读无关信息 |
| Recovery Ability | 失败后能否定位问题、重试、回滚或降级 |
| Trajectory Safety | 是否越权、泄漏、破坏环境、绕过规则 |
| Reproducibility | 同一任务多次运行是否稳定 |

### 5.2 轨迹审计清单

每次 Agent run 至少记录：

```text
task input
selected context
model messages
tool calls + arguments
tool outputs
file diffs
network requests
permission prompts
verification commands
final result
```

没有轨迹，就无法判断失败来自模型、工具、上下文选择、权限设计还是验证器。

### 5.3 安全边界

Agent Harness 应默认最小权限：

- 文件系统：限定可读 / 可写目录；
- Shell：危险命令需要确认或禁用；
- 网络：外部请求需要白名单或审计；
- Secret：任何 token、key、cookie 不应进入模型上下文；
- Git：提交、push、release 需要明确验证步骤；
- 数据：用户隐私和内部资料不能被自动上传或外发。

### 5.4 Harness 设计检查清单

- [ ] 是否有明确任务完成标准？
- [ ] 是否有工具权限边界？
- [ ] 是否记录完整轨迹并可回放？
- [ ] 是否有独立 verifier，而不是只听 Agent 自我汇报？
- [ ] 是否能检测重复循环和无效重试？
- [ ] 是否支持失败恢复、回滚或降级？
- [ ] 是否有小型 regression benchmark？
- [ ] 是否能解释每次失败属于哪类问题？

---

## 五、工具与框架生态

### 6.1 核心资源

| 资源 | 类型 | 链接 |
|------|------|------|
| Harness Engineering 学习项目 | GitHub 仓库 | https://github.com/deusyu/harness-engineering |
| JavaGuide 六层架构详解 | 文章 | https://javaguide.cn/ai/agent/harness-engineering.html |
| 腾讯云 Harness 完整解读 | 文章 | https://cloud.tencent.com/developer/article/2664396 |
| 十大实践指南（OpenAI/Stripe/Anthropic） | 文章 | https://edison-a-n.github.io/2026/03/14/harness-engineering-practical-guide/ |
| Anthropic Building Effective Agents | 官方工程文章 | https://www.anthropic.com/engineering/building-effective-agents |
| Anthropic Multi-agent Research System | 官方工程文章 | https://www.anthropic.com/engineering/built-multi-agent-research-system |
| DeepSky 博客 | 文章 | https://www.cnblogs.com/deep-sky/p/19867681 |
| 长运行多智能体框架设计 | 文章 | https://cloud.tencent.com/developer/article/2647567 |
| 从概念到落地（MornAI） | 文章 | https://www.mornai.cn/news/ai-agent/harness-engineering/ |
| 掘金 Anthropic 多智能体拆解 | 文章 | https://juejin.cn/post/7620708166142197802 |

### 6.2 重要论文

| 论文 | 链接 | 要点 |
|------|------|------|
| Meta-Harness（Stanford） | https://arxiv.org/abs/2603.28052 | 自动搜索优化 Harness 代码 |
| CMU/耶鲁/亚马逊 Harness 综述 | 搜索：\"Harness Engineering CMU Yale\" | 系统梳理 Harness 学术基础 |
| 上海交大 Agent Harness 综述 | 搜索：\"SJTU Agent Harness survey\" | Agent 时代基座理论 |

### 6.3 经典博文

| 作者 | 时间 | 标题/内容 |
|------|------|-----------|
| OpenAI | 2026.02 | Harness Engineering: Leveraging Codex in an Agent-First World |
| Mitchell Hashimoto | 2026.02.05 | My AI Adoption Journey（首次正式提出 Harness Engineering） |
| Anthropic | 2025.11 | Effective Harnesses for Long-Running Agents |
| LangChain | 2026.03 | The Anatomy of an Agent Harness（Vivek Trivedi） |
| ThoughtWorks (Böckeler) | 2026.03 | Martin Fowler 博客分析 |

---

## 六、关键洞察与趋势

### 7.1 环境比模型更关键（实证）

三个独立实验一致结论：
1. **LangChain**：不改模型，Terminal Bench 排名从 30 → 5
2. **Can Boluk**：Hashline 协议，成功率 6.7% → 68.3%
3. **HumanLayer**：沉默即成功，达成率 43% → 78%

### 7.2 模型-Harness 耦合与解耦

- 现在 Agent 产品（Claude Code、Codex）把 Model 和 Harness 一起调优
- 这会导致\"过拟合\"：Opus 在 Claude Code Harness 下得分远高于其他 Harness
- **结论**：为任务选择 Harness 时，不要默认自带的就最合适

### 7.3 尚待解决的问题

| 问题 | 现状 | 难点 |
|------|------|------|
| 棕地项目改造 | 公开成功案例几乎全是绿地项目 | 十年代码库，到处技术债，Harness 引入困难 |
| 功能验证 | 用 AI 测试验证 AI 代码，缺乏独立视角 | \"用同一双眼睛检查自己的作业\" |
| 长期可维护性 | AI 经常重新实现已有功能 | 长期效果不明 |
| 单 Agent vs 多 Agent | 取决于规模场景 | 小项目单 Agent 够用，大项目需专业化分工 |
| Harness 该做厚做薄 | 场景决定 | 模型变强后，Harness 应定期简化 |

### 7.4 核心金句

> \"为了获得更高的 AI 自主性，运行时必须受到更严格的约束。增加信任需要的不是更多自由，而是更多限制。\"
> — Birgitta Böckeler, ThoughtWorks

> \"If it cannot be enforced mechanically, agents will deviate.\"
> — OpenAI 内部原则

> \"你必须不断提醒自己：你是在为 AI 写这个框架，不是为自己写。\"
> — Nicholas Carlini

> \"Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing.\"
> — Anthropic Labs

---

## 七、推荐学习路线

### Step 1：理解核心理念（1-2 天）
- 阅读 JavaGuide 六层架构详解：https://javaguide.cn/ai/agent/harness-engineering.html
- 阅读腾讯云完整解读：https://cloud.tencent.com/developer/article/2664396
- 掌握 Agent = Model + Harness 的核心公式

### Step 2：深入学习实践案例（2-3 天）
- 阅读十大实践指南：https://edison-a-n.github.io/2026/03/14/harness-engineering-practical-guide/
- 阅读 Anthropic 工程实践文章：https://www.anthropic.com/engineering/building-effective-agents
- 重点理解 OpenAI、Anthropic、Stripe 三个案例

### Step 3：追踪前沿研究（1-2 天）
- 阅读 Meta-Harness 论文：https://arxiv.org/abs/2603.28052
- 搜索 CMU/耶鲁/亚马逊综述
- 关注 LangChain Terminal Bench 2.0 排行榜

### Step 4：动手实践（持续）
- 从 P0 开始：创建 AGENTS.md + 基础 Linter
- 搭建反馈回路：沉默即成功原则
- 引入架构约束：自定义 Linter + CI 阻断
- 渐进推进到自动化层

---

*本文档将持续更新。Harness Engineering 是 2026 年 AI 工程领域最重要的范式转变，它标志着 AI 开发的关注点从\"怎么跟模型说话\"转向\"怎么为 AI 构建可靠的运行环境\"。*

---
