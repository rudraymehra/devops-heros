# Coursework screenshot tracker

This tracks genuine screenshots required by the submission inventories. A command
log, generated log image, or reference image is not a native screenshot. Capture
screenshots from the actual run and keep secret values, tokens, and private data
out of frame.

| Session | Reference shots listed | Native captures accepted | Still required |
|---|---:|---:|---|
| 11 — Kubernetes Services | 7 | 13 | Native captures include ClusterIP, NodePort, LoadBalancer, ExternalName, headless DNS, and empty-endpoint troubleshooting. Review per-session submission checklist for any remaining requirements. |
| 12 — ConfigMaps, Secrets, Ingress | 11 | 6 | Native captures include ConfigMap injection, redacted Secret verification, HTTP/HTTPS host/path routing, TLS, and newline failure evidence. Review per-session submission checklist for remaining items. |
| 13 — Storage, HPA, probes | 9 | 0 | PVC persistence, HPA scale up/down, probe failure/recovery. |
| 14 — Troubleshooting | 15 | 0 | `kubectl get`, describe/logs/exec/events; config, ContainerCreating, CrashLoopBackOff, DNS, ImagePullBackOff, OOMKilled, Pending, Pod networking, Service, mini-project, cleanup. Current real run covered core cases but no screenshots were saved. |
| 15 — Helm | 11 | 2 | Install/list/status, upgrade/history/rollback/uninstall, rollback workflow, mini-project. Existing lint/template captures do not prove a release lifecycle. |
| 16 — GitHub Actions | 5 | 0 | Current tests/build and actual Actions run (tests, artifact, Docker build/deploy as applicable). Run 40083432667 is link/log evidence, not a screenshot. |
| 17 — DevSecOps | 14 | 0 | Tests; Bandit before/after; pip-audit before/after; Gitleaks; Docker build; Trivy before/after; gate; Kubernetes before/after; `act` run; browser dashboard. Only capture results that actually occurred. |
| 18 — Terraform | 7 | 7 | Real four-resource S3 apply/state/output/destroy completed and cleanup verified; all seven native screenshots are captured and visually reviewed. |
| 19 — Cloud Terraform | 8 | 0 accepted; 7 rejected | Live AWS apply/HTTP/destroy and exact-resource cleanup logs are saved; native screenshots need retaking. Authored topology diagram: `submissions/19-cloud/architecture-diagram.md`. See `submissions/19-cloud/current-run-20261024/`. |
| 20 — Monitoring/GitOps | 15 | 0 | Metrics/logs/alert; Prometheus target UP; Grafana live panel; Argo CD Synced/Healthy; Git-driven replica reconciliation. |
| 21 — Python capstone | See detailed audit | Partial | See `session21-python/evidence/SCREENSHOT-CHECKLIST.md`; authenticated AWS Console, Trivy job log, explicit native app/metrics/Terraform captures, and remaining items are still marked there. |
| 22 | None in the local coursework or Vivek reference repo | — | Reference repository ends at Session 21. No Session 22 materials or screenshot rubric were found. |

The per-session inventories in `submissions/*/screenshots/README.md` are the
source for the numbered reference-shot counts. Those references are not evidence
of our own run. No screenshot is marked complete merely because its command ran.
