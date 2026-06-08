# Generative Models 2026

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 前沿总览 / 路线图 |
| 难度 | 中级到前沿 |
| 优先级 | P0 / Survey / Frontier |
| 状态 | 推荐 |
| 建议用途 | 把 Diffusion、Flow Matching、DiT、图像/视频生成放到统一主线中理解 |

---

> 现代生成模型的主线已经从“GAN vs VAE”转向：**Diffusion / Flow Matching + Transformer backbone + 大规模多模态数据 + 高效采样与控制**。

---

## 先看结论

1. **GAN 不再是基础模型主线，但仍值得理解**：它解释了对抗训练、感知质量和 mode collapse 等核心问题。
2. **Diffusion 是现代图像生成的核心范式**：DDPM、DDIM、Score SDE、CFG、LDM 构成 Stable Diffusion 类系统的基础。
3. **Flow Matching / Rectified Flow 正在成为更统一的连续生成视角**：目标更简单，采样路径更直接，和现代大模型扩展性结合紧密。
4. **DiT 是图像/视频生成的架构主线**：Transformer 替代 U-Net 后，更容易 scaling，也更适合图文、多模态和时空 token。
5. **视频生成的关键难点不是“把图像模型多跑几帧”**：而是时序一致性、运动建模、长视频记忆、世界状态和成本。
6. **评估仍然困难**：FID / FVD / CLIPScore 只能覆盖一部分，真实质量还依赖人类偏好、可控性、安全和任务适配。

---

## 现代生成模型地图

```text
Classical Generative Models
├── AutoEncoder / VAE
├── GAN
└── Normalizing Flow
      ↓
Diffusion / Score-based Models
├── DDPM
├── DDIM
├── Score SDE
├── Classifier-Free Guidance
└── Latent Diffusion / Stable Diffusion
      ↓
Continuous Flow View
├── Flow Matching
├── Rectified Flow
├── Consistency Models
└── few-step / one-step generation
      ↓
Transformer Backbone
├── DiT
├── MM-DiT
├── MMDiT / Flux-style hybrid blocks
└── Spacetime DiT for video
      ↓
Modern Image / Video Generation
├── DALL·E / Imagen / Parti / Stable Diffusion / SDXL / SD3 / FLUX
├── Video Diffusion / Imagen Video / Make-A-Video / SVD
└── Sora / Veo / Movie Gen / Wan / CogVideoX
```

---

## 必读 Top 10

| 优先级 | 材料 | 关键词 | 为什么重要 |
|--------|------|--------|------------|
| P0 | VAE | latent variable | 理解潜空间生成和 LDM 的 VAE 编码器 |
| P1 | GAN | adversarial training | 理解感知质量、判别器和训练不稳定 |
| P0 | DDPM | diffusion foundation | 现代扩散模型基础 |
| P0 | DDIM | fast sampling | 扩散采样加速关键论文 |
| P0 | Score-based SDE | unified view | 统一 score matching 与 diffusion |
| P0 | Classifier-Free Guidance | conditional generation | 文生图和文生视频标配技术 |
| P0 | Latent Diffusion / Stable Diffusion | latent space | 现代开源图像生成基础 |
| P0 | DiT | Transformer backbone | 生成模型 scaling 的关键架构 |
| P0 | Flow Matching / Rectified Flow | continuous flow | 新一代生成模型统一视角 |
| P1 | Sora / Veo / Movie Gen / Wan / CogVideoX | video generation | 视频生成和世界模型方向代表 |

---

## 1. 从 VAE / GAN / Flow 到 Diffusion

### VAE

VAE 贡献了潜变量建模和 encoder-decoder 视角。即使现代图像生成主干通常是 diffusion / flow，VAE 仍然重要，因为 Stable Diffusion 类模型通常在 VAE latent space 中生成。

### GAN

GAN 的历史价值在于：

- 让生成模型第一次产生高感知质量图像；
- 引入 generator-discriminator 对抗框架；
- 暴露 mode collapse、训练不稳定、评估困难等问题。

但作为大规模基础生成模型路线，GAN 已经不再是主流。

### Normalizing Flow

Flow 的优点是可精确似然、可逆采样，但架构限制较强。现代 Flow Matching / Rectified Flow 继承了“连续变换”的思想，但不再要求传统 normalizing flow 那样严格可逆结构。

---

## 2. Diffusion 主线

Diffusion 模型的基本思想：

```text
训练：逐步加噪，然后学会从噪声中恢复数据
采样：从纯噪声开始，逐步去噪生成样本
```

重要节点：

| 阶段 | 代表 | 解决问题 |
|------|------|----------|
| DDPM | Ho et al. | 建立现代 diffusion 训练目标 |
| DDIM | Song et al. | 减少采样步数，提高速度 |
| Score SDE | Song et al. | 用 SDE / ODE 统一扩散和 score-based 模型 |
| CFG | Ho & Salimans | 让条件生成可控且高质量 |
| LDM | Rombach et al. | 在 latent space 生成，降低成本 |
| ControlNet / IP-Adapter | Zhang et al. / Ye et al. | 空间控制、图像条件和个性化 |

