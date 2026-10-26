# Session 09 — initial Kubernetes attempt

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshots supplied by the user.

The isolated Minikube profile started. The initial node listing was captured before the node became Ready; the deployment and NodePort Service were created and the initial request returned HTTP 200. During scale to three replicas, the service request reset. Image update and rollback were not reached, so this attempt is incomplete. The later run records the recovery.

- [Cluster and initial scale attempt](01-cluster-and-initial-scale-attempt.png)
- [Scale service reset](02-scale-service-reset.png)
