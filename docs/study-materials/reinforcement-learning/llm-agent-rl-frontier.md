# LLM / Agent 相关强化学习前沿论文

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Reinforcement Learning |
| 材料类型 | 前沿 / 论文路线 |
| 难度 | 前沿 |
| 优先级 | P0 / Frontier |
| 状态 | 需更新 |
| 建议用途 | 跟进 LLM reasoning、RLVR 与 Agent RL |

---

> 目标：在已掌握 Sutton 强化学习与基础 Deep RL 的前提下，理解当前最热的 LLM reasoning、RLHF/RLVR、Agent 训练、工具使用和自改进方向。  
> 更新时间：2026-05-24  
> 选择原则：优先收录影响力大、范式代表性强、能连接经典 RL 与 LLM/Agent 前沿的论文。

> 专题拆分：本文作为总览页；偏好优化见 [Preference Optimization](preference-optimization.md)，推理强化学习见 [Reasoning RL](reasoning-rl.md)，Agent 训练见 [Agentic RL](agentic-rl.md)。

---

## 先看结论

LLM / Agent 时代的 RL，已经不只是“在环境里最大化 reward”的经典形式，而分化成几条主线：

1. **RLHF / Preference Optimization**：用人类偏好或 AI 偏好训练 reward / preference signal，让模型更符合指令和人类期望。
2. **RLVR / Reasoning RL**：用可验证奖励训练数学、代码、逻辑推理能力；DeepSeek-R1 之后成为最热方向之一。
3. **Agentic RL**：把工具调用、网页操作、代码执行、多步规划作为轨迹，用成功/失败反馈训练 agent。
4. **Self-improvement / Synthetic Data**：模型自己生成任务、解法、反思、偏好数据，再用于训练或筛选。
5. **Inference-time Search + RL**：训练时学策略，推理时结合 verifier、tree search、self-consistency、tool feedback。

如果只想抓主线：

```text
Human Preferences → InstructGPT → DPO/KTO
        ↓
DeepSeekMath / DeepSeek-R1 → RLVR / GRPO / reasoning RL
        ↓
ReAct / Toolformer / WebGPT / Agent Q / WebRL → Agentic RL
        ↓
Self-Refine / Reflexion / STaR → Self-improvement
```

---

## 1. RLHF 与偏好优化：LLM 对齐的主线

### 1.1 Deep Reinforcement Learning from Human Preferences

