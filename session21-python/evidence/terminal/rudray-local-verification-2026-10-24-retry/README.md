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
| M7 — Terraform validation (not cloud execution) | PASS | [Output](04-terraform-validate.txt) | NOT CAPTURED |
| M7 — new Terraform plan | NOT RUN: Not requested or validation failed; historical plan remains separate | — | NOT CAPTURED |
| M4 — Docker client and server | PASS | [Output](05-docker-engine.txt) | NOT CAPTURED |
| M4 — build and start frontend/backend/PostgreSQL | PASS | [Output](06-compose-start.txt) | NOT CAPTURED |
| M4 — actual Compose service status | PASS | [Output](07-compose-status.txt) | NOT CAPTURED |
| M4 — backend non-root UID (must not be 0) | PASS | [Output](08-nonroot-backend.txt) | NOT CAPTURED |
| M4 — frontend non-root UID (must not be 0) | PASS | [Output](08-nonroot-frontend.txt) | NOT CAPTURED |
| M1 — migration revision in real PostgreSQL stack | PASS | [Output](09-alembic.txt) | NOT CAPTURED |
| M1 — live FastAPI health | PASS | [Output](10-health.txt) | NOT CAPTURED |
| M1 — real database/schema readiness | PASS | [Output](11-ready.txt) | NOT CAPTURED |
| M1 — live maintenance REST API | PASS | [Output](12-api.txt) | NOT CAPTURED |
| M9 — live Prometheus metrics (not evidence of a cluster scrape) | PASS | [Output](13-metrics.txt) | NOT CAPTURED |
| Kubernetes/Helm deployment | NOT RUN: No explicit --kube-context supplied; the earlier AWS lab was destroyed | — | NOT CAPTURED |
| AWS Console/destroy | NOT RUN: Historical logs exist; no new paid lab authorized or run by this helper | — | NOT CAPTURED |
| CI/Trivy/GHCR and cluster monitoring | NOT RUN: Requires actual pipeline/browser evidence; local checks do not substitute | — | NOT CAPTURED |

An exit code of zero proves only the named command succeeded.
Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.
No AWS resources were created or removed by this helper.
