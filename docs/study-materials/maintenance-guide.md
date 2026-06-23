# Study Materials 维护机制

## 文档元信息

| 字段 | 内容 |
|------|------|
| 主题领域 | Study Materials |
| 材料类型 | 维护机制 / 流程 |
| 难度 | 入门 |
| 优先级 | P0 / Survey |
| 状态 | 推荐 |
| 建议用途 | 约束学习资料的更新节奏、质量标准和长期维护方式 |

---

## 先看结论

这个目录的维护目标不是“链接越来越多”，而是让每个方向持续保持：

1. **入口清晰**：新人知道从哪里开始；
2. **材料少而精**：优先保留长期有效、影响力大、可实践的材料；
3. **结构统一**：文档有元信息、结论、路线、Top 材料、实践项目和完成标准；
4. **前沿不过载**：前沿论文只收代表范式变化、工程价值或评测变化的内容；
5. **可持续更新**：每次更新有明确目的、检查清单和提交边界。

维护时优先参考：[Study Materials 内容标准](content-standard.md)。

---

## 维护节奏

| 节奏 | 目标 | 适合动作 |
|------|------|----------|
| 每次新增 / 大改 | 保证单篇文档质量 | 补元信息、先看结论、Top 材料、实践项目、链接检查 |
| 每月 | 修正局部过时内容 | 更新课程年份、替换失效链接、补充重要论文 / 系统 |
| 每季度 | 调整方向路线 | 重排 Top 10、拆分过长文档、合并重复文档 |
| 每半年 | 做一次全局审计 | 检查目录结构、入口导航、重复链接、前沿覆盖和过时内容 |

原则：小更新可以频繁做；结构性调整要成批做，避免目录来回震荡。

---

## 更新类型

### 1. 新增文档

适合场景：

- 出现一个稳定的新主题，例如 Agent Benchmarks、Reasoning RL、LLM Serving Frontier；
- 原有文档已经过长，需要拆出专题；
- 该主题能形成独立学习路线、Top 材料和实践项目。

新增文档必须包含：

- 文档元信息；
- 先看结论；
- 知识地图或问题地图；
- 必读 Top 材料；
- 学习路线；
- 实践项目或完成标准；
- 延伸资料或维护标准。

### 2. 增强现有文档

适合场景：

- 原文只有链接，缺少判断；
- 方向出现关键新论文、系统或 benchmark；
- 学习路线和完成标准不清晰；
- 入口文档没有覆盖新专题。

增强时优先补：

1. 先看结论；
2. Top 10 / Top materials；
3. 实践项目；
4. 完成标准；
5. 与相关文档的交叉链接。

### 3. 删除或降级材料

适合场景：

- 链接长期失效且没有替代资源；
- 内容重复且质量低于已有材料；
- 只是一时新闻，不能代表长期趋势；
- 与当前知识库主线无关。

删除时不要只删链接，最好说明被哪个更好的材料替代。

---

## 选材决策树

新增材料前先问：

```text
它是一手资料吗？
  是 → 继续
  否 → 是否比一手资料更清晰 / 更可实践？否则不收

它是否代表经典基础、范式变化或重要系统？
  是 → 继续
  否 → 暂不收

它是否能帮助形成路线、实践或完成标准？
  是 → 收录到 P0/P1
  否 → 只作为 P2 或暂不收

它是否和已有材料重复？
  是 → 只保留更高质量的一项
  否 → 可以新增
```

---

## 前沿内容维护规则

前沿内容容易膨胀，因此只收以下几类：

| 类型 | 收录标准 | 示例 |
|------|----------|------|
| 新范式 | 改变训练、推理、评测或系统设计方式 | DPO、RLVR、Flow Matching、P/D 分离 |
| 新系统 | 被广泛引用、复现或工业采用 | vLLM、SGLang、TensorRT-LLM、FlashAttention |
| 新 benchmark | 改变评价方式或暴露旧评测缺陷 | SWE-bench、Terminal-Bench、WebArena |
| 高质量技术报告 | 信息密度高，代表产业趋势 | Sora、DeepSeek-R1、DeepSeek-V3 |
| 可复现项目 | 有代码、实验或可运行 demo | mini RLVR、serving benchmark、agent harness |

不收：

