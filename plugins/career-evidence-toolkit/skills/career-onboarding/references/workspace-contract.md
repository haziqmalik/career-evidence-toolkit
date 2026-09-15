# Private workspace contract

Use the storage provider's native equivalents for this logical structure:

```text
CareerProfile/
├── profile/
│   ├── profile.yaml
│   └── preferences.yaml
├── evidence/
│   ├── career-evidence.yaml
│   ├── employment/
│   ├── projects/
│   └── education/
├── certificates/
│   ├── originals/
│   └── certification-registry.xlsx
├── master-resume/
├── templates/
│   ├── ats/
│   └── executive/
├── applications/
└── exports/
```

Keep this workspace outside the public plugin repository. Do not delete or replace source evidence automatically. Store provider IDs in the private configuration, never in the public skill.
