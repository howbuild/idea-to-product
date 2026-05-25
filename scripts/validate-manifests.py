#!/usr/bin/env python3
"""Validate marketplace, plugin manifests, docs links, and frontmatter."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_JSON = {
    ".claude-plugin/marketplace.json": ["plugins"],
    ".agents/plugins/marketplace.json": ["plugins"],
    "plugins/idea-to-product/.claude-plugin/plugin.json": ["name", "displayName", "commands", "hooks", "agents", "skills"],
    "plugins/idea-to-product/.codex-plugin/plugin.json": ["name", "skills", "interface"],
    "plugins/idea-to-product/hooks/hooks.claude.json": ["hooks"],
    "plugins/idea-to-product/hooks/hooks.codex.json": ["hooks"],
    "plugins/idea-to-product/hooks/hooks.claude.windows.json": ["hooks"],
    "plugins/idea-to-product/hooks/hooks.codex.windows.json": ["hooks"],
}

TEXT_EXTENSIONS = {".md", ".yaml", ".yml", ".py", ".sh", ".ps1"}
ABSOLUTE_LOCAL_PATH = re.compile(r"/Users/[^\\s)]+")


def load_json(relative: str, failures: list[str]) -> dict | None:
    path = ROOT / relative
    if not path.exists():
        failures.append(f"missing: {relative}")
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"invalid json: {relative}: {exc}")
        return None


def validate_json_files(failures: list[str]) -> None:
    for relative, keys in REQUIRED_JSON.items():
        data = load_json(relative, failures)
        if data is None:
            continue
        missing_keys = [key for key in keys if key not in data]
        if missing_keys:
            failures.append(f"missing keys in {relative}: {', '.join(missing_keys)}")


def validate_plugin_names_and_paths(failures: list[str]) -> None:
    claude = load_json("plugins/idea-to-product/.claude-plugin/plugin.json", failures)
    codex = load_json("plugins/idea-to-product/.codex-plugin/plugin.json", failures)

    if claude and claude.get("name") != "idea-to-product":
        failures.append("Claude plugin name must be idea-to-product")
    if codex and codex.get("name") != "idea-to-product":
        failures.append("Codex plugin name must be idea-to-product")

    if codex:
        for key in ("skills",):
            value = codex.get(key)
            if isinstance(value, str) and not value.startswith("./"):
                failures.append(f"Codex manifest path {key} must start with ./")

    marketplace = load_json(".agents/plugins/marketplace.json", failures)
    if marketplace:
        plugins = marketplace.get("plugins", [])
        if not plugins:
            failures.append("Codex marketplace must contain plugins[]")
        for plugin in plugins:
            source = plugin.get("source", {})
            if source.get("path") != "./plugins/idea-to-product":
                failures.append("Codex marketplace source.path must be ./plugins/idea-to-product")


def validate_no_absolute_local_paths(failures: list[str]) -> None:
    scan_roots = [ROOT / "README.md", ROOT / "README.ko.md", ROOT / "PLUGIN.md", ROOT / "FILE_MANIFEST.md", ROOT / "plugins" / "idea-to-product"]
    for scan_root in scan_roots:
        paths = [scan_root] if scan_root.is_file() else sorted(scan_root.rglob("*"))
        for path in paths:
            if not path.is_file() or path.suffix not in {".md", ".json", ".yaml", ".yml"}:
                continue
            text = path.read_text(encoding="utf-8")
            if ABSOLUTE_LOCAL_PATH.search(text):
                failures.append(f"local absolute path found in {path.relative_to(ROOT)}")


def frontmatter_block(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def validate_frontmatter(failures: list[str]) -> None:
    for path in sorted((ROOT / "plugins" / "idea-to-product" / "skills").glob("*/SKILL.md")):
        text = path.read_text(encoding="utf-8")
        block = frontmatter_block(text)
        if block is None:
            failures.append(f"SKILL frontmatter missing or malformed: {path.relative_to(ROOT)}")
            continue
        for key in ("name:", "description:"):
            if key not in block:
                failures.append(f"SKILL frontmatter missing {key} {path.relative_to(ROOT)}")

    for path in sorted((ROOT / "plugins" / "idea-to-product" / "agents").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        block = frontmatter_block(text)
        if block is None:
            failures.append(f"Agent frontmatter missing or malformed: {path.relative_to(ROOT)}")
            continue
        for key in ("name:", "description:", "model:", "effort:", "maxTurns:"):
            if key not in block:
                failures.append(f"Agent frontmatter missing {key} {path.relative_to(ROOT)}")


def validate_linebreak_health(failures: list[str]) -> None:
    for path in sorted(ROOT.rglob("*")):
        if ".git" in path.parts or not path.is_file() or path.suffix not in TEXT_EXTENSIONS:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        lines = text.splitlines()
        relative = path.relative_to(ROOT)
        if len(lines) == 1 and len(text) > 160:
            failures.append(f"suspicious one-line file: {relative}")
        if path.suffix == ".py" and lines and lines[0].startswith("#!") and '"""' in lines[0]:
            failures.append(f"Python shebang/docstring are on the same line: {relative}")


def main() -> int:
    failures: list[str] = []
    validate_json_files(failures)
    validate_plugin_names_and_paths(failures)
    validate_no_absolute_local_paths(failures)
    validate_frontmatter(failures)
    validate_linebreak_health(failures)

    if failures:
        print("Manifest validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Manifest validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
