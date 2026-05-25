#!/usr/bin/env python3
"""Compile Python scripts and verify hook entrypoints."""

from __future__ import annotations

import py_compile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK_DIR = ROOT / "plugins" / "idea-to-product" / "hooks"
SCRIPT_DIR = ROOT / "scripts"


def python_files() -> list[Path]:
    return sorted(SCRIPT_DIR.glob("*.py")) + sorted(HOOK_DIR.glob("*.py"))


def has_entrypoint(text: str) -> bool:
    return "def main(" in text or 'if __name__ == "__main__"' in text or "if __name__ == '__main__'" in text


def validate_shape(path: Path, failures: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    relative = path.relative_to(ROOT)
    if not lines:
        failures.append(f"{relative}: empty file")
        return
    if not lines[0].startswith("#!"):
        failures.append(f"{relative}: first line must be a shebang")
    if '"""' in lines[0] or "from __future__" in lines[0] or "import " in lines[0]:
        failures.append(f"{relative}: code is attached to shebang line")
    if not has_entrypoint(text):
        failures.append(f"{relative}: missing main() or __main__ entrypoint")


def main() -> int:
    failures: list[str] = []
    for path in python_files():
        validate_shape(path, failures)
        try:
            py_compile.compile(str(path), doraise=True)
        except py_compile.PyCompileError as exc:
            failures.append(f"{path}: {exc.msg}")

    if failures:
        print("Python hook validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Python hook validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
