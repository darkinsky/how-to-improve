# 图像与视频生成模型 学习计划与资料汇总

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 前沿 / 应用路线 |
| 难度 | 进阶 |
| 优先级 | P0 / Frontier / Survey |
| 状态 | 需更新 |
| 建议用途 | 跟进图像与视频生成模型演进 |

---

> 整理时间：2026-03-27
> 目标：系统掌握当前主流图像/视频生成模型的原理、架构演进与实践方法
> 前置推荐：先完成 Diffusion Model 学习，理解去噪过程与条件生成基础

> 总览补充：现代生成模型路线见 [Generative Models 2026](generative-models-2026.md)。本文重点跟踪图像/视频生成系统、模型演进、评估和实践。

---

## 先看结论

图像与视频生成的核心主线：

```text
图像：DDPM → LDM / Stable Diffusion → SDXL / ControlNet / LoRA → SD3 / FLUX / DiT-flow hybrids
视频：Video Diffusion → AnimateDiff / SVD → Sora / Veo / Movie Gen / Wan / CogVideoX
```

判断一个模型是否重要，不只看 demo 漂亮不漂亮，还要看：

- 是否改变了架构范式：U-Net → DiT / MM-DiT / spacetime patch；
- 是否降低了训练或推理成本：latent compression、few-step sampling、distillation；
- 是否增强了可控性：ControlNet、IP-Adapter、camera control、trajectory control；
- 是否改善了长时一致性：identity、object permanence、motion consistency；
- 是否有可复现生态：开源权重、训练代码、推理框架、benchmark。

---

## 知识地图

```
图像 & 视频生成模型
    ├── 图像生成
    │       ├── 基础架构演进
    │       │       ├── U-Net based Diffusion（DDPM/DDIM）
    │       │       ├── Latent Diffusion（潜空间扩散）
    │       │       └── DiT（Diffusion Transformer）
    │       ├── 文本条件生成
    │       │       ├── CLIP / T5 文本编码
    │       │       ├── Classifier-Free Guidance (CFG)
    │       │       └── Cross-Attention 注入
    │       ├── 精细控制
    │       │       ├── ControlNet（姿态/边缘/深度控制）
    │       │       ├── IP-Adapter（图像风格迁移）
    │       │       └── LoRA / DreamBooth（个性化微调）
    │       └── 代表模型
    │               ├── Stable Diffusion 系列（开源）
    │               ├── DALL-E 系列（OpenAI）
    │               ├── Imagen 系列（Google）
    │               ├── Midjourney
    │               └── Flux.1（新一代开源）
    └── 视频生成
            ├── 架构方向
            │       ├── 时序 U-Net（3D Conv / Temporal Attention）
            │       ├── DiT-based（Sora 路线）
            │       └── 自回归视频（次要方向）
            ├── 关键技术
            │       ├── 时序一致性（Temporal Consistency）
            │       ├── 运动建模（Motion Prior）
            │       └── 视频 VAE（时空压缩）
            └── 代表模型
                    ├── Sora（OpenAI，闭源）
                    ├── Wan2.1（阿里，开源）
                    ├── CogVideoX（智谱，开源）
                    └── Stable Video Diffusion（开源）
```

---

## 架构演进时间线

```
2020  DDPM（Ho et al.）—— Diffusion 奠基
  ↓
2021  DDIM —— 加速采样
  ↓
2022  LDM / Stable Diffusion —— 潜空间，降低计算量 ★
      DALL-E 2 —— CLIP + Diffusion
  ↓
2023  SD XL —— 更大模型，更高质量
      ControlNet —— 精细空间控制 ★
      AnimateDiff —— 图像模型→视频 ★
  ↓
2024  SD 3 / Flux.1 —— DiT 骨干替换 U-Net ★★
      Sora —— 视频生成 DiT 里程碑 ★★
      Wan2.1 —— 最强开源视频模型
  ↓
2025  多模态统一生成模型（进行中）
```

---

## 图像生成核心论文

### 🏛️ 基础架构

#### Denoising Diffusion Probabilistic Models（DDPM）
- **作者：** Ho et al.（UC Berkeley）
- **发表：** NeurIPS 2020
- **论文：** https://arxiv.org/abs/2006.11239
- **代码：** https://github.com/hojonathanho/diffusion
- **摘要：** 现代图像 Diffusion 的奠基工作，确立了训练和采样范式

