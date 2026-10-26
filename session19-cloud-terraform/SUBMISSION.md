# Session 19 Submission

`08-mini-project/` provisions an end-to-end AWS lab: VPC, public subnet, Internet
Gateway, route table, security group, EC2 web server, and private S3 bucket. Variables,
outputs, explicit/implicit dependencies, state, plan/apply, and destroy are covered.

## Safe workflow

```bash
cd 08-mini-project
cp terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan -out=tfplan
terraform apply tfplan
terraform output
curl "$(terraform output -raw web_url)"
terraform destroy
```

## Evidence checklist

### Current live run — 2026-10-24

- [x] `terraform init`, format, validate, and 11-resource plan.
- [x] Apply to AWS and verify the personalized NGINX page over HTTP.
- [x] Terraform state/output and S3 public-access, encryption, and versioning configuration recorded.
- [x] Destroy all 11 resources; verify empty state and run exact-resource AWS cleanup checks.
- [x] Architecture diagram source at [`submissions/19-cloud/architecture-diagram.md`](../submissions/19-cloud/architecture-diagram.md).
- [ ] Correctly framed native screenshots. The generated images were visually rejected because their content did not match the labels; see [the audit](../submissions/19-cloud/screenshots/README.md).

The full sanitized transcript is at `../submissions/19-cloud/current-run-20261024/session19-live-run.txt`.
The live AWS resources were destroyed after verification.

- [ ] Architecture diagram and plan summary
- [ ] VPC, subnet, route, security group, EC2, and S3 resource views
- [ ] Web response and Terraform outputs
- [ ] Successful destroy output
