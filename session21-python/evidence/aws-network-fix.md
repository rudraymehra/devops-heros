# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:23:54.076438+00:00

Working directory: session21-python/terraform

```text
$ /tmp/campusfix-tools.FCoLVB/terraform apply -auto-approve -no-color
module.eks.data.aws_caller_identity.current[0]: Reading...
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.eks.module.kms.data.aws_partition.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Reading...
module.eks.module.kms.data.aws_caller_identity.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Reading...
module.eks.data.aws_partition.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.vpc.aws_vpc.this[0]: Refreshing state... [id=vpc-0b236660178acfe8c]
module.eks.aws_cloudwatch_log_group.this[0]: Refreshing state... [id=/aws/eks/sudhir-campusfix/cluster]
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Read complete after 0s [id=aws]
module.eks.module.kms.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2830595799]
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2560088296]
module.eks.aws_iam_role.this[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002]
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001]
module.eks.data.aws_iam_policy_document.custom[0]: Reading...
module.eks.data.aws_iam_policy_document.custom[0]: Read complete after 0s [id=513122117]
module.eks.aws_iam_policy.custom[0]: Refreshing state... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003]
module.eks.module.kms.data.aws_caller_identity.current[0]: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Read complete after 1s [id=[AWS_ACCOUNT_ID]]
module.eks.data.aws_caller_identity.current[0]: Read complete after 1s [id=[AWS_ACCOUNT_ID]]
module.eks.data.aws_iam_session_context.current[0]: Reading...
module.eks.data.aws_iam_session_context.current[0]: Read complete after 0s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.vpc.aws_internet_gateway.this[0]: Refreshing state... [id=igw-040d3c722f60f7daa]
module.vpc.aws_default_security_group.this[0]: Refreshing state... [id=sg-0f6d08c531be0d121]
module.vpc.aws_default_route_table.default[0]: Refreshing state... [id=rtb-09e2e3d49bb09de16]
module.eks.aws_security_group.cluster[0]: Refreshing state... [id=sg-0522074d7a5b86fe2]
module.vpc.aws_default_network_acl.this[0]: Refreshing state... [id=acl-041c4574a017016e1]
module.vpc.aws_subnet.private[0]: Refreshing state... [id=subnet-082b0fed2e03ccecf]
module.eks.aws_security_group.node[0]: Refreshing state... [id=sg-0cc92304f43995481]
module.vpc.aws_subnet.private[1]: Refreshing state... [id=subnet-04516a733d2088208]
module.vpc.aws_subnet.public[0]: Refreshing state... [id=subnet-0e2b1c27fe01362e1]
module.vpc.aws_subnet.public[1]: Refreshing state... [id=subnet-07d6c3997d4cef561]
module.vpc.aws_route_table.private[0]: Refreshing state... [id=rtb-07bfe9cc9e0aaff90]
module.vpc.aws_route_table.public[0]: Refreshing state... [id=rtb-0b9aab65ac4e4a3ba]
module.vpc.aws_eip.nat[0]: Refreshing state... [id=eipalloc-04a90e0128a0fddda]
module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"]: Refreshing state... [id=sgrule-4151595338]
module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"]: Refreshing state... [id=sgrule-3019032963]
module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"]: Refreshing state... [id=sgrule-223191551]
module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"]: Refreshing state... [id=sgrule-1395389093]
module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"]: Refreshing state... [id=sgrule-2163456516]
module.eks.aws_security_group_rule.node["egress_all"]: Refreshing state... [id=sgrule-390060527]
module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"]: Refreshing state... [id=sgrule-2058399253]
module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"]: Refreshing state... [id=sgrule-1777111604]
module.eks.aws_security_group_rule.node["ingress_cluster_443"]: Refreshing state... [id=sgrule-4251643989]
module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"]: Refreshing state... [id=sgrule-3292919307]
module.eks.aws_security_group_rule.cluster["ingress_nodes_443"]: Refreshing state... [id=sgrule-3797039093]
module.vpc.aws_route.public_internet_gateway[0]: Refreshing state... [id=r-rtb-0b9aab65ac4e4a3ba1080289494]
module.vpc.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-06f506a745155caff]
module.vpc.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-0dfdf06c56b879db3]
module.vpc.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-02fcb8b002b37c001]
module.vpc.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-062fd51226d12561a]
module.vpc.aws_nat_gateway.this[0]: Refreshing state... [id=nat-0385c62146773d8ce]
module.vpc.aws_route.private_nat_gateway[0]: Refreshing state... [id=r-rtb-07bfe9cc9e0aaff901080289494]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116561000000008]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116557100000007]
module.eks.aws_iam_role_policy_attachment.custom[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116581800000009]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116235800000004]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116243100000005]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116283300000006]
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Reading...
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Read complete after 0s [id=729080925]
module.eks.module.kms.aws_kms_key.this[0]: Refreshing state... [id=37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c]
module.eks.module.kms.aws_kms_alias.this["cluster"]: Refreshing state... [id=alias/eks/sudhir-campusfix]
module.eks.aws_iam_policy.cluster_encryption[0]: Refreshing state... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a]
module.eks.aws_eks_cluster.this[0]: Refreshing state... [id=sudhir-campusfix]
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-2026101302214389440000000b]
module.eks.aws_eks_access_entry.this["cluster_creator"]: Refreshing state... [id=sudhir-campusfix:arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Refreshing state... [id=sg-00c2059b40e40b1b0,ManagedBy]
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Refreshing state... [id=sg-00c2059b40e40b1b0,Environment]
module.eks.data.tls_certificate.this[0]: Reading...
module.eks.time_sleep.this[0]: Refreshing state... [id=2026-10-13T02:30:21Z]
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Refreshing state... [id=3032463307649055476]
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Refreshing state... [id=lt-0c342f02f8398c6cc]
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Refreshing state... [id=sudhir-campusfix#arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli#arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Refreshing state... [id=sudhir-campusfix:main-20261013023027045600000010]
module.eks.data.tls_certificate.this[0]: Still reading... [00m10s elapsed]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the
last "terraform apply" which may have affected this plan:

  # module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0] has changed
  ~ resource "aws_eks_node_group" "this" {
        id                     = "sudhir-campusfix:main-20261013023027045600000010"
      + labels                 = {}
        tags                   = {
            "Environment" = "dev"
            "ManagedBy"   = "Terraform"
            "Name"        = "main"
        }
        # (15 unchanged attributes hidden)

        # (4 unchanged blocks hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the
relevant attributes using ignore_changes, the following plan may include
actions to undo or respond to these changes.

─────────────────────────────────────────────────────────────────────────────

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform planned the following actions, but then encountered a problem:

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

Error: Failed to identify fetch peer certificates

  with module.eks.data.tls_certificate.this[0],
  on .terraform/modules/eks/main.tf line 412, in data "tls_certificate" "this":
 412: data "tls_certificate" "this" {

failed to fetch certificates from URL 'https': Get
"https://oidc.eks.ap-south-1.amazonaws.com:443/id/C8FE139F4147098CE5611530B3ADF3F5":
dial tcp: lookup oidc.eks.ap-south-1.amazonaws.com: no such host

```

Exit code: 1
