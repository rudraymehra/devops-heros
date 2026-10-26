# Session 19 live AWS run — 2026-10-24

Rudray Mehra | 24 BCS 10425 | Batch B

This run used the AWS CLI profile already configured on the machine and a unique
project suffix. The full Terraform output is in
[`session19-live-run.txt`](session19-live-run.txt); 12-digit account identifiers
were redacted. The exact-resource cleanup checks are in
[`cleanup-check.txt`](cleanup-check.txt).

## Results

- `terraform init`, `fmt -check`, `validate`, and the 11-resource plan completed.
- `terraform apply` created the lab VPC, subnet, route table, internet gateway,
  security group, one `t3.micro` EC2 instance, and private versioned encrypted S3
  bucket with all four public-access-block settings enabled.
- The EC2 user-data page returned HTTP successfully and displayed Rudray Mehra,
  student ID, and batch.
- `terraform destroy` removed all 11 resources and Terraform state was empty.
- Follow-up AWS API queries found no lab instance, attached EBS volume, VPC,
  security group, NAT gateway, or lab bucket.

The apply ran briefly and may incur small AWS charges. The lab resources are now
destroyed. This is not a claim that unrelated AWS account resources are absent.

Seven Terminal images were generated from saved log excerpts, then visually
checked. Their command sections did not consistently match their filenames, so
they are explicitly rejected in the screenshot inventory and native review
record. Do not submit them as screenshots. The live execution logs remain useful
as text evidence, but this submission still needs correctly framed native
screenshots and an architecture diagram.
