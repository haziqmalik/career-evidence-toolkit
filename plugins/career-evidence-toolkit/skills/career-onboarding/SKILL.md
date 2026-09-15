---
name: career-onboarding
description: Set up a private career workspace, import approved professional evidence, initialize a master resume, and approve resume templates. Use for first-time Career Evidence Toolkit setup or when the user asks to reconfigure its storage, sources, or templates.
---

# Career Onboarding

Configure the toolkit without placing personal data inside the plugin repository.

## Boundaries

- Require one durable private storage destination before generating career files.
- Explain the exact source and intended use before accessing an external profile or account.
- Treat public-profile review, authenticated-profile review, uploads, file organization, and document writes as separate permissions.
- Never request passwords, one-time codes, API keys, tokens, private keys, or payment information.
- “Credentials” in this workflow means professional certificates, not authentication secrets.
- Do not fork, clone, star, publish, share, or change repository visibility without explicit authorization for that action.

Read [references/onboarding-flow.md](references/onboarding-flow.md) for the staged interview. Read [references/workspace-contract.md](references/workspace-contract.md) before creating the workspace.

## Workflow

1. Detect available storage and profile/document capabilities. Do not claim a connector is available until a harmless read confirms it.
2. Ask the questions in short stages: identity, profiles, storage, existing evidence, career direction, permissions, and templates.
3. Show the proposed workspace location and structure. Create it only after approval.
4. Import or link only user-approved sources. Preserve originals.
5. Create a structured evidence inventory that records source, confidence, attribution, date precision, maturity, and verification status.
6. Invoke `master-resume-maintainer` in `INITIALIZE` mode. Do not mark the result canonical until factual and document validation pass and the user approves it.
7. Audit certificate evidence with `certificate-registry-sync`. Write or organize files only when authorized.
8. Preview the bundled ATS and Executive templates. Let the user approve the defaults, make restrained customization, or provide a `.docx` template.
9. For a custom template, preserve the original, sanitize a clone, replace personal content with placeholders, render every page, and obtain approval before activation.
10. Verify that the six bundled skills are discoverable. Provide storage, evidence, master-resume, registry, template, integration, and future-command status.

## Completion

Return a concise onboarding report. Never include sensitive source contents in the report merely to prove they were read.
