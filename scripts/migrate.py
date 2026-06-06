#!/usr/bin/env python3
"""Migrate Q-N/ folders to problems/NNN-slug/ layout."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_loader import load_catalog

ROOT = Path(__file__).resolve().parent.parent


def normalize_readme(content: str) -> str:
    """Light HTML to Markdown normalization."""
    text = content.strip()
    if not text:
        return text

    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<h1[^>]*>(.*?)</h1>", r"# \1\n", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<h2[^>]*>(.*?)</h2>", r"## \1\n", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<h3[^>]*>(.*?)</h3>", r"### \1\n", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<h4[^>]*>(.*?)</h4>", r"#### \1\n", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<p[^>]*>(.*?)</p>", r"\1\n\n", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<pre[^>]*>(.*?)</pre>", r"```\n\1\n```", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<code[^>]*>(.*?)</code>", r"`\1`", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<a[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", r"[\2](\1)", text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def migrate_problem(entry: dict, dry_run: bool) -> tuple[str, str | None]:
    pid = entry["id"]
    dest = ROOT / entry["path"]
    src = ROOT / f"Q-{pid}"

    if not src.exists():
        if dest.exists():
            return "skip", f"Q-{pid} already migrated"
        return "error", f"Q-{pid} not found and {dest} missing"

    if dry_run:
        return "ok", f"Q-{pid} -> {entry['path']}"

    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)

    lang = entry.get("language", "python")
    if lang == "go":
        for name in ("main.go", f"{pid}.go"):
            src_file = dest / name
            if src_file.exists():
                src_file.rename(dest / "solution.go")
                break
    else:
        py_file = dest / f"{pid}.py"
        if py_file.exists():
            py_file.rename(dest / "solution.py")

    readme = dest / "README.md"
    if readme.exists():
        readme.write_text(normalize_readme(readme.read_text(encoding="utf-8")), encoding="utf-8")

    shutil.rmtree(src)
    return "ok", f"Q-{pid} -> {entry['path']}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate Q-N folders to new layout")
    parser.add_argument("--dry-run", action="store_true", help="Print actions without changing files")
    args = parser.parse_args()

    catalog = load_catalog(ROOT / "catalog" / "problems.yaml")
    counts = {"ok": 0, "skip": 0, "error": 0}

    for entry in catalog:
        status, msg = migrate_problem(entry, args.dry_run)
        counts[status] += 1
        prefix = {"ok": "OK", "skip": "SKIP", "error": "ERROR"}[status]
        print(f"[{prefix}] {msg}")

    print(f"\nDone: {counts['ok']} migrated, {counts['skip']} skipped, {counts['error']} errors")
    return 1 if counts["error"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
