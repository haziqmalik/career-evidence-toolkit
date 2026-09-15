---
name: master-resume-maintainer
description: Initialize or update a comprehensive master resume from approved career evidence. Use when the user asks to create, refresh, reconcile, correct, or enrich their long-form career source of truth; do not use for a short job-specific resume.
---

# Master Resume Maintainer

Maintain a comprehensive, evidence-backed source of truth. The master resume has no artificial one- or two-page limit.

Read [references/evidence-policy.md](references/evidence-policy.md) before accepting claims. Read [references/document-model.md](references/document-model.md) before creating or restructuring the document.

## Modes

- `INITIALIZE`: create the first master resume and evidence inventory.
- `UPDATE`: compare new evidence with the current master and change only missing, stale, weaker, duplicated, or incorrect material.

## Workflow

1. Resolve the private configuration and canonical destination. If updating, read the current master first.
2. Read only user-approved sources. Build a semantic inventory of existing and candidate claims.
3. Classify each candidate as `ADD`, `ENRICH`, `CORRECT`, `IGNORE`, or `NEEDS CONFIRMATION`.
4. Accept material evidence: meaningful capability, ownership, architecture, leadership, production responsibility, verified scale, major project, employment change, education, or certification.
5. Reject routine ticket churn, speculative work, unsupported metrics, credential secrets, confidential data, and technology exposure with no meaningful use.
6. Draft factual accomplishment language using action, system or problem, personal contribution, and verified outcome or scale.
7. Preserve exact historical titles and distinguish personal ownership, team contribution, and company outcomes.
8. Show consequential corrections or unresolved conflicts before writing. Edit only when the configured permission allows it.
9. Re-read the result for duplication, chronology, attribution, maturity, unsupported claims, and storage consistency.

## Completion

Summarize added, enriched, corrected, unresolved, and intentionally skipped material. If nothing meaningful changed, say so.
