from __future__ import annotations

import json
from pathlib import Path

from .models import AuditReport


def to_json(report: AuditReport) -> str:
    return json.dumps(report.to_dict(), indent=2)


def to_markdown(report: AuditReport) -> str:
    lines: list[str] = []
    lines.append("# Repository Audit Report")
    lines.append("")
    lines.append(f"- Root: `{report.root}`")
    lines.append(f"- Total files: `{report.total_files}`")
    lines.append(f"- Total size (bytes): `{report.total_bytes}`")
    lines.append("")

    lines.append("## Language Breakdown")
    lines.append("")
    for language, count in sorted(
        report.language_counts.items(), key=lambda item: item[1], reverse=True
    ):
        lines.append(f"- {language}: {count}")
    lines.append("")

    lines.append("## Largest Files")
    lines.append("")
    if report.large_files:
        for item in report.large_files:
            lines.append(f"- `{item.file}`: {item.bytes_size} bytes")
    else:
        lines.append("- None")
    lines.append("")

    lines.append("## Secret Findings")
    lines.append("")
    if report.secret_findings:
        for finding in report.secret_findings:
            lines.append(
                f"- [{finding.rule}] `{finding.file}`:{finding.line} -> `{finding.snippet}`"
            )
    else:
        lines.append("- None")

    return "\n".join(lines)


def write_if_requested(path: str | None, content: str) -> None:
    if not path:
        return
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")
