# Development and Contributing

Contributions are welcome, but the repository has unusually important privacy and evidence-integrity constraints because it is intended to work with personal career data.

## Local setup

Fork the repository, clone your fork, and add it as a local plugin marketplace:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/career-evidence-toolkit.git
cd career-evidence-toolkit
codex plugin marketplace add .
```

## Repository validation

Run the complete repository validator before opening a pull request:

```bash
python3 plugins/career-evidence-toolkit/scripts/validate_repo.py .
```

## Word template sanitization

To sanitize a custom Word template during development:

```bash
python3 plugins/career-evidence-toolkit/scripts/sanitize_docx.py input.docx output.docx
```

Render and inspect every page of changed document templates before treating them as valid.

## Contribution rules

1. Do not add real resumes, contact information, account identifiers, certificates, profile photographs, or private URLs.
2. Keep each skill focused on one recognizable user goal.
3. Put conditional or extended detail in `references/` instead of making every `SKILL.md` excessively long.
4. Preserve explicit permission boundaries around external reads and writes.
5. Preserve evidence-first behavior and avoid instructions that encourage unsupported resume claims.
6. Run repository validation before submitting changes.
7. Test changed document templates through rendering, not just file-level inspection.

## Good contribution areas

Useful contributions include:

- improving evidence reconciliation;
- strengthening validation;
- making skill instructions clearer;
- adding privacy-safe examples;
- improving ATS compatibility;
- improving reusable template quality;
- documenting supported workflows;
- fixing portability issues across agent environments.

## Pull requests

Keep changes focused and explain the user problem being solved. For behavior changes, document how the change affects evidence integrity, permissions, privacy, or generated output.

Before contributing, read [CONTRIBUTING.md](https://github.com/haziqmalik/career-evidence-toolkit/blob/main/CONTRIBUTING.md), [SECURITY.md](https://github.com/haziqmalik/career-evidence-toolkit/blob/main/SECURITY.md), and [PRIVACY.md](https://github.com/haziqmalik/career-evidence-toolkit/blob/main/PRIVACY.md).
