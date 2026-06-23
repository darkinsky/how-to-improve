# Flow-based Models（流模型）学习计划与资料汇总

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Generative Models |
| 材料类型 | 基础 / 论文路线 |
| 难度 | 中级 |
| 优先级 | P1 / Classic |
| 状态 | 可用 |
| 建议用途 | 理解可逆生成模型与显式似然建模 |

---

> 整理时间：2026-03-27
> 目标：系统掌握 Flow-based 生成模型的理论基础、核心变体与应用场景
> 前置推荐：先完成 AE & VAE 学习，理解变分推断与隐空间概念；了解基础概率论（变量替换、Jacobian 行列式）

---

## 先看结论

- Flow-based Models 的核心优势是显式似然和可逆变换，核心代价是结构受限、维度守恒和 Jacobian 计算约束。
- NICE、RealNVP、Glow 的主线是设计易逆且 Jacobian determinant 易算的 coupling layer。
- Continuous Normalizing Flow / Neural ODE 把离散可逆层扩展到连续时间，但训练和采样成本更高。
- 传统 normalizing flow 在图像生成主线上已被 Diffusion / Flow Matching 超越，但它仍是理解 Flow Matching、CNF 和概率路径的重要基础。
- 学习重点不是背模型名字，而是理解 change of variables、log-likelihood、invertibility、coupling transform。
- 完成标准：能实现一个 RealNVP toy example，并解释 flow 与 VAE / GAN / Diffusion 的差异。

---

## 知识地图

```
Flow-based Models（流模型）
    ├── 理论基础
    │       ├── 变量替换公式（Change of Variables）
    │       ├── Jacobian 行列式（行列式计算技巧）
    │       ├── 标准化流（Normalizing Flow）
    │       └── 最大似然估计（Exact Log-Likelihood）
    ├── 核心架构
    │       ├── NICE（加法耦合层）
    │       ├── RealNVP（仿射耦合层）
    │       ├── Glow（1×1 可逆卷积 + ActNorm）
    │       ├── Neural ODE（连续流）
    │       └── Continuous Normalizing Flows (CNF)
    ├── 设计约束
    │       ├── 可逆性（Invertibility）
    │       ├── Jacobian 行列式高效计算
    │       └── 维度守恒（无法降维）
    └── 应用场景
            ├── 密度估计（异常检测）
            ├── 图像生成
            ├── 语音合成（WaveGlow、WaveFlow）
            └── 分子生成（药物设计）
```

---

## 学习路线

| 阶段 | 内容 | 建议时长 |
|------|------|---------|
| 第一阶段 | 变量替换公式 + Jacobian 直觉 | 3-5天 |
| 第二阶段 | NICE → RealNVP，理解耦合层设计 | 1周 |
| 第三阶段 | Glow 论文 + 代码实践 | 1周 |
| 第四阶段 | Neural ODE / CNF（选修） | 1周 |
| 第五阶段 | 实际应用：异常检测 / 语音合成 | 持续 |

---

## 核心论文（按时间顺序）

### 🏛️ 奠基之作

#### NICE: Non-linear Independent Components Estimation
- **作者：** Laurent Dinh, David Warde-Farley, Samy Bengio, Aaron Courville
- **发表：** ICLR 2015 Workshop
- **论文：** https://arxiv.org/abs/1410.8516
- **摘要：** Flow 的开山之作，提出加法耦合层（additive coupling layer），使 Jacobian 行列式计算为 O(1)；首次实现可精确计算似然的深度生成模型

#### RealNVP: Real-valued Non-Volume Preserving Transformations
- **作者：** Laurent Dinh, Jascha Sohl-Dickstein, Samy Bengio
- **发表：** ICLR 2017
- **论文：** https://arxiv.org/abs/1605.08803
- **摘要：** 将 NICE 的加法耦合改为仿射耦合（scale + shift），大幅提升表达能力；引入 multi-scale 架构，成为后续工作的基础

### 🌟 里程碑模型

