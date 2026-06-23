# Study Materials Material Index

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 全局索引 / 单一事实源 |
| 难度 | 入门 |
| 优先级 | P0 / Survey |
| 状态 | 推荐 |
| 建议用途 | 明确重要材料的主解释文档、相关文档和标签，减少重复维护 |

---

## 先看结论

这个索引用来解决一个问题：同一个材料可能出现在多个专题中，例如 LoRA、SWE-bench、GraphRAG、FlashAttention、DPO。为了避免解释分散，约定：

1. **主文档**：负责解释该材料的核心思想、阅读顺序和实践建议。
2. **相关文档**：可以引用材料，但不重复展开过多背景。
3. **标签**：帮助后续按主题检索和维护。
4. 新增重要材料时，优先同步更新本索引。
5. **治理字段**：P0/P1 材料应逐步补齐官方链接、代码入口、相关 Project Card 和最近审阅时间，形成单一事实源。

## 单一事实源字段

后续新增或整理 P0/P1 材料时，优先使用下列字段。已有分区表格可以先保留轻量格式，再逐步迁移。

| 字段 | 说明 |
|------|------|
| 材料 | 论文、课程、系统、benchmark 或项目名称 |
| 主文档 | 仓库中负责完整解释该材料的文档 |
| 类型 | 课程 / 论文 / 系统 / Benchmark / 项目 / 综述 |
| 优先级 | P0 / P1 / P2 / Classic / Frontier / Hands-on |
| 官方链接 | arXiv、官网、课程主页、官方博客或规范 |
| 代码 | 官方仓库或主流实现；没有代码时写 `N/A` |
| 相关 Project | 对应 [Project Cards](project-cards.md) 中的可验证项目 |
| 最近审阅 | `YYYY-MM`，用于 freshness 和失效链接治理 |

### P0/P1 治理样例

| 材料 | 主文档 | 类型 | 优先级 | 官方链接 | 代码 | 相关 Project | 最近审阅 |
|------|--------|------|--------|----------|------|--------------|----------|
| Transformer | `foundation-models/README.md` | 论文 | P0 / Classic | https://arxiv.org/abs/1706.03762 | N/A | Train a Tiny GPT | 2026-06 |
| LoRA / QLoRA | `foundation-models/README.md` | 论文 / 方法 | P0 / Hands-on | https://arxiv.org/abs/2106.09685 | https://github.com/huggingface/peft | LoRA / QLoRA Fine-tuning | 2026-06 |
| FlashAttention | `ai-infra/02-cuda-kernels.md` | 系统 / Kernel | P0 / Hands-on | https://arxiv.org/abs/2205.14135 | https://github.com/Dao-AILab/flash-attention | FlashAttention / FlashInfer Kernel Study | 2026-06 |
| vLLM | `ai-infra/04-llm-inference.md` | 系统 | P0 / Frontier | https://arxiv.org/abs/2309.06180 | https://github.com/vllm-project/vllm | vLLM / SGLang Serving Benchmark | 2026-06 |
| SGLang | `ai-infra/04-llm-inference.md` | 系统 | P0 / Frontier | https://github.com/sgl-project/sglang | https://github.com/sgl-project/sglang | vLLM / SGLang Serving Benchmark | 2026-06 |
| SWE-bench | `agent-engineering/agent-benchmarks.md` | Benchmark | P0 / Frontier | https://www.swebench.com/ | https://github.com/SWE-bench/SWE-bench | Mini SWE Agent | 2026-06 |
| Terminal-Bench | `agent-engineering/agent-benchmarks.md` | Benchmark | P0 / Frontier | https://www.tbench.ai/ | https://github.com/laude-institute/terminal-bench | Coding Agent Regression Suite | 2026-06 |
| MCP | `agent-engineering/agent-runtime-frameworks.md` | 协议 | P1 / Frontier | https://modelcontextprotocol.io/ | https://github.com/modelcontextprotocol | Agent Runtime Bake-off | 2026-06 |
| DPO | `reinforcement-learning/preference-optimization.md` | 论文 / 方法 | P0 / Classic | https://arxiv.org/abs/2305.18290 | N/A | Preference Optimization Mini Lab | 2026-06 |
| DeepSeek-R1 / RLVR | `reinforcement-learning/reasoning-rl.md` | 论文 / 方法 | P0 / Frontier | https://arxiv.org/abs/2501.12948 | N/A | Verifiable Reasoning RL Mini Lab | 2026-06 |
| RAGAS | `evaluation-benchmarking.md` | 工具 / Eval | P1 / Hands-on | https://docs.ragas.io/ | https://github.com/explodinggradients/ragas | Unified Eval Harness | 2026-06 |
| Contriever | `retrieval-rag/README.md` | 论文 / 系统 | P1 / Classic | https://arxiv.org/abs/2112.09118 | https://github.com/facebookresearch/contriever | RAG Evaluation Harness | 2026-06 |
| BGE / FlagEmbedding | `retrieval-rag/README.md` | 模型 / 工具 | P1 / Hands-on | https://github.com/FlagOpen/FlagEmbedding | https://github.com/FlagOpen/FlagEmbedding | RAG Evaluation Harness | 2026-06 |
| LangGraph | `agent-engineering/agent-runtime-frameworks.md` | 框架 | P1 / Hands-on | https://langchain-ai.github.io/langgraph/ | https://github.com/langchain-ai/langgraph | Agent Runtime Bake-off | 2026-06 |
| SWE-agent | `agent-engineering/code-agents.md` | 系统 | P1 / Hands-on | https://arxiv.org/abs/2405.15793 | https://github.com/SWE-agent/SWE-agent | Mini SWE Agent | 2026-06 |
| TensorRT-LLM | `ai-infra/04-llm-inference.md` | 系统 | P1 / Hands-on | https://github.com/NVIDIA/TensorRT-LLM | https://github.com/NVIDIA/TensorRT-LLM | vLLM / SGLang Serving Benchmark | 2026-06 |
| VBench | `evaluation-benchmarking.md` | Benchmark | P1 / Frontier | https://arxiv.org/abs/2311.17982 | https://github.com/Vchitect/VBench | VLM / Generation Evaluation | 2026-06 |

