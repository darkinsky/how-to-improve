#!/usr/bin/env python3
"""Lightweight Markdown quality checks for this repository.

Checks:
- local Markdown links point to existing files;
- study-materials documents contain metadata and conclusion sections;
- selected high-value topic documents contain learning/practice guidance;
- high-change frontier documents contain Freshness metadata;
- duplicate external URLs are reported when they may need centralization;
- long Markdown documents are reported for review.

External URLs are not fetched, so the script stays fast and stable in CI.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


MARKDOWN_LINK_RE = re.compile(r"(?<!!)(?<!\\!)\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://")
EXTERNAL_OR_MAIL_PREFIXES = ("http://", "https://", "mailto:")
FRONTIER_KEYWORDS = (
    "frontier",
    "runtime",
    "benchmark",
    "reasoning",
    "video",
    "serving",
    "multimodal",
    "papers-2026",
    "agent-runtime",
)
STRUCTURE_EXEMPT_FILES = {
    "README.md",
    "content-standard.md",
    "maintenance-guide.md",
    "material-index.md",
    "project-cards.md",
    "deep-reading-guide.md",
    "official-links.md",
}
CATALOG_HINTS = ("catalog", "open-courses", "papers", "official-links")
REQUIRED_GUIDANCE_DOCS = {
    "agent-engineering/agent-memory.md",
    "agent-engineering/code-agents.md",
    "agent-engineering/agent-runtime-frameworks.md",
    "agent-engineering/harness-engineering.md",
    "ai-infra/04-llm-inference.md",
    "ai-infra/08-llm-serving-frontier.md",
    "evaluation-benchmarking.md",
    "learning-systems/meta-learning.md",
    "reinforcement-learning/llm-agent-rl-frontier.md",
    "reinforcement-learning/reasoning-rl.md",
}


@dataclass
class Issue:
    level: str
    file: Path
    message: str

    def format(self, root: Path) -> str:
        return f"[{self.level}] {self.file.relative_to(root)}: {self.message}"


def normalize_link(raw: str) -> str:
    return raw.strip().split("#", 1)[0].strip()


def is_external_or_anchor(raw: str) -> bool:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return True
    if raw.startswith(EXTERNAL_OR_MAIL_PREFIXES):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
        return True
    return False


def is_external(raw: str) -> bool:
    return raw.strip().startswith(EXTERNAL_PREFIXES)


def is_study_material(path: Path, study_root: Path) -> bool:
    try:
        path.relative_to(study_root)
        return True
    except ValueError:
        return False


def rel_to_study(path: Path, study_root: Path) -> str:
    return str(path.relative_to(study_root)).replace("\\", "/")


def is_topic_doc(path: Path, study_root: Path) -> bool:
    if not is_study_material(path, study_root):
        return False
    if path.name in STRUCTURE_EXEMPT_FILES:
        return False
    rel_text = rel_to_study(path, study_root).lower()
    if any(hint in rel_text for hint in CATALOG_HINTS):
        return False
    return True


def check_local_links(root: Path, md_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw = match.group(1).strip()
            if is_external_or_anchor(raw):
                continue
            target = normalize_link(raw)
            if not target:
                continue
            target = urllib.parse.unquote(target)
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                issues.append(Issue("ERROR", path, f"missing local link: {raw}"))
    return issues


def check_duplicate_external_urls(
    root: Path,
    md_files: list[Path],
    duplicate_threshold: int,
    show_infos: bool,
) -> list[Issue]:
    if duplicate_threshold <= 1 or not show_infos:
        return []

    locations: dict[str, set[Path]] = defaultdict(set)
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw = normalize_link(match.group(1))
            if is_external(raw):
                locations[raw].add(path)

    issues: list[Issue] = []
    index_path = root / "docs" / "study-materials" / "material-index.md"
    for url, files in sorted(locations.items()):
        if len(files) < duplicate_threshold:
            continue
        if any(p == index_path for p in files):
            continue
        sample = ", ".join(str(p.relative_to(root)) for p in sorted(files)[:4])
        issues.append(
            Issue(
                "INFO",
                sorted(files)[0],
                f"duplicate external URL appears in {len(files)} files; consider centralizing in material-index.md: {url} ({sample})",
            )
        )
    return issues


def has_learning_guidance(text: str) -> bool:
    return any(
        heading in text
        for heading in (
            "## 学习路线",
            "## 推荐学习顺序",
            "## 建议学习路线",
            "## 推荐阅读顺序",
            "## 推理学习路径",
            "## 📅 学习计划",
            "## 七、推荐学习路线",
            "## 八、推荐学习路线",
            "## 8. 推荐实践路线",
        )
    )


def has_practice_guidance(text: str) -> bool:
    return any(
        heading in text
        for heading in (
            "## 实践",
            "## 实践项目",
            "## 实践项目 / 完成标准",
            "## 代码实践",
            "## 完成标准",
            "## 项目",
            "## Benchmark",
            "动手实践",
        )
    )


def check_study_materials_structure(
    root: Path,
    md_files: list[Path],
    long_threshold: int,
    show_infos: bool,
) -> list[Issue]:
    issues: list[Issue] = []
    study_root = root / "docs" / "study-materials"

    for path in md_files:
        if not is_study_material(path, study_root):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        rel_text = rel_to_study(path, study_root).lower()
        rel_path = rel_to_study(path, study_root)

        if path.name != "README.md" and "## 文档元信息" not in text:
            issues.append(Issue("WARN", path, "missing '## 文档元信息'"))

        if len(lines) >= 80 and "## 先看结论" not in text:
            issues.append(Issue("WARN", path, "long document without '## 先看结论'"))

        if is_topic_doc(path, study_root) and rel_path in REQUIRED_GUIDANCE_DOCS:
            if not has_learning_guidance(text):
                issues.append(Issue("WARN", path, "priority topic missing learning route"))
            if not has_practice_guidance(text):
                issues.append(Issue("WARN", path, "priority topic missing practice projects or completion standards"))

        if any(keyword in rel_text for keyword in FRONTIER_KEYWORDS) and "## Freshness" not in text:
            issues.append(Issue("WARN", path, "frontier/high-change document missing '## Freshness'"))

        if show_infos and len(lines) >= long_threshold:
            issues.append(Issue("INFO", path, f"long document: {len(lines)} lines"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown links and lightweight document quality.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--long-threshold", type=int, default=500, help="Report Markdown files longer than this many lines.")
    parser.add_argument("--duplicate-url-threshold", type=int, default=4, help="Report external URLs repeated in this many files.")
    parser.add_argument("--show-info", action="store_true", help="Show informational hints. Defaults to warnings/errors only.")
    parser.add_argument("--summary-only", action="store_true", help="Only print the final summary unless errors/warnings exist.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    md_files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)

    issues: list[Issue] = []
    issues.extend(check_local_links(root, md_files))
    issues.extend(check_study_materials_structure(root, md_files, args.long_threshold, args.show_info))
    issues.extend(check_duplicate_external_urls(root, md_files, args.duplicate_url_threshold, args.show_info))

    errors = [i for i in issues if i.level == "ERROR"]
    warnings = [i for i in issues if i.level == "WARN"]
    infos = [i for i in issues if i.level == "INFO"]

    visible_issues = issues if args.show_info else [i for i in issues if i.level != "INFO"]
    if args.summary_only and not errors and not warnings:
        visible_issues = []

    if visible_issues:
        for issue in visible_issues:
            print(issue.format(root))
    elif not args.summary_only:
        print("No Markdown issues found.")

    print(
        f"\nChecked {len(md_files)} Markdown files: "
        f"{len(errors)} errors, {len(warnings)} warnings, {len(infos)} info."
    )

    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
