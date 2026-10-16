# Fresh command evidence — reviewed index

Rudray Mehra | 24 BCS 10425 | Batch B

Raw logs and capture manifests are unchanged. Visual decisions are hash-bound in
[the review record](../../../../evidence/coursework/native-review.json).
Rejected images remain local and are excluded from publication. A pass is only for the named command.

## Session 15 — real chart lint (not install)

Execution: PASS.

[Original command output](01-helm-lint.txt)

Native capture: **accepted**. Actual Helm lint output visible; not proof of installing a release.

![Reviewed native window capture](01-helm-lint.png)

## Session 15 — actual template rendering (not install)

Execution: PASS.

[Original command output](02-helm-template.txt)

Native capture: **accepted**. Actual rendered-manifest output tail visible; paired log gives command context. Not proof of a live deployment.

![Reviewed native window capture](02-helm-template.png)

## Live Kubernetes/Helm/monitoring capture

Execution: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.

Native capture: **not-captured**. No native image captured.

## Reference-specific pending items

Execution: NOT RUN: Lint/template can run offline. Install, upgrade, history, rollback and uninstall screenshots require their actual lifecycle, not lint output..

Native capture: **not-captured**. No native image captured.
