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

- [ ] ConfigMap values shown inside a Pod
- [ ] Secret value shown safely (redact the real value)
- [ ] Ingress host and path routing responses
- [ ] Broken-secret behavior and corrected behavior
- [ ] `kubectl get ingress,configmap,secret,pods,svc`
