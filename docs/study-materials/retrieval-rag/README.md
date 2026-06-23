# Retrieval / RAG / Long Context

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Retrieval / RAG / Long Context / Memory Engineering |
| 材料类型 | 路线 / 论文 / 系统 / 实践 |
| 难度 | 入门到进阶 |
| 优先级 | P0 / Hands-on / Frontier |
| 状态 | 推荐 |
| 建议用途 | 系统学习 RAG、检索增强生成、长上下文和 Agent Memory 的工程路线 |

---

## 先看结论

1. RAG 的核心不是“向量库 + prompt”，而是 **query understanding → retrieval → rerank → context construction → generation → citation/evaluation** 的完整系统。
2. Long context 不能完全替代 RAG：RAG 在知识更新、成本控制、引用和权限隔离上仍然有优势。
3. Agent Memory、GraphRAG、Multimodal RAG 是 RAG 的自然延伸，但必须有 evaluation harness，否则很容易只做 demo。
4. 学习顺序建议：DPR / RAG / FiD / ColBERT → RETRO / Atlas → Self-RAG / GraphRAG → RAG eval / Agentic RAG。

---

## 知识地图

```text
Sparse Retrieval / BM25
  → Dense Retrieval / DPR
  → RAG / FiD
  → Late Interaction / ColBERT
  → Retrieval-augmented LM / RETRO / Atlas
  → Reranking / Query Rewriting / HyDE
  → Self-RAG / Corrective RAG
  → GraphRAG / Agentic RAG / Memory RAG
  → RAG Evaluation / Observability
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | DPR | 论文 | dense retrieval 的经典起点 |
| P0 | RAG: Retrieval-Augmented Generation | 论文 | RAG 基本范式来源 |
| P0 | FiD | 论文 | fusion-in-decoder，经典 reader 结构 |
| P0 | ColBERT | 论文 / 系统 | late interaction retrieval 代表 |
| P1 | REALM | 论文 | retrieval-augmented pretraining 早期代表 |
| P1 | RETRO | 论文 | retrieval-enhanced LLM 的代表工作 |
| P1 | Atlas | 论文 | retrieval-augmented few-shot learning |
| P1 | Self-RAG | 论文 | 模型学习何时检索、何时引用、何时反思 |
| P1 | HyDE | 方法 | hypothetical document expansion，实用 query rewriting 思路 |
| P1 | Contriever | 论文 / 代码 | 无监督 dense retrieval 强基线 |
| P1 | BGE / FlagEmbedding | 模型 / 工具 | 中文和多语种 embedding / reranker 实践入口 |
| P1 | RAGAS | 工具 / Eval | RAG faithfulness / answer relevance / context precision 评估 |
| P1 | LlamaIndex / LangChain RAG docs | 官方文档 | 工程 pipeline、chunking、retriever、reranker 实践参考 |
| Frontier | GraphRAG | 系统 / 方法 | 图结构知识组织和全局问题回答代表方向 |

---

## 1. Retrieval 基础

### Sparse Retrieval

- BM25 仍然是强 baseline。
- 优点：简单、可解释、稳定、成本低。
- 缺点：语义匹配能力有限。

### Dense Retrieval

- **DPR**：dual encoder 检索，问题和文档分别编码。
- 学习重点：negative sampling、embedding quality、recall@k。


推荐补充资料：

- Contriever 论文：https://arxiv.org/abs/2112.09118
- Contriever 代码：https://github.com/facebookresearch/contriever
- Sentence-BERT 论文：https://arxiv.org/abs/1908.10084
- BGE / FlagEmbedding：https://github.com/FlagOpen/FlagEmbedding

### Late Interaction

- **ColBERT**：token-level late interaction，兼顾语义和细粒度匹配。
- 适合理解“向量检索不只有单向量 embedding”。

---

## 2. RAG Pipeline

一个可靠 RAG 系统至少包含：

```text
Document parsing
  → chunking
  → embedding / indexing
  → query rewriting
  → retrieval
  → reranking
  → context packing
  → generation with citation
  → evaluation / logging