### P0/P1 维护检查

每季度优先检查上表，而不是全库平均用力：

- P0 材料是否仍由正确主文档解释；
- 官方链接和代码仓库是否失效或迁移；
- 相关 Project Card 是否仍能验证该材料的核心能力；
- `最近审阅` 是否超过一个季度；
- 同一材料是否在多个文档中重复长篇解释。


---

## Foundation Models / LLM

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| Attention Is All You Need | `foundation-models/README.md` | `ai-infra/04-llm-inference.md` | Transformer, Classic |
| GPT-1 / GPT-2 / GPT-3 | `foundation-models/README.md` | `learning-paths.md` | LLM, Classic |
| Scaling Laws / Chinchilla | `foundation-models/README.md` | `learning-systems/meta-learning.md` | Scaling, Classic |
| LLaMA | `foundation-models/README.md` | `ai-infra/04-llm-inference.md` | Open LLM |
| RoPE / ALiBi | `foundation-models/README.md` | `ai-infra/04-llm-inference.md` | Long Context |
| LoRA / QLoRA / DoRA | `foundation-models/README.md` | `generative-models/image-video-generation.md` | PEFT |
| GShard / Switch Transformer / Mixtral / DeepSeek-V3 | `foundation-models/README.md` | `ai-infra/03-distributed-training.md` | MoE |
| Mamba / RWKV / RetNet / Hyena / Jamba | `foundation-models/README.md` | `learning-systems/meta-learning.md` | Transformer Alternatives |

## RAG / Retrieval / Memory

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| DPR | `retrieval-rag/README.md` | `agent-engineering/agent-memory.md` | Dense Retrieval |
| RAG / FiD / ColBERT | `retrieval-rag/README.md` | `evaluation-benchmarking.md` | RAG, Classic |
| REALM / RETRO / Atlas | `retrieval-rag/README.md` | `foundation-models/README.md` | Retrieval-augmented LM |
| Self-RAG / CRAG / HyDE | `retrieval-rag/README.md` | `evaluation-benchmarking.md` | RAG, Frontier |
| GraphRAG | `retrieval-rag/README.md` | `agent-engineering/agent-memory.md` | Graph Memory |
| MemGPT / Letta | `agent-engineering/agent-memory.md` | `retrieval-rag/README.md` | Agent Memory |