- **论文**：[Deep reinforcement learning from human preferences](https://arxiv.org/abs/1706.03741)
- **作者**：Christiano et al., 2017
- **为什么重要**：RLHF 的早期源头之一。核心思想是不用手写 reward，而是让人类比较轨迹片段，由偏好训练 reward model，再用 RL 优化策略。
- **要读什么**：
  - preference comparison 如何转成 reward model；
  - 为什么这比人工设计 reward 更适合复杂行为；
  - reward model 误差如何导致 reward hacking。

### 1.2 A General Language Assistant as a Laboratory for Alignment

- **论文**：[A General Language Assistant as a Laboratory for Alignment](https://arxiv.org/abs/2112.00861)
- **作者**：Askell et al., 2021
- **为什么重要**：Anthropic 早期 alignment / helpful-harmless-honest 路线代表，展示语言助手如何作为对齐实验平台。
- **要读什么**：
  - helpfulness / harmlessness / honesty 的任务化方式；
  - preference model 和 rejection sampling 的作用；
  - 对齐评估为什么不能只看单一 reward。

### 1.3 InstructGPT

- **论文**：[Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- **作者**：Ouyang et al., 2022
- **为什么重要**：ChatGPT 技术路线的关键论文之一，把 **SFT → Reward Model → PPO** 流程系统化。
- **要读什么**：
  - instruction tuning 与 RLHF 的分工；
  - PPO 在语言模型上的 objective 形式；
  - KL penalty 为什么重要；
  - 小模型经过 RLHF 后为什么能比大模型更符合人类偏好。

### 1.4 Direct Preference Optimization (DPO)

- **论文**：[Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- **作者**：Rafailov et al., 2023
- **为什么重要**：把 RLHF 中的 reward model + PPO 简化成直接偏好优化，成为后续 LLM alignment 的强 baseline。
- **要读什么**：
  - DPO 如何从 KL-constrained reward maximization 推导出来；
  - 为什么可以绕过显式 reward model；
  - DPO 与行为克隆、pairwise ranking、implicit reward 的关系。

### 1.5 KTO

- **论文**：[KTO: Model Alignment as Prospect Theoretic Optimization](https://arxiv.org/abs/2402.01306)
- **作者**：Ethayarajh et al., 2024
- **为什么重要**：代表一类“非成对偏好”的 alignment 方法，用人类“好/坏”反馈即可训练。
- **要读什么**：
  - prospect theory 如何进入 preference optimization；
  - KTO 与 DPO/IPO/ORPO 的关系；
  - 数据格式从 pairwise preference 变成 binary feedback 后的优势与风险。

---

## 2. RLVR / Reasoning RL：当前最热方向

RLVR = Reinforcement Learning with Verifiable Rewards。核心想法：数学、代码、逻辑题有明确对错，可以不用复杂 reward model，而直接用 verifier 给 reward。

### 2.1 DeepSeekMath

- **论文**：[DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
- **作者**：DeepSeek-AI, 2024
- **为什么重要**：系统展示数学数据、SFT、RL 对开源数学推理模型的提升；其中 GRPO 思路为后续 R1 铺路。
- **要读什么**：
  - 数学语料构造与过滤；
  - GRPO 相比 PPO 的差异；
  - rule-based reward / verifier 在数学推理中的作用。

### 2.2 DeepSeek-R1

- **论文**：[DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
- **作者**：DeepSeek-AI, 2025
- **为什么重要**：让“纯 RL 激发推理能力”成为主流议题。R1-Zero 展示无需 SFT 也能通过 RL 形成长链推理行为，R1 则结合冷启动数据和多阶段训练提高可读性与稳定性。
- **要读什么**：
  - R1-Zero 与 R1 的训练流程差异；
  - GRPO 如何减少 value model 需求；
  - 可验证 reward 如何驱动 self-reflection、长 CoT、test-time compute；
  - 语言混杂、重复、可读性差等 RL 副作用。

### 2.3 STaR

- **论文**：[STaR: Bootstrapping Reasoning With Reasoning](https://arxiv.org/abs/2203.14465)
- **作者**：Zelikman et al., 2022
- **为什么重要**：虽然不是标准 RL，但它是 self-improvement / reasoning bootstrapping 的重要前驱：模型生成 rationale，用正确答案筛选，再迭代训练。
- **要读什么**：
  - rationales 如何自举；
  - 正确性筛选如何形成弱 verifier；
  - 与 RLVR 的联系：都依赖“可验证结果”推动推理改进。

---

## 3. Agentic RL：工具、网页、代码与多步任务

### 3.1 WebGPT

- **论文**：[WebGPT: Browser-assisted question-answering with human feedback](https://arxiv.org/abs/2112.09332)
- **为什么重要**：把网页浏览、引用、答案生成结合到 RLHF 框架，是 LLM agent + human feedback 的早期代表。
- **要读什么**：
  - 浏览器动作如何构成 agent trajectory；
  - evidence / citation 如何影响 reward；
  - 人类偏好如何评价多步工具使用。

### 3.2 ReAct

- **论文**：[ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- **作者**：Yao et al., 2022
- **为什么重要**：Reasoning + Acting 的代表范式，奠定了很多 agent prompt / tool-use 工作流。
- **要读什么**：
  - thought-action-observation loop；
  - 推理轨迹如何帮助工具选择；
  - ReAct 与 RL 中 partially observable control 的关系。

### 3.3 Toolformer

- **论文**：[Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)
- **作者**：Schick et al., 2023
- **为什么重要**：代表 self-supervised tool use：模型自己标注何时调用工具，并学习 API 调用。
- **要读什么**：
  - 工具调用数据如何自动构造；
  - API calling 与 policy learning 的关系；
  - 工具增强是否一定需要 RL，还是可以先靠筛选式监督学习。

### 3.4 Tree of Thoughts

- **论文**：[Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601)
- **作者**：Yao et al., 2023
- **为什么重要**：代表 inference-time search。虽然不是训练时 RL，但它把 value / search / planning 的经典 RL 思想引入 LLM 推理。
- **要读什么**：
  - thought state、proposal、evaluation、search；
  - BFS/DFS/MCTS 式搜索与 RL planning 的关系；
  - verifier/value model 在推理时的角色。

### 3.5 Reflexion

- **论文**：[Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366)
- **为什么重要**：提出 verbal reinforcement：不更新模型参数，而把失败经验写成语言记忆，下一轮改进。
- **要读什么**：
  - verbal feedback 与传统 scalar reward 的差异；
  - episodic memory 如何影响后续策略；
  - 为什么这更像 inference-time RL / memory-based policy improvement。

### 3.6 Agent Q / WebRL 类工作

- **Agent Q**：[Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents](https://arxiv.org/abs/2408.07199)
- **WebRL**：[WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://arxiv.org/abs/2411.02337)
- **为什么重要**：代表网页/任务型 Agent 开始使用在线 RL、自演化课程、失败轨迹再利用。
- **要读什么**：
  - 网页任务如何定义 state/action/reward；
  - self-evolving curriculum 如何从失败中产生新任务；
  - online RL 与离线轨迹训练如何结合。

---

## 4. Retrieval / Memory / Self-Improvement 与 RL 的交叉

### 4.1 Self-RAG

- **论文**：[Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/abs/2310.11511)
- **为什么重要**：模型学习何时检索、如何生成、如何自我批判。它不是经典 RL，但体现了“策略控制信息获取”的思想。
- **要读什么**：
  - retrieve / generate / critique 三类动作；
  - reflection token 如何像控制信号；
  - 与 agent memory、retrieval policy learning 的关系。

### 4.2 Generative Agents

- **论文**：[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)
- **为什么重要**：长期记忆、反思、规划构成 agent 行为生成循环。虽非 RL paper，但对 agent memory + planning 很有启发。
- **要读什么**：
  - memory stream、reflection、planning；
  - agent 行为如何由记忆和当前观察共同决定；
  - 与 RL 中 state abstraction / belief state 的连接。

### 4.3 Synthetic Data / Persona Scaling

- **论文**：[Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://arxiv.org/abs/2406.20094)
- **为什么重要**：代表用大规模合成 persona 生成训练数据的方向，可与 preference learning、self-play、agent curriculum 结合。
- **要读什么**：
  - synthetic data 如何覆盖多样任务；
  - 数据质量控制如何替代部分 reward 设计；
  - 与 self-play / curriculum RL 的联系。

---

## 5. 影响力最大的一组论文：建议优先读

如果时间有限，建议按这个顺序读：

1. [Deep RL from Human Preferences](https://arxiv.org/abs/1706.03741)
2. [InstructGPT](https://arxiv.org/abs/2203.02155)
3. [DPO](https://arxiv.org/abs/2305.18290)
4. [DeepSeekMath](https://arxiv.org/abs/2402.03300)
5. [DeepSeek-R1](https://arxiv.org/abs/2501.12948)
6. [ReAct](https://arxiv.org/abs/2210.03629)
7. [Toolformer](https://arxiv.org/abs/2302.04761)
8. [Tree of Thoughts](https://arxiv.org/abs/2305.10601)
9. [Reflexion](https://arxiv.org/abs/2303.11366)
10. [WebGPT](https://arxiv.org/abs/2112.09332)

这 10 篇基本覆盖：

- 人类偏好 → RLHF；
- 偏好优化 → DPO/KTO；
- 可验证奖励 → RLVR/GRPO；
- 工具使用 → Agentic workflow；
- 推理时搜索 → Planning / verifier；
- 自我改进 → reflection / curriculum。

---

## 6. 和经典 RL 的对应关系

| LLM / Agent 前沿概念 | 经典 RL 对应概念 | 关键差异 |
|---|---|---|
| Prompt / context | state / observation | 状态是语言化、可编辑、可压缩的 |
| Tool call | action | 动作空间结构化且可组合 |
| Verifier / unit test / math answer | reward function | 很多任务奖励稀疏但可靠 |
| Preference model | learned reward | reward 来自人类/AI 比较，而非环境天然给出 |
| Chain-of-thought | latent trajectory / plan | 可读但不一定忠实 |
| Self-reflection memory | value update / policy improvement | 不改参数也能改善下一轮行为 |
| Tree search / best-of-N | planning / policy improvement | 发生在 inference time |
| KL penalty | trust region / regularization | 约束策略不要偏离 base model 太远 |

---

## 7. 进阶研究问题

- **RLVR 是否真的需要 RL？** 对数学/代码任务，rejection sampling + SFT、DPO、GRPO、PPO 的边界在哪里？
- **Verifier 会不会导致 reward hacking？** 单测、数学答案、格式检查是否会诱导模型钻空子？
- **CoT 是策略还是解释？** 训练长 CoT 是否真的提升推理，还是只是改变输出风格？
- **Agent reward 如何设计？** 多步工具任务里，成功/失败、成本、时间、风险、引用质量如何共同进入 reward？
- **Memory 是否应参与训练？** 经验可以进参数、进检索库、进 prompt，三者如何取舍？
- **Inference-time compute 与 training-time RL 如何配合？** Best-of-N、MCTS、verifier-guided search 与 RL policy 谁更重要？

---

## 8. 推荐实践路线

1. **复现 DPO**：用一个小 preference dataset 跑通 SFT → DPO，对比 reward margin。
2. **做一个 RLVR toy task**：例如 GSM8K 子集或代码单测任务，用 rule-based verifier 给 reward。
3. **实现 ReAct agent**：让模型在 HotpotQA / WebShop / MiniWoB 风格任务中执行 thought-action-observation。
4. **加入 verifier reranking**：比较 greedy、best-of-N、self-consistency、verifier rerank。
5. **记录失败轨迹**：把失败分为 reward 设计错、工具调用错、状态压缩错、搜索不够、模型能力不够。

---

## 9. 与本目录其它文档的关系

- 主线基础：[强化学习进阶学习资料与论文路线](advanced-rl.md)
- Agent 工程视角：[Harness Engineering](../agent-engineering/harness-engineering.md)
- Agent 记忆视角：[Agent Memory](../agent-engineering/agent-memory.md)

建议学习顺序：

```text
advanced-rl.md
  → 本文档：llm-agent-rl-frontier.md
  → harness-engineering.md
  → agent-memory.md
```
