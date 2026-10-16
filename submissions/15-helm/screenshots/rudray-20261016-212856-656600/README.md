# Fresh command evidence

Rudray Mehra | 24 BCS 10425 | Batch B

These commands were actually executed. Logs are not screenshots.
Native images, if present, are untouched user-selected macOS window captures.
Check each image visually before submission; file creation alone does not prove its contents.

| Check | Execution | Log | Native screenshot |
|---|---|---|---|
| Session 15 — real chart lint (not install) | PASS | [Output](01-helm-lint.txt) | NOT CAPTURED |
| Session 15 — actual template rendering (not install) | PASS | [Output](02-helm-template.txt) | NOT CAPTURED |
| Live Kubernetes/Helm/monitoring capture | NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed | — | NOT CAPTURED |
| Reference-specific pending items | NOT RUN: Lint/template can run offline. Install, upgrade, history, rollback and uninstall screenshots require their actual lifecycle, not lint output. | — | NOT CAPTURED |

An exit code of zero proves only the named command succeeded.
Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.
No AWS resources were created or removed by this helper.
