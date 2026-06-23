# Top Materials Deep Reading Guide

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 深度阅读指南 |
| 难度 | 入门到前沿 |
| 优先级 | P0 / Classic / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 将各方向 Top 材料从“知道名字”升级为“知道怎么读、读完掌握什么、如何验证” |

---

## 先看结论

这份指南为每个大方向挑选 Top 5 材料，补充：

- 为什么读；
- 怎么读；
- 读完应该掌握什么；
- 常见误区；
- 建议实践。

详细材料归属见：[Material Index](material-index.md)，实践项目见：[Project Cards](project-cards.md)。

---

## Foundation Models Top 5

### 1. Attention Is All You Need

- **为什么读**：理解 Transformer 的结构起点。
- **怎么读**：重点看 scaled dot-product attention、multi-head attention、position encoding、residual、layer norm。
- **完成标准**：能手写 Q/K/V attention 公式，解释 O(n²) 复杂度和并行训练优势。
- **常见误区**：只记住架构图，不理解 attention 的矩阵形状和 mask。
- **实践**：在 tiny GPT 中实现 causal self-attention。

### 2. GPT-3

- **为什么读**：理解 decoder-only LM、in-context learning 和 scaling 的关系。
- **怎么读**：关注 prompt examples、few-shot evaluation、模型规模和数据规模。
- **完成标准**：能解释 zero-shot、one-shot、few-shot 的差异。
- **常见误区**：把 in-context learning 等同于真正参数更新。
- **实践**：用小模型做 prompt sensitivity test。

### 3. Scaling Laws / Chinchilla

- **为什么读**：理解 compute、data、model size 的配比。
- **怎么读**：对比 Kaplan 和 Chinchilla 的结论差异。
- **完成标准**：能说明为什么更多数据可能比更大模型更重要。
- **常见误区**：把 scaling law 当成无条件线性外推。
- **实践**：训练不同数据量 / 模型大小的 tiny LM，观察 loss。

### 4. LLaMA

- **为什么读**：理解现代开源 LLM 的基线设计。
- **怎么读**：关注数据、tokenizer、RoPE、pre-normalization、SwiGLU、训练细节。
- **完成标准**：能说明 LLaMA 与 GPT-3/BERT 的架构和训练差异。
- **常见误区**：只关注参数量，不关注数据和训练 recipe。
- **实践**：阅读一个 LLaMA-like 模型配置文件。

### 5. LoRA / QLoRA

- **为什么读**：理解低成本模型适配。
- **怎么读**：关注 low-rank update、target modules、rank、alpha、quantization。
- **完成标准**：能解释为什么 LoRA 能减少可训练参数。
- **常见误区**：不做数据审计，只比较微调后样例。
- **实践**：完成 Project Card 中的 LoRA / QLoRA Fine-tuning。

---

## RAG / Retrieval Top 5

### 1. DPR

- **为什么读**：dense retrieval 的基础。
- **怎么读**：关注 dual encoder、negative sampling、recall@k。
- **完成标准**：能解释 BM25 和 dense retrieval 的优缺点。
- **实践**：对同一 query 比较 BM25 和 embedding top-k。

### 2. RAG

- **为什么读**：检索增强生成的基本框架。
- **怎么读**：关注 retrieval、context construction、generation 的耦合。
- **完成标准**：能画出 RAG pipeline，并指出每步失败模式。
- **实践**：构建最小 RAG QA 系统。

### 3. ColBERT

- **为什么读**：理解 late interaction 的细粒度匹配。
- **怎么读**：关注 token-level interaction 和单向量 embedding 的差异。
- **完成标准**：能解释为什么 ColBERT 在召回质量上有优势。
- **实践**：比较 single-vector retrieval 和 rerank/late interaction。

### 4. Self-RAG / CRAG

- **为什么读**：RAG 从“检索更多”走向“判断是否需要检索和纠错”。
- **怎么读**：关注 retrieval decision、critique、rewrite、verification。
- **完成标准**：能设计一个 self-correction RAG loop。
- **实践**：加入检索结果可信度判断。

### 5. GraphRAG

- **为什么读**：处理全局问题、实体关系和组织知识。
- **怎么读**：关注 entity extraction、community summary、global QA。
- **完成标准**：能说清 GraphRAG 和 naive RAG 的适用场景。
- **实践**：做 Project Card 中的 GraphRAG mini system。

---

## AI Infra Top 5

### 1. FlashAttention

