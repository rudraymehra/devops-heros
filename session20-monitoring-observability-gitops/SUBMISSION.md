# Session 20 Submission

The numbered labs document monitoring, the metrics/logs/traces pillars, Prometheus,
Grafana, declarative GitOps, and Argo CD. `08-mini-project/` combines a namespace,
Deployment, Service, and Argo CD Application.

## Demonstration flow

1. Create the Kind cluster and install Argo CD.
2. Push workload manifests to your GitOps repository.
3. Confirm the repository URL in `08-mini-project/argocd-application.yaml`.
4. Apply the Application and verify `Synced`/`Healthy`.
5. Change replicas from two to three in Git and push.
6. Observe Argo CD reconcile the Deployment without manual `kubectl apply`.

## Evidence checklist

- [ ] Monitoring metrics, logs, and an alert example
- [ ] Prometheus target shown as `UP`
- [ ] Grafana panel with live data
- [ ] Argo CD Application `Synced` and `Healthy`
- [ ] Git commit and automatic two-to-three replica reconciliation
