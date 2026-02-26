# repo-audit

`repo-audit` is a portfolio-ready Python CLI app that analyzes a source repository and produces a security and structure report.

## Features

- Language composition by file extension
- Largest files (configurable threshold)
- Secret-like pattern detection (AWS key, private key headers, generic API key/token assignments)
- JSON and Markdown report export
- No third-party dependencies (Python standard library only)

## Run

```bash
cd /workspace/Home-Servers/portfolio-repo-audit
python3 -m repo_audit /workspace/Home-Servers --json out/report.json --md out/report.md
```

Or quick scan of current directory:

```bash
python3 -m repo_audit .
```

## CLI Options

- `--large-file-mb`: Threshold for large files (default `2.0`)
- `--max-text-scan-mb`: Max file size scanned as text for secrets (default `1.0`)
- `--top-large-files`: Number of largest files to include (default `10`)
- `--json`: Output path for JSON report
- `--md`: Output path for Markdown report

## Test

```bash
cd /workspace/Home-Servers/portfolio-repo-audit
python3 -m unittest discover -s tests -v
```