#### DDIM: Denoising Diffusion Implicit Models
- **作者：** Song et al.（Stanford）
- **发表：** ICLR 2021
- **论文：** https://arxiv.org/abs/2010.02502
- **摘要：** 非马尔可夫采样，将推理步数从 1000 步降至 50 步，速度提升 20x

#### High-Resolution Image Synthesis with Latent Diffusion Models（LDM / Stable Diffusion）
- **作者：** Rombach et al.（LMU Munich）
- **发表：** CVPR 2022
- **论文：** https://arxiv.org/abs/2112.10752
- **代码：** https://github.com/CompVis/latent-diffusion
- **摘要：** ★ 图像生成最重要的论文之一。将 Diffusion 移入 VAE 潜空间，计算量降低 ~8x，使高分辨率生成成为可能；Stable Diffusion 的直接来源

### 🎨 条件控制

#### CLIP: Learning Transferable Visual Models From Natural Language Supervision
- **作者：** Radford et al.（OpenAI）
- **发表：** ICML 2021
- **论文：** https://arxiv.org/abs/2103.00020
- **摘要：** 文图对齐的基础模型，几乎所有文生图模型的文本编码器来源

#### Classifier-Free Diffusion Guidance
- **作者：** Ho & Salimans（Google Brain）
- **发表：** NeurIPS 2021 Workshop
- **论文：** https://arxiv.org/abs/2207.12598
- **摘要：** CFG 是文生图最关键的技术之一，通过无条件和有条件预测的线性组合控制生成强度，几乎所有现代文生图模型都使用

#### Adding Conditional Control to Text-to-Image Diffusion Models（ControlNet）
- **作者：** Zhang et al.
- **发表：** ICCV 2023
- **论文：** https://arxiv.org/abs/2302.05543
- **代码：** https://github.com/lllyasviel/ControlNet
- **摘要：** ★ 通过附加控制网络，实现姿态/边缘/深度图等空间精确控制；开源后迅速成为 SD 生态最重要的插件

#### IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models
- **作者：** Ye et al.（腾讯 AI Lab）
- **发表：** 2023
- **论文：** https://arxiv.org/abs/2308.06721
- **代码：** https://github.com/tencent-ailab/IP-Adapter
- **摘要：** 解耦图像风格与内容，通过图像 prompt 控制生成风格；腾讯 AI Lab 出品

### 🌟 DiT：新一代骨干

#### Scalable Diffusion Models with Transformers（DiT）
- **作者：** Peebles & Xie（UC Berkeley）
- **发表：** ICCV 2023
- **论文：** https://arxiv.org/abs/2212.09748
- **代码：** https://github.com/facebookresearch/DiT
- **摘要：** ★★ 用 Vision Transformer 替换 U-Net 作为 Diffusion 去噪网络，FID 大幅提升且遵循 Scaling Law；Sora、Flux、SD3 的理论基础

#### Stable Diffusion 3（Multimodal Diffusion Transformer）
- **作者：** Esser et al.（Stability AI）
- **发表：** 2024
- **论文：** https://arxiv.org/abs/2403.03206
- **摘要：** SD3 采用 MM-DiT（多模态 DiT），图文 token 联合建模，文字渲染能力大幅提升

#### FLUX.1
- **作者：** Black Forest Labs（SD 原班人马）
- **发表：** 2024
- **模型：** https://huggingface.co/black-forest-labs/FLUX.1-dev
- **摘要：** ★★ 当前最强开源图像生成模型，混合架构（并行 DiT + 串行 DiT），图像质量和文字渲染超越 SD3

### 🔧 个性化微调

#### DreamBooth: Fine Tuning Text-to-Image Diffusion Models for Subject-Driven Generation
- **作者：** Ruiz et al.（Google）
- **发表：** CVPR 2023
- **论文：** https://arxiv.org/abs/2208.12242
- **摘要：** 用 3-5 张图像微调模型，使其学会特定主题（如你的脸/物品）的生成

#### LoRA: Low-Rank Adaptation of Large Language Models（用于图像模型）
- **论文：** https://arxiv.org/abs/2106.09685
- **摘要：** 低秩矩阵分解微调，参数量极小（~4MB）却效果好；SD 生态中最流行的个性化方案，civitai 上有数万个 LoRA

---

## 视频生成核心论文

