# Official Links for P0 Materials

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 官方链接索引 |
| 难度 | 入门 |
| 优先级 | P0 / Reference |
| 状态 | 可用 |
| 建议用途 | 为 P0 材料提供官方论文、代码、课程或项目入口，减少读者自行搜索成本 |

---

## 先看结论

本文件只收高优先级材料的官方入口。维护原则：

1. 优先 arXiv、论文官网、官方 repo、课程主页、官方技术报告。
2. 不收低质量二手解读。
3. 如果官方链接失效，优先替换为 arXiv 或 Internet Archive。
4. 更完整的材料归属见：[Material Index](material-index.md)。

---

## Foundation Models

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| Attention Is All You Need | https://arxiv.org/abs/1706.03762 | - | 先读模型结构和 attention 公式 |
| GPT-3 | https://arxiv.org/abs/2005.14165 | - | 重点读 scaling、few-shot、evaluation |
| Scaling Laws | https://arxiv.org/abs/2001.08361 | - | 和 Chinchilla 对比读 |
| Chinchilla | https://arxiv.org/abs/2203.15556 | - | 重点读 compute-optimal scaling |
| LLaMA | https://arxiv.org/abs/2302.13971 | https://github.com/meta-llama/llama | 关注训练 recipe 和架构细节 |
| LoRA | https://arxiv.org/abs/2106.09685 | https://github.com/microsoft/LoRA | 结合 PEFT 实践读 |
| QLoRA | https://arxiv.org/abs/2305.14314 | https://github.com/artidoro/qlora | 关注 4-bit quantization 和 adapter |
| Switch Transformer | https://arxiv.org/abs/2101.03961 | - | 和 GShard、MoE 并行一起读 |

## RAG / Retrieval

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| DPR | https://arxiv.org/abs/2004.04906 | https://github.com/facebookresearch/DPR | 关注 dual encoder 和 negatives |
| RAG | https://arxiv.org/abs/2005.11401 | https://github.com/facebookresearch/rag | 画出 retrieval-generation pipeline |
| FiD | https://arxiv.org/abs/2007.01282 | https://github.com/facebookresearch/FiD | 关注 fusion-in-decoder |
| ColBERT | https://arxiv.org/abs/2004.12832 | https://github.com/stanford-futuredata/ColBERT | 对比单向量 dense retrieval |
| Self-RAG | https://arxiv.org/abs/2310.11511 | https://github.com/AkariAsai/self-rag | 关注 retrieval decision 和 critique |
| GraphRAG | https://github.com/microsoft/graphrag | https://github.com/microsoft/graphrag | 从系统文档和 examples 入手 |

## AI Infra

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| FlashAttention | https://arxiv.org/abs/2205.14135 | https://github.com/Dao-AILab/flash-attention | 重点读 IO-aware tiling |
| Megatron-LM | https://arxiv.org/abs/1909.08053 | https://github.com/NVIDIA/Megatron-LM | 关注 tensor parallelism |
| ZeRO | https://arxiv.org/abs/1910.02054 | https://github.com/microsoft/DeepSpeed | 对比 stage 1/2/3 |
| vLLM / PagedAttention | https://arxiv.org/abs/2309.06180 | https://github.com/vllm-project/vllm | 关注 KV cache 管理 |
| SGLang | https://arxiv.org/abs/2312.07104 | https://github.com/sgl-project/sglang | 关注 structured generation 和 runtime |
| Ray | https://arxiv.org/abs/1712.05889 | https://github.com/ray-project/ray | 关注分布式任务和 actor 抽象 |

