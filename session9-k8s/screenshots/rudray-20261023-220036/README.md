# Session 09 — Kubernetes lifecycle lab

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshots supplied by the user.

The isolated Minikube node became Ready. The `kubernetes-bootcamp` Deployment and NodePort Service were created; the service returned HTTP 200 with v1 initially and after scaling to three replicas, v2 after image update, and v1 after `rollout undo`. Pod listings show replacement ReplicaSet pods through the rollouts. The helper removed the isolated profile after verification.

- [Cluster, deployment, scale, and update](01-cluster-deploy-scale-update.png)
- [Rollback verified back to v1](02-rollout-rollback-v1.png)
