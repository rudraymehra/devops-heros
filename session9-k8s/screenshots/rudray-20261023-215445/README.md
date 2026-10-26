# Session 09 — Kubernetes rollout attempt

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshots supplied by the user.

The Ready Minikube node ran the deployment and NodePort Service. The Service returned HTTP 200 at v1 initially and after scaling to three replicas. Updating the image to v2 succeeded, and `kubectl rollout undo` reported a successful rollback. The endpoint nevertheless returned `v=2` immediately afterward while old pods were terminating. The app-level rollback is therefore not yet verified; the helper now waits for the expected version before passing each stage.

- [Cluster, deploy, and scale](01-cluster-deploy-and-scale.png)
- [Image update and rollback attempt](02-update-and-rollback-attempt.png)
