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

### 2.2 Agent 常见失败模式

| 失败模式 | 现象 | 根因 |
|---------|------|------|
| 上下文焦虑 | 上下文快满时犹豫不决或提前收工 | 长期运行缺乏 Context Reset |
| 兜圈子（Doom Loop） | 同一文件反复修改 10+ 次 | 缺乏循环检测和视角切换 |
| 自我评价偏差 | Agent 自信地说做完了，实际质量一般 | 生成和评估用同一模型 |
| 成功幻觉 | 读到通过测试的输出就以为自己实现了功能 | 反馈噪声淹没信号 |

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

## 四、工程落地实践

### 4.1 OpenAI：100 万行零手写代码

**关键数据**：
- 3 名工程师 → 7 人，5 个月 → 约 100 万行代码，1500 个 PR
- 效率约人工 10 倍，零行手写代码

**核心实践**：

| 实践 | 做法 | 关键细节 |
|------|------|---------|
| 地图式文档 | AGENTS.md 仅约 100 行，指向 docs/ 子文档 | 渐进式披露，按需加载 |
| 机械化架构约束 | Types→Config→Repo→Service→Runtime→UI 层级依赖 | 自定义 Linter 阻断违规，报错附带修复说明 |
| 可观测性工具化 | 接入 Chrome DevTools Protocol | Agent 可自测、自验证 |
| 垃圾收集 | 每日\"GC Day\"，后台 Agent 自动清理 | 对抗 AI 生成代码的熵积累 |
| 仓库作为事实来源 | 团队知识作为版本控制制品 | 替代 Slack/Wiki/Docs 中的不可索引知识 |

### 4.2 Anthropic：三智能体架构与 Context Reset

**Carlini C 编译器项目**：
- 16 个并行 Claude Opus 实例，约 2000 个会话
- 产出 10 万行 Rust 代码，GCC torture test 99% 通过率
- 可编译 PostgreSQL、Redis、FFmpeg、CPython、Linux 6.9 Kernel 等 150+ 项目
- API 成本约 2 万美元

**Harness 关键细节**：
- 日志不输出到控制台，写文件 + grep 友好的单行格式
- 测试子采样：每 Agent 只跑随机 1-10% 测试
- Agent 角色专业化：核心编译、去重、优化、文档
- \"我不是在为自己写测试框架，是在为 Claude 写\"

**三智能体架构（GAN 启发）**：
```
Planner（规划） → Generator（执行） ⇄ Evaluator（评估）
```
- Evaluator 用 Playwright MCP 实际点击、打分
- Context Reset：上下文快满时结构化提取状态 → 启动新 Agent → 交接
- 重要发现：模型越强，Harness 中部分组件可能冗余，需要定期简化

### 4.3 Stripe Minions 系统

**关键数据**：每周 1300+ 个完全由 Agent 生成、无人手写代码的 PR 被合并

**组件**：

| 组件 | 关键设计 |
|------|---------|
| Devbox | AWS EC2 预装，预热池分配，10 秒启动，\"牲口不是宠物\" |
| 编排状态机 | 混合确定性节点（lint/push）+ Agent 节点（实现功能/修 CI） |
| Toolshed MCP | 集中式 MCP 服务，近 500 个工具，每 Minion 拿到筛选子集 |
| 反馈回路 | Pre-push hook 秒级修 lint；最多 2 轮 CI，覆盖 300 万+ 测试 |

**理念**：What's good for humans is good for agents → Agent 是一等公民

### 4.4 Mitchell Hashimoto：个人 Harness 实践

**六步路线**：

| 步骤 | 做法 |
|------|------|
| 放弃聊天模式 | 让 Agent 在能读文件、跑程序的环境干活 |
| 复现自己的工作 | 每件事做两次，自己一次 + 让 Agent 一次 |
| 下班前启动 Agent | 最后 30 分钟布置深度调研、模糊探索等任务 |
| 外包确定性任务 | Agent 几乎一定做好的任务后台跑 |
| 工程化 Harness | Agent 每犯一次错，工程化一个方案防再次犯错 |
| 始终有 Agent 跑 | 目标 10-20% 工作时间有后台 Agent 运行 |

**AGENTS.md 哲学**：每一行对应一个过去的 Agent 失败案例，是活的反馩循环，不是静态制品。

### 4.5 LangChain Harness 三阶段路线图

| 阶段 | 时间 | 目标 | 操作 |
|------|------|------|------|
| Phase 1：信息层 | 1-2 天 | 从\"百科全书\"到\"地图\" | 文档拆解 + 索引 |
| Phase 2：约束层 | 3-5 天 | 从\"软规范\"到\"硬检查\" | Linter + CI 集成 |
| Phase 3：自动化层 | 1-2 周 | 从\"人工治理\"到\"系统自愈\" | 多 Agent 协作 + 自动治理 |

### 4.6 沉默即成功（Silence is Success）

HumanLayer 团队的实验发现：

**问题**：完整测试套件输出 4000+ 行 → 噪音淹没关键失败信息 → Agent 产生\"成功幻觉\"

