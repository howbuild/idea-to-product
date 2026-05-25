#!/usr/bin/env python3
"""Run a hook script using the current Python interpreter.

This helper is useful for Windows/macOS manual validation where `python3`, `py`,
and `python` command availability differs.
"""

from __future__ import annotations

import runpy
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = ROOT / "plugins" / "idea-to-product"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: run-hook.py <hook-script-name> [args...]")
        return 2

    script = sys.argv[1]
    path = Path(script)
    if not path.is_absolute():
        path = PLUGIN_ROOT / "hooks" / script
    if not path.exists():
        print(f"Hook script not found: {path}")
        return 1

    sys.argv = [str(path), *sys.argv[2:]]
    runpy.run_path(str(path), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