#### Glow: Generative Flow with Invertible 1×1 Convolutions
- **作者：** Diederik P. Kingma, Prafulla Dhariwal（OpenAI）
- **发表：** NeurIPS 2018
- **论文：** https://arxiv.org/abs/1807.03039
- **代码：** https://github.com/openai/glow
- **摘要：** 引入可逆 1×1 卷积替代固定排列，ActNorm 替代 BatchNorm；首次用 Flow 模型生成高质量 256×256 人脸图像，展示了隐空间插值与属性编辑能力

#### Neural Ordinary Differential Equations
- **作者：** Ricky T. Q. Chen, Yulia Rubanova, Jesse Bettencourt, David Duvenaud
- **发表：** NeurIPS 2018（最佳论文）
- **论文：** https://arxiv.org/abs/1806.07366
- **代码：** https://github.com/rtqichen/torchdiffeq
- **摘要：** 将 ResNet 的离散残差连接推广到连续 ODE，形成"无限层"网络；在 Flow 领域衍生出 Continuous Normalizing Flows (CNF)

#### FFJORD: Free-form Jacobian of Reversible Dynamics
- **作者：** Grathwohl et al.
- **发表：** ICLR 2019
- **论文：** https://arxiv.org/abs/1810.01367
- **摘要：** 基于 Neural ODE 的连续流，用 Hutchinson 估计器解决 Jacobian 迹的计算瓶颈，大幅降低计算复杂度

### 🎵 语音合成应用

#### WaveGlow: A Flow-based Generative Network for Speech Synthesis
- **作者：** Ryan Prenger, Rafael Valle, Bryan Catanzaro（NVIDIA）
- **发表：** ICASSP 2019
- **论文：** https://arxiv.org/abs/1811.00002
- **代码：** https://github.com/NVIDIA/waveglow
- **摘要：** 将 Flow 模型应用于语音波形合成，结合 WaveNet 条件生成，推理速度比自回归快 500 倍

#### Flow TTS / Flowtron
- **作者：** Valle et al.（NVIDIA）
- **论文：** https://arxiv.org/abs/2005.05957
- **摘要：** Flow-based 文字转语音，支持风格迁移和说话人控制

### 🧬 分子生成应用

#### GraphNVP / GFlowNet
- **GFlowNet 综述：** https://arxiv.org/abs/2111.09266
- **摘要：** Flow 在药物分子设计领域的应用，用于生成满足特定属性的分子结构

---

## 经典教程与博客

### 理论入门

- **Lilian Weng - Flow-based Deep Generative Models（强烈推荐）**
  https://lilianweng.github.io/posts/2018-10-13-flow-models/
  ★ 从变量替换公式讲到 Glow，数学推导清晰，图示丰富，是最好的 Flow 入门文章

- **Eric Jang - Normalizing Flows Tutorial（两篇系列）**
  https://blog.evjang.com/2018/01/nf1.html
  https://blog.evjang.com/2018/01/nf2.html
  ★ 直觉讲解为主，配合代码，适合数学基础一般的读者

- **Adam Kosiorek - Normalizing Flows**
  http://akosiorek.github.io/ml/2018/04/03/norm_flows.html
  清晰的数学推导，含变量替换公式的完整推导

- **Normalizing Flows: An Introduction and Review of Current Methods**
  https://arxiv.org/abs/1908.09257
  综述论文，系统梳理各类 Flow 架构，适合有一定基础后阅读

### 可视化理解

- **A Visual Exploration of Gaussian Processes（背景知识）**
  https://distill.pub/2019/visual-exploration-gaussian-processes/

- **Normalizing Flows for Probabilistic Modeling and Inference（综述）**
  https://arxiv.org/abs/2012.05428
  最全面的 Flow 综述，覆盖理论、架构、应用，100+ 页

### 视频课程

- **Stanford CS236 - Deep Generative Models（含 Flow 完整章节）**
  https://deepgenerativemodels.github.io/
  ★ 斯坦福研究生课程，Flow 讲解非常系统，有课件和视频

- **Pieter Abbeel - Deep Unsupervised Learning（UC Berkeley）**
  https://sites.google.com/view/berkeley-cs294-158-sp20/home
  含 Flow 专题课，Pieter Abbeel 亲讲

- **DeepMind x UCL Lectures - Normalizing Flows**
  https://www.youtube.com/watch?v=7UZJOeAMBrI