**解决方案**：成功返回极简 ✓，失败才打印全部错误细节

**结果**：
- 10 步内完成任务比例：43% → 78%
- 平均节省约 35% 上下文 token

---

## 五、工具与框架生态

### 5.1 核心资源

| 资源 | 类型 | 链接 |
|------|------|------|
| Harness Engineering 学习项目 | GitHub 仓库 | https://github.com/deusyu/harness-engineering |
| JavaGuide 六层架构详解 | 文章 | https://javaguide.cn/ai/agent/harness-engineering.html |
| 腾讯云 Harness 完整解读 | 文章 | https://cloud.tencent.com/developer/article/2664396 |
| 十大实践指南（OpenAI/Stripe/Anthropic） | 文章 | https://edison-a-n.github.io/2026/03/14/harness-engineering-practical-guide/ |
| 最佳实践操作手册（知乎） | 文章 | https://zhuanlan.zhihu.com/p/2023068557592863537 |
| Anthropic Harness 架构拆解（知乎） | 文章 | https://zhuanlan.zhihu.com/p/2024114529022276730 |
| DeepSky 博客 | 文章 | https://www.cnblogs.com/deep-sky/p/19867681 |
| 长运行多智能体框架设计 | 文章 | https://cloud.tencent.com/developer/article/2647567 |
| 从概念到落地（MornAI） | 文章 | https://www.mornai.cn/news/ai-agent/harness-engineering/ |
| 掘金 Anthropic 多智能体拆解 | 文章 | https://juejin.cn/post/7620708166142197802 |

### 5.2 重要论文

| 论文 | 链接 | 要点 |
|------|------|------|
| Meta-Harness（Stanford） | https://arxiv.org/abs/2603.28052 | 自动搜索优化 Harness 代码 |
| CMU/耶鲁/亚马逊 Harness 综述 | 搜索：\"Harness Engineering CMU Yale\" | 系统梳理 Harness 学术基础 |
| 上海交大 Agent Harness 综述 | 搜索：\"SJTU Agent Harness survey\" | Agent 时代基座理论 |

### 5.3 经典博文

| 作者 | 时间 | 标题/内容 |
|------|------|-----------|
| OpenAI | 2026.02 | Harness Engineering: Leveraging Codex in an Agent-First World |
| Mitchell Hashimoto | 2026.02.05 | My AI Adoption Journey（首次正式提出 Harness Engineering） |
| Anthropic | 2025.11 | Effective Harnesses for Long-Running Agents |
| LangChain | 2026.03 | The Anatomy of an Agent Harness（Vivek Trivedi） |
| ThoughtWorks (Böckeler) | 2026.03 | Martin Fowler 博客分析 |

---

## 六、关键洞察与趋势

### 6.1 环境比模型更关键（实证）

三个独立实验一致结论：
1. **LangChain**：不改模型，Terminal Bench 排名从 30 → 5
2. **Can Boluk**：Hashline 协议，成功率 6.7% → 68.3%
3. **HumanLayer**：沉默即成功，达成率 43% → 78%

### 6.2 模型-Harness 耦合与解耦

- 现在 Agent 产品（Claude Code、Codex）把 Model 和 Harness 一起调优
- 这会导致\"过拟合\"：Opus 在 Claude Code Harness 下得分远高于其他 Harness
- **结论**：为任务选择 Harness 时，不要默认自带的就最合适

### 6.3 尚待解决的问题

| 问题 | 现状 | 难点 |
|------|------|------|
| 棕地项目改造 | 公开成功案例几乎全是绿地项目 | 十年代码库，到处技术债，Harness 引入困难 |
| 功能验证 | 用 AI 测试验证 AI 代码，缺乏独立视角 | \"用同一双眼睛检查自己的作业\" |
| 长期可维护性 | AI 经常重新实现已有功能 | 长期效果不明 |
| 单 Agent vs 多 Agent | 取决于规模场景 | 小项目单 Agent 够用，大项目需专业化分工 |
| Harness 该做厚做薄 | 场景决定 | 模型变强后，Harness 应定期简化 |

### 6.4 核心金句

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
- 阅读最佳实践操作手册：https://zhuanlan.zhihu.com/p/2023068557592863537
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

## 最新论文与研究进展（2026）

Harness Engineering 已经从工程经验进入研究阶段，近期论文主要围绕：

- **Harness 表示化**：例如 Natural-Language Agent Harnesses，将 harness 政策抽象成可编辑、可检查、可迁移的自然语言对象。
- **Harness 自动演化**：例如 Agentic Harness Engineering，通过组件/经验/决策可观测性，让 coding-agent harness 自动改进。
- **运行时适配与推理时对齐**：不改模型参数，而通过接口、工具、轨迹控制和验证门控改善稳定性。
- **安全审计**：从答案安全扩展到轨迹安全，检查工具调用、资源访问和上下文泄漏。
- **领域专用 Harness**：科研、算法发现、可视化、仿真、搜索等任务正在出现垂直 harness。

完整论文清单与阅读顺序见：

- [Harness Engineering 最新论文速读（2026）](harness-engineering-papers-2026.md)

