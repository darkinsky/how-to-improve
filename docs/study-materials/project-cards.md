# Study Materials Project Cards

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 实践项目 / 完成标准 |
| 难度 | 入门到前沿 |
| 优先级 | P0 / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 把学习资料转化为可验证的能力训练项目 |

---

## 先看结论

这个文档收集跨方向的实践项目卡片。每张卡片都回答：做什么、为什么做、输入是什么、输出是什么、如何验收。

建议使用方式：

```text
先选一条学习路线
  → 读 2-3 个核心文档
  → 做 1 张 project card
  → 写一份复盘 / benchmark report
  → 再进入下一阶段
```

---

## Project Card 模板

```markdown
## Project: 项目名

| 字段 | 内容 |
|------|------|
| 目标能力 | 这个项目训练什么能力 |
| 难度 | 入门 / 中级 / 进阶 / 前沿 |
| 预计时间 | 预估时间 |
| 前置知识 | 需要先读哪些材料 |
| 输入 | 数据、代码、模型、任务 |
| 输出物 | repo、报告、benchmark、复盘 |
| 完成标准 | 如何判断完成 |
| 相关材料 | Material Index 中对应的 P0/P1 材料 |
| 延伸方向 | 做完后可以怎么扩展 |
```

### 标准化样例

| 字段 | 内容 |
|------|------|
| 目标能力 | Retrieval evaluation / answer faithfulness / failure analysis |
| 难度 | 中级 |
| 预计时间 | 1-2 周 |
| 前置知识 | DPR / RAG / ColBERT / reranker |
| 输入 | 50-100 个 query-answer-citation 样例 |
| 输出物 | repo + benchmark report + JSONL traces |
| 完成标准 | 能比较 3 种 retrieval 设置，并解释失败案例来自检索、上下文噪音还是生成幻觉 |
| 相关材料 | RAG、ColBERT、Self-RAG、GraphRAG、RAGAS |
| 延伸方向 | GraphRAG / Self-RAG / agentic retrieval / online eval |


---

## 1. Train a Tiny GPT

| 字段 | 内容 |
|------|------|
| 目标 | 理解 decoder-only Transformer、tokenization、pretraining objective 和训练曲线 |
| 前置知识 | `foundation-models/README.md` 中 Transformer、GPT、Scaling Laws 部分 |
| 时间成本 | 1-2 周 |
| 输入 | 小型文本语料、nanoGPT 风格训练脚本 |
| 输出 | 训练日志、loss curve、sample outputs、简短报告 |
| 验收标准 | 能解释 embedding、attention、MLP、residual、KV cache、tokens/sec |
| 进阶 | 改 context length、batch size、模型大小，观察 loss 和吞吐变化 |

## 2. LoRA / QLoRA Fine-tuning

| 字段 | 内容 |
|------|------|
| 目标 | 理解参数高效微调、低比特量化和 instruction tuning |
| 前置知识 | LoRA、QLoRA、SFT、tokenization |
| 时间成本 | 1 周 |
| 输入 | 小模型、instruction dataset、PEFT 工具 |
| 输出 | 微调 checkpoint、评估样例、显存/速度记录 |
| 验收标准 | 能解释 rank、alpha、target modules、4-bit quantization 的影响 |
| 进阶 | 对比 full fine-tuning、LoRA、QLoRA、DoRA |

## 3. RAG Evaluation Harness

| 字段 | 内容 |
|------|------|
| 目标 | 建立可回归的 RAG 评估系统 |
| 前置知识 | DPR、RAG、rerank、citation correctness |
| 时间成本 | 1-2 周 |
| 输入 | 50-100 个 query-answer-citation 样例 |
| 输出 | evaluation report、JSONL traces、failure taxonomy |
| 验收标准 | 能比较 naive RAG、rerank RAG、HyDE、GraphRAG 的差异 |
| 进阶 | 加入 Self-RAG / CRAG / agentic retrieval |

## 4. VLM Mini Benchmark

