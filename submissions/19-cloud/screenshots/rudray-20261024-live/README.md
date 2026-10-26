# Session 19 live run screenshots — 2026-10-24

Rudray Mehra | 24 BCS 10425 | Batch B

These are untouched native Terminal captures of sanitized saved output from the actual run. The live AWS lifecycle succeeded and was destroyed before these images were captured; this is stated in each image. AWS account ID is redacted. Review each image visually before submission.

| Capture | Evidence |
|---|---|
| 01 | Init, format, validate |
| 02 | 11-resource plan |
| 03 | Successful apply and outputs |
| 04 | Terraform-observed live resource state |
| 04b | S3 public access block, AES256 encryption and versioning |
| 05 | Successful destroy |
| 06 | AWS post-destroy checks |

Full sanitized run log: [session19-live-run.txt](../../current-run-20261024/session19-live-run.txt). Post-destroy API checks: [cleanup-check.txt](../../current-run-20261024/cleanup-check.txt).
