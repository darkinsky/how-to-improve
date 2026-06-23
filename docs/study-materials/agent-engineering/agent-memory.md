# Agent Memory（智能体记忆）学习计划与资料汇总

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Agent Engineering |
| 材料类型 | 专题 / 论文路线 |
| 难度 | 中级到进阶 |
| 优先级 | P1 / Frontier |
| 状态 | 可用 |
| 建议用途 | 理解 Agent memory 的类型、架构与实践 |

---

> 整理时间：2026-04-11
> 目标：系统掌握 LLM Agent 记忆系统的类型、架构、核心算法及工程实践
> 前置推荐：先完成 LLM 基础、RAG、Transformer 注意力机制学习

---

## 先看结论

- Agent Memory 不是简单把聊天记录塞进向量库，而是要决定 **存什么、何时存、怎么检索、如何更新和遗忘**。
- 记忆系统通常分为 in-context、external、in-weights、in-cache；工程上最常见的是外部记忆 + 检索 + 反思。
- 好的 memory 需要同时管理 episodic memory、semantic memory 和 procedural memory，而不是只存事实。
- 长任务 Agent 的关键是状态连续性：memory 要和 planner、tool trace、verifier、harness logger 协同设计。
- 评估 memory 不能只看检索准确率，还要看任务成功率、长期一致性、污染率、隐私和过期清理。
- 完成标准：能设计一个带写入策略、检索策略、更新/删除策略和评测任务的 agent memory prototype。

---

## 🗺️ 知识地图

```
LLM Agent Memory（智能体记忆系统）
    │
    ├── 记忆类型（按存储方式）
    │       ├── In-Context Memory（上下文窗口内）
    │       ├── External Memory（外部存储 + 检索）
    │       ├── In-Weights Memory（参数记忆 / 微调）
    │       └── In-Cache Memory（KV Cache 复用）
    │
    ├── 记忆操作（CRUD）
    │       ├── 写入（Memory Writing）：何时存、存什么
    │       ├── 读取（Memory Retrieval）：语义检索、关键词匹配
    │       ├── 更新（Memory Update）：合并、遗忘、进化
    │       └── 删除（Memory Deletion）：过期清理
    │
    ├── 记忆粒度
    │       ├── 事件级（episodic memory）：具体交互记录
    │       ├── 语义级（semantic memory）：知识、事实、偏好
    │       └── 程序级（procedural memory）：操作步骤、技能
    │
    └── 系统架构
            ├── 单 Agent 记忆（MemGPT / A-MEM）
            ├── 多 Agent 共享记忆（ByteRover）
            └── 层次化记忆（短期 + 长期 + 档案）
```

---

## 📚 核心论文（必读）

### 第一阶段：奠基性工作

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **Generative Agents: Interactive Simulacra of Human Behavior** | Park et al. | UIST 2023 | [arXiv:2304.03442](https://arxiv.org/abs/2304.03442) | ⭐⭐ Agent 记忆系统的标志性工作，提出「记忆流 + 反思 + 计划」三层架构 |
| **MemGPT: Towards LLMs as Operating Systems** | Packer et al. | 2023 | [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) | ⭐ 借鉴 OS 虚拟内存思想，实现无限上下文的分层记忆管理 |
| **ReAct: Synergizing Reasoning and Acting in Language Models** | Yao et al. | ICLR 2023 | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) | 推理+行动交替，记忆以 Scratchpad 形式存在于 Trace 中 |
| **Reflexion: Language Agents with Verbal Reinforcement Learning** | Shinn et al. | NeurIPS 2023 | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) | ⭐ 用自然语言反思作为记忆，无需参数更新实现自我改进 |