```

常见失败模式：

- chunk 太粗或太碎；
- top-k recall 不够；
- reranker 缺失；
- context 塞太多导致模型忽略关键证据；
- 没有 citation correctness；
- 没有离线 eval set。

---

## 3. Long Context vs RAG

| 方案 | 优点 | 缺点 | 适合场景 |
|------|------|------|----------|
| Long Context | 实现简单，保留原文顺序 | 成本高，噪声多，更新困难 | 单文档分析、少量长上下文 |
| Naive RAG | 成本低，可更新 | recall 和 chunking 影响大 | FAQ、知识库问答 |
| Rerank RAG | 准确率更高 | 延迟增加 | 高质量企业知识库 |
| GraphRAG | 支持全局关系和聚合问题 | 构建复杂 | 组织知识、研究综述、复杂实体关系 |
| Agentic RAG | 支持多步检索和工具调用 | 不稳定、评估困难 | 长任务、研究助手、代码仓库问答 |

---

## 4. 前沿方向

### Self-RAG / Corrective RAG

重点不是加更多检索，而是让模型判断：

- 是否需要检索；
- 检索结果是否支持答案；
- 答案是否需要修正；
- 何时拒答。

### GraphRAG

适合补充：

- entity / relation extraction；
- community summary；
- global question answering；
- provenance tracking。


推荐补充资料：

- Microsoft GraphRAG：https://github.com/microsoft/graphrag
- GraphRAG 论文：https://arxiv.org/abs/2404.16130
- LightRAG：https://arxiv.org/abs/2410.05779

### Agentic RAG

RAG 与 Agent 结合后，检索成为 tool：

```text
plan → search → read → refine query → search again → synthesize → verify citation
```

### Multimodal RAG

处理 PDF、图片、表格、视频、网页截图。建议和 `../multimodal/README.md` 交叉阅读。

---

## 实践项目 / 完成标准

### Project 1：RAG Evaluation Harness

- 构建 50-100 个 query-answer-citation 样例。
- 对比 BM25、dense retrieval、rerank、HyDE。
- 指标：recall@k、answer correctness、faithfulness、citation correctness、latency、cost。
- 完成标准：能给出一份错误分类报告，而不是只给平均分。

### Project 2：GraphRAG Mini System

- 从一个小型文档集合抽取 entity / relation。
- 构建 graph + community summary。
- 对比 naive RAG 和 GraphRAG 在全局问题上的表现。

### Project 3：Long Context vs RAG

- 同一组文档分别用 long context 和 RAG 回答。
- 比较准确率、延迟、成本、引用质量。

---

## 延伸资料


### 高质量外部引用

| 方向 | 资料 | 类型 | 链接 |
|------|------|------|------|
| RAG 基础 | Retrieval-Augmented Generation | 论文 | https://arxiv.org/abs/2005.11401 |
| Dense Retrieval | DPR | 论文 / 代码 | https://arxiv.org/abs/2004.04906 / https://github.com/facebookresearch/DPR |
| Late Interaction | ColBERT | 论文 / 代码 | https://arxiv.org/abs/2004.12832 / https://github.com/stanford-futuredata/ColBERT |
| Long-context RAG | Lost in the Middle | 论文 | https://arxiv.org/abs/2307.03172 |
| RAG Eval | RAGAS | 文档 / 代码 | https://docs.ragas.io/ / https://github.com/explodinggradients/ragas |
| RAG Framework | LlamaIndex RAG Docs | 官方文档 | https://docs.llamaindex.ai/ |
| RAG Framework | LangChain RAG Docs | 官方文档 | https://python.langchain.com/docs/tutorials/rag/ |


- Agent Memory：`../agent-engineering/agent-memory.md`
- Agent Benchmarks：`../agent-engineering/agent-benchmarks.md`
- Foundation Models：`../foundation-models/README.md`
- Multimodal：`../multimodal/README.md`

### 补充：Corrective RAG / CRAG

- **Corrective RAG / CRAG**：在检索结果不可靠时引入自我评估、纠错和二次检索，适合理解 RAG 从 naive retrieval 走向 self-correcting retrieval pipeline 的方向。

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
