#!/usr/bin/env python3
"""Lightweight Markdown quality checks for this repository.

Checks:
- local Markdown links point to existing files;
- study-materials documents contain metadata and conclusion sections;
- topic documents are nudged toward required learning sections;
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


def is_topic_doc(path: Path, study_root: Path) -> bool:
    if not is_study_material(path, study_root):
        return False
    if path.name in STRUCTURE_EXEMPT_FILES:
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
) -> list[Issue]:
    if duplicate_threshold <= 1:
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


def check_study_materials_structure(root: Path, md_files: list[Path], long_threshold: int) -> list[Issue]:
    issues: list[Issue] = []
    study_root = root / "docs" / "study-materials"

    for path in md_files:
        if not is_study_material(path, study_root):
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()
        rel_text = str(path.relative_to(study_root)).lower()

        if path.name != "README.md" and "## 文档元信息" not in text:
            issues.append(Issue("WARN", path, "missing '## 文档元信息'"))

        if len(lines) >= 80 and "## 先看结论" not in text:
            issues.append(Issue("WARN", path, "long document without '## 先看结论'"))

        if is_topic_doc(path, study_root) and len(lines) >= 120:
            if "## 学习路线" not in text and "## 推荐学习顺序" not in text:
                issues.append(Issue("INFO", path, "topic document may need '## 学习路线' or '## 推荐学习顺序'"))
            if "## 实践" not in text and "## 实践项目" not in text and "## 代码实践" not in text and "## 完成标准" not in text:
                issues.append(Issue("INFO", path, "topic document may need practice projects or completion standards"))

        if any(keyword in rel_text for keyword in FRONTIER_KEYWORDS) and "## Freshness" not in text:
            issues.append(Issue("WARN", path, "frontier/high-change document missing '## Freshness'"))

        if len(lines) >= long_threshold:
            issues.append(Issue("INFO", path, f"long document: {len(lines)} lines"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown links and lightweight document quality.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--long-threshold", type=int, default=500, help="Report Markdown files longer than this many lines.")
    parser.add_argument("--duplicate-url-threshold", type=int, default=4, help="Report external URLs repeated in this many files.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    md_files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)

    issues: list[Issue] = []
    issues.extend(check_local_links(root, md_files))
    issues.extend(check_study_materials_structure(root, md_files, args.long_threshold))
    issues.extend(check_duplicate_external_urls(root, md_files, args.duplicate_url_threshold))

    errors = [i for i in issues if i.level == "ERROR"]
    warnings = [i for i in issues if i.level == "WARN"]
    infos = [i for i in issues if i.level == "INFO"]

    if issues:
        for issue in issues:
            print(issue.format(root))
    else:
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