- 只有营销表述、没有技术细节的发布；
- 没有实验、没有代码、没有清晰问题定义的短文；
- 与已有材料高度重复的新链接；
- 需要非公开权限访问的资料。

---

## 文档质量检查清单

每次提交前检查：

- [ ] 是否包含文档元信息？
- [ ] 是否有“先看结论”？
- [ ] 是否说明为什么重要，而不是只放链接？
- [ ] 是否区分 P0 / P1 / P2 或 Classic / Frontier / Hands-on / Survey？
- [ ] 是否包含实践项目或完成标准？
- [ ] 是否和上级 README 建立链接？
- [ ] 是否避免重复、低质量或短期噪音链接？
- [ ] 是否通过本地 Markdown 相对链接检查？

---

## 索引更新规则

新增或大改文档后，同步检查这些入口：

1. 当前目录的 `README.md`；
2. `docs/study-materials/README.md`；
3. 根目录 `README.md`，如果新增主题影响仓库主路线；
4. 相关专题文档的“延伸阅读”或“总览补充”。

如果只是补充某篇文档内部内容，不一定需要更新根 README。

---

## 提交流程

建议一次维护提交控制在一个主题内：

```text
1. 明确本次更新目标
2. 修改或新增文档
3. 更新相关索引
4. 运行 Markdown 质量检查脚本
5. 查看 git diff / stat
6. commit with concise message
7. push
```

推荐检查命令：

```bash
python scripts/check_markdown_links.py
```

如果想把结构性 warning 也作为失败处理：

```bash
python scripts/check_markdown_links.py --strict
```

推荐提交信息格式：

```text
Enhance <topic> study materials
Add <topic> study materials
Improve study materials maintenance
```

---

## 长期演进方向

后续维护可以按以下方向推进：

1. **拆分过长文档**：超过 300-500 行且包含多个主题时，考虑拆成总览 + 专题；
2. **补实践项目**：每个方向至少有 2-3 个可执行 mini project；
3. **补评测标准**：AI Infra、Agent、RL、生成模型都应有 benchmark / evaluation 入口；
4. **补完成标准**：每条路线都应说明学到什么程度算完成；
5. **定期清理**：删除低质量链接和过时材料，避免知识库退化成链接堆。


---

## Quarterly Frontier Review

每季度对高变化方向做一次审计：

| 方向 | 审计重点 |
|------|----------|
| LLM Serving | vLLM、SGLang、P/D 分离、KV cache、speculative decoding、新 benchmark |
| Agent Runtime | MCP、A2A、OpenAI Agents SDK、LangGraph、AutoGen、Code Agents |
| Reasoning RL | RLVR、GRPO、PRM、verifier、test-time compute、reward hacking |
| Multimodal / VLM | GPT-4V/4o、Gemini、Qwen-VL、InternVL、GUI Agent、Document AI |
| Video Generation | Sora、Veo、Movie Gen、CogVideoX、Wan、VideoPoet、VBench |
| RAG | Self-RAG、CRAG、GraphRAG、Agentic RAG、RAG eval |

审计步骤：

1. 检查前沿材料是否仍然代表主线；
2. 标记过时或被替代的材料；
3. 更新 `最后审阅` 和 `过时风险`；
4. 同步 [Material Index](material-index.md)；
5. 运行 Markdown 检查和链接检查。

---

## 单一事实源维护流程

新增或调整重要材料时：

1. 判断它属于哪个主文档；
2. 更新主文档；
3. 在相关文档中只保留简短引用；
4. 更新 [Material Index](material-index.md)；
5. 如果材料对应实践项目，更新 [Project Cards](project-cards.md)。

---

## 外部链接维护策略

- 每次新增 P0 材料，优先添加官方链接或官方 repo。
- 外部链接检查可以抽样进行，避免 CI 因临时网络失败不稳定。
- 失效链接优先替换为 arXiv、官方仓库或 Internet Archive。
- 对前沿产品页面，优先保留技术报告或官方文档，而不是新闻稿。

---

## 自动化检查建议

本仓库当前至少应运行：

```bash
python scripts/check_markdown_links.py --strict
git diff --check
```

后续可增加：

- 重复标题检查；
- 重复材料检查；
- required sections 检查；
- 外部链接抽样检查；
- 文档长度和拆分建议。
