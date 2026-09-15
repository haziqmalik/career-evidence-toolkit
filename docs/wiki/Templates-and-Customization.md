# Templates and Customization

Career Evidence Toolkit separates career content from document presentation. This makes it possible to change the visual style of a resume without changing the underlying evidence.

## Bundled templates

The toolkit includes two resume presentation modes:

### ATS Professional Resume

Designed for conventional application workflows and automated parsing.

Typical characteristics:

- restrained formatting;
- clear section hierarchy;
- single-column layout;
- minimal decorative elements;
- strong text extraction and parsing behavior;
- concise 1–2 page output where appropriate.

### Executive / Senior Technical Resume

Designed for senior technical and leadership roles where a human reader benefits from stronger editorial hierarchy.

Typical characteristics:

- selective project emphasis;
- clearer business and architecture context;
- stronger visual hierarchy;
- polished but professional presentation;
- emphasis on senior ownership and high-value evidence.

## Customization during onboarding

You can:

- approve the bundled templates as-is;
- choose an accent color;
- make modest typography adjustments; or
- provide your own `.docx` template.

## Using a custom Word template

A user-provided `.docx` template should be cloned and sanitized before use.

The sanitization process should:

1. preserve the original file unchanged;
2. replace personal text with placeholders;
3. remove document metadata;
4. preserve reusable layout and styling where possible;
5. render the sanitized result for review;
6. adopt it only after approval.

## Content before decoration

Template styling should never be used to hide poor content selection. The recommended order is:

```text
Verified evidence
  → target-specific selection
  → concise resume content
  → template application
  → rendered validation
```

## Page length

The toolkit is intended to produce focused application resumes rather than shrinking a master resume until everything fits. Less relevant evidence should be removed before typography is compressed.

## Validation

After customization, render every page and check:

- headings and dates align correctly;
- bullets are not clipped;
- page breaks are sensible;
- links remain usable;
- no placeholder text remains;
- text extraction still works for ATS-oriented output.
