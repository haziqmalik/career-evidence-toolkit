# Career Evidence Toolkit

Career Evidence Toolkit is an open-source set of agent skills for maintaining a verified career record and turning it into truthful, role-specific resumes.

It helps you:

- create and maintain a comprehensive master resume;
- reconcile professional certificates and credential evidence;
- generate ATS and executive resumes for a job title or vacancy;
- select relevant work experience, projects, and credentials without inventing claims;
- keep personal career data outside the public plugin repository.

## What is included

The plugin bundles six skills:

1. `career-onboarding` — configures storage, evidence sources, permissions, and templates.
2. `master-resume-maintainer` — initializes or updates the comprehensive career source of truth.
3. `certificate-registry-sync` — audits certificates and maintains a deduplicated registry.
4. `targeted-resume-generator` — creates role-title or vacancy-specific application resumes.
5. `ats-professional-resume` — produces conventional, ATS-safe resumes.
6. `executive-technical-resume` — produces selective, human-facing senior resumes.

## Install

### Install from the repository marketplace

```bash
codex plugin marketplace add haziqmalik/career-evidence-toolkit
```

Open the Plugins directory, select the `Career Evidence Toolkit` marketplace, install the plugin, and start a new chat.

### Fork for development

Fork this repository on GitHub, then clone your fork:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/career-evidence-toolkit.git
cd career-evidence-toolkit
codex plugin marketplace add .
```

Forking is optional. If the toolkit helps you, consider starring the repository so other people can find it.

## Start onboarding

After installation, use:

```text
Use $career-onboarding to set up my private career workspace. Explain each external access or write before doing it. Keep my personal information outside the plugin repository. Help me import an existing CV, public professional profiles, project evidence, and certificate files; initialize and validate my master resume; then help me approve or customize the bundled resume templates.
```

Onboarding requires one durable private storage location. This may be a local folder, Google Drive, ChatGPT Library, Dropbox, or another storage system available to your agent.

The toolkit never needs passwords, API keys, access tokens, or other secrets. In this project, “credentials” means professional certificates and public credential records.

## Typical future requests

```text
Update my master resume with my recent completed work.
```

```text
Synchronize my professional certificates and show me discrepancies.
```

```text
Create an ATS resume for a Senior Backend Engineer role.
```

```text
Analyze this vacancy and create both resume versions using only verified evidence: [job URL or description]
```

```text
Create an Executive resume for a Solution Architect position. Prioritize cloud architecture, delivery leadership, and the most relevant three projects.
```

## Privacy model

The plugin contains workflows and blank templates only. Your career workspace must live outside this repository. Never commit resumes, certificates, profile photographs, contact information, application records, or generated documents here.

External profiles and connected storage must be accessed only with the user's permission. Read-only discovery does not authorize uploads, edits, renames, repository actions, or public sharing.

See [SECURITY.md](SECURITY.md) for reporting and data-safety guidance.

## Template customization

During onboarding, you can:

- approve the bundled ATS and Executive templates;
- choose an accent color and modest typography adjustments; or
- provide your own `.docx` template.

An uploaded template must be cloned and sanitized. The original remains unchanged. Personal text is replaced with placeholders, document metadata is removed, and the resulting template is rendered for approval before adoption.

## Development

Validate the complete repository with:

```bash
python3 plugins/career-evidence-toolkit/scripts/validate_repo.py .
```

Sanitize a Word template with:

```bash
python3 plugins/career-evidence-toolkit/scripts/sanitize_docx.py input.docx output.docx
```

## License

Licensed under Apache-2.0. User-provided career data and generated resumes remain the user's content.
