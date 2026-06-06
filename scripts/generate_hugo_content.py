#!/usr/bin/env python3
"""Generate Hugo content pages from catalog and problem READMEs."""

from __future__ import annotations

import argparse
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_loader import load_catalog

ROOT = Path(__file__).resolve().parent.parent
GITHUB_BASE = "https://github.com/Amirmahdikahdouii/Python-Exercises/blob/master"
DEFAULT_DATE = date.today().isoformat()


def yaml_quote(value: str) -> str:
    if not value:
        return '""'
    if any(c in value for c in ':"\'{}[],&*#?|-<>=!%@\\'):
        escaped = value.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'
    return value


def build_front_matter(entry: dict) -> str:
    lang = entry.get("language", "python")
    ext = "go" if lang == "go" else "py"
    rel_path = entry["path"]
    tags = entry.get("tags") or []
    source_url = entry.get("source_url")

    lines = [
        "---",
        f"title: {yaml_quote(entry['title_fa'])}",
        f"title_en: {yaml_quote(entry.get('title_en', ''))}",
        f"date: {DEFAULT_DATE}",
        f"categories: [{yaml_quote(entry['category'])}]",
        f"difficulties: [{yaml_quote(entry['difficulty'])}]",
        f"tags: [{', '.join(yaml_quote(t) for t in tags)}]",
        "params:",
        f"  problem_id: {entry['id']}",
        f"  language: {yaml_quote(lang)}",
        f"  github_readme: {yaml_quote(f'{GITHUB_BASE}/{rel_path}/README.md')}",
        f"  github_solution: {yaml_quote(f'{GITHUB_BASE}/{rel_path}/solution.{ext}')}",
        f"  source_url: {yaml_quote(source_url) if source_url else 'null'}",
        "  rtl: true",
        "---",
        "",
    ]
    return "\n".join(lines)


def build_body(entry: dict, readme: str) -> str:
    lang = entry.get("language", "python")
    ext = "go" if lang == "go" else "py"
    meta = [
        f"**#{entry['id']:03d}** · **{entry['title_en']}** · `{entry['category']}` · `{entry['difficulty']}` · `{lang}`",
        "",
    ]
    if entry.get("source_url"):
        meta.append(f"[منبع سوال]({entry['source_url']})")
        meta.append("")
    meta.extend([
        f"[مشاهده راه‌حل در GitHub]({GITHUB_BASE}/{entry['path']}/solution.{ext})",
        "",
        "---",
        "",
    ])
    return "\n".join(meta) + readme.strip() + "\n"


def generate(output_dir: Path) -> int:
    catalog = load_catalog(ROOT / "catalog" / "problems.yaml")
    if output_dir.exists():
        for child in output_dir.iterdir():
            if child.is_dir():
                import shutil
                shutil.rmtree(child)
            else:
                child.unlink()
    output_dir.mkdir(parents=True, exist_ok=True)

    written = 0
    for entry in catalog:
        folder = f"{entry['id']:03d}-{entry['slug']}"
        problem_dir = ROOT / entry["path"]
        readme_path = problem_dir / "README.md"
        if not readme_path.exists():
            print(f"[WARN] Missing README: {readme_path}", file=sys.stderr)
            readme = "_Problem statement not available._"
        else:
            readme = readme_path.read_text(encoding="utf-8")

        dest = output_dir / folder / "index.md"
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(build_front_matter(entry) + build_body(entry, readme), encoding="utf-8")
        written += 1

    print(f"Generated {written} problem pages in {output_dir}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Hugo problem content")
    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for content/problems/",
    )
    args = parser.parse_args()
    return generate(args.output.resolve())


if __name__ == "__main__":
    raise SystemExit(main())
