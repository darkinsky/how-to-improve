# Flow Matching 学习计划与资料汇总

> 整理时间：2026-03-27
> 目标：系统掌握 Flow Matching 的理论基础、与 Diffusion 的关系、核心变体及工业应用
> 前置推荐：先了解 Diffusion Model 基础（DDPM/DDIM），理解去噪生成过程；了解常微分方程（ODE）基本概念

---

## 知识地图

```
Flow Matching
    ├── 理论基础
    │       ├── 连续归一化流（CNF / Neural ODE）
    │       ├── 概率路径（Probability Path）
    │       ├── 速度场（Velocity Field）学习
    │       └── 最优传输（Optimal Transport）
    ├── 核心算法
    │       ├── Flow Matching（FM，Lipman et al. 2022）
    │       ├── Conditional Flow Matching（CFM）
    │       ├── Rectified Flow（刘宇等，2022）
    │       └── Stochastic Interpolants
    ├── 与 Diffusion 的关系
    │       ├── Score Matching vs Flow Matching
    │       ├── SDE（随机）vs ODE（确定）路径
    │       └── 统一框架视角
    └── 工业应用
            ├── FLUX.1（图像生成）
            ├── Stable Diffusion 3（图像生成）
            ├── Wan2.1（视频生成）
            └── Voicebox / Matcha-TTS（语音合成）
```

---

## 学习路线

| 阶段 | 内容 | 建议时长 |
|------|------|---------|
| 第一阶段 | 直觉理解：为什么需要 Flow Matching | 2-3天 |
| 第二阶段 | 核心论文：FM + CFM | 1周 |
| 第三阶段 | Rectified Flow，理解直线路径 | 3-5天 |
| 第四阶段 | 代码实现（2D toy → 图像） | 1周 |
| 第五阶段 | 阅读 FLUX / SD3 技术报告 | 3-5天 |

---

## 核心论文（按时间顺序）

### 🏛️ 前置基础

#### Neural Ordinary Differential Equations
- **作者：** Ricky T. Q. Chen et al.（多伦多大学）
- **发表：** NeurIPS 2018（最佳论文）
- **论文：** https://arxiv.org/abs/1806.07366
- **代码：** https://github.com/rtqichen/torchdiffeq
- **摘要：** Flow Matching 的理论前身。提出用 ODE 描述连续变换，衍生出 Continuous Normalizing Flows（CNF）；Flow Matching 本质是高效训练 CNF 的方法

#### Score-Based Generative Modeling through SDEs
- **作者：** Yang Song et al.（Stanford）
- **发表：** ICLR 2021（最佳论文）
- **论文：** https://arxiv.org/abs/2011.13456
- **摘要：** 将 Diffusion 统一为随机微分方程（SDE）视角；理解这篇有助于对比 Flow Matching 的 ODE 路线为何更高效

### 🔑 Flow Matching 奠基

#### Flow Matching for Generative Modeling
- **作者：** Yaron Lipman, Ricky T. Q. Chen et al.（Meta FAIR）
- **发表：** ICLR 2023
- **论文：** https://arxiv.org/abs/2210.02747
- **摘要：** ★★ Flow Matching 的开山之作。提出直接回归速度场 v(x,t) 的训练目标，避免了 CNF 训练时昂贵的 ODE 求解；证明条件速度场的边缘化等价性，使训练变得简单高效

#### Improving and Generalizing Flow Matching（Conditional Flow Matching，CFM）
- **作者：** Lipman, Albergo et al.（Meta / NYU）
- **发表：** ICML 2023
- **论文：** https://arxiv.org/abs/2302.00482
- **摘要：** ★★ CFM 是 FM 的重要扩展，引入最优传输（OT-CFM），使概率路径更直（接近直线），采样步数进一步减少；目前大多数工业实现基于 CFM

### 🚀 Rectified Flow

#### Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow
- **作者：** Xingchao Liu（刘宇）et al.（UT Austin）
- **发表：** ICLR 2023
- **论文：** https://arxiv.org/abs/2209.03003
- **代码：** https://github.com/gnobitab/RectifiedFlow
- **摘要：** ★★ 与 FM 同期独立提出，思路略有不同：通过"整流"（Reflow）操作迭代拉直概率路径；理论上 1 步采样即可（虽然实际需要多步）；SD3 和 FLUX.1 的直接技术来源

#### InstaFlow: One Step is Enough for High-Quality Diffusion-Based Text-to-Image Generation
- **作者：** Liu et al.
- **发表：** ICLR 2024
- **论文：** https://arxiv.org/abs/2309.06380
- **摘要：** 将 Rectified Flow 应用于 SD，实现 1 步高质量图像生成；证明 Rectified Flow 的极限潜力

### 🎯 统一理论视角

#### Stochastic Interpolants: A Unifying Framework for Flows and Diffusions
- **作者：** Albergo & Vanden-Eijnden（NYU）
- **发表：** 2023
- **论文：** https://arxiv.org/abs/2303.08797
- **摘要：** 将 Flow Matching 和 Diffusion 统一在同一框架下，证明两者是同一思想的不同实例；有助于从更高视角理解两者关系

#### Scaling Rectified Flow Transformers for High-Resolution Image Synthesis（SD3）
- **作者：** Esser et al.（Stability AI）
- **发表：** ICML 2024
- **论文：** https://arxiv.org/abs/2403.03206
- **摘要：** ★ SD3 技术报告，详细描述了 Rectified Flow + MM-DiT 的结合方式；是理解工业级 Flow Matching 应用的必读文章

---

## 经典教程与博客

### 直觉入门

- **Flow Matching: A New Paradigm for Generative Modeling（强烈推荐）**
  https://mlg.eng.cam.ac.uk/blog/2024/01/20/flow-matching.html
  ★ 剑桥 MLG 出品，图文并茂，从 OT 和速度场角度讲透 Flow Matching，是目前最好的入门博客

- **An Introduction to Flow Matching（Cambridge MLG）**
  https://mlg.eng.cam.ac.uk/blog/2024/01/20/flow-matching.html

- **Lilian Weng - Flow Matching（2024）**
  https://lilianweng.github.io/posts/2023-10-09-generative-compared/
  ★ Lilian Weng 对比讲解 Diffusion vs Flow Matching，清晰对比两者优劣

- **Rectified Flow 作者 Blog（刘宇）**
  https://www.cs.utexas.edu/~lqiang/rectflow/html/blog.html
  ★ 作者亲自写的直觉解释，含动态可视化

- **Flow Matching 直觉可视化（交互式）**
  https://nnplayground.com/flow-matching
  可以直接在浏览器里感受粒子从噪声"流向"数据的过程

### 深度技术

- **Understanding Flow Matching（Sander Dieleman）**
  https://sander.ai/2024/09/02/flow-matching.html
  ★ Spotify Research 的 Sander Dieleman 出品，数学推导严谨，适合有一定基础后阅读

- **从 DDPM 到 Flow Matching 的演进（The Annotated Diffusion Model 作者续篇）**
  https://huggingface.co/blog/annotated-diffusion

- **Flow Matching vs Diffusion：详细对比**
  https://diffusionflow.github.io/

### 视频讲解

- **Yaron Lipman - Flow Matching Tutorial（ICML 2023 Tutorial）**
  https://www.youtube.com/watch?v=5ZSwYogAxYg
  ★★ Flow Matching 原作者亲自讲解，权威且系统，约 1 小时

- **Rectified Flow 作者报告（刘宇，NeurIPS）**
  https://www.youtube.com/watch?v=sDLp1M_RsFE

- **Stanford CS236 - Flow Matching 章节**
  https://deepgenerativemodels.github.io/

---

## 代码实践

### 上手项目（推荐顺序）

1. **2D Toy Dataset Flow Matching（最直观）**
   - 推荐库：https://github.com/atong01/conditional-flow-matching
   - ★ torchcfm 官方库，含 2D 数据可视化示例，5 分钟看到效果

