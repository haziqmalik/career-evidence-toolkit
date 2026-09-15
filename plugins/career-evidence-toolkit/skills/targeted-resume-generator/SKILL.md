---
name: targeted-resume-generator
description: Analyze a target job title or specific vacancy against a verified master resume, select relevant evidence, and create truthful ATS or executive resumes. Use for generic role positioning, job descriptions, job URLs, recruiter requests, and application packages; do not silently update the master resume.
---

# Targeted Resume Generator

Use the current approved master resume and evidence inventory as the factual authority. A job description controls relevance and terminology, never candidate facts.

Read [references/analysis-and-selection.md](references/analysis-and-selection.md) before selecting content. Read [references/output-quality.md](references/output-quality.md) before generating documents.

## Modes

- `ROLE_TITLE`: create reusable positioning for a named job title without inventing an employer.
- `VACANCY`: analyze a complete job description or URL and target that opportunity.

## Workflow

1. Resolve mode, requested deliverables, template choice, and approved evidence source.
2. In vacancy mode, ingest the complete opportunity and preserve its URL when supplied.
3. Classify important requirements as `STRONG MATCH`, `PARTIAL MATCH`, or `NOT EVIDENCED`.
4. Recommend positioning and an application decision. Separate blocking gaps, learnable gaps, and irrelevant nice-to-haves.
5. Build an evidence budget. Every selected experience, project, credential, and skill must prove a target need.
6. Honor user selection preferences, but flag requested evidence that is weak, irrelevant, unverified, or redundant.
7. Choose one or two pages from evidence density. Two pages are a ceiling, not a target.
8. Invoke `ats-professional-resume`, `executive-technical-resume`, or both.
9. Render and inspect every page. Correct factual, semantic, pagination, and visual failures before delivery.
10. Report potentially valuable missing master evidence without modifying the master.

Historical titles remain exact. Target headlines may be adapted without pretending they were formal employment titles.
