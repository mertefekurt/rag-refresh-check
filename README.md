# rag-refresh-check

> Check RAG index refresh plans for stale documents and missing rebuild triggers.

## CI gate Overview

Check RAG index refresh plans for stale documents and missing rebuild triggers. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts RAG refresh plan. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
rag-refresh-check examples/sample.txt
rag-refresh-check examples/sample.txt --json --fail-on medium
python -m rag_refresh_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `stale-refresh` | high | index refresh is stale |
| `missing-trigger` | medium | rebuild trigger missing |
| `high-stale-docs` | low | stale docs noted |

## Validation Notes

```bash
ruff check .
pytest
python -m rag_refresh_check --help
```

Example risky input:

```text
last_refresh 2024 rebuild_trigger none stale_docs high
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
