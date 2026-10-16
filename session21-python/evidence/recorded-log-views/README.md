# Recorded execution log views — Rudray Mehra

24 BCS 10425 · Batch B.

These images render this repository's actual execution records. They are
**not native terminal captures, AWS Console screenshots, or newly executed cloud
commands**. Every image displays that distinction, the source path and checksum.
Line-numbered excerpts retain original commands, dates, identities and outcomes.
The AWS deployment shown in the historical records has been destroyed.

| View | Full source |
|---|---|
| [Terraform plan](terraform-plan.png) | [Original plan log](../aws-plan.md) |
| [Terraform destroy](terraform-destroy.png) | [Original destroy log](../aws-destroy.md) |
| [EKS Pods, Services and storage](eks-pods-services.png) | [Original verification log](../eks-verification.md) |
| [Helm installation](eks-helm-deployment.png) | [Original Helm deployment log](../eks-helm-deploy.md) |
| [Prometheus target results](prometheus-target-results.png) | [Original observability JSON](../observability/result.json) |
| [Local pytest run, 2026-10-16](pytest-2026-10-16.png) | [Captured command output](../pytest-2026-10-16.md) |

The original Mac test screenshot is separate: [native terminal evidence](../terminal/README.md).
Ask the instructor before treating rendered log views as substitutes for an
explicit screenshot-format requirement. The Helm view proves installation; it
does not fabricate a separate `helm list` command. The Prometheus view shows
selected recorded JSON fields, not a fabricated `curl /metrics` run.

Reproduce the views on macOS with Python and Command Line Tools installed.
Rendering is offline and does not access a browser, display capture, or network:

```bash
python session21-python/scripts/render-recorded-evidence.py
```

`manifest.json` records the source hashes and rendering timestamps. No supplied
reference ZIP image is used by the rendering script.
