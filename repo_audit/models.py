from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(slots=True)
class SecretFinding:
    rule: str
    file: Path
    line: int
    snippet: str


@dataclass(slots=True)
class LargeFile:
    file: Path
    bytes_size: int


@dataclass(slots=True)
class AuditReport:
    root: Path
    total_files: int = 0
    total_bytes: int = 0
    language_counts: dict[str, int] = field(default_factory=dict)
    large_files: list[LargeFile] = field(default_factory=list)
    secret_findings: list[SecretFinding] = field(default_factory=list)

    def to_dict(self) -> dict[str, object]:
        return {
            "root": str(self.root),
            "total_files": self.total_files,
            "total_bytes": self.total_bytes,
            "language_counts": dict(sorted(self.language_counts.items())),
            "large_files": [
                {"file": str(item.file), "bytes_size": item.bytes_size}
                for item in self.large_files
            ],
            "secret_findings": [
                {
                    "rule": finding.rule,
                    "file": str(finding.file),
                    "line": finding.line,
                    "snippet": finding.snippet,
                }
                for finding in self.secret_findings
            ],
        }
