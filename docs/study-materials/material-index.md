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

## 维护规则

1. 新增 P0/P1 材料时，同步更新本索引。
2. 如果一个材料跨多个方向，只选择一个主文档做完整解释。
3. 相关文档只保留短引用，并链接回主文档。
4. 每季度检查：是否有材料重复解释、主文档失效或前沿材料已过时。