2. **torchcfm：Conditional Flow Matching 官方库**
   ```bash
   pip install torchcfm
   ```
   - https://github.com/atong01/conditional-flow-matching
   - 支持 FM、CFM、OT-CFM、Rectified Flow 多种变体

3. **Rectified Flow 官方代码**
   - https://github.com/gnobitab/RectifiedFlow
   - 含 CIFAR-10 和 CelebA-HQ 完整训练代码

4. **FLUX.1 推理代码（Hugging Face Diffusers）**
   ```python
   from diffusers import FluxPipeline
   pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev")
   image = pipe("a photo of a cat").images[0]
   ```
   - https://huggingface.co/docs/diffusers/api/pipelines/flux

### 核心代码逻辑（Flow Matching 训练伪代码）

```python
# Flow Matching 训练核心（比 Diffusion 更简洁！）
def flow_matching_loss(model, x1):
    # x1: 真实数据, x0: 随机噪声
    x0 = torch.randn_like(x1)
    t = torch.rand(x1.shape[0])           # 随机时间步 t ∈ [0,1]

    # 线性插值：从噪声到数据的直线路径
    xt = (1 - t) * x0 + t * x1           # 当前位置

    # 目标速度：直线路径的速度 = 数据 - 噪声（常数！）
    v_target = x1 - x0

    # 模型预测速度场
    v_pred = model(xt, t)

    # 简单的 MSE loss
    return F.mse_loss(v_pred, v_target)

# 对比 DDPM：目标是预测噪声 ε，Flow Matching 目标是预测速度 v
# 两者形式相近，但 Flow Matching 的路径更直，训练更稳定
```

---

## Flow Matching vs Diffusion 深度对比

### 数学本质

| 维度 | Diffusion（DDPM） | Flow Matching |
|------|-----------------|---------------|
| 框架 | 随机微分方程（SDE） | 常微分方程（ODE） |
| 路径 | 弯曲随机路径 | **直线（最优传输）** |
| 训练目标 | 预测噪声 ε | 预测**速度 v**（更直观） |
| 采样步数 | 1000 步（DDPM）/ 50 步（DDIM） | **20-50 步，可达 1 步** |
| 训练复杂度 | 需要噪声调度器 | **更简洁**，无需精心设计 |
| 理论保证 | 近似 | **精确**（ODE 可逆） |

### 采样效率（为什么 Flow Matching 步数少）

```
Diffusion 路径：                Flow Matching 路径：
噪声 ↗↘↗↘↗↘↗↘ 数据           噪声 ————————→ 数据
   （随机游走）                    （直线！）

需要 1000 小步                  20-50 步足够
```

---

## 工业应用现状

| 产品 | FM 变体 | 骨干 | 发布时间 |
|------|---------|------|---------|
| **Stable Diffusion 3** | Rectified Flow | MM-DiT | 2024.03 |
| **FLUX.1** | Rectified Flow | 双路 DiT | 2024.08 |
| **Wan2.1** | Flow Matching | DiT | 2025.02 |
| **Voicebox**（Meta TTS） | Flow Matching | Transformer | 2023 |
| **Matcha-TTS** | Flow Matching | U-Net | 2023 |
| **Genie 2**（DeepMind） | 推测 FM | DiT | 2024 |

> **趋势明确：** 新一代图像/视频/语音生成模型几乎都在迁移到 Flow Matching

---

## 推荐学习顺序

1. **看** Yaron Lipman 的 ICML Tutorial 视频（建立整体框架）
2. **读** 剑桥 MLG 博客（直觉理解速度场）
3. **玩** torchcfm 的 2D 示例（5 分钟上手，可视化路径）
4. **读** Flow Matching 原论文（Lipman 2022，精读核心推导）
5. **读** Rectified Flow 论文（理解"整流"思想）
6. **读** SD3 技术报告（理解工业落地细节）
7. **跑** FLUX.1 推理代码（感受最终效果）

---

*资料整理：Lovely | 更新时间：2026-03-27 | 仅含外网资料*
