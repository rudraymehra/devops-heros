# Session 17 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 14. Native captures: 0 accepted; 0 awaiting review; 0 rejected.

## Fresh execution records

### GitHub Actions run 40083592566

- Unit tests (10), Bandit, and pip-audit: PASS.
- Gitleaks: FAILED on historical matches in unrelated Session 12 training files;
  the image scan and Kubernetes smoke-test jobs were skipped. Secret values are
  intentionally not copied into this audit.
- The workflow was scoped to scan all commits affecting `session-17-devsecops/demo`.
  A local run of the same pinned Gitleaks command scanned four relevant commits
  and found no leaks. The updated GitHub workflow has not yet been rerun.
- GHCR publish: NOT RUN; this was a manual dispatch and the workflow only publishes
  on a push to `main`.
- This is log evidence only. No native screenshots were captured for this run.

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- [Session 17 — actual project tests](rudray-20261016-212856-656600/01-pytest.txt): FAILED / BLOCKED.
- [Session 17 — actual source scan](rudray-20261016-212856-656600/02-bandit.txt): PASS.
- CI/image/security/deployment screenshots: NOT RUN: Use actual jobs for the submitted SHA; local test success alone is not CI success.
- Reference-specific pending items: NOT RUN: Capture real unit/SAST/SCA/secret/image scan and deployment results. Before/after findings must come from real revisions; never invent a vulnerable scan..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [Earlier GitHub Actions run](https://github.com/rudraymehra/devops-heros/actions/runs/38342666869)
- [session17-ci.png](../../../session21-python/evidence/published/session17-ci.png)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

Capture real unit/SAST/SCA/secret/image scan and deployment results. Before/after findings must come from real revisions; never invent a vulnerable scan. For the current run, tests/Bandit/SCA can be captured as passes; Gitleaks should show its actual blocked result. Image scan and deployment need a successful rerun after the repository-scope issue is resolved.

Use the [coursework capture guide](../../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/01-build-unit-test-01.png`
- `screenshots/02-sast-bandit-after-01.png`
- `screenshots/02-sast-bandit-before-01.png`
- `screenshots/03-sca-pip-audit-after-01.png`
- `screenshots/03-sca-pip-audit-before-01.png`
- `screenshots/04-secret-scan-gitleaks-01.png`
- `screenshots/05-docker-build-01.png`
- `screenshots/06-image-scan-trivy-alpine-after-01.png`
- `screenshots/06-image-scan-trivy-debian-before-01.png`
- `screenshots/07-security-gate-01.png`
- `screenshots/08-deploy-kubernetes-after-01.png`
- `screenshots/08-deploy-kubernetes-before-01.png`
- `screenshots/09-act-pipeline-run-01.png`
- `screenshots/browser-dashboard.png`

## Checked source files

- [session17-devsecops.yml](../../../.github/workflows/session17-devsecops.yml)
- [test_app.py](../../../session-17-devsecops/demo/tests/test_app.py)
