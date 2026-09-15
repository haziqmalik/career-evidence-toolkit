# Contributing

Contributions are welcome when they improve truthful evidence handling, portability, document quality, accessibility, privacy, onboarding, testing, or documentation.

## Good places to start

Look for issues labeled `good first issue`, `help wanted`, `documentation`, or `enhancement`. The project roadmap also lists planned work that can be discussed before implementation.

Useful contribution areas include:

- synthetic behavioral test fixtures;
- rendered template regression checks;
- accessibility validation guidance;
- storage/provider workflow documentation;
- import/export helpers;
- documentation and examples; and
- improvements to validation and contributor tooling.

## Before opening a pull request

1. Do not add real resumes, contact information, account identifiers, certificates, profile photographs, private URLs, application records, or other personal career data.
2. Keep examples and fixtures synthetic.
3. Keep each skill focused on one recognizable user goal.
4. Put conditional detail in `references/` instead of expanding every `SKILL.md`.
5. Preserve explicit permission boundaries around external reads and writes.
6. Do not weaken claim-strength rules to make generated resumes appear more impressive.
7. Run `python3 plugins/career-evidence-toolkit/scripts/validate_repo.py .`.
8. Test changed document templates by rendering every page.
9. Update documentation or the changelog when behavior changes materially.

## Issues

Use the repository issue forms for bugs and feature requests. Reproduction examples must be synthetic or fully redacted. Security vulnerabilities should follow [SECURITY.md](SECURITY.md) rather than being reported publicly.

## Pull requests

Keep pull requests focused. Explain the user problem, the behavior being changed, how it was validated, and any privacy or compatibility implications.

Changes to skills should preserve the project's evidence-first model. Changes to templates should be validated both structurally and visually.

## Community standard

Participation in this project is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
