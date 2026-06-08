# How to Improve

一个面向 **AI、CS、工程实践与科研能力提升** 的个人知识库。

这个仓库用于沉淀可公开分享的学习资料、研究路线、工程实践和复盘模板。目标不是收藏尽可能多的链接，而是把重要材料组织成可以持续迭代的学习路径：知道 **先学什么、为什么学、学到什么程度、下一步做什么**。

---

## 核心内容

| 方向 | 内容 | 入口 |
|------|------|------|
| CS 基础 | 计算机公开课、数据结构、算法、系统、数据库、分布式、AI 课程 | [CS 公开课资源](docs/study-materials/computer-science/README.md) |
| AI Infra / LLM Systems | GPU 体系结构、CUDA、分布式训练、LLM 推理、网络存储、调度编排 | [AI Infra 入门资料](docs/study-materials/ai-infra/README.md) |
| 生成模型 | VAE、GAN、Flow、Diffusion、Flow Matching、图像/视频生成 | [Generative Models](docs/study-materials/generative-models/README.md) |
| 强化学习 / LLM RL | Deep RL、RLHF、DPO、RLVR、Reasoning RL、Agentic RL | [Reinforcement Learning](docs/study-materials/reinforcement-learning/README.md) |
| Agent Engineering | Agent Memory、Harness Engineering、Agent 运行时、工具与评估 | [Agent Engineering](docs/study-materials/agent-engineering/README.md) |
| 工程与科研方法 | 工程实践、科研方法、复盘模板 | [docs](docs/) |

---

## 推荐学习路线

如果只想按目标选择路线，优先看：[Study Materials Learning Paths](docs/study-materials/learning-paths.md)。

### 1. AI Infra / LLM Systems 路线

适合目标：大模型训练系统、推理系统、AI Infra、CUDA / GPU 性能优化。

```text
CSAPP / 计算机系统基础
  → GPU 体系结构
  → CUDA / Triton / TileLang / FlashAttention
  → 分布式训练：DDP / FSDP / ZeRO / Megatron
  → LLM 推理系统：vLLM / SGLang / TensorRT-LLM
  → 网络、存储、调度：NCCL / RDMA / Ray / K8s / Slurm
```

入口：[AI Infra 入门资料整理](docs/study-materials/ai-infra/README.md)

### 2. LLM / Agent 路线

适合目标：LLM Agent、工具调用、Agent 记忆、Harness Engineering、Agent 评估。

```text
LLM / Transformer 基础
  → RLHF / DPO / RLVR
  → ReAct / Toolformer / WebGPT / Agentic RL
  → Agent Memory
  → Harness Engineering
  → Agent Benchmark 与轨迹级评估
```

入口：[Agent Engineering](docs/study-materials/agent-engineering/README.md)

### 3. 生成模型路线

适合目标：图像生成、视频生成、Diffusion / Flow Matching、生成模型研究。

```text
AutoEncoder / VAE
  → GAN / Flow-based Models
  → Diffusion / Score-based Models
  → Flow Matching / Rectified Flow
  → DiT / Image & Video Generation
```

入口：[Generative Models](docs/study-materials/generative-models/README.md)

### 4. CS 基础路线

适合目标：系统补齐计算机基础，建立长期技术底座。

```text
CS61A / CS50x
  → CS61B
  → MIT 6.006
  → CSAPP
  → MIT 6.S081 / Berkeley CS162
  → CMU 15-445
  → MIT 6.5840
```

入口：[CS 公开课资源整理](docs/study-materials/computer-science/README.md)

---

## 目录结构

```text
.
├── docs/
│   ├── engineering/        # 工程实践、效率工具、代码质量、架构思考
│   ├── research/           # 科研方法、论文阅读、实验设计、写作积累
│   ├── notes/              # 日常笔记与复盘模板
│   ├── roadmap.md          # 仓库建设路线图
│   └── study-materials/    # AI / CS 学习资料与研究路线
│       ├── content-standard.md
│       ├── maintenance-guide.md
│       ├── learning-paths.md
│       ├── ai-infra/
│       ├── agent-engineering/
│       ├── computer-science/
│       ├── generative-models/
│       ├── learning-systems/
│       └── reinforcement-learning/
├── .editorconfig
├── .gitignore
├── scripts/
│   └── check_markdown_links.py
└── README.md
```

---

## 维护原则

1. **优先收录一手资料**：课程官网、论文、官方博客、官方代码仓库优先。
2. **少而精**：每个方向优先整理最重要材料，而不是无限堆链接。
3. **说明为什么重要**：材料不只给链接，也要解释它解决什么问题、适合什么时候读。
4. **区分经典与前沿**：经典材料用于打基础，前沿材料用于跟进研究和工程趋势。
5. **尽量可执行**：学习路线应包含实践项目、完成标准或下一步行动。
6. **只收公开资料**：不包含公司内网链接、内部文档、聊天记录或私人内容。
7. **统一内容标准**：学习资料新增或大改时，参考 [`docs/study-materials/content-standard.md`](docs/study-materials/content-standard.md)，标注难度、优先级和状态。
8. **维护机制显式化**：定期按 [`docs/study-materials/maintenance-guide.md`](docs/study-materials/maintenance-guide.md) 做链接检查、前沿材料筛选、索引同步和过时内容清理。Markdown 质量检查可运行 `python scripts/check_markdown_links.py`。

---

## 核心循环

这个仓库仍然服务于“持续改进”的目标：

1. **Observe / 观察**：发现问题、瓶颈或可提升点。
2. **Measure / 度量**：明确现状，用事实和数据描述问题。
3. **Hypothesize / 假设**：提出一个可验证的改进假设。
4. **Act / 行动**：做一个足够小、能快速验证的实验。
5. **Reflect / 复盘**：记录结果，保留有效做法，淘汰无效做法。
6. **Iterate / 迭代**：把经验沉淀为流程、模板或原则。

可以从 [`docs/notes/improvement-note-template.md`](docs/notes/improvement-note-template.md) 开始记录实践。

---

## License

暂未指定许可证。公开发布或接受贡献前，建议补充合适的开源许可证。