## Agent / Code Agent

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| ReAct | https://arxiv.org/abs/2210.03629 | - | 关注 thought-action-observation loop |
| Toolformer | https://arxiv.org/abs/2302.04761 | - | 关注自监督工具调用数据构造 |
| Generative Agents | https://arxiv.org/abs/2304.03442 | https://github.com/joonspk-research/generative_agents | 关注 memory/reflection/planning |
| SWE-bench | https://arxiv.org/abs/2310.06770 | https://github.com/swe-bench/SWE-bench | 先读 benchmark 设计 |
| OpenHands | https://github.com/All-Hands-AI/OpenHands | https://github.com/All-Hands-AI/OpenHands | 从 runtime 和 sandbox 看起 |
| LangGraph | https://github.com/langchain-ai/langgraph | https://github.com/langchain-ai/langgraph | 关注 stateful graph workflow |
| Model Context Protocol | https://modelcontextprotocol.io/ | https://github.com/modelcontextprotocol | 关注 tool/context 接入协议 |

## RL / Reasoning

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| DQN | https://www.nature.com/articles/nature14236 | - | 关注 replay buffer 和 target network |
| PPO | https://arxiv.org/abs/1707.06347 | - | 关注 clipped objective |
| AlphaZero | https://arxiv.org/abs/1712.01815 | - | 关注 self-play + MCTS |
| MuZero | https://arxiv.org/abs/1911.08265 | - | 关注 learned dynamics |
| Decision Transformer | https://arxiv.org/abs/2106.01345 | https://github.com/kzl/decision-transformer | 关注 sequence modeling for RL |
| DPO | https://arxiv.org/abs/2305.18290 | - | 关注 preference objective 推导 |
| STaR | https://arxiv.org/abs/2203.14465 | - | 关注 rationale self-improvement |

## Generative / Multimodal

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| DDPM | https://arxiv.org/abs/2006.11239 | - | 关注 forward/reverse process |
| DDIM | https://arxiv.org/abs/2010.02502 | - | 关注 deterministic sampling |
| Score SDE | https://arxiv.org/abs/2011.13456 | https://github.com/yang-song/score_sde | 和 DDPM/DDIM 对比读 |
| Latent Diffusion | https://arxiv.org/abs/2112.10752 | https://github.com/CompVis/latent-diffusion | 关注 latent space 和 CFG |
| DiT | https://arxiv.org/abs/2212.09748 | https://github.com/facebookresearch/DiT | 关注 Transformer backbone |
| Flow Matching | https://arxiv.org/abs/2210.02747 | - | 关注 vector field 和 transport path |
| CLIP | https://arxiv.org/abs/2103.00020 | https://github.com/openai/CLIP | 关注 image-text contrastive learning |
| BLIP-2 | https://arxiv.org/abs/2301.12597 | https://github.com/salesforce/LAVIS | 关注 Q-Former |
| LLaVA | https://arxiv.org/abs/2304.08485 | https://github.com/haotian-liu/LLaVA | 关注 visual instruction tuning |
| SAM | https://arxiv.org/abs/2304.02643 | https://github.com/facebookresearch/segment-anything | 关注 promptable segmentation |

## Evaluation

| 材料 | 官方链接 | 代码 / 项目 | 推荐阅读方式 |
|------|----------|-------------|--------------|
| HELM | https://crfm.stanford.edu/helm/ | https://github.com/stanford-crfm/helm | 关注 evaluation dimensions |
| MMLU | https://arxiv.org/abs/2009.03300 | - | 作为通用知识评估基线 |
| BIG-bench | https://arxiv.org/abs/2206.04615 | https://github.com/google/BIG-bench | 关注任务集合设计 |
| HumanEval | https://arxiv.org/abs/2107.03374 | https://github.com/openai/human-eval | 函数级代码生成基线 |
| WebArena | https://arxiv.org/abs/2307.13854 | https://github.com/web-arena-x/webarena | 关注 web agent 任务设计 |
| OSWorld | https://arxiv.org/abs/2404.07972 | https://github.com/xlang-ai/OSWorld | 关注 GUI agent 评估 |
| VBench | https://arxiv.org/abs/2311.17982 | https://github.com/Vchitect/VBench | 视频生成评估 |
