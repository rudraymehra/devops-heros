# TaskBoard Monitoring

The FastAPI backend exposes Prometheus metrics at `/metrics`. The Helm chart creates
a `ServiceMonitor` when `monitoring.serviceMonitor.enabled=true`.

Install the monitoring stack and dashboard:

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm upgrade --install kube-prometheus-stack \
  prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace \
  -f prometheus-values.yaml
kubectl apply -f grafana-dashboard-configmap.yaml
kubectl get servicemonitor -n taskboard
kubectl get pods -n monitoring
```

Generate traffic with `scripts/load-test.sh`, then open Grafana and select the
TaskBoard Application dashboard. It includes request rate, HTTP 5xx ratio, and p95
request latency panels.

Evidence required: the Prometheus Targets page showing the backend as `UP`, the raw
`/metrics` response, and a Grafana screenshot with populated panels.
