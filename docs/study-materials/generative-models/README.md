# Generative Models

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 索引 / 路线 |
| 难度 | 入门到进阶 |
| 优先级 | P0 / Survey / Frontier |
| 状态 | 推荐 |
| 建议用途 | 建立生成模型主线 |

---

这个目录整理生成模型的核心路线：AutoEncoder / VAE、GAN、Flow-based Models、Diffusion、Flow Matching，以及现代图像与视频生成模型。

---

## 先看结论

现代生成模型可以粗略理解为几条路线的演化：

```text
VAE：学习潜空间表示，但样本质量通常偏平滑
GAN：对抗训练带来高质量样本，但训练不稳定、模式崩溃明显
Flow：可精确似然、可逆变换，但架构约束较强
Diffusion：训练稳定、样本质量高，成为图像/视频生成主线
Flow Matching / Rectified Flow：用更简单的连续流视角统一和改进生成过程
DiT / Video Diffusion：将生成模型扩展到更大规模图像、视频和多模态生成
```

如果目标是现代图像 / 视频生成，建议快速理解 VAE、GAN、Flow 的核心思想后，把主要精力放在 **Diffusion、Flow Matching、DiT、Image/Video Generation** 上。

---

## 推荐学习顺序

1. [Generative Models 2026](generative-models-2026.md)：先建立现代生成模型全景。
2. [AutoEncoder & VAE](autoencoder-vae.md)：理解 latent space 和 VAE encoder / decoder。
3. [GAN](gan.md)：理解对抗训练、感知质量和 mode collapse。
4. [Flow-based Models](flow-based-models.md)：理解可逆变换和似然建模。
5. [Diffusion Model](diffusion-model.md)：掌握 DDPM、DDIM、Score SDE、CFG、LDM。
6. [Flow Matching](flow-matching.md)：理解 Rectified Flow、velocity prediction 和少步采样。
7. [Image & Video Generation](image-video-generation.md)：跟进 DiT、FLUX、Sora、Wan、CogVideoX 等现代系统。
8. [Image / Video Frontier Appendix](image-video-generation-frontier-appendix.md)：维护更易变化的前沿补充材料和范式对比。

---

## 必读 Top 10

1. **Generative Models 2026** — 现代生成模型总览：Diffusion / Flow Matching / DiT / Video
2. **VAE** — Auto-Encoding Variational Bayes
3. **GAN** — Generative Adversarial Nets
4. **NICE / RealNVP / Glow** — Flow-based Models 代表路线
5. **DDPM** — Denoising Diffusion Probabilistic Models
6. **DDIM** — Denoising Diffusion Implicit Models
7. **Score-based SDE / CFG / LDM** — 现代文生图基础组件
8. **DiT** — Scalable Diffusion Models with Transformers
9. **Flow Matching / Rectified Flow** — 连续流生成的新主线
10. **Sora / Flux / Wan / CogVideoX** — 图像与视频生成前沿代表

---

## 按目标选择

| 目标 | 建议路线 |
|------|----------|
| 建立生成模型基础 | [Generative Models 2026](generative-models-2026.md) → VAE → GAN → Flow → Diffusion |
| 学现代图像生成 | [Diffusion Model](diffusion-model.md) → LDM / Stable Diffusion → ControlNet → DiT / FLUX |
| 学视频生成 | Diffusion → Video Diffusion → [Image & Video Generation](image-video-generation.md) → Sora / CogVideoX / Wan |
| 跟进研究前沿 | [Flow Matching](flow-matching.md) → Rectified Flow → Consistency Models → DiT Scaling |
| 做生成模型系统和推理优化 | Diffusers → sampler 对比 → quantization / batching → video inference cost profiling |
| 做工程实践 | Hugging Face Diffusers → Stable Diffusion → LoRA / ControlNet → 视频生成模型 |

---

## 实践项目建议

- 从零实现一个 MNIST / CIFAR-10 DDPM；
- 使用 Hugging Face Diffusers 跑通 Stable Diffusion 推理；
- 对比 DDPM、DDIM、DPM-Solver 的采样速度和质量；
- 用 LoRA 或 DreamBooth 做一个小型个性化生成实验；
- 跑通一个开源视频生成模型，记录显存、速度和效果；
- 阅读 DiT 或 Flux 的架构说明，画出模型数据流。

---

## 目前还值得补强的方向

- Rectified Flow / Consistency Models 的统一整理；
- DiT scaling 与现代图像生成模型架构对比；
- 视频生成评估：VBench、T2VBench 等；
- 多模态统一生成模型；
- 生成模型的 evaluation、alignment 和 safety。

---

## 相邻路线

- [Multimodal / Vision-Language Models](../multimodal/README.md)：补 CLIP、BLIP-2、LLaVA、SAM、文档理解和 GUI Agent。
- [Evaluation / Benchmarking](../evaluation-benchmarking.md)：补 FID、CLIPScore、FVD、VBench 和人工偏好评估。
