# Fresh command evidence

Rudray Mehra | 24 BCS 10425 | Batch B

These commands were actually executed. Logs are not screenshots.
Native images, if present, are untouched user-selected macOS window captures.
Check each image visually before submission; file creation alone does not prove its contents.

| Check | Execution | Log | Native screenshot |
|---|---|---|---|
| M2 — actual isolated API tests | PASS | [Output](01-pytest.txt) | NOT CAPTURED |
| M1/M5 — React production build | PASS | [Output](02-frontend-build.txt) | NOT CAPTURED |
| M8 — Helm syntax check (not deployment) | PASS | [Output](03-helm-lint.txt) | NOT CAPTURED |
| M7 — Terraform validation (not cloud execution) | FAILED / BLOCKED | [Output](04-terraform-validate.txt) | NOT CAPTURED |
| Compose/live API/browser | NOT RUN: Not requested; add --compose to run this local lab | — | NOT CAPTURED |
| Kubernetes/Helm deployment | NOT RUN: No explicit --kube-context supplied; the earlier AWS lab was destroyed | — | NOT CAPTURED |
| AWS plan/Console/destroy | NOT RUN: Historical logs exist; no new paid lab authorized or run by this helper | — | NOT CAPTURED |
| CI/Trivy/GHCR and cluster monitoring | NOT RUN: Requires actual pipeline/browser evidence; local checks do not substitute | — | NOT CAPTURED |

An exit code of zero proves only the named command succeeded.
Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.
No AWS resources were created or removed by this helper.
