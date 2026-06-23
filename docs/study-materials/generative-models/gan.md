# GAN（生成对抗网络）学习计划与资料汇总

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 基础 / 论文路线 |
| 难度 | 中级 |
| 优先级 | P1 / Classic |
| 状态 | 可用 |
| 建议用途 | 理解对抗式生成建模和训练问题 |

---

> 整理时间：2026-03-27
> 目标：系统掌握 GAN 的理论基础、核心变体、训练技巧及前沿应用
> 前置推荐：先完成 AE & VAE 学习，理解生成模型基础与隐空间概念

---

## 先看结论

- GAN 的历史价值很高：它定义了对抗式生成建模，并推动了高保真图像生成、图像翻译和人脸生成。
- 但在现代基础生成模型主线上，GAN 已经不是图像 / 视频生成的主力；Diffusion、Flow Matching、DiT 更值得优先投入。
- 学 GAN 的重点是理解 generator / discriminator 的博弈、mode collapse、训练不稳定、Wasserstein 距离和 FID。
- StyleGAN 系列仍然是理解 latent editing、高质量人脸生成和生成模型可控性的经典材料。
- 如果时间有限，建议只学原始 GAN、DCGAN、WGAN-GP、Pix2Pix / CycleGAN、StyleGAN2。
- 完成标准：能实现一个 DCGAN 或 WGAN-GP，并解释为什么 GAN 难训练、为什么 Diffusion 后来成为主线。

---

## 知识地图

```
GAN（生成对抗网络）
    ├── 理论基础
    │       ├── 对抗博弈（Generator vs Discriminator）
    │       ├── 极小极大目标函数（Minimax Loss）
    │       ├── JS 散度 / Wasserstein 距离
    │       └── 纳什均衡（Nash Equilibrium）
    ├── 核心变体
    │       ├── DCGAN（卷积结构）
    │       ├── WGAN / WGAN-GP（稳定训练）
    │       ├── cGAN（条件生成）
    │       ├── Pix2Pix（图像翻译）
    │       ├── CycleGAN（非配对图像翻译）
    │       ├── StyleGAN / StyleGAN2 / StyleGAN3（高质量人脸）
    │       └── BigGAN（大规模类别条件生成）
    ├── 训练挑战
    │       ├── 模式崩塌（Mode Collapse）
    │       ├── 训练不稳定（梯度消失/爆炸）
    │       └── 评估困难（IS、FID 指标）
    └── 应用领域
            ├── 图像生成与超分辨率
            ├── 风格迁移
            ├── 数据增强
            ├── 人脸编辑 / Deepfake
            └── 视频生成
```

---

## 学习路线

| 阶段 | 内容 | 建议时长 |
|------|------|---------|
| 第一阶段 | 原始 GAN 论文 + 直觉理解 | 1周 |
| 第二阶段 | DCGAN / WGAN，动手实现 | 1周 |
| 第三阶段 | 条件 GAN：cGAN / Pix2Pix / CycleGAN | 1-2周 |
| 第四阶段 | StyleGAN 系列，深入理解 | 1-2周 |
| 第五阶段 | 评估指标 + 实际项目 | 持续 |

---

## 核心论文（按时间顺序）

### 🏛️ 奠基之作

#### Generative Adversarial Nets（原始 GAN）
- **作者：** Ian Goodfellow et al.
- **发表：** NeurIPS 2014
- **论文：** https://arxiv.org/abs/1406.2661
- **摘要：** GAN 的开山之作，提出生成器与判别器对抗训练框架

#### DCGAN（Deep Convolutional GAN）
- **作者：** Radford et al.
- **发表：** ICLR 2016
- **论文：** https://arxiv.org/abs/1511.06434
- **摘要：** 将卷积网络引入 GAN，使图像生成质量大幅提升，是入门必读

### ⚙️ 训练稳定性改进

#### WGAN（Wasserstein GAN）
- **作者：** Arjovsky et al.
- **发表：** ICML 2017
- **论文：** https://arxiv.org/abs/1701.07875
- **摘要：** 用 Wasserstein 距离替代 JS 散度，从理论上解决梯度消失和训练不稳定问题