## Multimodal / VLM

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| CLIP / ALIGN / SigLIP | `multimodal/README.md` | `generative-models/image-video-generation.md` | Vision-Language |
| Flamingo / BLIP / BLIP-2 | `multimodal/README.md` | `foundation-models/README.md` | VLM |
| LLaVA / MiniGPT-4 / Qwen-VL / InternVL | `multimodal/README.md` | `agent-engineering/agent-benchmarks.md` | Open VLM |
| Kosmos-2 / Grounding DINO / SAM / SAM 2 | `multimodal/README.md` | `agent-engineering/agent-benchmarks.md` | Grounding |
| PaLI / PaLI-X / Florence-2 | `multimodal/README.md` | `evaluation-benchmarking.md` | Vision Foundation Model |

## Agent / Code Agent / Runtime

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| ReAct / Toolformer / WebGPT | `agent-engineering/README.md` | `agent-engineering/harness-engineering.md` | Agent, Classic |
| Generative Agents / Reflexion / Voyager | `agent-engineering/agent-memory.md` | `reinforcement-learning/agentic-rl.md` | Memory, Lifelong Learning |
| SWE-bench / Terminal-Bench | `agent-engineering/agent-benchmarks.md` | `agent-engineering/code-agents.md` | Benchmark |
| SWE-agent / OpenHands / Aider | `agent-engineering/code-agents.md` | `evaluation-benchmarking.md` | Code Agent |
| Claude Code / Codex CLI / Cursor / Cline / Devin | `agent-engineering/code-agents.md` | `agent-engineering/agent-runtime-frameworks.md` | Code Agent, Product |
| MCP / A2A | `agent-engineering/agent-runtime-frameworks.md` | `agent-engineering/harness-engineering.md` | Protocol |
| LangGraph / AutoGen / CrewAI / Semantic Kernel | `agent-engineering/agent-runtime-frameworks.md` | `agent-engineering/harness-engineering.md` | Runtime |
| DSPy / Guidance / Outlines / Instructor / PydanticAI | `agent-engineering/agent-runtime-frameworks.md` | `evaluation-benchmarking.md` | Structured Generation |

## AI Infra / Systems

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| CUDA / Triton / CUTLASS / CuTe | `ai-infra/02-cuda-kernels.md` | `ai-infra/01-architecture.md` | Kernel |
| FlashAttention / FlashInfer / ThunderKittens | `ai-infra/02-cuda-kernels.md` | `ai-infra/04-llm-inference.md` | Kernel, Serving |
| Megatron-LM / ZeRO / DeepSpeed | `ai-infra/03-distributed-training.md` | `ai-infra/07-ai-infra-papers.md` | Distributed Training |
| GPipe / PipeDream / GSPMD / Alpa / FlexFlow | `ai-infra/03-distributed-training.md` | `computer-science/systems-classic-papers.md` | Parallelism |
| vLLM / SGLang / TensorRT-LLM | `ai-infra/04-llm-inference.md` | `ai-infra/08-llm-serving-frontier.md` | Serving |
| Orca / Sarathi / DistServe / Mooncake / Splitwise | `ai-infra/04-llm-inference.md` | `ai-infra/08-llm-serving-frontier.md` | Serving Frontier |
| Medusa / EAGLE / SpecInfer | `ai-infra/04-llm-inference.md` | `foundation-models/README.md` | Speculative Decoding |
| Lamport / Paxos / Raft / GFS / MapReduce / Spanner | `computer-science/systems-classic-papers.md` | `ai-infra/README.md` | Systems Classic |

