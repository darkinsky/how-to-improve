# Multimodal / Vision-Language Models

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Multimodal / Vision-Language Models / Document AI / GUI Agents |
| 材料类型 | 路线 / 论文 / 系统 / 实践 |
| 难度 | 中级到前沿 |
| 优先级 | P1 / Frontier / Hands-on |
| 状态 | 推荐 |
| 建议用途 | 补齐 VLM、多模态理解、视觉 grounding、文档理解和 GUI Agent 的基础材料 |

---

## 先看结论

1. 多模态不只是图像生成；VLM 是 Agent、GUI automation、document AI、robotics、multimodal RAG 的共同基础。
2. 经典路线是 **CLIP / ALIGN → Flamingo / BLIP-2 → LLaVA / MiniGPT-4 → GPT-4V / Gemini / Qwen-VL / InternVL**。
3. 需要区分四类能力：图文对齐、视觉问答、grounding、长上下文多模态推理。
4. 学习时不要只看 demo，要用 OCR、图表、GUI screenshot、视觉幻觉检测做评估。

---

## 知识地图

```text
Vision Representation
  → Image-Text Contrastive Learning
  → Multimodal Pretraining
  → Instruction-tuned VLM
  → Grounding / Detection / Segmentation
  → Document AI / Chart Understanding
  → GUI Agents / Screen Understanding
  → Multimodal RAG / Memory
```

---

## 必读 Top 10

| 优先级 | 材料 | 类型 | 为什么重要 |
|--------|------|------|------------|
| P0 | CLIP | 论文 | 图文对比学习的事实起点 |
| P0 | ALIGN | 论文 | 大规模 noisy image-text pretraining 代表 |
| P0 | Flamingo | 论文 | few-shot multimodal LM 代表 |
| P0 | BLIP / BLIP-2 | 论文 | captioning、retrieval、Q-Former 主线 |
| P0 | LLaVA | 论文 / 系统 | 开源 instruction-tuned VLM 代表 |
| P1 | MiniGPT-4 | 论文 / 系统 | 早期开源 VLM 代表 |
| P1 | Kosmos-2 | 论文 | multimodal grounding 代表 |
| P1 | SigLIP | 论文 | CLIP 损失和训练改进 |
| P1 | DINOv2 | 论文 | self-supervised visual representation 代表 |
| P1 | SAM / SAM 2 | 系统 | segmentation foundation model，视觉 grounding 重要组件 |

---

## 1. 图文对齐与视觉表征

- **CLIP**：理解 contrastive learning、zero-shot classification、image-text embedding。
- **ALIGN / SigLIP**：理解大规模弱监督图文对齐。
- **DINO / DINOv2 / MAE**：理解 self-supervised vision representation。

---

## 2. VLM 架构主线

常见架构：

```text
Vision Encoder
  → Projector / Q-Former / Adapter
  → LLM
  → Multimodal instruction tuning
```

代表材料：

- Flamingo：cross-attention + few-shot multimodal。
- BLIP-2：Q-Former 连接 frozen vision encoder 和 LLM。
- LLaVA：visual instruction tuning。
- Qwen-VL / InternVL / LLaVA-NeXT：开源 VLM 主线。
- GPT-4V / GPT-4o / Gemini：商业多模态系统的能力边界参考。

---

## 3. Grounding / Document / GUI

### Grounding

- Grounding DINO：open-vocabulary detection。
- SAM / SAM 2：segmentation foundation model。
- Kosmos-2：phrase grounding。

### Document AI

重点任务：

- OCR；
- layout understanding；
- table / chart understanding；
- PDF QA；
- citation / evidence tracking。

### GUI Agents

关联 Agent Benchmark：

- OSWorld；
- AndroidWorld；
- WebArena；
- VisualWebArena。

重点不是“看懂截图”本身，而是：

```text
screen understanding → action grounding → feedback observation → long-horizon task completion
```

---

## 4. 前沿方向

- Native multimodal models：文本、图像、音频、视频统一建模。
- Multimodal long context：多图、多页 PDF、视频帧序列。
- Multimodal RAG：图像 / 文档 / 表格混合检索。
- GUI grounding：从视觉元素定位到可执行 action。
- Visual hallucination evaluation：检测不存在对象、错误 OCR、错误图表解读。

---

## 实践项目 / 完成标准

### Project 1：VLM Mini Benchmark

构建 40-80 个样例，覆盖：

- OCR；
- 图表理解；
- UI screenshot；
- object counting；
- spatial relation；
- visual hallucination。

完成标准：能比较 2-4 个 VLM 的失败模式。

### Project 2：Multimodal RAG

- 对 PDF / 图片 / 表格进行解析。
- 建立 text + image evidence store。
- 回答问题时给出引用。
- 完成标准：能评估 citation correctness。

### Project 3：GUI Agent Grounding

- 用 screenshot + accessibility tree 建立任务。
- 让模型输出 action plan。
- 记录失败：元素定位错误、状态理解错误、动作不可执行。

---

## 延伸资料

- Agent Benchmarks：`../agent-engineering/agent-benchmarks.md`
- RAG / Long Context：`../retrieval-rag/README.md`
- Image & Video Generation：`../generative-models/image-video-generation.md`
- Foundation Models：`../foundation-models/README.md`

### 补充：大规模 VLM / Vision Foundation Models

| 材料 | 方向 | 为什么值得补 |
|------|------|--------------|
| PaLI / PaLI-X | large-scale VLM | Google 大规模多语言、多模态 vision-language 模型路线 |
| Florence-2 | vision foundation model | 统一 detection、caption、grounding、OCR 等视觉任务的代表系统 |

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度；高变化阶段可每月 |
| 过时风险 | 高 |
| 维护重点 | 新论文、新系统、新 benchmark、官方技术报告、失效链接 |
| 稳定性 | 经典材料稳定，前沿系统观察中 |
