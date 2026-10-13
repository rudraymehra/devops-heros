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

- [ ] `terraform validate` and plan output
- [ ] S3 bucket shown in AWS
- [ ] `terraform state list` and outputs
- [ ] Successful destroy output