### 第二阶段：记忆架构进阶

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **A-MEM: Agentic Memory for LLM Agents** | Xu et al. | NeurIPS 2025 | [arXiv:2502.12110](https://arxiv.org/abs/2502.12110) | ⭐ 主动式记忆：自动生成笔记、建立记忆链接、动态进化，克服 MemGPT 结构僵化 |
| **ByteRover: Agent-Native Hierarchical Memory** | Nguyen et al. | 2026 | [SemanticScholar](https://www.semanticscholar.org/paper/ByteRover) | 智能体原生分层记忆，LLM 自身主导记忆的策划、结构化与检索 |
| **LightThinker++: From Reasoning Compression to Memory Management** | Zhu et al. | 2026 | arXiv:2604.xxxxx | 将推理链压缩表示作为「工作记忆」，CoT 压缩与外部记忆统一框架 |
| **Memory in the LLM Era: A Survey** | Liu et al. | 2025 | [GitHub Paper List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | ⭐ 最新全面综述，覆盖 2024-2025 年 Agent 记忆系统全貌 |

### 第三阶段：检索与外部记忆

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **Retrieval-Augmented Generation (RAG)** | Lewis et al. | NeurIPS 2020 | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) | ⭐ RAG 奠基作，外部知识库 + 稠密检索 + 生成的经典范式 |
| **MSA: Memory Sparse Attention (100M Token Context)** | Chen et al. | 2026 | arXiv（2026-03） | 内化记忆于注意力机制，端到端训练支持 100M Token 超长上下文 |
| **RelayCaching: KV Cache 复用加速多 Agent 协作** | Geng et al. | 2026 | arXiv（2026-03） | 解码阶段 KV Cache 跨 Agent 复用，降低多 Agent 协作延迟 |
| **Agentic RAG Survey** | Singh et al. | 2025 | [arXiv:2501.09136](https://arxiv.org/abs/2501.09136) | 将自主 Agent 嵌入 RAG 流程，动态路由与自适应检索策略 |

### 第四阶段：综述与系统性研究

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **A Survey on the Memory Mechanism of LLM-based Agents** | Zhang et al. | ACM 2025 | [arXiv:2404.13501](https://arxiv.org/abs/2404.13501) | ⭐ 最系统的记忆机制综述，分类框架清晰，必读 |
| **ContextBudget: Budget-Aware Context Management for Long-Horizon Search Agents** | 2026 | arXiv:2604.xxxxx | 长视野搜索 Agent 的预算感知上下文管理，解决记忆窗口压力 |

---

## 🧠 核心概念详解

### 记忆四大类型对比

| 类型 | 存储位置 | 优点 | 缺点 | 适用场景 |
|------|----------|------|------|----------|
| **In-Context** | Prompt / 上下文窗口 | 无延迟，推理直接可见 | 受 Token 限制，不持久 | 短对话、单轮任务 |
| **External** | 向量数据库 / KV 存储 | 无限容量，可持久化 | 检索延迟，相关性有损 | 长期记忆、知识库 |
| **In-Weights** | 模型参数（微调） | 零检索开销，泛化强 | 灾难性遗忘，更新成本高 | 专域知识固化 |
| **In-Cache** | KV Cache | 复用前缀无需重算 | 受显存限制，跨会话难 | 多轮对话、共享前缀 |

### Generative Agents 三层记忆架构

```
原始经验流（Memory Stream）
    ↓ 重要性评分 + 时间衰减
检索（Retrieval）← 相关性 + 近期性 + 重要性加权
    ↓
反思（Reflection）：定期归纳高层洞察
    ↓
计划（Planning）：基于记忆制定行动计划
```

---

## 🎓 课程推荐

### 入门课程

| 课程 | 平台 | 语言 | 链接 | 说明 |
|------|------|------|------|------|
| **CS224N: NLP with Deep Learning** | Stanford | 英文 | [web.stanford.edu/class/cs224n](https://web.stanford.edu/class/cs224n/) | NLP 与 LLM 基础，理解 Transformer 上下文机制 |
| **CS330: Deep Multi-Task and Meta-Learning** | Stanford | 英文 | [cs330.stanford.edu](https://cs330.stanford.edu/) | 含记忆增强网络（MANN）等模型记忆方法 |
| **LLM Agents (MOOC)** | Berkeley | 英文 | [llmagents-learning.org](https://llmagents-learning.org/) | ⭐ Berkeley 最新 LLM Agent 课程，含记忆专题 |
| 动手学深度学习（d2l.ai） | - | 中文 | [zh.d2l.ai](https://zh.d2l.ai/) | Attention 机制与序列建模基础 |

---

## 📝 博客与技术文章

| 文章 | 作者 | 链接 | 亮点 |
|------|------|------|------|
| **LLM Powered Autonomous Agents** | Lilian Weng (OpenAI) | [lilianweng.github.io](https://lilianweng.github.io/posts/2023-06-23-agent/) | ⭐ Agent 系统最全博客，含记忆模块专节，必读 |
| **The Landscape of Emerging AI Agent Memory** | Various | [felo.ai/blog](https://felo.ai/zh-Hant/blog/ai-agent-memory-technology-explained/) | Context Window / RAG / 持久工作区三类记忆技术对比 |
| **A-MEM 论文解读** | 知乎 | [zhuanlan.zhihu.com](https://zhuanlan.zhihu.com/p/1888290059859514793) | A-MEM 主动记忆系统中文详解 |
| **MemGPT 解析** | Various | Medium / 知乎 | MemGPT OS 式分层记忆管理思路讲解 |

---

## 🛠️ 实践代码资源

| 资源 | 链接 | 说明 |
|------|------|------|
| **MemGPT / Letta** | [github.com/cpacker/MemGPT](https://github.com/cpacker/MemGPT) | ⭐ 最成熟的 Agent 记忆框架，生产可用 |
| **A-MEM** | [github.com/WujiangXu/A-mem](https://github.com/WujiangXu/A-mem) | NeurIPS 2025，主动式记忆系统官方实现 |
| **LangChain Memory** | [python.langchain.com/docs/modules/memory](https://python.langchain.com/docs/modules/memory/) | LangChain 内置记忆模块，含多种记忆类型 |
| **LlamaIndex** | [github.com/run-llama/llama_index](https://github.com/run-llama/llama_index) | RAG + 外部记忆的工程框架首选 |
| **Agent Memory Paper List** | [github.com/Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | 最新论文汇总列表，持续更新 |
| **Chroma / Qdrant / Milvus** | 各自官网 | 向量数据库，外部记忆存储首选方案 |

---

## 📅 学习计划（8 周）

### 第一周：概念入门

**目标**：建立 Agent 记忆的全局认知

- [ ] 阅读 Lilian Weng 博客《LLM Powered Autonomous Agents》记忆部分
- [ ] 理解记忆四大类型（In-Context / External / In-Weights / In-Cache）
- [ ] 阅读 ACM 2025 综述摘要（Zhang et al. 2404.13501）
- [ ] 了解现实产品中的记忆设计：ChatGPT Memory、Claude Projects

**检验**：能说出四种记忆类型的适用场景和核心 trade-off

---

### 第二周：Generative Agents 经典架构

**目标**：理解 Agent 记忆的标志性设计

- [ ] 精读 Generative Agents 论文（Park et al. 2023）
- [ ] 理解「记忆流 → 检索 → 反思 → 计划」四层结构
- [ ] 理解记忆检索的三要素权重：相关性 + 近期性 + 重要性
- [ ] 了解 Reflection（反思）机制：如何从细节记忆归纳高层洞察

**核心伪代码**：
```python
# 记忆检索加权
score = α * relevance + β * recency + γ * importance
# 反思触发：重要性累计超过阈值
if sum(recent_importance) > threshold:
    reflections = llm.reflect(recent_memories)
    memory_stream.add(reflections)
```

**检验**：能画出 Generative Agents 的完整记忆架构图

---

### 第三周：MemGPT 与分层记忆管理

**目标**：掌握 OS 类比的分层记忆设计

- [ ] 精读 MemGPT 论文（Packer et al. 2023）
- [ ] 理解「主内存（上下文窗口）+ 外部存储」的 OS 类比
- [ ] 理解 MemGPT 的自主内存管理：决定何时存入/调出
- [ ] 跑通 MemGPT/Letta 的 Quick Start

**检验**：能解释为什么 MemGPT 能支持"无限长"对话

---

### 第四周：Reflexion 与语言强化记忆

**目标**：理解用自然语言反思作为记忆

- [ ] 精读 Reflexion 论文（Shinn et al. NeurIPS 2023）
- [ ] 理解「执行 → 评估 → 语言反思 → 下次尝试」循环
- [ ] 理解 Reflexion 与传统 RL 的区别：无参数更新
- [ ] 对比 Reflexion 与 Generative Agents 反思机制的异同

**检验**：能分析 Reflexion 在哪类任务上有效/失效

---

### 第五周：RAG 与外部检索记忆

**目标**：掌握外部记忆的工程实现

- [ ] 阅读 RAG 原论文（Lewis et al. NeurIPS 2020）
- [ ] 理解稠密检索（DPR）+ 生成的完整流程
- [ ] 了解 Agentic RAG：动态决策何时检索、检索什么
- [ ] 动手：用 LlamaIndex 搭建一个基础 RAG 系统
- [ ] 了解向量数据库选型：Chroma / Qdrant / Milvus

**检验**：能独立搭建一个带外部记忆的简单 Agent

---

### 第六周：A-MEM 与主动记忆进化

**目标**：了解最新主动式记忆设计

- [ ] 精读 A-MEM 论文（Xu et al. NeurIPS 2025）
- [ ] 理解「记忆笔记生成 → 链接构建 → 记忆进化」三阶段
- [ ] 对比 A-MEM 与 MemGPT 的设计差异
- [ ] 跑通 A-MEM 官方代码

**检验**：能分析 A-MEM 相比 MemGPT 解决了哪些问题

---

### 第七周：长上下文与 KV Cache 优化

**目标**：理解底层机制层面的记忆优化

- [ ] 了解 MSA（Memory Sparse Attention）100M Token 超长上下文
- [ ] 了解 RelayCaching：多 Agent KV Cache 跨实例复用
- [ ] 理解 KV Cache 与外部记忆的互补关系
- [ ] 了解流式压缩记忆（LightThinker++ CoT 压缩）

---

### 第八周：总结与项目实践

**目标**：综合应用，构建完整记忆系统

- [ ] 选择一个方向做项目（任选）：
  - 基于 MemGPT/Letta 构建有长期记忆的对话 Agent
  - 用 LangChain + Chroma 实现带反思的 Task Agent
  - 复现 Generative Agents 记忆流架构（小规模）
  - 对比不同记忆方案在长对话任务上的性能
- [ ] 整理学习笔记，输出一篇技术博客
- [ ] 更新此文档，补充学习心得

---

## 💡 学习建议

1. **从 Generative Agents 入手**：这篇论文把记忆系统讲得最清楚，是理解后续工作的基础
2. **理解 trade-off**：每种记忆类型都有代价，核心是理解 latency / capacity / persistence 的平衡
3. **动手跑 MemGPT**：直接跑起来体验远比读论文理解更深
4. **关注检索质量**：外部记忆系统的上限由检索质量决定，重视 embedding 选型
5. **与 meta-learning 类比**：Agent 记忆的「反思机制」本质上是 meta-learning 的一种形式

---

## 🔗 快速参考

| 概念 | 简要说明 |
|------|----------|
| Memory Stream | Generative Agents 中的原始经验流，按时间序存储所有事件 |
| Reflection | 定期从底层记忆归纳高层洞察，提升记忆抽象层次 |
| Retrieval Scoring | 相关性 + 近期性 + 重要性的加权召回 |
| Working Memory | Agent 当前活跃推理使用的短期记忆（对应上下文窗口） |
| Episodic Memory | 具体事件/经历的记录，时序性强 |
| Semantic Memory | 知识、事实、概念的抽象存储，无时序 |
| Procedural Memory | 技能、操作步骤的记忆，类比工具调用模式 |
| Memory Consolidation | 将短期记忆转化为长期记忆的过程（类比睡眠巩固） |
| Forgetting Curve | 遗忘曲线，指导记忆衰减权重设计 |
| KV Cache | Transformer 中键值对的计算缓存，可视为一种 In-Cache 记忆 |

---

*文档由 OpenClaw AI 助手整理生成，持续更新中 🤖*

---

## Agent Memory 补充清单

| 优先级 | 材料 | 方向 | 建议关注点 |
|--------|------|------|------------|
| P0 | MemGPT / Letta | virtual context / memory OS | working memory 与 archival memory 管理 |
| P0 | Generative Agents | episodic / reflective memory | observation、reflection、planning 三层结构 |
| P0 | Reflexion | verbal memory | 失败反思如何影响下一次行动 |
| P1 | Voyager | skill library / lifelong learning | procedural memory 和自动课程 |
| P1 | GraphRAG | graph memory | entity/relation/community summary |
| P1 | MemoryBank | long-term personal memory | 用户长期偏好和情节记忆 |
| P1 | Zep / A-Mem / memory service systems | engineering memory | 生产化记忆服务、检索、TTL、权限 |
| P1 | Multimodal Memory / MIRIX-like systems | multimodal memory | 图像、文本、事件的统一记忆 |

建议统一采用以下分类：

```text
working memory
episodic memory
semantic memory
procedural memory
external retrieval memory
graph memory
multimodal memory
```

评估 memory 不能只看主观体验，至少要记录：recall accuracy、staleness、privacy risk、retrieval latency、memory pollution。
