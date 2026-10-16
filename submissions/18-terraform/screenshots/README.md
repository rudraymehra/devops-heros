# Session 18 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 7. New native files awaiting visual review: 0.

## Fresh execution records

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- [Session 18 — Terraform format check](rudray-20261016-212856-656600/01-format.txt): PASS.
- [Session 18 — actual Terraform validate (not apply)](rudray-20261016-212856-656600/02-validate.txt): FAILED / BLOCKED.
- AWS plan/apply/output/destroy screenshots: NOT RUN: Old lab destroyed; no cloud apply/destroy performed.
- Reference-specific pending items: NOT RUN: Original S3 apply/destroy logs exist, but native images were not captured. Validation now is not proof of that earlier apply/destroy. No paid lab is recreated automatically..


## Existing historical evidence

- [OUTPUT.md](../OUTPUT.md)
- [DESTROY-RETRY.md](../DESTROY-RETRY.md)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

Original S3 apply/destroy logs exist, but native images were not captured. Validation now is not proof of that earlier apply/destroy. No paid lab is recreated automatically.

Use the [coursework capture guide](../../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

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