#### WGAN-GP（Gradient Penalty）
- **作者：** Gulrajani et al.
- **发表：** NeurIPS 2017
- **论文：** https://arxiv.org/abs/1704.00028
- **摘要：** 对 WGAN 的 weight clipping 改进为梯度惩罚，训练更稳定

#### Spectral Normalization for GAN
- **作者：** Miyato et al.
- **发表：** ICLR 2018
- **论文：** https://arxiv.org/abs/1802.05957
- **摘要：** 通过谱归一化约束判别器 Lipschitz 条件，简单有效

### 🎨 条件生成与图像翻译

#### cGAN（Conditional GAN）
- **作者：** Mirza & Osindero
- **发表：** 2014
- **论文：** https://arxiv.org/abs/1411.1784
- **摘要：** 在生成器和判别器中引入条件标签，实现可控生成

#### Pix2Pix（Image-to-Image Translation）
- **作者：** Isola et al.
- **发表：** CVPR 2017
- **论文：** https://arxiv.org/abs/1611.07004
- **项目：** https://phillipi.github.io/pix2pix/
- **摘要：** 配对图像翻译的经典框架，如草图→照片、白天→夜晚

#### CycleGAN（Unpaired Image-to-Image Translation）
- **作者：** Zhu et al.
- **发表：** ICCV 2017
- **论文：** https://arxiv.org/abs/1703.10593
- **项目：** https://junyanz.github.io/CycleGAN/
- **摘要：** 非配对图像翻译，引入循环一致性损失，如马→斑马

### 🌟 高质量生成（StyleGAN 系列）

#### StyleGAN
- **作者：** Karras et al.（NVIDIA）
- **发表：** CVPR 2019
- **论文：** https://arxiv.org/abs/1812.04948
- **代码：** https://github.com/NVlabs/stylegan
- **摘要：** 基于风格的生成架构，AdaIN 注入风格，逐层可控，生成超真实人脸

#### StyleGAN2
- **作者：** Karras et al.（NVIDIA）
- **发表：** CVPR 2020
- **论文：** https://arxiv.org/abs/1912.04958
- **代码：** https://github.com/NVlabs/stylegan2
- **摘要：** 去除水珠伪影，改进归一化设计，目前仍是 GAN 质量基准

#### StyleGAN3（Alias-Free GAN）
- **作者：** Karras et al.（NVIDIA）
- **发表：** NeurIPS 2021
- **论文：** https://arxiv.org/abs/2106.12423
- **代码：** https://github.com/NVlabs/stylegan3
- **摘要：** 解决平移/旋转对齐问题，适合视频生成

### 📈 大规模生成

#### BigGAN
- **作者：** Brock et al.（DeepMind）
- **发表：** ICLR 2019
- **论文：** https://arxiv.org/abs/1809.11096
- **摘要：** 大 batch + 类别条件生成，ImageNet 1000 类高质量生成

#### ProGAN（Progressive Growing of GANs）
- **作者：** Karras et al.（NVIDIA）
- **发表：** ICLR 2018
- **论文：** https://arxiv.org/abs/1710.10196
- **摘要：** 渐进式生长训练，从低分辨率逐步提升，首个高质量 1024×1024 人脸生成

---

## 经典教程与博客

### 入门教程

- **PyTorch 官方 DCGAN 教程**
  https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
  ★ 最推荐的上手教程，代码清晰，可直接运行

- **Lilian Weng - From GAN to WGAN（强烈推荐）**
  https://lilianweng.github.io/posts/2017-08-20-gan/
  ★ 深入浅出讲透 GAN 理论与训练技巧，Lilian Weng 是 OpenAI 前研究员

- **GANs in 50 lines of code（Medium）**
  https://medium.com/@devnag/generative-adversarial-networks-gans-in-50-lines-of-code-pytorch-e81b79659e3f

- **GAN — How does it work?（Towards Data Science）**
  https://towardsdatascience.com/generative-adversarial-network-gan-for-dummies-a-step-by-step-tutorial-81dfd8f5db5f

### 深入技术博客

- **The GAN Zoo（所有 GAN 变体列表）**
  https://github.com/hindupuravinash/the-gan-zoo
  ★ 收录了 500+ GAN 变体，当"GAN 百科全书"用