### 🎬 开山之作

#### Video Diffusion Models
- **作者：** Ho et al.（Google Brain）
- **发表：** NeurIPS 2022
- **论文：** https://arxiv.org/abs/2204.03458
- **摘要：** 首个将 Diffusion 扩展到视频生成的工作，引入 3D U-Net（空间+时间注意力）

#### AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models
- **作者：** Guo et al.
- **发表：** ICLR 2024
- **论文：** https://arxiv.org/abs/2307.04725
- **代码：** https://github.com/guoyww/AnimateDiff
- **摘要：** ★ 在现有图像 SD 模型上插入运动模块，无需重训即可生成视频；开源后成为视频生成的基础框架

### 🚀 里程碑模型

#### Sora: Video generation models as world simulators
- **作者：** OpenAI
- **发表：** 2024.02 技术报告
- **报告：** https://openai.com/research/video-generation-models-as-world-simulators
- **摘要：** ★★ 用 Spacetime Patch（时空 patch）+ DiT 实现高质量长视频生成；首次展示视频生成模型具备"世界模拟"能力；架构基于 DiT，在压缩的时空潜空间中操作

#### CogVideoX
- **作者：** 智谱 AI
- **发表：** 2024
- **论文：** https://arxiv.org/abs/2408.06072
- **代码：** https://github.com/THUDM/CogVideo
- **摘要：** 开源视频生成模型，支持文生视频和图生视频，5B/2B 参数版本

#### Wan2.1
- **作者：** 阿里巴巴
- **发表：** 2025
- **论文：** https://arxiv.org/abs/2503.20314
- **代码：** https://github.com/Wan-Video/Wan2.1
- **摘要：** ★★ 当前最强开源视频生成模型，14B 参数，支持文生视频/图生视频/视频编辑；在多个 benchmark 超越闭源模型

#### Stable Video Diffusion（SVD）
- **作者：** Stability AI
- **发表：** 2023
- **论文：** https://arxiv.org/abs/2311.15127
- **代码：** https://github.com/Stability-AI/generative-models
- **摘要：** 开源图生视频模型，从静态图像生成短视频片段

---

## 图像生成路线速览

| 阶段 | 代表模型 | 关键变化 |
|------|----------|----------|
| Early text-to-image | DALL·E, GLIDE | 文本条件生成初步成型 |
| Diffusion scaling | Imagen, DALL·E 2 | 语言模型文本编码器 + diffusion |
| Open ecosystem | Stable Diffusion, LDM | latent diffusion 让消费级 GPU 可用 |
| Control ecosystem | ControlNet, IP-Adapter, LoRA, DreamBooth | 控制、个性化和社区生态爆发 |
| High-res / composition | SDXL | 更高分辨率、更好构图和风格 |
| DiT / Flow era | SD3, FLUX | Transformer backbone、flow matching、文字渲染增强 |

图像生成学习重点：

- prompt following 与文本渲染；
- subject consistency 和 personalization；
- inpainting / editing / controllable generation；
- LoRA、ControlNet、IP-Adapter 的工程生态；
- 采样速度、显存和部署成本。

---

## 视频生成关键问题

视频生成不是简单地逐帧生成图像，核心挑战包括：

| 问题 | 说明 |
|------|------|
| Temporal Consistency | 同一角色、物体、背景在多帧中保持一致 |
| Motion Control | 控制运动方向、速度、动作和镜头 |
| Long Video Memory | 长视频中保持世界状态和因果连续性 |
| Camera Control | 推拉摇移、视角变化、景深和构图 |
| Multimodal Conditioning | 文本、图像、音频、姿态、轨迹等条件融合 |
| Cost | 时空 token 多，训练和推理显存成本极高 |
| Evaluation | 人眼敏感但指标不完善，benchmark 仍不稳定 |

实践判断视频模型时，至少看：

```text
prompt following
+ motion realism
+ identity consistency
+ object permanence
+ camera controllability
+ temporal flicker
+ inference cost
```

---

## 评估指标