## RL / Alignment / Reasoning

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| DQN / Rainbow / PPO / SAC | `reinforcement-learning/advanced-rl.md` | `reinforcement-learning/README.md` | RL Classic |
| AlphaGo / AlphaZero / MuZero | `reinforcement-learning/advanced-rl.md` | `reinforcement-learning/reasoning-rl.md` | Search, RL |
| Dreamer / Decision Transformer / TD-MPC | `reinforcement-learning/advanced-rl.md` | `learning-systems/meta-learning.md` | World Model, Offline RL |
| InstructGPT / RLHF / Constitutional AI | `reinforcement-learning/preference-optimization.md` | `foundation-models/README.md` | Alignment |
| DPO / IPO / KTO / ORPO / SimPO | `reinforcement-learning/preference-optimization.md` | `reinforcement-learning/llm-agent-rl-frontier.md` | Preference Optimization |
| DeepSeek-R1 / GRPO / RLVR / PRM | `reinforcement-learning/reasoning-rl.md` | `reinforcement-learning/llm-agent-rl-frontier.md` | Reasoning RL |
| STaR / ReST / Tree of Thoughts / Reflexion | `reinforcement-learning/reasoning-rl.md` | `agent-engineering/agent-memory.md` | Test-time Compute |

## Generative Models

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| VQ-VAE / VQGAN | `generative-models/autoencoder-vae.md` | `generative-models/image-video-generation.md` | Tokenizer |
| DDPM / DDIM / Score SDE / EDM | `generative-models/diffusion-model.md` | `generative-models/generative-models-2026.md` | Diffusion |
| Latent Diffusion / Stable Diffusion | `generative-models/diffusion-model.md` | `generative-models/image-video-generation.md` | T2I |
| ControlNet / IP-Adapter / DreamBooth | `generative-models/diffusion-model.md` | `generative-models/image-video-generation.md` | Control, Personalization |
| Flow Matching / Rectified Flow | `generative-models/flow-matching.md` | `generative-models/generative-models-2026.md` | Flow |
| Consistency Models / LCM | `generative-models/diffusion-model.md` | `generative-models/image-video-generation.md` | Fast Sampling |
| DiT / SD3 / FLUX / PixArt | `generative-models/image-video-generation.md` | `generative-models/generative-models-2026.md` | T2I Frontier |
| PixelCNN / DALL-E 1 / Parti / Muse / VAR | `generative-models/image-video-generation.md` | `generative-models/autoencoder-vae.md` | Autoregressive Image |
| Sora / Veo / Movie Gen / CogVideoX / Wan / VideoPoet | `generative-models/image-video-generation.md` | `evaluation-benchmarking.md` | Video Generation |

## Evaluation / Benchmarking

| 材料 | 主文档 | 相关文档 | 标签 |
|------|--------|----------|------|
| HELM / MMLU / BIG-bench | `evaluation-benchmarking.md` | `foundation-models/README.md` | LLM Eval |
| GSM8K / MATH / GPQA / ARC-AGI | `evaluation-benchmarking.md` | `reinforcement-learning/reasoning-rl.md` | Reasoning Eval |
| HumanEval / MBPP / SWE-bench | `evaluation-benchmarking.md` | `agent-engineering/code-agents.md` | Code Eval |
| WebArena / OSWorld / AndroidWorld / GAIA | `agent-engineering/agent-benchmarks.md` | `multimodal/README.md` | Agent Eval |
| RAGAS / TruLens / DeepEval | `evaluation-benchmarking.md` | `retrieval-rag/README.md` | RAG Eval |
| FID / CLIPScore / FVD / VBench | `evaluation-benchmarking.md` | `generative-models/image-video-generation.md` | Generative Eval |

---

## 外部引用质量分层

| 层级 | 优先收录 | 说明 |
|------|----------|------|
| S | arXiv / 会议论文 / 官方技术报告 / 官方文档 / 官方 repo | 默认优先，适合作为主引用 |
| A | 课程主页 / 教材 / 一线研究者或工程师长文 | 可作为解释性补充 |
| B | 社区教程 / 博客 / 复现仓库 | 只在实践价值明显且链接稳定时保留 |
| C | 聚合站、转载、短新闻、缺少出处的二手解读 | 原则上不作为核心引用；若保留需有替代官方来源 |

更新资料时优先用 S/A 层替换 C 层来源。中文文章可以作为入门辅助，但核心论点必须能回到论文、官方文档、代码或一线作者文章。

---

## 维护规则

1. 新增 P0/P1 材料时，同步更新本索引。
2. 如果一个材料跨多个方向，只选择一个主文档做完整解释。
3. 相关文档只保留短引用，并链接回主文档。
4. 每季度检查：是否有材料重复解释、主文档失效或前沿材料已过时。
