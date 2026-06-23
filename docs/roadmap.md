# Roadmap

这个路线图反映当前仓库状态：仓库已经不再是早期骨架阶段，而是进入 **内容质量治理、可执行化和长期维护自动化** 阶段。

---

## Phase 1: 骨架与主题建立，已完成

- [x] 初始化仓库结构
- [x] 补充根目录 README
- [x] 建立 Study Materials 总入口
- [x] 建立 AI Infra / RL / Agent / Generative / CS 主线
- [x] 建立内容标准和维护机制
- [x] 建立学习路线入口

---

## Phase 2: 材料覆盖扩展，已完成

- [x] 补 Foundation Models / LLM Fundamentals
- [x] 补 Retrieval / RAG / Long Context
- [x] 补 Multimodal / VLM
- [x] 补 Code Agents / SWE Agents
- [x] 补 Agent Runtime Frameworks / Protocols
- [x] 补 Systems Classic Papers
- [x] 补 Evaluation / Benchmarking
- [x] 更新各专题索引和全局学习路线

---

## Phase 3: 内容质量提升，进行中

- [x] 建立 [Material Index](study-materials/material-index.md)，明确主文档和相关文档
- [x] 建立 [Project Cards](study-materials/project-cards.md)，把学习路线转化为实践项目
- [x] 在 [Learning Paths](study-materials/learning-paths.md) 中加入路线决策树和 4/8/12 周路线
- [ ] 每个专题挑 Top 5 材料做深度解读：怎么读、读完掌握什么、常见误区
- [ ] 将末尾的“补充清单”逐步融入正文结构
- [ ] 为 P0 材料补官方链接、代码仓库和推荐阅读顺序

---

## Phase 4: 维护自动化，进行中

- [x] 本地 Markdown 链接检查脚本
- [x] GitHub Actions 自动运行 Markdown 检查
- [x] `git diff --check` 空白字符检查
- [ ] 增加外部链接抽样检查
- [x] 增加重复标题 / 重复材料检查
- [x] 增加 required sections 检查：元信息、先看结论、实践项目、维护信息

---

## Phase 5: Freshness 与前沿治理，进行中

- [x] 在内容标准中加入 freshness metadata
- [x] 在维护机制中加入 quarterly frontier review
- [x] 为高变化 frontier 文档补 `最后审阅`、`过时风险`、`维护重点`
- [ ] 每季度审计一次：LLM Serving、Agent Runtime、VLM、Reasoning RL、Video Generation

---

## Phase 6: 公开协作，进行中

- [x] 增加 License
- [x] 增加 CONTRIBUTING.md
- [x] 增加 PR checklist
- [x] 增加 Issue templates
- [ ] 如果开始接受外部贡献，补充更详细的贡献示例和 review policy

---

## 当前优先级

1. 将各专题 Top 5 从“材料清单”升级成“深度学习说明”。
2. 为 P0 材料补官方链接。
3. 为 frontier 文档补 freshness metadata。
4. 增加自动化重复材料检查。
5. 每季度做一次全局材料审计。

## Next 10 Tasks

- [x] 补齐 Deep Reading Guide 中的 CS / Systems Top 5。
- [x] 补齐 Deep Reading Guide 中的 Evaluation / Benchmarking Top 5。
- [x] 补齐 Deep Reading Guide 中的 Learning Systems / Meta-learning Top 5。
- [x] 为高变化 frontier 文档补齐 `Freshness`：LLM Serving、Agent Runtime、VLM、Reasoning RL、Video Generation。
- [x] 将 [Material Index](study-materials/material-index.md) 扩展为 P0/P1 材料的单一事实源：官方链接、代码、主文档、相关 Project、最近审阅。
- [x] 增强 `scripts/check_markdown_links.py`：重复 URL / 重复材料 warning。
- [x] 增强 `scripts/check_markdown_links.py`：required sections warning，包括实践项目、完成标准和 Freshness。
- [x] 拆分或压缩超过 450 行的长文档：open-courses、image-video-generation。
- [x] 补充 `docs/engineering` 的 Debugging / Code Review / System Design workflow。
- [x] 补充 `docs/research` 的 Paper Reading / Experiment Design / Literature Review workflow。

## Backlog 分层

| 优先级 | 任务类型 | 目标 |
|--------|----------|------|
| P0 | 导航与深读补齐 | 让读者能从目标直接进入路线、深读和项目 |
| P1 | Freshness 治理 | 降低前沿内容过时风险 |
| P1 | 自动化检查 | 用脚本发现重复材料、缺失章节和失效链接 |
| P2 | 长文档拆分 | 降低单篇阅读负担，提高专题可维护性 |
| P2 | Engineering / Research 扩展 | 让仓库从学习资料库扩展为完整改进系统 |
