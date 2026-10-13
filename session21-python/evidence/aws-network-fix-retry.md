# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:34:18.423129+00:00

Working directory: session21-python/terraform

```text
$ /tmp/campusfix-tools.FCoLVB/terraform apply '-target=module.eks.aws_security_group_rule.node["ingress_http_self"]' -auto-approve -no-color
module.vpc.aws_vpc.this[0]: Refreshing state... [id=vpc-0b236660178acfe8c]
module.eks.aws_security_group.cluster[0]: Refreshing state... [id=sg-0522074d7a5b86fe2]
module.eks.aws_security_group.node[0]: Refreshing state... [id=sg-0cc92304f43995481]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # module.eks.aws_security_group_rule.node["ingress_http_self"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "HTTP between application pods on worker nodes"
      + from_port                = 80
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = "sg-0cc92304f43995481"
      + security_group_rule_id   = (known after apply)
      + self                     = true
      + source_security_group_id = (known after apply)
      + to_port                  = 80
      + type                     = "ingress"
    }

Plan: 1 to add, 0 to change, 0 to destroy.
module.eks.aws_security_group_rule.node["ingress_http_self"]: Creating...
module.eks.aws_security_group_rule.node["ingress_http_self"]: Creation complete after 0s [id=sgrule-3554879769]

Warning: Resource targeting is in effect

You are creating a plan with the -target option, which means that the result
of this plan may not represent all of the changes requested by the current
configuration.

The -target option is not for routine use, and is provided only for
exceptional situations such as recovering from errors or mistakes, or when
Terraform specifically suggests to use it as part of an error message.

Warning: Applied changes may be incomplete

The plan was created with the -target option in effect, so some changes
requested in the configuration may have been ignored and the output values
may not be fully updated. Run the following command to verify that no other
changes are pending:
    terraform plan

Note that the -target option is not suitable for routine use, and is provided
only for exceptional situations such as recovering from errors or mistakes,
or when Terraform specifically suggests to use it as part of an error
message.

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.

Outputs:

cluster_endpoint = "https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com"
cluster_name = "sudhir-campusfix"
configure_kubectl = "aws eks update-kubeconfig --region ap-south-1 --name sudhir-campusfix"
vpc_id = "vpc-0b236660178acfe8c"

```

Exit code: 0
