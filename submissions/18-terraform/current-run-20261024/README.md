# Session 18 local Terraform run — 2026-10-24

Terraform 1.17.0 initialized the local working directory, `fmt -check -recursive` passed, and `validate` passed. The four-resource S3 plan was applied, the bucket configuration/state/outputs were queried, and the four resources were destroyed. The plan file was outside the repository at `/tmp/session18.tfplan`.

Post-destroy `terraform state list` is empty and the bucket is absent from AWS.
The account-wide check across all 17 enabled regions found no EC2 instances,
EBS volumes, Elastic IPs, NAT gateways, RDS instances, EKS clusters, or load
balancers. Cost Explorer showed the same pre-existing $0.30 EC2-Other amount
before and after; it showed no S3 cost. The AWS budget is configured with a
$150 monthly limit but its three notification rules have no subscribers.

Outputs are raw command logs from this run; they are not native screenshots.
