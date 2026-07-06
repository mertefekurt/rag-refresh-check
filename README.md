<img src="assets/readme-cover.svg" alt="RAG Refresh Check cover" width="100%" />

# RAG Refresh Check

Check RAG index refresh plans for stale documents and missing rebuild triggers.

![stack](https://img.shields.io/badge/stack-Python-be185d?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-4b5563?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-2563eb?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-16a34a?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `rag-refresh-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `stale-refresh` | high | index refresh is stale |
| `missing-trigger` | medium | rebuild trigger missing |
| `high-stale-docs` | low | stale docs noted |

## Command line

```bash
python -m pip install -e ".[dev]"
rag-refresh-check examples/sample.txt
rag-refresh-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
last_refresh 2024 rebuild_trigger none stale_docs high
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```