- **StyleGAN 解析（distill.pub 风格）**
  https://towardsdatascience.com/explained-a-style-based-generator-architecture-for-gans-generating-and-tuning-realistic-6cb2be0f431

- **GAN 训练技巧大全（ganhacks）**
  https://github.com/soumith/ganhacks
  ★ Soumith Chintala（PyTorch 作者之一）整理的 GAN 训练 Tips

- **Lilian Weng - GAN for NLP**
  https://lilianweng.github.io/posts/2021-01-02-controllable-text-generation/

### 视频课程

- **Andrew Ng - DeepLearning.AI GANs Specialization（Coursera）**
  https://www.coursera.org/specializations/generative-adversarial-networks-gans
  共 3 门课，从基础到 StyleGAN，附配套 Colab notebook

- **MIT 6.S191 - Deep Learning（含 GAN 章节）**
  https://introtodeeplearning.com/
  ★ 免费，每年更新，2024版有 GAN + Diffusion 对比讲解

- **Fast.ai - Practical Deep Learning（Part 2 含生成模型）**
  https://course.fast.ai/

---

## 代码实践

### 上手项目（推荐顺序）

1. **从零实现 DCGAN（MNIST / CelebA）**
   - PyTorch 官方教程：https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html
   - TensorFlow 版：https://www.tensorflow.org/tutorials/generative/dcgan

2. **CycleGAN 实现（马→斑马）**
   - 官方 PyTorch 代码：https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix
   - ★ 代码质量很高，值得精读

3. **StyleGAN2 微调（自定义数据集）**
   - Roboflow 教程：https://blog.roboflow.com/how-to-train-stylegan2/
   - StyleGAN2-ADA（少样本训练）：https://github.com/NVlabs/stylegan2-ada-pytorch

### GAN 框架与工具库

| 工具 | 说明 | 链接 |
|------|------|------|
| pytorch-fid | 计算 FID 评估指标 | https://github.com/mseitzer/pytorch-fid |
| clean-fid | 更准确的 FID 实现 | https://github.com/GaParmar/clean-fid |
| StyleGAN2-ADA | 少样本 StyleGAN | https://github.com/NVlabs/stylegan2-ada-pytorch |
| GAN Zoo | 500+ GAN 变体汇总 | https://github.com/hindupuravinash/the-gan-zoo |

---

## 评估指标

| 指标 | 全称 | 说明 |
|------|------|------|
| IS | Inception Score | 衡量生成图像质量与多样性，越高越好 |
| FID | Frechet Inception Distance | 衡量生成分布与真实分布距离，越低越好 |
| LPIPS | Learned Perceptual Similarity | 感知相似度，越低越好 |
| PPL | Perceptual Path Length | StyleGAN 专用，衡量隐空间平滑度 |

> **FID 是目前最主流的 GAN 评估指标**，几乎所有论文都汇报此指标。

---

## GAN vs Diffusion：现状与选择

| 场景 | 推荐 | 原因 |
|------|------|------|
| 需要快速推理（实时应用） | GAN | 单次前向传播，ms 级 |
| 最高图像质量 | Diffusion | SOTA 指标更好 |
| 图像编辑 / 风格迁移 | GAN（CycleGAN、StyleGAN） | 隐空间更易操控 |
| 文本生成图像 | Diffusion | Stable Diffusion 生态更成熟 |
| 数据增强 | GAN | 轻量快速 |
| 视频生成 | 两者都在快速发展 | - |

> GAN 并没有"死"，在推理速度要求高、隐空间可控性强的场景下仍是首选。

---

## 推荐学习顺序

1. **看** 原始 GAN 论文（Goodfellow 2014），理解对抗思想
2. **读** Lilian Weng 的 From GAN to WGAN 博客
3. **做** PyTorch DCGAN 官方教程
4. **理解** WGAN-GP（为什么训练不稳定？如何解决？）
5. **玩** CycleGAN 官方代码（图像翻译非常有趣）
6. **深入** StyleGAN2 论文 + 微调实验
7. **评估** 用 FID 定量比较你的模型

---

*资料整理：Lovely | 更新时间：2026-03-27 | 仅含外网资料*
