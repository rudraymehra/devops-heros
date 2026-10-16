# Session 11 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 7. Native captures: 0 accepted; 0 awaiting review; 0 rejected.

## Fresh execution records

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Live Kubernetes/Helm/monitoring capture: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.
- Reference-specific pending items: NOT RUN: Capture five Service types, DNS/HTTP and endpoint checks; an external LoadBalancer address needs a real controller/tunnel, not an invented IP..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- Live Kubernetes/Helm/monitoring capture: NOT RUN: No explicit --kube-context provided; historical EKS lab was destroyed.
- Reference-specific pending items: NOT RUN: Capture five Service types, DNS/HTTP and endpoint checks; an external LoadBalancer address needs a real controller/tunnel, not an invented IP..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [OUTPUT.md](../OUTPUT.md)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

Capture five Service types, DNS/HTTP and endpoint checks; an external LoadBalancer address needs a real controller/tunnel, not an invented IP.

Use the [coursework capture guide](../../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/01-clusterip-01.png`
- `screenshots/02-nodeport-01.png`
- `screenshots/03-loadbalancer-01.png`
- `screenshots/03-loadbalancer-02.png`
- `screenshots/04-externalname-01.png`
- `screenshots/05-headless-01.png`
- `screenshots/05-headless-02.png`

## Checked source files

- [services.yaml](../services.yaml)
