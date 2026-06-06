"""Minimal YAML loader for catalog/problems.yaml (no external deps)."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "catalog" / "problems.yaml"


def _parse_scalar(raw: str) -> Any:
    raw = raw.strip()
    if raw == "null":
        return None
    if raw == "true":
        return True
    if raw == "false":
        return False
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [item.strip().strip('"').strip("'") for item in inner.split(",")]
    if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
        return raw[1:-1]
    if raw.isdigit():
        return int(raw)
    return raw


def load_catalog(path: Path | None = None) -> list[dict[str, Any]]:
    text = (path or CATALOG_PATH).read_text(encoding="utf-8")
    entries: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None

    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- id:"):
            if current:
                entries.append(current)
            current = {"id": int(stripped.split(":", 1)[1].strip())}
            continue
        if current is None:
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        current[key.strip()] = _parse_scalar(value)

    if current:
        entries.append(current)
    return entries