| 指标 / Benchmark | 用途 | 局限 |
|------------------|------|------|
| FID | 图像质量和分布距离 | 不评估 prompt following |
| IS | 图像分类置信度 | 信息有限，现代文生图较少单独使用 |
| CLIPScore | 图文一致性 | CLIP 偏差不等于人类偏好 |
| Aesthetic Score | 美学质量估计 | 容易风格偏置 |
| FVD | 视频分布质量 | 对局部错误和文本遵循不敏感 |
| VBench | 视频多维评测 | 仍需人工评估补充 |
| T2VBench | 文生视频评测 | 覆盖有限，易被 benchmark 优化 |
| Human Preference | 最贴近真实感受 | 昂贵、慢、重复性差 |

建议评估报告同时写：质量、文本遵循、运动一致性、可控性、安全、速度和成本。

---

## 实践 Checklist

| 任务 | 建议记录 |
|------|----------|
| 文生图 | prompt、negative prompt、seed、steps、CFG、sampler、分辨率 |
| 图生图 / 编辑 | strength、mask、参考图、ControlNet 条件 |
| LoRA / DreamBooth | 数据量、caption 质量、rank、学习率、过拟合样例 |
| 视频生成 | fps、帧数、分辨率、motion bucket、camera prompt、显存 |
| 模型对比 | 同 prompt、同 seed、同分辨率、同预算 |

---

## 教程与博客

### 图像生成

- **The Illustrated Stable Diffusion（Jay Alammar，强烈推荐）**
  https://jalammar.github.io/illustrated-stable-diffusion/
  ★ 图文并茂讲透 SD 全流程，是最好的 SD 入门文章

- **How Stable Diffusion Works（Andrej Karpathy 推荐过）**
  https://mccormickml.com/2022/12/21/how-stable-diffusion-works/

- **Lilian Weng - What are Diffusion Models?**
  https://lilianweng.github.io/posts/2021-07-11-diffusion-models/

- **DiT 论文精读（Yannic Kilcher）**
  https://www.youtube.com/watch?v=wIIBN2ao4v0

- **Flux.1 架构解析**
  https://blackforestlabs.ai/announcing-black-forest-labs/

### 视频生成

- **Sora 技术报告原文**
  https://openai.com/research/video-generation-models-as-world-simulators

- **Sora 架构深度解析（AK）**
  https://arxiv.org/abs/2402.17177

- **生成视频综述（2024）**
  https://arxiv.org/abs/2405.05711

### 视频课程

- **Stanford CS236 - Deep Generative Models**
  https://deepgenerativemodels.github.io/
  含完整 Diffusion + 条件生成章节

- **Hugging Face Diffusion Models Course（免费）**
  https://huggingface.co/learn/diffusion-course/unit0/1
  ★ 实操性最强，含 Colab notebook，适合快速上手

---

## 代码实践

### 图像生成上手路径

1. **Hugging Face Diffusers 库（最推荐）**
   - 文档：https://huggingface.co/docs/diffusers/index
   - 支持 SD、FLUX、ControlNet、IP-Adapter 等一键调用
   ```python
   from diffusers import StableDiffusionPipeline
   pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
   image = pipe("a photo of an astronaut riding a horse").images[0]
   ```

2. **ComfyUI（节点式工作流，适合实验）**
   - https://github.com/comfyanonymous/ComfyUI
   - 可视化拼接 SD/FLUX/ControlNet 等模块

3. **FLUX.1 快速体验**
   - Hugging Face Space：https://huggingface.co/spaces/black-forest-labs/FLUX.1-schnell
   - 本地部署：https://github.com/black-forest-labs/flux

4. **ControlNet 实践**
   - 官方示例：https://github.com/lllyasviel/ControlNet

### 视频生成上手路径

1. **CogVideoX 本地运行**
   - https://github.com/THUDM/CogVideo
   - 2B 版本单卡 24G 可运行

2. **Wan2.1 本地运行**
   - https://github.com/Wan-Video/Wan2.1
   - 1.3B 版本约 8G 显存可运行

3. **AnimateDiff + ComfyUI**
   - 最成熟的开源视频生成工作流
   - 教程：https://civitai.com/articles/2056

---

## 关键技术对比

### 图像生成骨干：U-Net vs DiT

| 维度 | U-Net（SD1.x/2.x） | DiT（SD3/Flux/Sora） |
|------|-------------------|---------------------|
| 架构 | 卷积 + 注意力 | 纯 Transformer |
| 扩展性 | 一般 | 强（遵循 Scaling Law） |
| 训练效率 | 高 | 需要更多数据 |
| 生成质量 | 好 | **更好** |
| 文字渲染 | 差 | **明显更好** |
| 开源生态 | 非常成熟 | 快速成长 |

