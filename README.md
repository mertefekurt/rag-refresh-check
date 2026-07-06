# RAG Refresh Check

Check RAG index refresh plans for stale documents and missing rebuild triggers. The idea is simple: give RAG Refresh Check the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Project card

<img src="assets/readme-cover.svg" alt="RAG Refresh Check cover" width="100%" />

| Detail | Value |
| --- | --- |
| Area | model quality |
| Command | `rag-refresh-check` |
| Example | `examples/sample.txt` |

## What would make me stop a review

| Stopper | Level | Why it matters |
| --- | --- | --- |
| `stale-refresh` | high | index refresh is stale |
| `missing-trigger` | medium | rebuild trigger missing |
| `high-stale-docs` | low | stale docs noted |

## Run from a fresh clone

```bash
git clone https://github.com/mertefekurt/rag-refresh-check.git
cd rag-refresh-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
rag-refresh-check examples/sample.txt
rag-refresh-check examples/sample.txt --json
```
