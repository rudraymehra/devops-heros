# Session 18 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 7. Native captures: 7 accepted; 0 awaiting review; 0 rejected.

## Fresh execution record — 2026-10-24

- [Terraform version](../current-run-20261024/00-terraform-version.txt),
  [format check](../current-run-20261024/01-fmt-check.txt),
  [validate](../current-run-20261024/02-validate.txt), and
  [plan](../current-run-20261024/03-plan.txt): PASS.
- The plan created four S3 resources in `ap-south-1`: the bucket, public-access
  block, encryption configuration, and versioning. Bucket configuration and
  Terraform state/outputs were queried, then all four resources were destroyed.
- Post-destroy Terraform state is empty and AWS no longer lists the bucket.
- Account cleanup checks across all 17 enabled regions found no EC2 instances,
  EBS volumes, Elastic IPs, NAT gateways, RDS instances, EKS clusters, or load
  balancers. Cost Explorer showed the same pre-existing $0.30 EC2-Other October
  amount before and after; it showed no S3 cost. Existing account resources were
  not modified.
- Actual command logs and the cleanup audit are in
  [current-run-20261024](../current-run-20261024/README.md).
- The seven actual native Terminal captures are in
  [rudray-20261024-applycheck](rudray-20261024-applycheck/README.md). The apply
  and destroy screenshots show saved actual outputs captured after completion;
  the AWS settings image is explicitly labelled as a summary from saved API
  responses collected before deletion.

## Native screenshot inventory

The seven reference images have corresponding visually reviewed native captures:

1. `screenshots/01-init-fmt-validate-01.png` — Terraform init, format, validate.
2. `screenshots/02-plan-01.png` — the four-resource plan.
3. `screenshots/03-apply-01.png` — successful four-resource apply.
4. `screenshots/04-show-output-01.png` — `terraform state list` and outputs.
5. `screenshots/04-show-output-02.png` — AWS bucket security configuration.
6. `screenshots/05-destroy-01.png` — successful four-resource destroy.
7. `screenshots/05-destroy-02.png` — empty state and absent bucket after cleanup.

## Fresh execution records

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- [Session 18 — Terraform format check](rudray-20261016-212856-656600/01-format.txt): PASS.
- [Session 18 — actual Terraform validate (not apply)](rudray-20261016-212856-656600/02-validate.txt): FAILED / BLOCKED.
- AWS plan/apply/output/destroy screenshots: NOT RUN: Old lab destroyed; no cloud apply/destroy performed.
- Reference-specific pending items: NOT RUN: Original S3 apply/destroy logs exist, but native images were not captured. Validation now is not proof of that earlier apply/destroy. No paid lab is recreated automatically..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [OUTPUT.md](../OUTPUT.md)
- [DESTROY-RETRY.md](../DESTROY-RETRY.md)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Reference image inventory (not copied)

- `screenshots/01-init-fmt-validate-01.png`
- `screenshots/02-plan-01.png`
- `screenshots/03-apply-01.png`
- `screenshots/04-show-output-01.png`
- `screenshots/04-show-output-02.png`
- `screenshots/05-destroy-01.png`
- `screenshots/05-destroy-02.png`

## Checked source files

- [main.tf](../../../session18-terraform-iac/terraform-s3-demo/main.tf)
