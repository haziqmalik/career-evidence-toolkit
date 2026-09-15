# Getting Started

This guide takes you from installation to your first evidence-backed resume.

## 1. Install the toolkit

### ChatGPT Plugins Directory

The recommended installation path is the ChatGPT Plugins Directory. Open the Career Evidence Toolkit listing, select **Install**, then start a new chat so the plugin skills are available.

### Repository marketplace

For development or manual installation:

```bash
codex plugin marketplace add haziqmalik/career-evidence-toolkit --ref v0.1.0
```

Then open the Plugins directory, select the Career Evidence Toolkit marketplace, install it, and start a new chat.

### Local development

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/career-evidence-toolkit.git
cd career-evidence-toolkit
codex plugin marketplace add .
```

## 2. Run onboarding

Start with:

```text
Use $career-onboarding to set up my private career workspace. Explain each external access or write before doing it. Keep my personal information outside the plugin repository. Help me import an existing CV, public professional profiles, project evidence, and certificate files; initialize and validate my master resume; then help me approve or customize the bundled resume templates.
```

## 3. Choose private storage

Onboarding needs one durable storage location for your career workspace. Examples include:

- a local folder;
- Google Drive;
- ChatGPT Library;
- Dropbox;
- another storage system available to your agent.

Do not store personal resumes, certificates, contact information, profile photographs, application records, or generated documents in the public plugin repository.

## 4. Build your source of truth

The toolkit will help establish a comprehensive master resume containing verified experience, projects, education, skills, and credentials. This long-form document is the source used to produce shorter application resumes.

## 5. Generate a targeted resume

Examples:

```text
Create an ATS resume for a Senior Backend Engineer role.
```

```text
Analyze this vacancy and create both resume versions using only verified evidence: [job URL or description]
```

```text
Create an Executive resume for a Solution Architect position. Prioritize cloud architecture, delivery leadership, and the most relevant three projects.
```

## What to expect

The toolkit should ask before external writes, preserve claim strength, avoid unsupported achievements, and prefer relevant verified evidence over keyword stuffing.

Next: [How It Works](How-It-Works)
