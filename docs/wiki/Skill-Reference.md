# Skill Reference

Career Evidence Toolkit currently bundles six focused skills. Each skill has a distinct responsibility so evidence collection, maintenance, targeting, and presentation remain separate.

## `career-onboarding`

Use this first. It configures the private career workspace, identifies evidence sources, establishes permission boundaries, and helps approve or customize resume templates.

Typical request:

```text
Use $career-onboarding to set up my private career workspace.
```

## `master-resume-maintainer`

Maintains the comprehensive career source of truth. Use it to initialize a master resume, merge verified updates, correct stale information, and preserve useful historical evidence.

Typical request:

```text
Update my master resume with my recent completed work.
```

## `certificate-registry-sync`

Audits professional certificates and public credential records, then maintains a deduplicated credential registry. It is intended for professional credentials—not passwords, tokens, or secrets.

Typical request:

```text
Synchronize my professional certificates and show me discrepancies.
```

## `targeted-resume-generator`

Analyzes a role title or vacancy and selects the most relevant verified evidence from the master career record. It should preserve claim strength and avoid filling gaps with invented experience.

Typical request:

```text
Analyze this vacancy and create both resume versions using only verified evidence: [job URL or description]
```

## `ats-professional-resume`

Produces a conventional ATS-friendly resume with restrained formatting, clear hierarchy, and a structure suitable for automated parsing.

Typical request:

```text
Create an ATS resume for a Senior Backend Engineer role.
```

## `executive-technical-resume`

Produces a more selective, human-facing resume for senior technical, architecture, engineering leadership, and similar roles. It emphasizes evidence hierarchy, business context, and high-value projects rather than maximizing keyword density.

Typical request:

```text
Create an Executive resume for a Solution Architect position.
```

## Recommended sequence

For a new workspace:

```text
career-onboarding
  → master-resume-maintainer
  → certificate-registry-sync
  → targeted-resume-generator
  → ATS and/or Executive resume skill
```

For ongoing use, you normally only need the skill relevant to the current task. The master resume and certificate registry should be updated when the underlying evidence changes.
