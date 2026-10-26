# Session 18 Submission

The `terraform-s3-demo/` project implements the complete S3 lifecycle exercise.
The `aws-services/` directory contains the five required research reports.

```bash
cd terraform-s3-demo
terraform init
terraform fmt -check
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform show
terraform output
terraform destroy
```

Do not commit credentials, `terraform.tfvars`, state, or `.terraform/`. Use a lab AWS
account, enable billing alerts, and destroy resources immediately after collecting
evidence.

## Evidence checklist

- [x] `terraform validate` and plan output — Terraform 1.17.0 validated the project and planned 4 resources (bucket, public-access block, encryption, versioning).
- [x] S3 bucket shown in AWS — its public-access block, encryption, and versioning were queried before cleanup.
- [x] `terraform state list` and outputs — all four resources and Terraform outputs were recorded before destroy.
- [x] Successful destroy output — Terraform destroyed all four resources; post-destroy state is empty and AWS no longer lists the bucket.
- [x] Seven native screenshots captured and visually reviewed — see `submissions/18-terraform/screenshots/rudray-20261024-applycheck/README.md`.

The plan used bucket name `rudraym-session18-iac-20261024` in `ap-south-1` and
was saved outside the repository at `/tmp/session18.tfplan`. The apply/destroy
lifecycle has now been run and verified. No Session 18 AWS resources remain.
Actual command logs are under `submissions/18-terraform/current-run-20261024/`;
the seven visually reviewed native captures are under
`submissions/18-terraform/screenshots/rudray-20261024-applycheck/`.