现代文生图系统常见结构：

```text
text encoder
  → latent diffusion / flow backbone
  → scheduler / sampler
  → VAE decoder
  → safety checker / upscaler / editor
```

---

## 3. Flow Matching / Rectified Flow

Flow Matching 和 Rectified Flow 把生成看作从简单分布到数据分布的连续路径学习：

```text
noise distribution  →  learn velocity field  →  data distribution
```

相比传统 diffusion，常见优势是：

- 训练目标更直接；
- 概念上更接近 ODE transport；
- 可以更自然地做少步采样；
- 与 Transformer backbone 和大规模训练结合顺畅。

和 diffusion 的关系可以粗略理解为：

```text
Diffusion: learn denoising / score along noisy path
Flow Matching: learn velocity field along probability path
Rectified Flow: learn straighter transport path for faster sampling
```

---

## 4. DiT 与 Scaling

U-Net 在早期 diffusion 中很成功，但随着模型规模变大，Transformer 的优势越来越明显：

| 架构 | 优点 | 局限 |
|------|------|------|
| U-Net | 局部归纳偏置强，图像任务成熟 | scaling 和多模态 token 融合不如 Transformer 直接 |
| DiT | 遵循 Transformer scaling，适合 patch / token 化 | 训练成本高，需要大量数据和算力 |
| MM-DiT | 图文 token 联合建模 | 架构复杂，对数据质量敏感 |
| Spacetime DiT | 图像/视频统一为时空 patch | 上下文长度和显存压力极大 |

现代图像 / 视频生成越来越像 LLM：都是 token 化、Transformer、scaling law、数据质量和推理系统的综合竞争。

---

## 5. 图像生成主线

```text
DALL·E / GLIDE / Imagen
  → Latent Diffusion / Stable Diffusion
  → SDXL / ControlNet / LoRA ecosystem
  → SD3 / FLUX / modern DiT-flow hybrids
```

重点能力：

- prompt following；
- text rendering；
- spatial control；
- style consistency；
- subject consistency；
- editing and inpainting；
- personalization；
- safety filtering。

---

## 6. 视频生成主线

视频生成比图像生成多了时间维度：

```text
image quality
+ temporal consistency
+ motion realism
+ camera control
+ long-range state memory
+ physical plausibility
```

代表路线：

| 路线 | 代表 | 关键词 |
|------|------|--------|
| Video Diffusion | Video Diffusion Models, Imagen Video | temporal attention / 3D U-Net |
| Image-to-Video | Stable Video Diffusion, AnimateDiff | motion module / image conditioning |
| DiT Video | Sora, Veo, Movie Gen, Wan, CogVideoX | spacetime patch / latent video tokens |
| Controllable Video | camera / pose / depth / trajectory control | motion control / editing |
| World Simulation | Sora-style technical reports | long-horizon consistency / implicit world model |

---

## 7. 评估指标

| 指标 | 用途 | 局限 |
|------|------|------|
| FID | 图像分布质量 | 对 prompt following 不敏感 |
| IS | 图像分类置信度 | 已较少作为主指标 |
| CLIPScore | 文图一致性 | 会偏向 CLIP 语义，不等于人类偏好 |
| FVD | 视频分布质量 | 对细节和时序错误不总敏感 |
| VBench | 视频多维评估 | 仍需人类评估补充 |
| T2VBench | 文生视频评测 | benchmark 覆盖有限 |
| Human Preference | 真实主观质量 | 昂贵、慢、可重复性差 |

评估生成模型时，不要只看单一 leaderboard。至少同时看：质量、文本遵循、可控性、一致性、速度、成本和安全。

---

## 实践路线

### 项目 1：Diffusion Sampler Lab

比较 DDPM、DDIM、DPM-Solver、Euler / Heun 等 scheduler：

- 同一 prompt；
- 不同步数；
- 不同 guidance scale；
- 记录速度、质量、失败样例。

### 项目 2：Latent vs Pixel Diffusion

在小数据集上对比 pixel diffusion 和 latent diffusion：

- 显存占用；
- 训练速度；
- 样本质量；
- VAE reconstruction error。

### 项目 3：Video Generation Evaluation

跑一个开源视频生成模型，记录：

- prompt following；
- motion consistency；
- identity consistency；
- camera control；
- flicker / artifacts；
- inference cost。

---

## 推荐学习顺序

1. VAE / GAN / Flow：快速补基础，不要陷太深；
2. DDPM / DDIM：理解 diffusion 核心；
3. Score SDE / CFG / LDM：理解现代文生图 pipeline；
4. Flow Matching / Rectified Flow：建立连续流统一视角；
5. DiT / MM-DiT：理解 scaling 和多模态 token；
6. Image & Video Generation：跟进现代系统和评估。

---

## 和现有文档的关系

- [Diffusion Model](diffusion-model.md)：扩散模型基础和 6 周学习计划。
- [Flow Matching](flow-matching.md)：连续流生成的专题路线。
- [Image & Video Generation](image-video-generation.md)：图像与视频生成模型演进和实践。
