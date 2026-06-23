# Contributing

感谢你考虑贡献这个知识库。这个仓库的目标不是堆链接，而是维护一套可执行、可复盘、可长期更新的 AI / CS / Engineering 学习系统。

---

## 贡献原则

1. **少而精**：优先补长期有效、影响力大、可实践的材料。
2. **一手资料优先**：课程官网、论文、官方代码仓库、官方技术报告优先。
3. **说明为什么重要**：不要只放链接，需要解释它解决什么问题、适合什么时候读。
4. **可执行**：尽量补学习路线、实践项目或完成标准。
5. **公开资料**：不提交内网链接、私人聊天记录、非公开文档或需要特殊权限的材料。

---

## 新增材料流程

1. 判断材料是否已经存在于 [Material Index](docs/study-materials/material-index.md)。
2. 如果已存在，优先更新主文档，不要在多个地方重复解释。
3. 如果是新材料，选择一个主文档并同步更新 Material Index。
4. 如果材料适合实践，更新 [Project Cards](docs/study-materials/project-cards.md)。
5. 如果是前沿材料，补充 freshness 信息或维护说明。

---

## 文档结构建议

新增或大改文档时参考：

- [Study Materials 内容标准](docs/study-materials/content-standard.md)
- [Study Materials 维护机制](docs/study-materials/maintenance-guide.md)

推荐结构：

```markdown
# Topic

## 文档元信息
## 先看结论
## 知识地图
## 必读 Top 10
## 学习路线
## 材料详解
## 实践项目 / 完成标准
## Freshness
## 延伸资料
```

---

## 本地检查

提交前运行：

```bash
python scripts/check_markdown_links.py --strict
git diff --check
```

---

## PR Checklist

- [ ] 新增材料有“为什么重要”说明。
- [ ] P0/P1 材料已更新 Material Index。
- [ ] 新增或大改文档已更新相关 README。
- [ ] 前沿材料已考虑 freshness / 过时风险。
- [ ] 本地检查通过。
