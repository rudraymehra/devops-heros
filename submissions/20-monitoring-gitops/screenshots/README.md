# Session 20 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 15. Native captures: 0 accepted; 0 awaiting review; 0 rejected.

## Fresh execution records

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Live Kubernetes/Helm/monitoring capture: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.
- Reference-specific pending items: NOT RUN: Targets/dashboard/self-healing have historical evidence. New alert firing/recovery, cAdvisor and live cluster captures are not proven by those images; the cloud cluster is offline..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [prometheus-targets.png](../../../session21-python/evidence/observability/prometheus-targets.png)
- [grafana-dashboard.png](../../../session21-python/evidence/observability/grafana-dashboard.png)
- [argocd-synced.png](../../../session21-python/evidence/observability/argocd-synced.png)
- [eks-verification.md](../../../session21-python/evidence/eks-verification.md)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

Targets/dashboard/self-healing have historical evidence. New alert firing/recovery, cAdvisor and live cluster captures are not proven by those images; the cloud cluster is offline.

Use the [coursework capture guide](../../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/argocd-login.png`
- `screenshots/cadvisor.png`
- `screenshots/grafana-dashboard.png`
- `screenshots/prometheus-alerts-firing.png`
- `screenshots/prometheus-cpu-graph.png`
- `screenshots/prometheus-targets.png`
- `screenshots/task1-alerts-01.png`
- `screenshots/task1-cpu-memory-app-health-01.png`
- `screenshots/task1-kubernetes-metrics-logs-01.png`
- `screenshots/task1-prometheus-targets-metrics-01.png`
- `screenshots/task1-prometheus-targets-metrics-02.png`
- `screenshots/task3-argocd-api-01.png`
- `screenshots/task3-argocd-app-sync-01.png`
- `screenshots/task3-argocd-app-sync-02.png`
- `screenshots/task3-argocd-self-heal-01.png`

## Checked source files

- [prometheus.yml](../../../session20-monitoring-observability-gitops/03-prometheus/prometheus.yml)
- [application.yaml](../../../session21-python/gitops/application.yaml)