- **为什么读**：理解 attention 的 IO 瓶颈和 kernel 优化。
- **完成标准**：能解释 tiling、HBM access、online softmax。
- **实践**：对比 naive attention 和 FlashAttention 的显存/速度。

### 2. Megatron-LM

- **为什么读**：tensor parallelism 的经典实现。
- **完成标准**：能解释 MLP 和 attention 的列/行并行切分。
- **实践**：画出一次 forward/backward 的通信模式。

### 3. ZeRO / DeepSpeed

- **为什么读**：理解 optimizer/gradient/parameter sharding。
- **完成标准**：能比较 ZeRO stage 1/2/3 的显存和通信 trade-off。
- **实践**：估算 7B/70B 模型训练显存。

### 4. vLLM / PagedAttention

- **为什么读**：理解 serving 中 KV cache 管理。
- **完成标准**：能解释 paged KV cache 如何降低碎片。
- **实践**：跑 vLLM benchmark，记录 TTFT/TPOT/throughput。

### 5. DistServe / Mooncake

- **为什么读**：理解 prefill/decode disaggregation 和 KV cache-centric serving。
- **完成标准**：能说明 P/D 分离适合什么 workload。
- **实践**：设计一个 P/D 分离 serving 架构图。

---

## Agent / Code Agent Top 5

### 1. ReAct

- **为什么读**：reasoning + acting 的基本范式。
- **完成标准**：能区分 thought、action、observation。
- **实践**：实现一个最小 ReAct tool-use agent。

### 2. Generative Agents

- **为什么读**：理解 observation、reflection、planning 的 memory architecture。
- **完成标准**：能画出 episodic/semantic/procedural memory 的关系。
- **实践**：给 agent 增加 reflection memory。

### 3. SWE-bench

- **为什么读**：repo-level coding agent 的核心 benchmark。
- **完成标准**：能解释 resolved rate、test patch、环境复现问题。
- **实践**：设计 10 个 toy issue 作为 regression suite。

### 4. SWE-agent / OpenHands

- **为什么读**：理解真实 coding agent runtime。
- **完成标准**：能描述 issue parsing、context search、edit、test、repair loop。
- **实践**：完成 Mini SWE Agent project。

### 5. MCP / LangGraph

- **为什么读**：理解 tool/context protocol 和 stateful workflow。
- **完成标准**：能比较自由 agent loop 和显式 workflow graph。
- **实践**：用同一任务分别实现 raw tool calling 与 graph workflow。

---

## RL / Reasoning Top 5

### 1. PPO / TRPO

- **为什么读**：现代 RLHF 和 policy optimization 的基础。
- **完成标准**：能解释 policy gradient、KL constraint、clip objective。
- **实践**：阅读 PPO 伪代码并标出 advantage、ratio、clip。

### 2. AlphaZero / MuZero

- **为什么读**：search + learned policy/value/world model 的经典路线。
- **完成标准**：能解释 MCTS、self-play、learned dynamics 的关系。
- **实践**：在 toy game 上实现简化 MCTS。

### 3. DPO

- **为什么读**：preference optimization 的入门核心。
- **完成标准**：能解释 chosen/rejected、reference model、implicit reward。
- **实践**：完成 Tiny DPO。

### 4. RLVR / PRM

- **为什么读**：理解 reasoning RL、verifier 和过程奖励。
- **完成标准**：能区分 ORM、PRM、environment reward。
- **实践**：完成 Tiny RLVR / Verifier Loop。

### 5. Tree of Thoughts / ReST / STaR

- **为什么读**：理解 inference-time search 和 self-training。
- **完成标准**：能设计 sampling → verify → filter → train loop。
- **实践**：用数学题做 rejection sampling。

---

## Generative / Multimodal Top 5

### 1. DDPM / DDIM / Score SDE

- **为什么读**：理解 diffusion 的基本训练和采样。
- **完成标准**：能解释 forward noising、reverse denoising、ODE/SDE。
- **实践**：实现 toy DDPM sampler。

### 2. Latent Diffusion / Stable Diffusion

- **为什么读**：现代 T2I 生态基础。
- **完成标准**：能解释 VAE latent、UNet、text encoder、CFG。
- **实践**：对比 latent diffusion 和 pixel diffusion 的成本。

### 3. Flow Matching / Rectified Flow

- **为什么读**：理解 diffusion 之外的现代生成主线。
- **完成标准**：能解释 vector field、transport path、ODE sampler。
- **实践**：实现 2D flow matching toy example。

### 4. DiT / SD3 / FLUX

