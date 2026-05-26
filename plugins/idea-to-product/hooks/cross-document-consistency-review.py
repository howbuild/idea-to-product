#!/usr/bin/env python3
"""Check consistency across PRD, AC, POLICY, MEASUREMENT, DECISION_LOG, and REVIEW_REPORT."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

from hook_context import existing_files, print_skipped


REQUIRED = ["PRD.md", "AC.md", "POLICY.md", "MEASUREMENT.md", "DECISION_LOG.md", "REVIEW_REPORT.md"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def parse_tables(text: str) -> list[list[dict[str, str]]]:
    tables: list[list[dict[str, str]]] = []
    lines = [line.strip() for line in text.splitlines()]
    i = 0
    while i < len(lines) - 1:
        if not lines[i].startswith("|") or not lines[i + 1].startswith("|"):
            i += 1
            continue
        header = split_row(lines[i])
        separator = split_row(lines[i + 1])
        if not header or not all(set(cell) <= {"-", ":"} for cell in separator):
            i += 1
            continue
        rows: list[dict[str, str]] = []
        i += 2
        while i < len(lines) and lines[i].startswith("|"):
            values = split_row(lines[i])
            if len(values) == len(header):
                rows.append(dict(zip(header, values)))
            i += 1
        tables.append(rows)
    return tables


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def split_requirements(value: str) -> list[str]:
    if not value or value == "전체 문서":
        return []
    normalized = value.replace("、", ",").replace("，", ",")
    return [part.strip() for part in normalized.split(",") if part.strip()]


def requirement_rows(docs: dict[str, str]) -> dict[str, dict[str, dict[str, str]]]:
    result: dict[str, dict[str, dict[str, str]]] = {}
    for name, text in docs.items():
        rows: dict[str, dict[str, str]] = {}
        for table in parse_tables(text):
            for row in table:
                req_value = row.get("요구사항") or row.get("관련 요구사항") or ""
                for req in split_requirements(req_value):
                    rows[req] = row
        result[name] = rows
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-dir", default=".")
    parser.add_argument("--review-dir", default=os.environ.get("ITP_REVIEW_DIR", "reviews"))
    args = parser.parse_args()

    base = Path(args.base_dir)
    required_paths = [str(base / name) for name in REQUIRED]
    if not existing_files(required_paths):
        print_skipped("No Idea to Product final documents found; cross-document review was not written.")
        return 0

    docs = {name: read(base / name) for name in REQUIRED}
    missing_files = [name for name, text in docs.items() if not text]
    issues = []

    if "Given" not in docs["AC.md"] or "When" not in docs["AC.md"] or "Then" not in docs["AC.md"]:
        issues.append("AC does not clearly use Given / When / Then.")
    if "정책" in docs["PRD.md"] and "관련 AC" not in docs["POLICY.md"]:
        issues.append("POLICY should connect policies to AC.")
    if "이벤트" in docs["MEASUREMENT.md"] and "KPI" not in docs["PRD.md"]:
        issues.append("MEASUREMENT references events but PRD KPI is weak or missing.")
    if "보류" in docs["DECISION_LOG.md"] and "미결정" not in docs["PRD.md"]:
        issues.append("Decision log includes held items; PRD should keep unresolved items visible.")
    for term in ["Must-have", "Nice-to-have", "운영 의도", "확장 가능성"]:
        if term in docs["PRD.md"] and term not in docs["DECISION_LOG.md"]:
            issues.append(f"DECISION_LOG should preserve PRD term: {term}.")
    if "운영 의도" in docs["PRD.md"]:
        for name in ["POLICY.md", "MEASUREMENT.md", "AC.md", "REVIEW_REPORT.md"]:
            if "운영 의도" not in docs[name]:
                issues.append(f"{name} should preserve operating intent for related requirements.")
    if "확장 가능성" in docs["PRD.md"]:
        for name in ["POLICY.md", "MEASUREMENT.md", "AC.md", "DECISION_LOG.md", "REVIEW_REPORT.md"]:
            if "확장 가능성" not in docs[name]:
                issues.append(f"{name} should preserve scalability for related requirements.")

    rows_by_doc = requirement_rows(docs)
    prd_requirements = rows_by_doc.get("PRD.md", {})
    for name, rows in rows_by_doc.items():
        if name == "PRD.md":
            continue
        for req, row in rows.items():
            baseline = prd_requirements.get(req)
            if not baseline:
                issues.append(f"{name} references requirement not found in PRD: {req}.")
                continue
            for column in ["우선순위", "운영 의도", "확장 가능성"]:
                if not row.get(column):
                    continue
                if baseline.get(column) and row[column] != baseline[column]:
                    issues.append(f"{name} has different {column} for {req}: {row[column]} != {baseline[column]}.")

    review_dir = Path(args.review_dir)
    review_dir.mkdir(parents=True, exist_ok=True)
    report_path = review_dir / "cross-document-consistency-review.md"
    report_path.write_text(
        "\n".join(
            [
                "# Cross-Document Consistency Review",
                "",
                "## Missing Files",
                *(f"- {name}" for name in missing_files),
                "",
                "## Issues",
                *(f"- {issue}" for issue in issues),
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(json.dumps({"missing_files": missing_files, "issues": issues, "report_path": str(report_path)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
