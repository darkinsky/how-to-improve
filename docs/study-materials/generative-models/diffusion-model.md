# Diffusion Model 扩散模型 学习计划与资料汇总

> 整理时间：2026-03-27
> 目标：系统掌握扩散模型（Diffusion Models）的理论基础、核心变体、实现方法及前沿应用
> 前置推荐：先完成 AE & VAE 学习，理解隐空间与生成模型基础

---

## 知识地图

```
扩散模型（Diffusion Models）
    ├── 理论基础
    │       ├── 非平衡热力学（物理启发）
    │       ├── 马尔可夫链（前向加噪过程）
    │       ├── 变分推断（反向去噪过程）
    │       └── Score Matching（分数匹配）
    ├── 核心模型
    │       ├── DDPM（去噪扩散概率模型）
    │       ├── DDIM（隐式扩散，加速采样）
    │       ├── Score-Based / SDE（随机微分方程）
    │       └── Consistency Models（一步生成）
    ├── 条件生成
    │       ├── Classifier Guidance（分类器引导）
    │       ├── Classifier-Free Guidance（无分类器引导，CFG）
    │       └── ControlNet / IP-Adapter（精细控制）
    ├── 骨干架构
    │       ├── U-Net（主流去噪网络）
    │       └── DiT（Diffusion Transformer）
    └── 代表应用
            ├── 图像生成（Stable Diffusion, DALL-E 2, Imagen）
            ├── 视频生成（Sora, Stable Video Diffusion）
            └── 音频/3D/分子生成
```

---

## 核心论文（必读）

