# Session 12 Submission

## Completed deliverables

- ConfigMap creation and both environment/volume injection: `01-configmap/`
- Secret creation and Pod injection: `02-secret/`
- Host/path/TLS Ingress examples: `03-ingress/`
- Integrated frontend/backend demonstration: `04-full-demo/`
- Secret newline failure investigation: `troubleshooting/secret-base64-gotcha.md`
- Complete exercise workbook: `lab.md`

An Ingress is a routing API object. An Ingress controller is the running software
that watches those objects and configures a proxy/load balancer. Creating an Ingress
without a controller does not route traffic.

Secrets are base64-encoded, not encrypted by that encoding. Never commit production
credentials; use a secret manager, encryption at rest, RBAC, and short-lived access.

## Evidence checklist

- [x] ConfigMap values shown inside a Pod
- [x] Secret value shown safely (redact the real value)
- [x] Ingress host, path, and TLS routing responses
- [x] Broken-secret behavior and corrected behavior (disposable value; trailing `0a` shown safely)
- [x] `kubectl get ingress,configmap,secret,pods,svc`

For the ConfigMap environment and volume checks, use the two isolated Pods in
`01-configmap/configmap-env-pod.yaml` and
`01-configmap/configmap-volume-pod.yaml`; the step-by-step commands are in
`01-configmap/README.md`.
