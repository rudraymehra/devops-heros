# Session 17 Submission

`demo/` provides the application, tests, Dockerfile, Kubernetes resources, security
documentation, and pipeline source. The repository-root workflow
`.github/workflows/session17-devsecops.yml` runs the monorepo version.

Security controls covered:

- Bandit SAST for Python source
- pip-audit SCA for Python dependencies
- Gitleaks secret scanning
- Trivy filesystem and container scanning
- Build/test/scan gates before publishing an image
- Kubernetes rollout verification after deployment

## Evidence checklist

- [x] Tests and coverage output — GitHub Actions run 40083592566 passed all 10 tests.
- [x] Bandit SAST and pip-audit SCA — passed in run 40083592566.
- [ ] Gitleaks, Trivy image scan, and Kubernetes rollout — run 40083592566's repo-wide Gitleaks scan found historical matches in unrelated Session 12 training materials, so downstream image and deploy jobs were skipped. The workflow now scans Session 17's full Git history only; a new Actions run is still needed to verify the changed workflow and downstream jobs.
- [ ] GHCR image page with commit-SHA tag
- [x] Explain the Gitleaks gate result and its impact; no secret values are reproduced here.
- [ ] Native screenshots from the actual scans and deployment (see `submissions/17-devsecops/screenshots/README.md`).

The manual dispatch does not publish to GHCR; publishing is restricted to a push
to `main`. The screenshot checklist is tracked in the repository-root
`COURSEWORK-SCREENSHOT-TRACKER.md`.
