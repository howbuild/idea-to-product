#!/usr/bin/env python3
"""Create a local Claude Code plugin zip package."""

from __future__ import annotations

import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "idea-to-product"
OUT_DIR = ROOT / "dist"


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    out = OUT_DIR / "idea-to-product-claude-plugin.zip"
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(PLUGIN_ROOT.rglob("*")):
            if path.is_file() and "__pycache__" not in path.parts:
                zf.write(path, path.relative_to(PLUGIN_ROOT))
    print(f"Created {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