| 字段 | 内容 |
|------|------|
| 目标 | 评估 VLM 的 OCR、图表、GUI 和视觉幻觉能力 |
| 前置知识 | CLIP、BLIP-2、LLaVA、SAM、grounding |
| 时间成本 | 1 周 |
| 输入 | 40-80 个图片/截图/图表样例 |
| 输出 | 模型对比表、失败案例集 |
| 验收标准 | 能区分 OCR 错误、grounding 错误、推理错误、幻觉 |
| 进阶 | 加入 VisualWebArena / OSWorld 风格任务 |

## 5. Mini SWE Agent

| 字段 | 内容 |
|------|------|
| 目标 | 理解 repo-level coding agent 的运行循环 |
| 前置知识 | SWE-bench、Terminal-Bench、harness、tool use |
| 时间成本 | 2-3 周 |
| 输入 | 10-20 个 toy repo issues |
| 输出 | mini agent、trajectory logs、success rate report |
| 验收标准 | 能完成 issue parsing、file search、patch、test、repair loop、日志记录 |
| 进阶 | 加入 SWE-bench Lite 风格任务和 trajectory replay viewer |

## 6. vLLM / SGLang Serving Benchmark

| 字段 | 内容 |
|------|------|
| 目标 | 理解 LLM serving 的吞吐、延迟、显存和调度权衡 |
| 前置知识 | KV cache、continuous batching、TTFT、TPOT |
| 时间成本 | 1-2 周 |
| 输入 | 一个开源模型、若干 sequence length / batch workload |
| 输出 | benchmark report、metrics table、瓶颈分析 |
| 验收标准 | 能解释 TTFT、TPOT、throughput、P95/P99、GPU memory 的变化 |
| 进阶 | 对比 prefill/decode 分离、prefix cache、speculative decoding |

## 7. FlashAttention / FlashInfer Kernel Study

| 字段 | 内容 |
|------|------|
| 目标 | 理解 attention kernel 的 IO-aware 优化和 inference kernel 栈 |
| 前置知识 | CUDA memory hierarchy、Triton、CUTLASS/CuTe |
| 时间成本 | 2 周 |
| 输入 | naive attention、FlashAttention、FlashInfer benchmark |
| 输出 | kernel study notes、profiling results |
| 验收标准 | 能解释 shared memory、tiling、HBM traffic、occupancy、decode attention |
| 进阶 | 用 Triton 写一个简化 attention kernel |

## 8. Tiny DPO

| 字段 | 内容 |
|------|------|
| 目标 | 理解 preference optimization 和 chosen/rejected 数据质量 |
| 前置知识 | SFT、DPO、KL/reference model、preference dataset |
| 时间成本 | 1 周 |
| 输入 | 小模型、小型 preference dataset |
| 输出 | DPO 训练脚本、数据审计报告 |
| 验收标准 | 能解释 length bias、distribution shift、reference-free/objective 变体 |
| 进阶 | 对比 KTO、ORPO、SimPO |

## 9. Tiny RLVR / Verifier Loop

| 字段 | 内容 |
|------|------|
| 目标 | 理解 verifier、rejection sampling、reward hacking 和 reasoning RL |
| 前置知识 | RLVR、ORM/PRM、STaR、ReST |
| 时间成本 | 1-2 周 |
| 输入 | 数学题或代码题、小型 verifier |
| 输出 | verifier loop、采样记录、reward hacking audit |
| 验收标准 | 能区分 outcome reward、process reward、environment reward |
| 进阶 | 加入 tree search 或 process reward model |

## 10. DDPM / Flow Matching / LCM Sampler Lab

| 字段 | 内容 |
|------|------|
| 目标 | 对比 diffusion、flow matching 和 consistency/LCM 的采样差异 |
| 前置知识 | DDPM、DDIM、Score SDE、Flow Matching、LCM |
| 时间成本 | 2 周 |
| 输入 | toy 2D dataset 或小型图像数据 |
| 输出 | sampler 对比图、训练曲线、生成样例 |
| 验收标准 | 能解释 noise schedule、ODE/SDE、solver step、few-step generation |
| 进阶 | 对比 DiT / latent diffusion / rectified flow |

---

## 项目完成后的复盘模板

```markdown
# Project Review

## Goal
## What I Built
## Metrics
## What Worked
## What Failed
## Failure Taxonomy
## What I Would Change
## Links to Code / Report
```
