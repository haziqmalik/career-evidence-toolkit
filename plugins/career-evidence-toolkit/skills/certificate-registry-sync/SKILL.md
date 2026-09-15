---
name: certificate-registry-sync
description: Audit professional certificate files and public credential records, maintain a deduplicated certification registry, and report discrepancies with a master resume or professional profile. Use when the user asks to check, sync, enrich, organize, or reconcile certificates.
---

# Certificate Registry Sync

Maintain verified professional credential evidence without assuming one provider contains the complete archive.

Read [references/registry-schema.md](references/registry-schema.md) before creating or changing a registry.

## Modes

- `AUDIT`: read approved sources and report findings without external writes.
- `SYNC`: update the registry and approved archive after confirming write scope.

## Source roles

- Stored certificate file: primary evidence that an artifact is archived.
- Public verification page: primary evidence for title, issuer, date, and credential ID.
- Official course page: enrichment for description, objectives, and provider-listed skills.
- Professional profile: discovery and reconciliation source.
- Master resume: reconciliation target, not primary certificate authority.

## Workflow

1. Resolve approved certificate locations and registry destination.
2. Inventory certificate files without deleting anything.
3. Inspect approved profiles and public credential links when accessible.
4. Match records by credential ID; otherwise use normalized platform, issuer, title, and date.
5. Preserve discrepancies until a stronger source resolves them.
6. Separate provider-listed `Official Skills` from conservative `Resume Skills`.
7. In `SYNC` mode, update registry rows and rename only clearly matched files when explicitly authorized. Never delete evidence automatically.
8. Report verified, enriched, missing-file, missing-profile, duplicate, conflicting, and unresolved records.

If master-resume editing was not explicitly requested, report resume discrepancies without changing the resume.