---

## 代码实践

### 上手项目（推荐顺序）

1. **从零实现 RealNVP（2D toy dataset）**
   - 推荐教程：https://github.com/senya-ashukha/real-nvp-pytorch
   - 先在 2D 数据（月牙形、同心圆）上验证，直观感受流的变换过程

2. **Glow 官方代码（OpenAI）**
   - https://github.com/openai/glow
   - 包含人脸生成、隐空间插值的完整实现

3. **PyTorch Flows 库**
   - nflows：https://github.com/bayesiains/nflows
   - normflows：https://github.com/VincentStimper/normalizing-flows
   - ★ 封装好的 Flow 组件库，适合快速实验

4. **Neural ODE 实现**
   - torchdiffeq：https://github.com/rtqichen/torchdiffeq
   - 官方库，支持多种 ODE solver

### 关键概念代码示例

```python
# RealNVP 仿射耦合层核心逻辑（PyTorch 伪代码）
def forward(self, x):
    x1, x2 = x.chunk(2, dim=1)          # 分成两半
    log_s, t = self.net(x1)             # 用 x1 预测 scale 和 shift
    y2 = x2 * log_s.exp() + t           # 仿射变换（可逆！）
    log_det = log_s.sum(dim=[1,2,3])    # Jacobian 行列式 = scale 之积
    return torch.cat([x1, y2], dim=1), log_det

def inverse(self, y):
    y1, y2 = y.chunk(2, dim=1)
    log_s, t = self.net(y1)
    x2 = (y2 - t) * (-log_s).exp()     # 精确逆变换
    return torch.cat([y1, x2], dim=1)
```

---

## 核心数学（一页速查）

### 变量替换公式
$$\log p_X(x) = \log p_Z(f(x)) + \log \left| \det \frac{\partial f(x)}{\partial x} \right|$$

- $p_Z$：简单基分布（标准高斯）
- $f$：可逆变换（Flow 网络）
- $\det J$：Jacobian 行列式，衡量体积变化

### 为什么需要行列式可计算？
- 一般矩阵行列式计算：O(d³)，d=维度
- Flow 设计目标：让 Jacobian 是**三角矩阵**，行列式 = 对角线之积 → O(d)
- 耦合层的精妙：只变换一半维度，另一半不变 → Jacobian 自动是下三角

---

## 评估指标

| 指标 | 说明 |
|------|------|
| Bits per Dimension (BPD) | Flow 最常用指标，越低越好；标准化后可跨数据集比较 |
| NLL（Negative Log-Likelihood） | 精确负对数似然，Flow 独有优势 |
| FID | 图像生成质量（与 GAN/Diffusion 对比时用） |

> Flow 的核心优势就是能汇报**精确 NLL / BPD**，VAE 只能报 ELBO 下界，GAN 根本没有似然。

---

## Flow vs 其他方法：何时选 Flow？

| 场景 | 推荐 | 原因 |
|------|------|------|
| 需要**精确密度估计** | ✅ Flow | 唯一能精确计算 log p(x) |
| 异常检测 / OOD 检测 | ✅ Flow | 精确似然直接用于判断 |
| 语音合成（实时） | ✅ Flow（WaveGlow） | 并行推理，比自回归快 |
| 高质量图像生成 | ❌ 选 Diffusion | Flow 图像质量不如 Diffusion |
| 需要压缩隐空间 | ❌ 选 VAE/GAN | Flow 维度不能降低 |
| 隐变量可解释操控 | ⚠️ Glow 有一定能力 | 但不如 StyleGAN |

---

## 推荐学习顺序

1. **补** 变量替换公式数学基础（Jacobian 行列式）
2. **读** Lilian Weng 的 Flow-based 博客
3. **看** Stanford CS236 Flow 章节视频
4. **做** 2D toy dataset 上的 RealNVP 实现（最直观）
5. **读** Glow 论文 + 跑官方代码
6. **探** Neural ODE（选修，数学较难但很优雅）
7. **思考** 何时用 Flow vs Diffusion vs GAN

---

*资料整理：Lovely | 更新时间：2026-03-27 | 仅含外网资料*
