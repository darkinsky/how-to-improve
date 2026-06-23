# Harness Engineering Cases

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering / Harness Engineering |
| 材料类型 | 案例 / 工程实践 |
| 难度 | 进阶 |
| 优先级 | P1 / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 对比 OpenAI、Anthropic、Stripe、LangChain 等 harness 落地方式 |

---

## 先看结论

- Harness 案例的共性不是“用了哪个模型”，而是把任务、工具、状态、验证和恢复做成可执行系统。
- 生产级案例普遍强调：仓库即事实源、机械化约束、trajectory logging、测试反馈和权限边界。
- 读案例时不要照搬架构，而要抽取 workload、约束、反馈回路和可观测性设计。

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

---

## 阅读方法

1. 先画出每个案例的 harness 组成：context、tools、executor、verifier、logger。
2. 标注哪些约束是机械执行的，哪些仍靠 prompt 或人工流程。
3. 对比不同团队的失败模式：上下文过载、循环、权限、测试噪声、状态丢失。
4. 把可复用做法转成自己的 AGENTS.md、linter、CI 或 regression benchmark。
