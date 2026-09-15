# Certification registry schema

Use these columns where the storage format supports them:

1. Credential ID
2. Certificate Title
3. Provider / Issuer
4. Platform
5. Credential Type
6. Issue Date
7. Credential URL
8. Course / Specialization URL
9. Official Description
10. Learning Objectives
11. Official Skills
12. Resume Skills
13. Evidence File ID or Path
14. Evidence File Name
15. Profile Status
16. Resume Status
17. Verification Status
18. Last Verified
19. Notes

Primary identity is credential ID. When absent, use normalized platform, provider, title, and issue date. Do not merge records merely because titles are similar.

Preferred evidence filename:

```text
{Certificate Title} - {Provider} - {Credential ID}.{ext}
```

Omit the credential-ID segment when no verified ID exists.
