# CampusFix security gates

The root workflow runs these checks before publishing images:

| Gate | What it checks | Failure behaviour |
|---|---|---|
| Pytest | Domain workflow and API behaviour | Stops downstream jobs |
| Bandit | Python source for insecure patterns | Blocks medium/high findings |
| pip-audit / npm audit | Dependency advisories | Blocks vulnerable Python dependencies or high/critical Node advisories |
| Gitleaks | Repository history for credentials | Blocks detected secrets |
| Trivy | OS and application packages in both images | Blocks HIGH/CRITICAL vulnerabilities, including unfixed findings |

Reports from each image scan are uploaded as workflow artifacts even on failure.
The workflow never uses `continue-on-error` to bypass a security gate.

Local reports describe the image actually scanned and its architecture; the GitHub
runner scans its own freshly built image. A clean scan means no matching advisories
were found in that scan's database, not proof that the image can never be vulnerable.

The application is an educational, unauthenticated maintenance desk. Use synthetic
reports in this lab. A real campus rollout needs authentication, permissions,
backups, HTTPS and access controls before collecting operational data.
