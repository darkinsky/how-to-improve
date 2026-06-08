#!/usr/bin/env python3
"""Lightweight Markdown quality checks for this repository.

Checks:
- local Markdown links point to existing files;
- study-materials documents contain a metadata section;
- study-materials documents contain a "先看结论" section when they are long enough;
- long Markdown documents are reported for review.

The script intentionally avoids checking external URLs to keep it fast and stable.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from dataclasses import dataclass
from pathlib import Path


LOCAL_LINK_RE = re.compile(r"(?<!!)(?<!\\!)\[[^\]]+\]\(([^)]+)\)")
EXTERNAL_PREFIXES = ("http://", "https://", "mailto:")


@dataclass
class Issue:
    level: str
    file: Path
    message: str

    def format(self, root: Path) -> str:
        return f"[{self.level}] {self.file.relative_to(root)}: {self.message}"


def is_external_or_anchor(raw: str) -> bool:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return True
    if raw.startswith(EXTERNAL_PREFIXES):
        return True
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", raw):
        return True
    return False


def check_local_links(root: Path, md_files: list[Path]) -> list[Issue]:
    issues: list[Issue] = []
    for path in md_files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for match in LOCAL_LINK_RE.finditer(text):
            raw = match.group(1).strip()
            if is_external_or_anchor(raw):
                continue
            target = raw.split("#", 1)[0].strip()
            if not target:
                continue
            target = urllib.parse.unquote(target)
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                issues.append(Issue("ERROR", path, f"missing local link: {raw}"))
    return issues


def check_study_materials_structure(root: Path, md_files: list[Path], long_threshold: int) -> list[Issue]:
    issues: list[Issue] = []
    study_root = root / "docs" / "study-materials"

    for path in md_files:
        try:
            path.relative_to(study_root)
        except ValueError:
            continue

        text = path.read_text(encoding="utf-8", errors="ignore")
        lines = text.splitlines()

        if path.name != "README.md" and "## 文档元信息" not in text:
            issues.append(Issue("WARN", path, "missing '## 文档元信息'"))

        if len(lines) >= 80 and "## 先看结论" not in text:
            issues.append(Issue("WARN", path, "long document without '## 先看结论'"))

        if len(lines) >= long_threshold:
            issues.append(Issue("INFO", path, f"long document: {len(lines)} lines"))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Markdown links and lightweight document quality.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--long-threshold", type=int, default=500, help="Report Markdown files longer than this many lines.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors.")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    md_files = sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)

    issues: list[Issue] = []
    issues.extend(check_local_links(root, md_files))
    issues.extend(check_study_materials_structure(root, md_files, args.long_threshold))

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
