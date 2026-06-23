# 图像 / 视频生成前沿补充清单

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 前沿补充 / 附录 |
| 难度 | 进阶 |
| 优先级 | P1 / Frontier |
| 状态 | 需更新 |
| 建议用途 | 维护图像 / 视频生成主文档之外的前沿材料、范式对比和补充条目 |

---

## 先看结论

本文件承接 [图像与视频生成模型](image-video-generation.md) 的前沿补充清单。主文档保留核心路线、论文、实践和评估，本附录用于追踪更容易变化的模型、范式和补充材料。

---

## 图像 / 视频生成前沿补充清单

| 优先级 | 材料 | 方向 | 建议关注点 |
|--------|------|------|------------|
| P0 | DiT | diffusion transformer | Transformer 作为扩散骨干 |
| P0 | Stable Diffusion 3 | MMDiT / flow matching | 文本图像生成新主线 |
| P0 | FLUX | rectified flow / T2I | 开源高质量 T2I 代表 |
| P1 | PixArt-alpha / PixArt-sigma | efficient T2I | 训练效率和数据质量 |
| P1 | MaskGIT / Muse | masked token generation | 非自回归 token 图像生成 |
| P1 | Parti | autoregressive T2I | token-based AR 图像生成 |
| P1 | VAR | visual autoregressive modeling | 下一尺度预测的 AR 视觉建模 |
| P1 | VideoPoet | autoregressive video | 视频生成的 token/AR 路线 |
| P1 | Sora / Veo / Movie Gen | video foundation models | 世界模拟、长视频一致性、数据和评估 |
| P1 | CogVideoX / Wan | open video generation | 开源视频生成实践 |

建议新增范式对比：

| 范式 | 代表 | 优点 | 缺点 |
|------|------|------|------|
| Autoregressive image tokens | DALL-E, Parti, VAR | scaling 清晰 | 解码慢、tokenizer 关键 |
| Diffusion | DDPM, Stable Diffusion | 质量高、生态成熟 | 多步采样成本高 |
| Flow Matching / Rectified Flow | SD3, FLUX | 训练/采样路径简洁 | 工程细节仍在快速变化 |
| Consistency / LCM | CM, LCM | 少步生成 | 质量和稳定性 trade-off |
| GAN | StyleGAN | 快速高质量 | 训练不稳定、覆盖不足 |

### 补充：Autoregressive / Unified Generation

| 材料 | 方向 | 为什么值得补 |
|------|------|--------------|
| PixelCNN / PixelRNN | autoregressive image modeling | 图像自回归建模的经典起点 |
| PixelSNAIL | autoregressive image modeling | 改进 PixelCNN 类模型的 long-range dependency 建模 |
| Lumina-T2X | unified generation | 统一 text-to-image / text-to-video / multi-resolution generation 的前沿系统之一 |

### 补充：DALL-E 1

- **DALL-E 1**：discrete image tokens + autoregressive Transformer 的文本生成图像代表工作，适合理解 VQ/VQGAN tokenizer、Parti、Muse、VAR 等 token-based 图像生成路线的历史脉络。

---

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度 |
| 过时风险 | 高 |
| 维护重点 | Autoregressive / unified generation、视频 foundation models、开源模型和评估指标变化 |