### 主流文生图模型对比（2024-2025）

| 模型 | 开源 | 特点 | 推荐场景 |
|------|------|------|---------|
| FLUX.1-dev | ✅ | 当前开源最强，细节丰富 | 本地高质量生成 |
| FLUX.1-schnell | ✅ | 4步快速版 | 快速原型 |
| SD XL | ✅ | 生态最丰富，LoRA多 | 定制化场景 |
| SD 3.5 | ✅ | 文字渲染好 | 含文字的图像 |
| DALL-E 3 | ❌ | 文本理解最强 | API 调用 |
| Midjourney v6 | ❌ | 艺术风格最佳 | 艺术创作 |
| Imagen 3 | ❌ | 细节质量顶级 | Google Gemini内置 |

---

## 评估指标

| 指标 | 说明 | 越好 |
|------|------|------|
| FID | 生成图与真实图分布距离 | 越低越好 |
| CLIP Score | 图文匹配度 | 越高越好 |
| IS（Inception Score） | 生成质量与多样性 | 越高越好 |
| Human Eval | 人工评分（最终标准） | 越高越好 |
| VBench | 视频生成专用综合评测 | 越高越好 |

---

## 推荐学习顺序

### 图像生成
1. **读** Jay Alammar 的 Illustrated Stable Diffusion
2. **跑** Hugging Face Diffusers 官方教程（Colab）
3. **玩** ComfyUI + FLUX.1，感受现代工作流
4. **读** LDM 论文（理解潜空间设计）
5. **读** DiT 论文（理解新骨干为何更强）
6. **深入** ControlNet / IP-Adapter（精细控制）

### 视频生成
1. **读** Sora 技术报告（建立直觉）
2. **跑** CogVideoX 或 Wan2.1（本地体验）
3. **读** AnimateDiff 论文（理解图→视频迁移思路）
4. **思考** 时序一致性如何建模（核心挑战）

---

*资料整理：Lovely | 更新时间：2026-03-27 | 仅含外网资料*

---

## 前沿补充清单

更易变化的前沿补充条目已拆分到 [图像 / 视频生成前沿补充清单](image-video-generation-frontier-appendix.md)，包括：

- DiT / SD3 / FLUX / PixArt；
- Sora / Veo / Movie Gen / CogVideoX / Wan；
- autoregressive image tokens、flow matching、consistency / LCM 等范式对比；
- DALL-E 1、Parti、Muse、VAR、VideoPoet 等补充路线。

---

## 高质量外部引用

| 方向 | 资料 | 类型 | 链接 |
|------|------|------|------|
| Diffusion 基础 | DDPM / DDIM / Score SDE | 论文 | https://arxiv.org/abs/2006.11239 / https://arxiv.org/abs/2010.02502 / https://arxiv.org/abs/2011.13456 |
| Latent Diffusion | LDM / Stable Diffusion | 论文 / 代码 | https://arxiv.org/abs/2112.10752 / https://github.com/CompVis/latent-diffusion |
| 条件控制 | ControlNet / IP-Adapter | 论文 / 代码 | https://arxiv.org/abs/2302.05543 / https://github.com/tencent-ailab/IP-Adapter |
| DiT 主线 | DiT / SD3 | 论文 | https://arxiv.org/abs/2212.09748 / https://arxiv.org/abs/2403.03206 |
| FLUX | Black Forest Labs / Diffusers | 官方资料 | https://blackforestlabs.ai/announcing-black-forest-labs/ / https://huggingface.co/docs/diffusers/api/pipelines/flux |
| 视频生成 | Sora / Movie Gen / CogVideoX / Wan | 技术报告 / 代码 | https://openai.com/index/video-generation-models-as-world-simulators/ / https://ai.meta.com/research/movie-gen/ / https://github.com/THUDM/CogVideo / https://github.com/Wan-Video/Wan2.1 |
| 生成评估 | VBench | 论文 / 代码 | https://arxiv.org/abs/2311.17982 / https://github.com/Vchitect/VBench |

---

## Freshness

| 字段 | 内容 |
|------|------|
| 最后审阅 | 2026-06 |
| 更新频率 | 每季度 |
| 过时风险 | 高 |
| 维护重点 | DiT / Flow、视频生成模型、VBench/T2VBench、开源权重和推理成本 |
