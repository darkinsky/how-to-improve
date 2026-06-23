# Foundation Models / LLM Fundamentals

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Foundation Models / LLM |
| 材料类型 | 路线 / 论文 / 系统 / 实践 |
| 难度 | 入门到前沿 |
| 优先级 | P0 / Classic / Frontier |
| 状态 | 推荐 |
| 建议用途 | 补齐 Transformer、Scaling Laws、预训练、微调、MoE、长上下文和推理时计算的共同底座 |

---

## 先看结论

1. LLM 主线不是从 Agent 或 RL 开始，而是从 **Transformer → GPT → Scaling Laws → Instruction Tuning / RLHF → Long Context / MoE / Inference-time Compute** 演化而来。
2. 如果后续要学 AI Infra、Agentic RL、RAG、VLM，至少要理解 Transformer decoder、KV cache、tokenization、pretraining objective、post-training 和 scaling law。
3. 经典材料优先看 Transformer、GPT-3、Scaling Laws、Chinchilla、LLaMA、LoRA/QLoRA；前沿材料重点跟 MoE、长上下文、推理时搜索、Transformer alternatives。
4. 这篇文档是 Agent Engineering、RL、RAG、Multimodal 和 AI Infra 的前置入口。

---

## 知识地图

```text
Transformer 基础
  → Decoder-only LM / GPT 系列
  → Scaling Laws / Data-Centric Pretraining
  → Instruction Tuning / Alignment / Preference Optimization
  → PEFT / LoRA / QLoRA
  → Long Context / Position Encoding
  → MoE / Sparse Models
  → Inference-time Compute / Search / Verifier
  → Transformer Alternatives / Hybrid Models
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | Attention Is All You Need | 论文 | Transformer 架构起点，理解 self-attention、multi-head attention、position encoding |
| P0 | GPT-2 / GPT-3 | 论文 | decoder-only language model 和 in-context learning 主线 |
| P0 | Scaling Laws for Neural Language Models | 论文 | Kaplan scaling laws，理解模型规模、数据、计算的关系 |
| P0 | Training Compute-Optimal Large Language Models / Chinchilla | 论文 | data/model compute optimality，对现代预训练配比影响很大 |
| P0 | LLaMA / LLaMA 2 / LLaMA 3 Technical Reports | 技术报告 | 开源 LLM 生态的重要基线 |
| P0 | RoPE | 论文 / 技术 | 主流位置编码方案，理解长上下文扩展的基础 |
| P0 | LoRA | 论文 | 参数高效微调的事实标准之一 |
| P1 | QLoRA | 论文 | 量化 + PEFT，低成本微调核心方法 |
| P1 | Switch Transformer / GShard | 论文 | MoE / sparse expert 模型经典路线 |
| P1 | Constitutional AI / InstructGPT | 论文 | alignment、RLHF、RLAIF 和 instruction following 的关键材料 |
| P1 | The Illustrated Transformer / The Annotated Transformer | 经典教程 | 适合把论文结构落实到代码和图解 |
| P1 | The Hardware Lottery / Bitter Lesson | 经典文章 | 理解为什么 scaling、硬件和通用方法反复胜出 |

---

## 经典主线

### 1. Transformer 与 GPT

- **Attention Is All You Need**：理解 query/key/value、scaled dot-product attention、multi-head attention、residual、layer norm。
- **GPT / GPT-2 / GPT-3**：理解 decoder-only LM、next-token prediction、prompting、in-context learning。
- **BERT / T5**：不是当前 LLM agent 的主线架构，但有助于理解 encoder、masked LM、text-to-text 范式。

高质量补充：

- The Illustrated Transformer：https://jalammar.github.io/illustrated-transformer/
- The Annotated Transformer：http://nlp.seas.harvard.edu/annotated-transformer/
- nanoGPT：https://github.com/karpathy/nanoGPT
- Andrej Karpathy - Neural Networks: Zero to Hero：https://github.com/karpathy/nn-zero-to-hero

### 2. Scaling Laws

- **Kaplan Scaling Laws**：早期 scaling law，提出 loss 与模型、数据、计算的幂律关系。
- **Chinchilla**：强调 compute-optimal 训练中数据量更重要，影响后续 LLM 训练配比。
- **Data quality / dedup / contamination**：现代训练中数据治理和 benchmark 污染和 scaling 同样重要。

高质量补充：

- The Bitter Lesson：http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- The Hardware Lottery：https://arxiv.org/abs/2009.06489
- Scaling Laws for Neural Language Models：https://arxiv.org/abs/2001.08361
- Training Compute-Optimal Large Language Models：https://arxiv.org/abs/2203.15556

### 3. Post-training 与 Alignment

- **Instruction Tuning**：从预训练 LM 到可用 assistant 的关键阶段。
- **InstructGPT**：SFT + reward model + PPO RLHF 的经典 pipeline。
- **Constitutional AI**：RLAIF 和可解释原则约束的重要路线。
- 后续细节见：`../reinforcement-learning/preference-optimization.md`、`../reinforcement-learning/reasoning-rl.md`。

### 4. PEFT 与模型适配

- **LoRA**：低秩适配，理解 adapter 参数化。
- **QLoRA**：4-bit quantization + LoRA，低成本微调。
- **DoRA / LoRA variants**：作为 P2/Frontier 跟进即可，不必初学时展开。

### 5. Long Context

- **RoPE**：主流位置编码基础。
- **ALiBi**：另一类相对位置偏置思路。
- **LongRoPE / YaRN / NTK-aware scaling**：长上下文扩展常见技术。
- **RAG vs Long Context**：长上下文不是 RAG 的简单替代；RAG 仍然在可更新知识、可引用、成本控制上有优势。

### 6. MoE 与 Sparse Models

- **GShard / Switch Transformer**：MoE 训练和 routing 的基础。
- **Mixtral / DeepSeek-V3**：现代开源/技术报告中的 MoE 代表。
- 学习重点：expert routing、load balancing、expert parallelism、通信瓶颈。

### 7. Transformer Alternatives

这些不一定取代 Transformer，但值得了解其问题意识：降低长序列复杂度、提升状态建模能力。

- **Mamba**：state space model 路线代表。
- **RWKV**：RNN-like LM 代表。
- **RetNet**：retention mechanism。
- **Hyena**：implicit long convolution。
- **Jamba**：Transformer + SSM hybrid。

---

## 学习路线

### 4 周压缩路线

1. Week 1：Transformer + GPT-2/GPT-3。
2. Week 2：Scaling Laws + Chinchilla + LLaMA。
3. Week 3：Instruction tuning + InstructGPT + LoRA/QLoRA。
4. Week 4：RoPE/long context + MoE + tiny GPT 实验。

### 8 周系统路线

1. Transformer 结构与代码实现。
2. GPT pretraining objective 与 tokenization。
3. Scaling law 与数据治理。
4. Post-training：SFT / RLHF / DPO 概览。
5. PEFT：LoRA / QLoRA。
6. Long context：RoPE、ALiBi、YaRN。
7. MoE：Switch、GShard、Mixtral、DeepSeek-V3。
8. Inference-time compute：self-consistency、verifier、tree search。

---

## 实践项目 / 完成标准

### Project 1：Train a Tiny GPT

- 实现或复用 nanoGPT 风格训练脚本。
- 在小语料上训练 decoder-only LM。
- 记录 loss curve、context length、batch size、tokens/sec。
- 完成标准：能解释 embedding、attention、MLP、residual、KV cache 的作用。

### Project 2：LoRA / QLoRA 微调实验

- 选择一个小模型和一个 instruction dataset。
- 对比 full fine-tuning、LoRA、QLoRA 的显存和效果。
- 完成标准：能解释 rank、alpha、target modules、quantization 对结果的影响。

### Project 3：Long Context / RAG 对比

- 准备一组长文档问答任务。
- 对比直接 long context、chunked RAG、rerank RAG。
- 完成标准：能说清楚准确率、引用、成本、延迟的 trade-off。

---

## 延伸资料

- AI Infra 推理系统：`../ai-infra/04-llm-inference.md`
- Preference Optimization：`../reinforcement-learning/preference-optimization.md`
- Reasoning RL：`../reinforcement-learning/reasoning-rl.md`
- Agent Engineering：`../agent-engineering/README.md`
- RAG / Long Context：`../retrieval-rag/README.md`

### 补充：早期 GPT 与模型家族脉络

- **GPT-1**：decoder-only + unsupervised pretraining + supervised fine-tuning 的早期代表，用于理解 GPT 系列如何从迁移学习范式走向 GPT-2/GPT-3 的 scaling 路线。

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