### 第一阶段：理论奠基

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| Deep Unsupervised Learning using Nonequilibrium Thermodynamics | Sohl-Dickstein et al. | 2015 | [ICML 2015](https://arxiv.org/abs/1503.03585) | 扩散模型最早起源，用热力学原理建模 |
| **Denoising Diffusion Probabilistic Models (DDPM)** | Ho et al. | 2020 | [arXiv:2006.11239](https://arxiv.org/abs/2006.11239) | DDPM 奠基作，现代扩散模型基础 |
| Generative Modeling by Estimating Gradients (NCSN) | Song & Ermon | 2019 | [NeurIPS 2019](https://arxiv.org/abs/1907.05600) | Score-based 生成，噪声条件分数网络 |
| Score-Based Generative Modeling through SDEs | Song et al. | 2020 | [ICLR 2021](https://arxiv.org/abs/2011.13456) | 统一 DDPM 与 Score-based，SDE 框架 |

### 第二阶段：加速采样

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **Denoising Diffusion Implicit Models (DDIM)** | Song et al. | 2020 | [arXiv:2010.02502](https://arxiv.org/abs/2010.02502) | 非马尔可夫过程，大幅加速推理（10-50x） |
| Improved DDPM | Nichol & Dhariwal | 2021 | [ICML 2021](https://arxiv.org/abs/2102.09672) | 改进噪声调度与模型架构 |
| Consistency Models | Song et al. | 2023 | [arXiv:2303.01469](https://arxiv.org/abs/2303.01469) | 一步或少步生成，蒸馏扩散模型 |

### 第三阶段：条件生成与控制

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **Diffusion Models Beat GANs** | Dhariwal & Nichol | 2021 | [arXiv:2105.05233](https://arxiv.org/abs/2105.05233) | Classifier Guidance，扩散模型超越 GAN |
| Classifier-Free Diffusion Guidance | Ho & Salimans | 2022 | [arXiv:2207.12598](https://arxiv.org/abs/2207.12598) | CFG（无分类器引导），现代文生图标配 |
| **Latent Diffusion Models (LDM)** | Rombach et al. | 2022 | [CVPR 2022](https://arxiv.org/abs/2112.10752) | Stable Diffusion 基础，隐空间扩散 |
| GLIDE | Nichol et al. | 2021 | [arXiv:2112.10741](https://arxiv.org/abs/2112.10741) | 文本引导图像生成 |
| ControlNet | Zhang et al. | 2023 | [ICCV 2023](https://arxiv.org/abs/2302.05543) | 精细条件控制（边缘、姿态、深度等） |

### 第四阶段：架构演进

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| **Scalable Diffusion Models with Transformers (DiT)** | Peebles & Xie | 2022 | [arXiv:2212.09748](https://arxiv.org/abs/2212.09748) | 用 Transformer 替换 U-Net，可扩展性强 |
| U-Net Architecture | Ronneberger et al. | 2015 | [MICCAI 2015](https://arxiv.org/abs/1505.04597) | U-Net 原始论文，扩散模型去噪骨干 |

### 第五阶段：前沿应用

| 论文 | 作者 | 年份 | 链接 | 核心贡献 |
|------|------|------|------|----------|
| DALL-E 2 (unCLIP) | Ramesh et al. | 2022 | [arXiv:2204.06125](https://arxiv.org/abs/2204.06125) | OpenAI 文生图，CLIP + 扩散模型 |
| Imagen | Saharia et al. | 2022 | [arXiv:2205.11487](https://arxiv.org/abs/2205.11487) | Google 文生图，大语言模型 + 扩散 |
| Stable Video Diffusion | Blattmann et al. | 2023 | [arXiv:2311.15127](https://arxiv.org/abs/2311.15127) | 视频生成扩散模型 |
| Flow Matching | Lipman et al. | 2022 | [arXiv:2210.02747](https://arxiv.org/abs/2210.02747) | 更简单的训练目标，新兴主流方向 |

---

## 课程推荐

### 入门课程

| 课程 | 平台 | 说明 |
|------|------|------|
| **Diffusion Models from Scratch** | fast.ai | 从零实现扩散模型，代码驱动 |
| MIT 6.S191: Generative Models | MIT | 含 Diffusion 专题，免费公开课 |
| CS236: Deep Generative Models | Stanford | 覆盖 DDPM、Score-based、Flow 全系列 |
| 动手学深度学习（d2l.ai）生成模型章节 | - | 中文权威教材 |

### 进阶课程 / 讲座

| 课程 | 平台 | 说明 |
|------|------|------|
| Diffusion Models: Theory to Application | CVPR/NeurIPS Tutorial | 顶会 Tutorial，系统全面 |
| Score-Based Generative Modeling | Yang Song 博客 | Score matching 权威讲解 |

---

## 博客与技术文章

| 文章 | 作者 | 链接 | 亮点 |
|------|------|------|------|
| **What are Diffusion Models?** | Lilian Weng (OpenAI) | [lilianweng.github.io](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) | 最全面的扩散模型综述博客，必读 |
| **Generative Modeling by Estimating Gradients** | Yang Song | [yang-song.github.io/blog/2021/score](https://yang-song.github.io/blog/2021/score/) | Score-based 模型作者亲写，权威直觉讲解 |
| The Illustrated Stable Diffusion | Jay Alammar | [jalammar.github.io](https://jalammar.github.io/illustrated-stable-diffusion/) | 图解 Stable Diffusion，超直观 |
| How Diffusion Models Work | DeepLearning.AI | [deeplearning.ai](https://www.deeplearning.ai/short-courses/how-diffusion-models-work/) | 短课程，含代码，1-2小时上手 |
| Annotated Diffusion | Hugging Face | [huggingface.co/blog/annotated-diffusion](https://huggingface.co/blog/annotated-diffusion) | 逐行注释 DDPM 代码，极佳实践参考 |

---

## 实践代码资源

| 资源 | 链接 | 说明 |
|------|------|------|
| DDPM 官方实现 | [github.com/hojonathanho/diffusion](https://github.com/hojonathanho/diffusion) | Ho et al. 原始 TensorFlow 代码 |
| Improved DDPM（PyTorch）| [github.com/openai/improved-diffusion](https://github.com/openai/improved-diffusion) | OpenAI 官方 PyTorch 版本 |
| Hugging Face Diffusers | [github.com/huggingface/diffusers](https://github.com/huggingface/diffusers) | 工业级扩散模型库，支持多种模型 |
| Stable Diffusion | [github.com/CompVis/stable-diffusion](https://github.com/CompVis/stable-diffusion) | Stable Diffusion 官方实现 |
| Annotated Diffusion（可运行）| [colab 链接](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/annotated_diffusion.ipynb) | Hugging Face 注释版，Colab 可直接运行 |
| DiT 官方代码 | [github.com/facebookresearch/DiT](https://github.com/facebookresearch/DiT) | Meta DiT 官方实现 |

---

## 学习计划（6 周）

> 前置：已完成 AE & VAE 学习，理解隐空间、ELBO、KL 散度

### 第一周：核心原理建立

**目标**：理解扩散模型的物理直觉与数学基础

- [ ] 阅读 Lilian Weng 博客《What are Diffusion Models?》
- [ ] 理解前向过程：逐步加噪（x0 -> xT，高斯噪声 Markov 链）
- [ ] 理解反向过程：神经网络预测噪声，逐步去噪
- [ ] 精读 DDPM 论文（Ho et al. 2020），理解训练目标
- [ ] 核心公式：噪声预测损失 = ||eps - eps_theta(x_t, t)||^2

**检验**：能用白板画出扩散模型的前向/反向过程，解释为什么要预测噪声而不是直接预测 x0

---

### 第二周：DDPM 代码实战

**目标**：从头实现 DDPM 并跑通实验

- [ ] 阅读 Hugging Face《Annotated Diffusion》逐行注释版
- [ ] 在 MNIST / CIFAR-10 上实现并训练 DDPM
- [ ] 理解 noise schedule（线性 vs cosine）
- [ ] 可视化去噪过程（T 步逆扩散动画）
- [ ] 使用 Hugging Face Diffusers 快速体验高质量生成

**检验**：能生成清晰样本，理解 timestep embedding 的作用

---

### 第三周：加速采样与 DDIM

**目标**：理解推理加速方案

- [ ] 精读 DDIM 论文（Song et al. 2020）
- [ ] 理解非马尔可夫过程与确定性采样
- [ ] 实验：对比 DDPM（1000步）与 DDIM（50步）的速度与质量
- [ ] 了解 Consistency Models 的蒸馏思路
- [ ] 了解 DPM-Solver 等高阶 ODE 求解器

**检验**：能解释 DDIM 为何比 DDPM 快，理解 eta 参数的含义

---

### 第四周：条件生成与控制

**目标**：掌握文本/图像条件引导生成

- [ ] 理解 Classifier Guidance（梯度引导采样）
- [ ] 精读 CFG 论文，理解无分类器引导的实现原理
- [ ] 阅读 LDM 论文（Stable Diffusion 基础），理解隐空间扩散
- [ ] 了解 ControlNet 如何实现精细空间控制
- [ ] 实践：用 Diffusers 做文生图 + 调整 CFG scale 观察效果

**检验**：能解释 guidance_scale 参数对生成效果的影响

---

### 第五周：架构进阶——DiT 与 Flow Matching

**目标**：了解扩散模型的架构演进方向

- [ ] 精读 DiT 论文（Peebles & Xie 2022）
- [ ] 理解为何 Transformer 在扩散模型中可替代 U-Net
- [ ] 了解 Flow Matching 与扩散模型的关系（更简单的训练目标）
- [ ] 了解 Sora、SD3、FLUX 等前沿模型的架构选择

**检验**：能对比 U-Net 和 DiT 的优劣，解释 DiT 的 scalability

---

### 第六周：综合实践与专题深入

**目标**：在感兴趣方向做深度实践

- [ ] 选择一个专题（任选）：
  - 图像编辑（SDEdit、Prompt2Prompt、InstructPix2Pix）
  - 视频生成（Stable Video Diffusion）
  - 推理加速（量化 + 步数减少）
  - 医学/科学应用（分子生成、蛋白质设计）
- [ ] 输出：技术博客 or 代码 demo
- [ ] 更新此文档，补充实践心得

---

## 学习建议

1. **先看 Lilian Weng 博客，再读论文**：博客能建立直觉，论文补充细节
2. **DDPM 和 DDIM 是基石**：理解这两篇，后续所有变体都好理解
3. **动手跑 Annotated Diffusion**：注释版代码 = 最好的教材
4. **关注 CFG**：几乎所有现代文生图都用 CFG，务必理解
5. **对比 VAE vs Diffusion**：两者都做生成，理解差异有助于加深认知

---

## 快速参考

| 概念 | 简要说明 |
|------|----------|
| Forward Process | 前向加噪：x0 逐步加高斯噪声到 xT（纯噪声） |
| Reverse Process | 反向去噪：神经网络预测噪声，从 xT 恢复 x0 |
| Noise Schedule | 每个时间步的加噪强度曲线（线性/cosine） |
| Timestep Embedding | 将时间步 t 编码为向量，输入去噪网络 |
| DDPM | 马尔可夫链扩散，1000步采样，质量高但慢 |
| DDIM | 非马尔可夫，50步可达相近质量，速度快 |
| CFG | Classifier-Free Guidance，scale 越大生成越贴近条件 |
| LDM | 在 VAE 压缩的隐空间做扩散，节省计算量 |
| Score Function | 数据分布对数概率的梯度，等价于扩散模型的去噪方向 |
| DiT | 用 Transformer 替代 U-Net 的扩散模型骨干 |

---

*文档由 OpenClaw AI 助手整理生成，持续更新中*