- **为什么读**：理解 diffusion transformer 和新一代 T2I。
- **完成标准**：能说明 UNet backbone 和 Transformer backbone 的差异。
- **实践**：读一个 DiT-like config。

### 5. CLIP / BLIP-2 / LLaVA

- **为什么读**：理解多模态从图文对齐到 instruction-tuned VLM。
- **完成标准**：能解释 vision encoder、projector/Q-Former、LLM 的连接。
- **实践**：完成 VLM Mini Benchmark。

---

## Computer Science / Systems Top 5

### 1. CSAPP / Computer Systems: A Programmer's Perspective

- **为什么读**：建立程序、内存、链接、异常、并发和性能优化的系统底座。
- **怎么读**：先抓 data representation、machine-level programming、memory hierarchy、linking、exceptional control flow。
- **完成标准**：能解释一次 C 程序从编译、链接到运行时的关键路径，并能用 cache / locality 分析性能问题。
- **常见误区**：只刷章节习题，不把汇编、内存布局和实际调试联系起来。
- **实践**：完成 Bomb Lab / Attack Lab / Cache Lab 中至少两个，并写复盘。

### 2. MIT 6.S081 / xv6

- **为什么读**：理解 OS 的进程、系统调用、页表、文件系统和并发控制。
- **怎么读**：把 lecture、xv6 book、lab 代码放在一起读；每个 lab 先画出 kernel path。
- **完成标准**：能说明一次 syscall 从用户态进入内核态再返回的路径。
- **常见误区**：只改到测试通过，不理解锁、页表和 trapframe 的边界条件。
- **实践**：完成 syscall / page table / thread 或 file system 相关 lab。

### 3. CMU 15-445 / Database Systems

- **为什么读**：数据库是存储、并发、查询优化和系统工程的综合训练场。
- **怎么读**：重点看 buffer pool、B+Tree、query execution、transactions、recovery。
- **完成标准**：能解释一条 SQL 从 parser 到 executor 的路径，以及并发事务为什么需要 isolation。
- **常见误区**：把数据库只当 SQL 用法，而不理解存储引擎和优化器。
- **实践**：完成 BusTub 中 buffer pool、index 或 execution 相关 project。

### 4. MIT 6.5840 / Distributed Systems

- **为什么读**：掌握复制、容错、共识、分片和一致性这些长期稳定的分布式系统核心问题。
- **怎么读**：论文和 lab 配套读，优先理解 Raft、MapReduce、KV replication、sharding。
- **完成标准**：能解释 leader election、log replication、linearizability 和 failure recovery 的关系。
- **常见误区**：只背 CAP / Paxos 术语，不通过 lab 暴露真实 race 和 failure case。
- **实践**：完成 Raft lab，并记录至少 5 个调试过的分布式失败模式。

### 5. Systems Classic Papers

- **为什么读**：用少量经典论文建立系统设计品味，理解工程 trade-off 的历史来源。
- **怎么读**：按问题读：存储、复制、调度、数据流、容错、可观测性，而不是按年份扫论文。
- **完成标准**：能用 1 页设计评审说明一篇论文的目标、假设、机制、局限和今天是否仍适用。
- **常见误区**：只摘摘要，不分析 workload、failure model 和实现约束。
- **实践**：从 [Systems Classic Papers](computer-science/systems-classic-papers.md) 选 3 篇写 design review。

---

## Evaluation / Benchmarking Top 5

### 1. Train / Validation / Test 与数据泄漏

- **为什么读**：所有模型与系统评估都建立在可靠数据切分和无泄漏假设上。
- **怎么读**：重点看 split strategy、distribution shift、contamination、leaderboard overfitting。
- **完成标准**：能为一个任务设计 train/dev/test，并说明如何防止 prompt、文档或 benchmark 泄漏。
- **常见误区**：只看最终分数，不审计数据来源和样本重叠。
- **实践**：为一个小型 RAG / Agent 数据集写 data card 和 leakage checklist。

### 2. LLM Evaluation Harness / HELM 思路

- **为什么读**：理解统一评测框架如何管理任务、指标、prompt、模型配置和可复现性。
- **怎么读**：关注 task abstraction、metric aggregation、model adapter、run config、结果记录。
- **完成标准**：能解释为什么同一个 benchmark 在不同 prompt / decoding 下不可直接比较。
- **常见误区**：把 leaderboard 当绝对能力排序，而忽略评测设置。
- **实践**：实现一个最小 eval harness，支持 2 个任务、2 个模型配置和可复现实验输出。

### 3. RAG Evaluation

