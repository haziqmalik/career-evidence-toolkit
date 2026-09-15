# FAQ

## Is Career Evidence Toolkit a resume-writing prompt collection?

No. It is a set of agent skills organized around maintaining a durable career evidence record and generating targeted resumes from that record.

## Does it invent experience to match a job description?

It should not. The job description is used to decide which verified evidence deserves emphasis. Missing evidence should remain a gap unless the user provides supporting information.

## Where is my career data stored?

In a private workspace selected during onboarding, such as a local folder, Google Drive, ChatGPT Library, Dropbox, or another supported storage system. Personal career data should not be committed to the public plugin repository.

## Does the toolkit need my passwords or API keys?

No. It does not need account secrets. In this project, “credentials” means professional certificates and public credential records.

## Can I start with an existing CV?

Yes. Existing CVs and resumes are useful evidence sources. The onboarding and master-resume workflows can use them as a starting point and reconcile them with other sources.

## Can it use LinkedIn or other professional profiles?

Yes, when the relevant profile is available to the agent and the user authorizes access. Reading a profile does not authorize editing or republishing it.

## What is the master resume?

It is the comprehensive long-form source of truth used to generate shorter, role-specific application resumes. It is not intended to be sent unchanged to every employer.

## Why keep a separate certificate registry?

Certificate files and public credential records can become duplicated or inconsistent over time. A registry provides a normalized list that can be checked before credentials are copied into a resume.

## What is the difference between ATS and Executive resumes?

The ATS version prioritizes conventional structure and machine parsing. The Executive / Senior Technical version uses more selective editorial hierarchy for senior human readers. Both should use the same verified career facts.

## Can I use my own Word resume template?

Yes. The toolkit should clone and sanitize it first, removing personal text and document metadata while preserving the reusable design. The sanitized template should be rendered for approval before adoption.

## Can I generate a generic resume without a job description?

Yes. A role title such as “Senior Full Stack Engineer” or “Solution Architect” can be used as the targeting context.

## Can I generate a resume for a specific vacancy?

Yes. Provide the vacancy text or URL when the agent can access it. The toolkit can analyze the requirements and select relevant verified evidence.

## Does it guarantee ATS success or job interviews?

No. ATS systems, employer processes, and hiring decisions vary. The toolkit is intended to improve evidence quality, relevance, document structure, and consistency—not to guarantee an outcome.

## How do I report a bug or request help?

Use the repository's issue tracker and consult [SUPPORT.md](https://github.com/haziqmalik/career-evidence-toolkit/blob/main/SUPPORT.md) for the supported channels and expectations.
