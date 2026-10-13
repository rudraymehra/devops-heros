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

- [ ] Architecture diagram and plan summary
- [ ] VPC, subnet, route, security group, EC2, and S3 resource views
- [ ] Web response and Terraform outputs
- [ ] Successful destroy output