- **为什么读**：RAG 失败可能来自检索、重排、上下文构造、生成或引用，不拆分评估无法定位问题。
- **怎么读**：区分 retrieval recall、context precision、answer faithfulness、citation correctness。
- **完成标准**：能把一次错误回答归因到 retrieval miss、context noise、generation hallucination 或 evaluator bias。
- **常见误区**：只用 answer accuracy 评价 RAG，导致不知道该优化 retriever 还是 generator。
- **实践**：对同一 QA 集比较 BM25、embedding、reranker 三种设置并做失败案例归因。

### 4. Agent / SWE Benchmarking

- **为什么读**：Agent 评估不是单轮问答，而是轨迹、工具调用、环境状态和最终产物的综合评估。
- **怎么读**：关注 resolved rate、trajectory quality、tool-call validity、sandbox reproducibility、test oracle。
- **完成标准**：能解释 SWE-bench 类任务为什么需要可复现环境和隐藏测试。
- **常见误区**：只看成功率，不分析 agent 是靠正确推理、偶然 patch 还是 benchmark artifact 成功。
- **实践**：设计 10 个 toy coding issues，包含测试、预期 patch、失败轨迹标签。

### 5. Serving / System Benchmarking

- **为什么读**：LLM serving 的评价必须同时看 latency、throughput、cost、quality 和 workload shape。
- **怎么读**：重点看 TTFT、TPOT、QPS、batching、KV cache、prompt/output length distribution。
- **完成标准**：能说明为什么单请求 latency、离线吞吐和线上混合 workload 的结论可能相反。
- **常见误区**：只报告 tokens/s，不报告硬件、并发、输入输出长度和调度策略。
- **实践**：用固定 workload 对比两个 serving 配置，并输出 benchmark report。

---

## Learning Systems / Meta-learning Top 5

### 1. Learning to Learn / Meta-learning Problem Setup

- **为什么读**：理解 meta-learning 的核心不是单任务拟合，而是跨任务快速适应。
- **怎么读**：重点看 task distribution、support/query split、inner loop / outer loop、few-shot evaluation。
- **完成标准**：能区分普通 supervised learning、multi-task learning 和 meta-learning。
- **常见误区**：把 few-shot prompting、fine-tuning 和严格 meta-learning 混为一谈。
- **实践**：构造一个 toy few-shot classification 任务集合，明确 support/query 切分。

### 2. MAML / Optimization-based Meta-learning

- **为什么读**：MAML 是理解“学一个容易适应的初始化”的经典入口。
- **怎么读**：关注 inner-loop adaptation、outer-loop gradient、first-order approximation。
- **完成标准**：能写出 MAML 的两层优化流程，并说明它为什么计算成本高。
- **常见误区**：只记住算法名，不理解 task batch 和 gradient through adaptation。
- **实践**：在 sinusoid regression 或 toy classification 上实现一版 first-order MAML。

### 3. Prototypical Networks / Metric-based Meta-learning

- **为什么读**：metric-based 方法是 few-shot learning 中最清晰、最容易复现的路线之一。
- **怎么读**：重点看 embedding space、class prototype、distance metric、episode training。
- **完成标准**：能解释为什么 episodic training 要模拟测试时的 N-way K-shot 设置。
- **常见误区**：只调 backbone，不检查 embedding 可分性和 episode 构造。
- **实践**：实现一个 prototypical network，并可视化 support/query embedding。

### 4. In-context Learning as Meta-learning Lens

- **为什么读**：用 meta-learning 视角理解 LLM 为什么能从上下文示例中适应任务。
- **怎么读**：关注 demonstration selection、order sensitivity、task induction、implicit Bayesian inference。
- **完成标准**：能说明 in-context learning 与参数更新式 meta-learning 的相同点和差异。
- **常见误区**：把 prompt 中给例子简单等同于模型真的学会了任务规则。
- **实践**：设计 prompt order / example selection ablation，观察同一模型的 few-shot 波动。

### 5. Continual Learning / Evaluation Protocols

- **为什么读**：长期学习系统需要处理灾难性遗忘、任务漂移和评估协议不稳定。
- **怎么读**：重点看 replay、regularization、adapter、task-free continual learning、forgetting metrics。
- **完成标准**：能设计一个评估协议，同时报告新任务表现、旧任务保持和适应成本。
- **常见误区**：只报告最后一个任务分数，不看 backward transfer / forgetting。
- **实践**：用小模型做 sequential tasks 实验，比较 full fine-tune、LoRA 和 replay。
