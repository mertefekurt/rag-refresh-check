from __future__ import annotations

from rag_refresh_check.models import Rule

PROJECT_NAME = 'rag-refresh-check'
SUMMARY = 'Check RAG index refresh plans for stale documents and missing rebuild triggers.'
SAMPLE_RISK = 'last_refresh 2024 rebuild_trigger none stale_docs high'
SAMPLE_CLEAN = 'last_refresh 2026 rebuild_trigger docs_changed stale_docs low'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='stale-refresh',
        severity='high',
        pattern='last_refresh\\s+20(1[0-9]|2[0-4])',
        message='index refresh is stale',
        recommendation='schedule rebuild',
    ),
    Rule(
        code='missing-trigger',
        severity='medium',
        pattern='rebuild_trigger\\s+(none|missing|unknown)',
        message='rebuild trigger missing',
        recommendation='define rebuild trigger',
    ),
    Rule(
        code='high-stale-docs',
        severity='low',
        pattern='stale_docs\\s+high',
        message='stale docs noted',
        recommendation='measure and reduce stale documents',
    ),
)
