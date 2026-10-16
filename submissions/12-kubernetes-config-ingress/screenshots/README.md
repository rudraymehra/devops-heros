# Session 12 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 11. Native captures: 0 accepted; 0 awaiting review; 0 rejected.

## Fresh execution records

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Live Kubernetes/Helm/monitoring capture: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.
- Reference-specific pending items: NOT RUN: Capture ConfigMap/Secret metadata and actual ingress requests, plus the failure/recovery exercises. Never screenshot decoded real Secret values..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- Live Kubernetes/Helm/monitoring capture: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.
- Reference-specific pending items: NOT RUN: Capture ConfigMap/Secret metadata and actual ingress requests, plus the failure/recovery exercises. Never screenshot decoded real Secret values..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [OUTPUT.md](../OUTPUT.md)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

Capture ConfigMap/Secret metadata and actual ingress requests, plus the failure/recovery exercises. Never screenshot decoded real Secret values.

Use the [coursework capture guide](../../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/task1-configmap-01.png`
- `screenshots/task1-configmap-02.png`
- `screenshots/task1-configmap-03.png`
- `screenshots/task2-secret-01.png`
- `screenshots/task2-secret-02.png`
- `screenshots/task3-ingress-01.png`
- `screenshots/task3-ingress-02.png`
- `screenshots/task3-ingress-03.png`
- `screenshots/task5-troubleshooting-ingress-503-01.png`
- `screenshots/task5-troubleshooting-secret-newline-01.png`
- `screenshots/task5-troubleshooting-secret-newline-02.png`

## Checked source files

- [app.yaml](../app.yaml)
- [configmap.yaml](../configmap.yaml)
- [secret.yaml](../secret.yaml)
- [ingress.yaml](../ingress.yaml)
