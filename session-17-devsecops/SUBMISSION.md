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

- [ ] Tests and coverage output
- [ ] SAST, SCA, secret, and image scan results
- [ ] GHCR image page with commit-SHA tag
- [ ] Kubernetes rollout and application response
- [ ] Explanation of one finding or a clean result
