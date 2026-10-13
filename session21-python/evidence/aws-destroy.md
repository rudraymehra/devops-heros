# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:51:47.107308+00:00

Working directory: session21-python/terraform

```text
$ /tmp/campusfix-tools.FCoLVB/terraform destroy -auto-approve -no-color
module.eks.module.kms.data.aws_caller_identity.current[0]: Reading...
module.eks.module.kms.data.aws_partition.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Reading...
module.eks.data.aws_caller_identity.current[0]: Reading...
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Reading...
module.eks.data.aws_partition.current[0]: Reading...
module.vpc.aws_vpc.this[0]: Refreshing state... [id=vpc-0b236660178acfe8c]
module.eks.aws_cloudwatch_log_group.this[0]: Refreshing state... [id=/aws/eks/sudhir-campusfix/cluster]
module.eks.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.module.kms.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Read complete after 0s [id=aws]
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2560088296]
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2830595799]
module.eks.aws_iam_role.this[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002]
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001]
module.eks.data.aws_iam_policy_document.custom[0]: Reading...
module.eks.data.aws_iam_policy_document.custom[0]: Read complete after 0s [id=513122117]
module.eks.aws_iam_policy.custom[0]: Refreshing state... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003]
module.eks.module.kms.data.aws_caller_identity.current[0]: Read complete after 1s [id=[AWS_ACCOUNT_ID]]
module.eks.data.aws_caller_identity.current[0]: Read complete after 1s [id=[AWS_ACCOUNT_ID]]
module.eks.data.aws_iam_session_context.current[0]: Reading...
module.eks.data.aws_iam_session_context.current[0]: Read complete after 0s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Read complete after 1s [id=[AWS_ACCOUNT_ID]]
module.vpc.aws_default_security_group.this[0]: Refreshing state... [id=sg-0f6d08c531be0d121]
module.vpc.aws_default_route_table.default[0]: Refreshing state... [id=rtb-09e2e3d49bb09de16]
module.vpc.aws_default_network_acl.this[0]: Refreshing state... [id=acl-041c4574a017016e1]
module.vpc.aws_route_table.public[0]: Refreshing state... [id=rtb-0b9aab65ac4e4a3ba]
module.vpc.aws_subnet.private[1]: Refreshing state... [id=subnet-04516a733d2088208]
module.vpc.aws_subnet.private[0]: Refreshing state... [id=subnet-082b0fed2e03ccecf]
module.vpc.aws_subnet.public[0]: Refreshing state... [id=subnet-0e2b1c27fe01362e1]
module.vpc.aws_subnet.public[1]: Refreshing state... [id=subnet-07d6c3997d4cef561]
module.vpc.aws_route_table.private[0]: Refreshing state... [id=rtb-07bfe9cc9e0aaff90]
module.eks.aws_security_group.node[0]: Refreshing state... [id=sg-0cc92304f43995481]
module.vpc.aws_internet_gateway.this[0]: Refreshing state... [id=igw-040d3c722f60f7daa]
module.eks.aws_security_group.cluster[0]: Refreshing state... [id=sg-0522074d7a5b86fe2]
module.vpc.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-0dfdf06c56b879db3]
module.vpc.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-06f506a745155caff]
module.vpc.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-02fcb8b002b37c001]
module.vpc.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-062fd51226d12561a]
module.vpc.aws_route.public_internet_gateway[0]: Refreshing state... [id=r-rtb-0b9aab65ac4e4a3ba1080289494]
module.eks.aws_security_group_rule.cluster["ingress_nodes_443"]: Refreshing state... [id=sgrule-3797039093]
module.vpc.aws_eip.nat[0]: Refreshing state... [id=eipalloc-04a90e0128a0fddda]
module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"]: Refreshing state... [id=sgrule-2163456516]
module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"]: Refreshing state... [id=sgrule-3019032963]
module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"]: Refreshing state... [id=sgrule-223191551]
module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"]: Refreshing state... [id=sgrule-4151595338]
module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"]: Refreshing state... [id=sgrule-1777111604]
module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"]: Refreshing state... [id=sgrule-1395389093]
module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"]: Refreshing state... [id=sgrule-3292919307]
module.eks.aws_security_group_rule.node["ingress_http_self"]: Refreshing state... [id=sgrule-3554879769]
module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"]: Refreshing state... [id=sgrule-2058399253]
module.eks.aws_security_group_rule.node["egress_all"]: Refreshing state... [id=sgrule-390060527]
module.eks.aws_security_group_rule.node["ingress_cluster_443"]: Refreshing state... [id=sgrule-4251643989]
module.vpc.aws_nat_gateway.this[0]: Refreshing state... [id=nat-0385c62146773d8ce]
module.vpc.aws_route.private_nat_gateway[0]: Refreshing state... [id=r-rtb-07bfe9cc9e0aaff901080289494]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116557100000007]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116561000000008]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116235800000004]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116243100000005]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Refreshing state... [id=main-eks-node-group-20261013022113872700000001-20261013022116283300000006]
module.eks.aws_iam_role_policy_attachment.custom[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116581800000009]
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Reading...
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Read complete after 0s [id=729080925]
module.eks.module.kms.aws_kms_key.this[0]: Refreshing state... [id=37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c]
module.eks.module.kms.aws_kms_alias.this["cluster"]: Refreshing state... [id=alias/eks/sudhir-campusfix]
module.eks.aws_iam_policy.cluster_encryption[0]: Refreshing state... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a]
module.eks.aws_eks_cluster.this[0]: Refreshing state... [id=sudhir-campusfix]
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Refreshing state... [id=sudhir-campusfix-cluster-20261013022113872700000002-2026101302214389440000000b]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Refreshing state... [id=sg-00c2059b40e40b1b0,ManagedBy]
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Refreshing state... [id=sg-00c2059b40e40b1b0,Environment]
module.eks.aws_eks_access_entry.this["cluster_creator"]: Refreshing state... [id=sudhir-campusfix:arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.eks.data.tls_certificate.this[0]: Reading...
module.eks.time_sleep.this[0]: Refreshing state... [id=2026-10-13T02:30:21Z]
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Refreshing state... [id=lt-0c342f02f8398c6cc]
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Refreshing state... [id=3032463307649055476]
module.eks.data.tls_certificate.this[0]: Read complete after 0s [id=1e3a331631939a1ae4a625cd4244a4963dabbfa2]
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Refreshing state... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5]
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Refreshing state... [id=sudhir-campusfix#arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli#arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Refreshing state... [id=sudhir-campusfix:main-20261013023027045600000010]
data.aws_iam_policy_document.ebs_csi_trust: Reading...
data.aws_iam_policy_document.ebs_csi_trust: Read complete after 0s [id=393383685]
aws_iam_role.ebs_csi: Refreshing state... [id=sudhir-campusfix-ebs-csi]
aws_iam_role_policy_attachment.ebs_csi: Refreshing state... [id=sudhir-campusfix-ebs-csi-2026101302300466330000000d]
module.eks.data.aws_eks_addon_version.this["coredns"]: Reading...
module.eks.data.aws_eks_addon_version.this["vpc-cni"]: Reading...
module.eks.data.aws_eks_addon_version.this["aws-ebs-csi-driver"]: Reading...
module.eks.data.aws_eks_addon_version.this["kube-proxy"]: Reading...
module.eks.data.aws_eks_addon_version.this["coredns"]: Read complete after 0s [id=coredns]
module.eks.data.aws_eks_addon_version.this["kube-proxy"]: Read complete after 0s [id=kube-proxy]
module.eks.data.aws_eks_addon_version.this["vpc-cni"]: Read complete after 0s [id=vpc-cni]
module.eks.data.aws_eks_addon_version.this["aws-ebs-csi-driver"]: Read complete after 0s [id=aws-ebs-csi-driver]
module.eks.aws_eks_addon.this["coredns"]: Refreshing state... [id=sudhir-campusfix:coredns]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Refreshing state... [id=sudhir-campusfix:aws-ebs-csi-driver]
module.eks.aws_eks_addon.this["kube-proxy"]: Refreshing state... [id=sudhir-campusfix:kube-proxy]
module.eks.aws_eks_addon.before_compute["vpc-cni"]: Refreshing state... [id=sudhir-campusfix:vpc-cni]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_iam_role.ebs_csi will be destroyed
  - resource "aws_iam_role" "ebs_csi" {
      - arn                   = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/sudhir-campusfix-ebs-csi" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "sts:AssumeRoleWithWebIdentity"
                      - Condition = {
                          - StringEquals = {
                              - "oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5:aud" = "sts.amazonaws.com"
                              - "oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5:sub" = "system:serviceaccount:kube-system:ebs-csi-controller-sa"
                            }
                        }
                      - Effect    = "Allow"
                      - Principal = {
                          - Federated = "arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5"
                        }
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2026-10-13T02:30:03Z" -> null
      - force_detach_policies = false -> null
      - id                    = "sudhir-campusfix-ebs-csi" -> null
      - managed_policy_arns   = [
          - "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy",
        ] -> null
      - max_session_duration  = 3600 -> null
      - name                  = "sudhir-campusfix-ebs-csi" -> null
      - path                  = "/" -> null
      - tags                  = {} -> null
      - tags_all              = {} -> null
      - unique_id             = "AROAQ3AHBKZXRQK6UPKSS" -> null
        # (3 unchanged attributes hidden)
    }

  # aws_iam_role_policy_attachment.ebs_csi will be destroyed
  - resource "aws_iam_role_policy_attachment" "ebs_csi" {
      - id         = "sudhir-campusfix-ebs-csi-2026101302300466330000000d" -> null
      - policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy" -> null
      - role       = "sudhir-campusfix-ebs-csi" -> null
    }

  # module.eks.aws_cloudwatch_log_group.this[0] will be destroyed
  - resource "aws_cloudwatch_log_group" "this" {
      - arn               = "arn:aws:logs:ap-south-1:[AWS_ACCOUNT_ID]:log-group:/aws/eks/sudhir-campusfix/cluster" -> null
      - id                = "/aws/eks/sudhir-campusfix/cluster" -> null
      - log_group_class   = "STANDARD" -> null
      - name              = "/aws/eks/sudhir-campusfix/cluster" -> null
      - retention_in_days = 90 -> null
      - skip_destroy      = false -> null
      - tags              = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "/aws/eks/sudhir-campusfix/cluster"
        } -> null
      - tags_all          = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "/aws/eks/sudhir-campusfix/cluster"
        } -> null
        # (2 unchanged attributes hidden)
    }

  # module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"] will be destroyed
  - resource "aws_ec2_tag" "cluster_primary_security_group" {
      - id          = "sg-00c2059b40e40b1b0,Environment" -> null
      - key         = "Environment" -> null
      - resource_id = "sg-00c2059b40e40b1b0" -> null
      - value       = "dev" -> null
    }

  # module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"] will be destroyed
  - resource "aws_ec2_tag" "cluster_primary_security_group" {
      - id          = "sg-00c2059b40e40b1b0,ManagedBy" -> null
      - key         = "ManagedBy" -> null
      - resource_id = "sg-00c2059b40e40b1b0" -> null
      - value       = "Terraform" -> null
    }

  # module.eks.aws_eks_access_entry.this["cluster_creator"] will be destroyed
  - resource "aws_eks_access_entry" "this" {
      - access_entry_arn  = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:access-entry/sudhir-campusfix/user/[AWS_ACCOUNT_ID]/rudray-cli/bcd0998c-22ef-c698-1c95-dbf67f30bc0f" -> null
      - cluster_name      = "sudhir-campusfix" -> null
      - created_at        = "2026-10-13T02:29:51Z" -> null
      - id                = "sudhir-campusfix:arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli" -> null
      - kubernetes_groups = [] -> null
      - modified_at       = "2026-10-13T02:29:51Z" -> null
      - principal_arn     = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli" -> null
      - tags              = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all          = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - type              = "STANDARD" -> null
      - user_name         = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli" -> null
    }

  # module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"] will be destroyed
  - resource "aws_eks_access_policy_association" "this" {
      - associated_at = "2026-10-13 02:29:51.931 +0000 UTC" -> null
      - cluster_name  = "sudhir-campusfix" -> null
      - id            = "sudhir-campusfix#arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli#arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy" -> null
      - modified_at   = "2026-10-13 02:29:51.931 +0000 UTC" -> null
      - policy_arn    = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy" -> null
      - principal_arn = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli" -> null

      - access_scope {
          - namespaces = [] -> null
          - type       = "cluster" -> null
        }
    }

  # module.eks.aws_eks_addon.before_compute["vpc-cni"] will be destroyed
  - resource "aws_eks_addon" "before_compute" {
      - addon_name                  = "vpc-cni" -> null
      - addon_version               = "v1.22.4-eksbuild.3" -> null
      - arn                         = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:addon/sudhir-campusfix/vpc-cni/84d0998c-3d4d-50bf-9460-4627e7439abc" -> null
      - cluster_name                = "sudhir-campusfix" -> null
      - created_at                  = "2026-10-13T02:30:04Z" -> null
      - id                          = "sudhir-campusfix:vpc-cni" -> null
      - modified_at                 = "2026-10-13T02:30:11Z" -> null
      - preserve                    = true -> null
      - resolve_conflicts_on_create = "OVERWRITE" -> null
      - resolve_conflicts_on_update = "OVERWRITE" -> null
      - tags                        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all                    = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
        # (2 unchanged attributes hidden)

      - timeouts {}
    }

  # module.eks.aws_eks_addon.this["aws-ebs-csi-driver"] will be destroyed
  - resource "aws_eks_addon" "this" {
      - addon_name                  = "aws-ebs-csi-driver" -> null
      - addon_version               = "v1.66.0-eksbuild.1" -> null
      - arn                         = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:addon/sudhir-campusfix/aws-ebs-csi-driver/2ad0998d-8d24-695d-0413-11a7b0fe6ab4" -> null
      - cluster_name                = "sudhir-campusfix" -> null
      - created_at                  = "2026-10-13T02:32:56Z" -> null
      - id                          = "sudhir-campusfix:aws-ebs-csi-driver" -> null
      - modified_at                 = "2026-10-13T02:33:33Z" -> null
      - preserve                    = true -> null
      - resolve_conflicts_on_create = "OVERWRITE" -> null
      - resolve_conflicts_on_update = "OVERWRITE" -> null
      - service_account_role_arn    = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/sudhir-campusfix-ebs-csi" -> null
      - tags                        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all                    = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
        # (1 unchanged attribute hidden)

      - timeouts {}
    }

  # module.eks.aws_eks_addon.this["coredns"] will be destroyed
  - resource "aws_eks_addon" "this" {
      - addon_name                  = "coredns" -> null
      - addon_version               = "v1.13.2-eksbuild.50" -> null
      - arn                         = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:addon/sudhir-campusfix/coredns/12d0998d-8d23-6b35-46e6-6dd58d5185ae" -> null
      - cluster_name                = "sudhir-campusfix" -> null
      - created_at                  = "2026-10-13T02:32:56Z" -> null
      - id                          = "sudhir-campusfix:coredns" -> null
      - modified_at                 = "2026-10-13T02:33:08Z" -> null
      - preserve                    = true -> null
      - resolve_conflicts_on_create = "OVERWRITE" -> null
      - resolve_conflicts_on_update = "OVERWRITE" -> null
      - tags                        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all                    = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
        # (2 unchanged attributes hidden)

      - timeouts {}
    }

  # module.eks.aws_eks_addon.this["kube-proxy"] will be destroyed
  - resource "aws_eks_addon" "this" {
      - addon_name                  = "kube-proxy" -> null
      - addon_version               = "v1.35.3-eksbuild.29" -> null
      - arn                         = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:addon/sudhir-campusfix/kube-proxy/d6d0998d-8d1e-b9f8-2614-c2357aa0b61f" -> null
      - cluster_name                = "sudhir-campusfix" -> null
      - created_at                  = "2026-10-13T02:32:56Z" -> null
      - id                          = "sudhir-campusfix:kube-proxy" -> null
      - modified_at                 = "2026-10-13T02:33:02Z" -> null
      - preserve                    = true -> null
      - resolve_conflicts_on_create = "OVERWRITE" -> null
      - resolve_conflicts_on_update = "OVERWRITE" -> null
      - tags                        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all                    = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
        # (2 unchanged attributes hidden)

      - timeouts {}
    }

  # module.eks.aws_eks_cluster.this[0] will be destroyed
  - resource "aws_eks_cluster" "this" {
      - arn                           = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:cluster/sudhir-campusfix" -> null
      - bootstrap_self_managed_addons = true -> null
      - certificate_authority         = [
          - {
              - data = "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURNVENDQWhtZ0F3SUJBZ0lRRTBENXFWd3ZkVjVDZi9hSFlDd2R2akFOQmdrcWhraUc5dzBCQVFzRkFEQW4KTVJBd0RnWURWUVFLRXdkQlYxTWdSVXRUTVJNd0VRWURWUVFERXdwcmRXSmxjbTVsZEdWek1CNFhEVEkyTVRBeApNekF5TWpJd05Wb1hEVE14TVRBeE1qQXlNakl3TlZvd0p6RVFNQTRHQTFVRUNoTUhRVmRUSUVWTFV6RVRNQkVHCkExVUVBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUIKQUtvdmJTTGRvSFRUNld0TUVqRStOU0d3RVE5VHl3SXZLR1Y4V2NWS1FSaUdQZ3daa0xNcStTS1FmU1ZUQTdyMwpMak9lL3NpUjhYLy9NQkgyQWlRNmlKWVF6QUVpZzFMWDVhbVp6bkVwc0NkNENsNnNaa01BNUdqK21rdzV4RjBYCmRmWGh5bTRTTjJ5WmtSMElaRjUwZE96eWp2Q3lnVXZHN2VUZEVNNHRNN09MbFpoVEN3emI0MEdTMlQ4bWRHY0gKQmlaQXNTOU5tWVR4TXRiREo3dEtFVVkxeWZ4L0lhL3JVMEx5dnRDSEtBNFdkTEJLdkpkeENMR2M0M0JpREZSYwpoREtOTDVYSlpXQU1jL2hXTVh6R0ZNWlRhMUhnZGRaN0MzWHBTY2daRnZZWlhIQWJWbnpuN3ZvT3czQitUWXdWCmFtUWF6Z3Z1VkxZVUVGS203NHo2RWljQ0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWQKRXdFQi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZLeDI5ZnEvOTBabzVoSXVJdjMveHdpZXd6VWVNQlVHQTFVZApFUVFPTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBRUtpV0VZNjdjMFQzL1VSCitXNVFESk9YN3VtRkt3Y21Gb3lhbGkzMkNoY3RNMkR2UENyOXZDVGM5c0FoYmg2b21nbXNrTGR4VVI5WlpEUFUKZ09TSzFJOG1WR1FSRThZVEgvTTI4WUhkb0o2a3ZCUXNQNXVHaVc1QzN3QzBWUUY1eHp0aFM0RDQyM1Jlbm8vOAprYjZ3WkFld05JdE0vU2xFazN4STUxR3N2dGxRK3BnWW9CR2oxV0EybDgrSVhxSEd3M3RBMy9wUUlvbmZndGpICjZEWnMxeGZDcU5zTGdoMUxLdHQxUWFMREZ3a05NaGJ4bS9kV3BaaHI4OHp6SzF1RmVMYWJSYXZZcW1tQmtULzgKMzNvNmJ6NWdkOVRRNjVlZVYxV2pIZklscXlqNmJibmNnVXJid24zTGg2ZUdYb1VKZnEwVTMrL1hSN0tjYUhZdgoySFNBbCtZPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg=="
            },
        ] -> null
      - created_at                    = "2026-10-13T02:21:49Z" -> null
      - enabled_cluster_log_types     = [
          - "api",
          - "audit",
          - "authenticator",
        ] -> null
      - endpoint                      = "https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com" -> null
      - id                            = "sudhir-campusfix" -> null
      - identity                      = [
          - {
              - oidc = [
                  - {
                      - issuer = "https://oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5"
                    },
                ]
            },
        ] -> null
      - name                          = "sudhir-campusfix" -> null
      - platform_version              = "eks.24" -> null
      - role_arn                      = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/sudhir-campusfix-cluster-20261013022113872700000002" -> null
      - status                        = "ACTIVE" -> null
      - tags                          = {
          - "Environment"           = "dev"
          - "ManagedBy"             = "Terraform"
          - "terraform-aws-modules" = "eks"
        } -> null
      - tags_all                      = {
          - "Environment"           = "dev"
          - "ManagedBy"             = "Terraform"
          - "terraform-aws-modules" = "eks"
        } -> null
      - version                       = "1.35" -> null

      - access_config {
          - authentication_mode                         = "API_AND_CONFIG_MAP" -> null
          - bootstrap_cluster_creator_admin_permissions = false -> null
        }

      - encryption_config {
          - resources = [
              - "secrets",
            ] -> null

          - provider {
              - key_arn = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:key/37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
            }
        }

      - kubernetes_network_config {
          - ip_family         = "ipv4" -> null
          - service_ipv4_cidr = "172.20.0.0/16" -> null
            # (1 unchanged attribute hidden)

          - elastic_load_balancing {
              - enabled = false -> null
            }
        }

      - timeouts {}

      - upgrade_policy {
          - support_type = "EXTENDED" -> null
        }

      - vpc_config {
          - cluster_security_group_id = "sg-00c2059b40e40b1b0" -> null
          - endpoint_private_access   = true -> null
          - endpoint_public_access    = true -> null
          - public_access_cidrs       = [
              - "0.0.0.0/0",
            ] -> null
          - security_group_ids        = [
              - "sg-0522074d7a5b86fe2",
            ] -> null
          - subnet_ids                = [
              - "subnet-04516a733d2088208",
              - "subnet-082b0fed2e03ccecf",
            ] -> null
          - vpc_id                    = "vpc-0b236660178acfe8c" -> null
        }
    }

  # module.eks.aws_iam_openid_connect_provider.oidc_provider[0] will be destroyed
  - resource "aws_iam_openid_connect_provider" "oidc_provider" {
      - arn             = "arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5" -> null
      - client_id_list  = [
          - "sts.amazonaws.com",
        ] -> null
      - id              = "arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5" -> null
      - tags            = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-eks-irsa"
        } -> null
      - tags_all        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-eks-irsa"
        } -> null
      - thumbprint_list = [
          - "06b25927c42a721631c1efd9431e648fa62e1e39",
        ] -> null
      - url             = "oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5" -> null
    }

  # module.eks.aws_iam_policy.cluster_encryption[0] will be destroyed
  - resource "aws_iam_policy" "cluster_encryption" {
      - arn              = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a" -> null
      - attachment_count = 1 -> null
      - description      = "Cluster encryption policy to allow cluster role to utilize CMK provided" -> null
      - id               = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a" -> null
      - name             = "sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a" -> null
      - name_prefix      = "sudhir-campusfix-cluster-ClusterEncryption" -> null
      - path             = "/" -> null
      - policy           = jsonencode(
            {
              - Statement = [
                  - {
                      - Action   = [
                          - "kms:Encrypt",
                          - "kms:Decrypt",
                          - "kms:ListGrants",
                          - "kms:DescribeKey",
                        ]
                      - Effect   = "Allow"
                      - Resource = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:key/37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - policy_id        = "ANPAQ3AHBKZXSYNU4KEQN" -> null
      - tags             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all         = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
    }

  # module.eks.aws_iam_policy.custom[0] will be destroyed
  - resource "aws_iam_policy" "custom" {
      - arn              = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003" -> null
      - attachment_count = 1 -> null
      - id               = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003" -> null
      - name             = "sudhir-campusfix-cluster-20261013022113872700000003" -> null
      - name_prefix      = "sudhir-campusfix-cluster-" -> null
      - path             = "/" -> null
      - policy           = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = [
                          - "ec2:RunInstances",
                          - "ec2:CreateLaunchTemplate",
                          - "ec2:CreateFleet",
                        ]
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                          - StringLike   = {
                              - "aws:RequestTag/eks:kubernetes-node-class-name" = "*"
                              - "aws:RequestTag/eks:kubernetes-node-pool-name"  = "*"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = "*"
                      - Sid       = "Compute"
                    },
                  - {
                      - Action    = [
                          - "ec2:CreateVolume",
                          - "ec2:CreateSnapshot",
                        ]
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = [
                          - "arn:aws:ec2:*:*:volume/*",
                          - "arn:aws:ec2:*:*:snapshot/*",
                        ]
                      - Sid       = "Storage"
                    },
                  - {
                      - Action    = "ec2:CreateNetworkInterface"
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name"         = "${aws:PrincipalTag/eks:eks-cluster-name}"
                              - "aws:RequestTag/eks:kubernetes-cni-node-name" = "*"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = "*"
                      - Sid       = "Networking"
                    },
                  - {
                      - Action    = [
                          - "elasticloadbalancing:CreateTargetGroup",
                          - "elasticloadbalancing:CreateRule",
                          - "elasticloadbalancing:CreateLoadBalancer",
                          - "elasticloadbalancing:CreateListener",
                          - "ec2:CreateSecurityGroup",
                        ]
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = "*"
                      - Sid       = "LoadBalancer"
                    },
                  - {
                      - Action    = "shield:CreateProtection"
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = "*"
                      - Sid       = "ShieldProtection"
                    },
                  - {
                      - Action    = "shield:TagResource"
                      - Condition = {
                          - StringEquals = {
                              - "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      - Effect    = "Allow"
                      - Resource  = "arn:aws:shield::*:protection/*"
                      - Sid       = "ShieldTagResource"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - policy_id        = "ANPAQ3AHBKZXXBJVWFQWT" -> null
      - tags             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all         = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
        # (1 unchanged attribute hidden)
    }

  # module.eks.aws_iam_role.this[0] will be destroyed
  - resource "aws_iam_role" "this" {
      - arn                   = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/sudhir-campusfix-cluster-20261013022113872700000002" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = [
                          - "sts:TagSession",
                          - "sts:AssumeRole",
                        ]
                      - Effect    = "Allow"
                      - Principal = {
                          - Service = "eks.amazonaws.com"
                        }
                      - Sid       = "EKSClusterAssumeRole"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2026-10-13T02:21:15Z" -> null
      - force_detach_policies = true -> null
      - id                    = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
      - managed_policy_arns   = [
          - "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003",
          - "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a",
          - "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy",
          - "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController",
        ] -> null
      - max_session_duration  = 3600 -> null
      - name                  = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
      - name_prefix           = "sudhir-campusfix-cluster-" -> null
      - path                  = "/" -> null
      - tags                  = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all              = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - unique_id             = "AROAQ3AHBKZX75FYUTLFL" -> null
        # (2 unchanged attributes hidden)
    }

  # module.eks.aws_iam_role_policy_attachment.cluster_encryption[0] will be destroyed
  - resource "aws_iam_role_policy_attachment" "cluster_encryption" {
      - id         = "sudhir-campusfix-cluster-20261013022113872700000002-2026101302214389440000000b" -> null
      - policy_arn = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a" -> null
      - role       = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
    }

  # module.eks.aws_iam_role_policy_attachment.custom[0] will be destroyed
  - resource "aws_iam_role_policy_attachment" "custom" {
      - id         = "sudhir-campusfix-cluster-20261013022113872700000002-20261013022116581800000009" -> null
      - policy_arn = "arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003" -> null
      - role       = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
    }

  # module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"] will be destroyed
  - resource "aws_iam_role_policy_attachment" "this" {
      - id         = "sudhir-campusfix-cluster-20261013022113872700000002-20261013022116561000000008" -> null
      - policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy" -> null
      - role       = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
    }

  # module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"] will be destroyed
  - resource "aws_iam_role_policy_attachment" "this" {
      - id         = "sudhir-campusfix-cluster-20261013022113872700000002-20261013022116557100000007" -> null
      - policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController" -> null
      - role       = "sudhir-campusfix-cluster-20261013022113872700000002" -> null
    }

  # module.eks.aws_security_group.cluster[0] will be destroyed
  - resource "aws_security_group" "cluster" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:security-group/sg-0522074d7a5b86fe2" -> null
      - description            = "EKS cluster security group" -> null
      - egress                 = [] -> null
      - id                     = "sg-0522074d7a5b86fe2" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = "Node groups to cluster API"
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0cc92304f43995481",
                ]
              - self             = false
              - to_port          = 443
            },
        ] -> null
      - name                   = "sudhir-campusfix-cluster-20261013020153414100000006" -> null
      - name_prefix            = "sudhir-campusfix-cluster-" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-cluster"
        } -> null
      - tags_all               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-cluster"
        } -> null
      - vpc_id                 = "vpc-0b236660178acfe8c" -> null
    }

  # module.eks.aws_security_group.node[0] will be destroyed
  - resource "aws_security_group" "node" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:security-group/sg-0cc92304f43995481" -> null
      - description            = "EKS node shared security group" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = "Allow all egress"
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - id                     = "sg-0cc92304f43995481" -> null
      - ingress                = [
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node 4443/tcp webhook"
              - from_port        = 4443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 4443
            },
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node 6443/tcp webhook"
              - from_port        = 6443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 6443
            },
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node 8443/tcp webhook"
              - from_port        = 8443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 8443
            },
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node 9443/tcp webhook"
              - from_port        = 9443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 9443
            },
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node groups"
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 443
            },
          - {
              - cidr_blocks      = []
              - description      = "Cluster API to node kubelets"
              - from_port        = 10250
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = [
                  - "sg-0522074d7a5b86fe2",
                ]
              - self             = false
              - to_port          = 10250
            },
          - {
              - cidr_blocks      = []
              - description      = "HTTP between application pods on worker nodes"
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = true
              - to_port          = 80
            },
          - {
              - cidr_blocks      = []
              - description      = "Node to node CoreDNS UDP"
              - from_port        = 53
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "udp"
              - security_groups  = []
              - self             = true
              - to_port          = 53
            },
          - {
              - cidr_blocks      = []
              - description      = "Node to node CoreDNS"
              - from_port        = 53
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = true
              - to_port          = 53
            },
          - {
              - cidr_blocks      = []
              - description      = "Node to node ingress on ephemeral ports"
              - from_port        = 1025
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = true
              - to_port          = 65535
            },
        ] -> null
      - name                   = "sudhir-campusfix-node-20261013020153418300000007" -> null
      - name_prefix            = "sudhir-campusfix-node-" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment"                            = "dev"
          - "ManagedBy"                              = "Terraform"
          - "Name"                                   = "sudhir-campusfix-node"
          - "kubernetes.io/cluster/sudhir-campusfix" = "owned"
        } -> null
      - tags_all               = {
          - "Environment"                            = "dev"
          - "ManagedBy"                              = "Terraform"
          - "Name"                                   = "sudhir-campusfix-node"
          - "kubernetes.io/cluster/sudhir-campusfix" = "owned"
        } -> null
      - vpc_id                 = "vpc-0b236660178acfe8c" -> null
    }

  # module.eks.aws_security_group_rule.cluster["ingress_nodes_443"] will be destroyed
  - resource "aws_security_group_rule" "cluster" {
      - description              = "Node groups to cluster API" -> null
      - from_port                = 443 -> null
      - id                       = "sgrule-3797039093" -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0522074d7a5b86fe2" -> null
      - security_group_rule_id   = "sgr-072f7bbbd23bcdabb" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0cc92304f43995481" -> null
      - to_port                  = 443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["egress_all"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - cidr_blocks            = [
          - "0.0.0.0/0",
        ] -> null
      - description            = "Allow all egress" -> null
      - from_port              = 0 -> null
      - id                     = "sgrule-390060527" -> null
      - prefix_list_ids        = [] -> null
      - protocol               = "-1" -> null
      - security_group_id      = "sg-0cc92304f43995481" -> null
      - security_group_rule_id = "sgr-0258f8acb07d21fed" -> null
      - self                   = false -> null
      - to_port                = 0 -> null
      - type                   = "egress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_443"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node groups" -> null
      - from_port                = 443 -> null
      - id                       = "sgrule-4251643989" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-0106056a41c129189" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node 4443/tcp webhook" -> null
      - from_port                = 4443 -> null
      - id                       = "sgrule-3019032963" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-022bd4bddce455a59" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 4443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node 6443/tcp webhook" -> null
      - from_port                = 6443 -> null
      - id                       = "sgrule-2058399253" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-09b935a9dba67f49b" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 6443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node 8443/tcp webhook" -> null
      - from_port                = 8443 -> null
      - id                       = "sgrule-1777111604" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-0ce0aec2a441186b0" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 8443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node 9443/tcp webhook" -> null
      - from_port                = 9443 -> null
      - id                       = "sgrule-223191551" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-0f18f54404debc735" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 9443 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description              = "Cluster API to node kubelets" -> null
      - from_port                = 10250 -> null
      - id                       = "sgrule-2163456516" -> null
      - prefix_list_ids          = [] -> null
      - protocol                 = "tcp" -> null
      - security_group_id        = "sg-0cc92304f43995481" -> null
      - security_group_rule_id   = "sgr-08416ee0883173251" -> null
      - self                     = false -> null
      - source_security_group_id = "sg-0522074d7a5b86fe2" -> null
      - to_port                  = 10250 -> null
      - type                     = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_http_self"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description            = "HTTP between application pods on worker nodes" -> null
      - from_port              = 80 -> null
      - id                     = "sgrule-3554879769" -> null
      - prefix_list_ids        = [] -> null
      - protocol               = "tcp" -> null
      - security_group_id      = "sg-0cc92304f43995481" -> null
      - security_group_rule_id = "sgr-055f3a04006b27fb6" -> null
      - self                   = true -> null
      - to_port                = 80 -> null
      - type                   = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description            = "Node to node ingress on ephemeral ports" -> null
      - from_port              = 1025 -> null
      - id                     = "sgrule-3292919307" -> null
      - prefix_list_ids        = [] -> null
      - protocol               = "tcp" -> null
      - security_group_id      = "sg-0cc92304f43995481" -> null
      - security_group_rule_id = "sgr-047eebcb3e31856ba" -> null
      - self                   = true -> null
      - to_port                = 65535 -> null
      - type                   = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description            = "Node to node CoreDNS" -> null
      - from_port              = 53 -> null
      - id                     = "sgrule-1395389093" -> null
      - prefix_list_ids        = [] -> null
      - protocol               = "tcp" -> null
      - security_group_id      = "sg-0cc92304f43995481" -> null
      - security_group_rule_id = "sgr-014fb54d5e7e36eb9" -> null
      - self                   = true -> null
      - to_port                = 53 -> null
      - type                   = "ingress" -> null
    }

  # module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"] will be destroyed
  - resource "aws_security_group_rule" "node" {
      - description            = "Node to node CoreDNS UDP" -> null
      - from_port              = 53 -> null
      - id                     = "sgrule-4151595338" -> null
      - prefix_list_ids        = [] -> null
      - protocol               = "udp" -> null
      - security_group_id      = "sg-0cc92304f43995481" -> null
      - security_group_rule_id = "sgr-0d4a339d9c51cc3ed" -> null
      - self                   = true -> null
      - to_port                = 53 -> null
      - type                   = "ingress" -> null
    }

  # module.eks.time_sleep.this[0] will be destroyed
  - resource "time_sleep" "this" {
      - create_duration = "30s" -> null
      - id              = "2026-10-13T02:30:21Z" -> null
      - triggers        = {
          - "cluster_certificate_authority_data" = "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURNVENDQWhtZ0F3SUJBZ0lRRTBENXFWd3ZkVjVDZi9hSFlDd2R2akFOQmdrcWhraUc5dzBCQVFzRkFEQW4KTVJBd0RnWURWUVFLRXdkQlYxTWdSVXRUTVJNd0VRWURWUVFERXdwcmRXSmxjbTVsZEdWek1CNFhEVEkyTVRBeApNekF5TWpJd05Wb1hEVE14TVRBeE1qQXlNakl3TlZvd0p6RVFNQTRHQTFVRUNoTUhRVmRUSUVWTFV6RVRNQkVHCkExVUVBeE1LYTNWaVpYSnVaWFJsY3pDQ0FTSXdEUVlKS29aSWh2Y05BUUVCQlFBRGdnRVBBRENDQVFvQ2dnRUIKQUtvdmJTTGRvSFRUNld0TUVqRStOU0d3RVE5VHl3SXZLR1Y4V2NWS1FSaUdQZ3daa0xNcStTS1FmU1ZUQTdyMwpMak9lL3NpUjhYLy9NQkgyQWlRNmlKWVF6QUVpZzFMWDVhbVp6bkVwc0NkNENsNnNaa01BNUdqK21rdzV4RjBYCmRmWGh5bTRTTjJ5WmtSMElaRjUwZE96eWp2Q3lnVXZHN2VUZEVNNHRNN09MbFpoVEN3emI0MEdTMlQ4bWRHY0gKQmlaQXNTOU5tWVR4TXRiREo3dEtFVVkxeWZ4L0lhL3JVMEx5dnRDSEtBNFdkTEJLdkpkeENMR2M0M0JpREZSYwpoREtOTDVYSlpXQU1jL2hXTVh6R0ZNWlRhMUhnZGRaN0MzWHBTY2daRnZZWlhIQWJWbnpuN3ZvT3czQitUWXdWCmFtUWF6Z3Z1VkxZVUVGS203NHo2RWljQ0F3RUFBYU5aTUZjd0RnWURWUjBQQVFIL0JBUURBZ0trTUE4R0ExVWQKRXdFQi93UUZNQU1CQWY4d0hRWURWUjBPQkJZRUZLeDI5ZnEvOTBabzVoSXVJdjMveHdpZXd6VWVNQlVHQTFVZApFUVFPTUF5Q0NtdDFZbVZ5Ym1WMFpYTXdEUVlKS29aSWh2Y05BUUVMQlFBRGdnRUJBRUtpV0VZNjdjMFQzL1VSCitXNVFESk9YN3VtRkt3Y21Gb3lhbGkzMkNoY3RNMkR2UENyOXZDVGM5c0FoYmg2b21nbXNrTGR4VVI5WlpEUFUKZ09TSzFJOG1WR1FSRThZVEgvTTI4WUhkb0o2a3ZCUXNQNXVHaVc1QzN3QzBWUUY1eHp0aFM0RDQyM1Jlbm8vOAprYjZ3WkFld05JdE0vU2xFazN4STUxR3N2dGxRK3BnWW9CR2oxV0EybDgrSVhxSEd3M3RBMy9wUUlvbmZndGpICjZEWnMxeGZDcU5zTGdoMUxLdHQxUWFMREZ3a05NaGJ4bS9kV3BaaHI4OHp6SzF1RmVMYWJSYXZZcW1tQmtULzgKMzNvNmJ6NWdkOVRRNjVlZVYxV2pIZklscXlqNmJibmNnVXJid24zTGg2ZUdYb1VKZnEwVTMrL1hSN0tjYUhZdgoySFNBbCtZPQotLS0tLUVORCBDRVJUSUZJQ0FURS0tLS0tCg=="
          - "cluster_endpoint"                   = "https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com"
          - "cluster_name"                       = "sudhir-campusfix"
          - "cluster_service_cidr"               = "172.20.0.0/16"
          - "cluster_version"                    = "1.35"
        } -> null
    }

  # module.vpc.aws_default_network_acl.this[0] will be destroyed
  - resource "aws_default_network_acl" "this" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:network-acl/acl-041c4574a017016e1" -> null
      - default_network_acl_id = "acl-041c4574a017016e1" -> null
      - id                     = "acl-041c4574a017016e1" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - subnet_ids             = [
          - "subnet-04516a733d2088208",
          - "subnet-07d6c3997d4cef561",
          - "subnet-082b0fed2e03ccecf",
          - "subnet-0e2b1c27fe01362e1",
        ] -> null
      - tags                   = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - tags_all               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - vpc_id                 = "vpc-0b236660178acfe8c" -> null

      - egress {
          - action          = "allow" -> null
          - from_port       = 0 -> null
          - icmp_code       = 0 -> null
          - icmp_type       = 0 -> null
          - ipv6_cidr_block = "::/0" -> null
          - protocol        = "-1" -> null
          - rule_no         = 101 -> null
          - to_port         = 0 -> null
            # (1 unchanged attribute hidden)
        }
      - egress {
          - action          = "allow" -> null
          - cidr_block      = "0.0.0.0/0" -> null
          - from_port       = 0 -> null
          - icmp_code       = 0 -> null
          - icmp_type       = 0 -> null
          - protocol        = "-1" -> null
          - rule_no         = 100 -> null
          - to_port         = 0 -> null
            # (1 unchanged attribute hidden)
        }

      - ingress {
          - action          = "allow" -> null
          - from_port       = 0 -> null
          - icmp_code       = 0 -> null
          - icmp_type       = 0 -> null
          - ipv6_cidr_block = "::/0" -> null
          - protocol        = "-1" -> null
          - rule_no         = 101 -> null
          - to_port         = 0 -> null
            # (1 unchanged attribute hidden)
        }
      - ingress {
          - action          = "allow" -> null
          - cidr_block      = "0.0.0.0/0" -> null
          - from_port       = 0 -> null
          - icmp_code       = 0 -> null
          - icmp_type       = 0 -> null
          - protocol        = "-1" -> null
          - rule_no         = 100 -> null
          - to_port         = 0 -> null
            # (1 unchanged attribute hidden)
        }
    }

  # module.vpc.aws_default_route_table.default[0] will be destroyed
  - resource "aws_default_route_table" "default" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:route-table/rtb-09e2e3d49bb09de16" -> null
      - default_route_table_id = "rtb-09e2e3d49bb09de16" -> null
      - id                     = "rtb-09e2e3d49bb09de16" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - propagating_vgws       = [] -> null
      - route                  = [] -> null
      - tags                   = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - tags_all               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - vpc_id                 = "vpc-0b236660178acfe8c" -> null

      - timeouts {
          - create = "5m" -> null
          - update = "5m" -> null
        }
    }

  # module.vpc.aws_default_security_group.this[0] will be destroyed
  - resource "aws_default_security_group" "this" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:security-group/sg-0f6d08c531be0d121" -> null
      - description            = "default VPC security group" -> null
      - egress                 = [] -> null
      - id                     = "sg-0f6d08c531be0d121" -> null
      - ingress                = [] -> null
      - name                   = "default" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - tags_all               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-default"
        } -> null
      - vpc_id                 = "vpc-0b236660178acfe8c" -> null
        # (1 unchanged attribute hidden)
    }

  # module.vpc.aws_eip.nat[0] will be destroyed
  - resource "aws_eip" "nat" {
      - allocation_id            = "eipalloc-04a90e0128a0fddda" -> null
      - arn                      = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:elastic-ip/eipalloc-04a90e0128a0fddda" -> null
      - association_id           = "eipassoc-054603affaf5567a0" -> null
      - domain                   = "vpc" -> null
      - id                       = "eipalloc-04a90e0128a0fddda" -> null
      - network_border_group     = "ap-south-1" -> null
      - network_interface        = "eni-04ad2eafe77821828" -> null
      - private_dns              = "ip-10-20-101-163.ap-south-1.compute.internal" -> null
      - private_ip               = "10.20.101.163" -> null
      - public_dns               = "ec2-13-204-144-145.ap-south-1.compute.amazonaws.com" -> null
      - public_ip                = "13.204.144.145" -> null
      - public_ipv4_pool         = "amazon" -> null
      - tags                     = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        } -> null
      - tags_all                 = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        } -> null
      - vpc                      = true -> null
        # (5 unchanged attributes hidden)
    }

  # module.vpc.aws_internet_gateway.this[0] will be destroyed
  - resource "aws_internet_gateway" "this" {
      - arn      = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:internet-gateway/igw-040d3c722f60f7daa" -> null
      - id       = "igw-040d3c722f60f7daa" -> null
      - owner_id = "[AWS_ACCOUNT_ID]" -> null
      - tags     = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc"
        } -> null
      - tags_all = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc"
        } -> null
      - vpc_id   = "vpc-0b236660178acfe8c" -> null
    }

  # module.vpc.aws_nat_gateway.this[0] will be destroyed
  - resource "aws_nat_gateway" "this" {
      - allocation_id                      = "eipalloc-04a90e0128a0fddda" -> null
      - association_id                     = "eipassoc-054603affaf5567a0" -> null
      - connectivity_type                  = "public" -> null
      - id                                 = "nat-0385c62146773d8ce" -> null
      - network_interface_id               = "eni-04ad2eafe77821828" -> null
      - private_ip                         = "10.20.101.163" -> null
      - public_ip                          = "13.204.144.145" -> null
      - secondary_allocation_ids           = [] -> null
      - secondary_private_ip_address_count = 0 -> null
      - secondary_private_ip_addresses     = [] -> null
      - subnet_id                          = "subnet-0e2b1c27fe01362e1" -> null
      - tags                               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        } -> null
      - tags_all                           = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        } -> null
    }

  # module.vpc.aws_route.private_nat_gateway[0] will be destroyed
  - resource "aws_route" "private_nat_gateway" {
      - destination_cidr_block      = "0.0.0.0/0" -> null
      - id                          = "r-rtb-07bfe9cc9e0aaff901080289494" -> null
      - nat_gateway_id              = "nat-0385c62146773d8ce" -> null
      - origin                      = "CreateRoute" -> null
      - route_table_id              = "rtb-07bfe9cc9e0aaff90" -> null
      - state                       = "active" -> null
        # (13 unchanged attributes hidden)

      - timeouts {
          - create = "5m" -> null
        }
    }

  # module.vpc.aws_route.public_internet_gateway[0] will be destroyed
  - resource "aws_route" "public_internet_gateway" {
      - destination_cidr_block      = "0.0.0.0/0" -> null
      - gateway_id                  = "igw-040d3c722f60f7daa" -> null
      - id                          = "r-rtb-0b9aab65ac4e4a3ba1080289494" -> null
      - origin                      = "CreateRoute" -> null
      - route_table_id              = "rtb-0b9aab65ac4e4a3ba" -> null
      - state                       = "active" -> null
        # (13 unchanged attributes hidden)

      - timeouts {
          - create = "5m" -> null
        }
    }

  # module.vpc.aws_route_table.private[0] will be destroyed
  - resource "aws_route_table" "private" {
      - arn              = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:route-table/rtb-07bfe9cc9e0aaff90" -> null
      - id               = "rtb-07bfe9cc9e0aaff90" -> null
      - owner_id         = "[AWS_ACCOUNT_ID]" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                 = "0.0.0.0/0"
              - nat_gateway_id             = "nat-0385c62146773d8ce"
                # (11 unchanged attributes hidden)
            },
        ] -> null
      - tags             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-private"
        } -> null
      - tags_all         = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-private"
        } -> null
      - vpc_id           = "vpc-0b236660178acfe8c" -> null
    }

  # module.vpc.aws_route_table.public[0] will be destroyed
  - resource "aws_route_table" "public" {
      - arn              = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:route-table/rtb-0b9aab65ac4e4a3ba" -> null
      - id               = "rtb-0b9aab65ac4e4a3ba" -> null
      - owner_id         = "[AWS_ACCOUNT_ID]" -> null
      - propagating_vgws = [] -> null
      - route            = [
          - {
              - cidr_block                 = "0.0.0.0/0"
              - gateway_id                 = "igw-040d3c722f60f7daa"
                # (11 unchanged attributes hidden)
            },
        ] -> null
      - tags             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-public"
        } -> null
      - tags_all         = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc-public"
        } -> null
      - vpc_id           = "vpc-0b236660178acfe8c" -> null
    }

  # module.vpc.aws_route_table_association.private[0] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-06f506a745155caff" -> null
      - route_table_id = "rtb-07bfe9cc9e0aaff90" -> null
      - subnet_id      = "subnet-082b0fed2e03ccecf" -> null
        # (1 unchanged attribute hidden)
    }

  # module.vpc.aws_route_table_association.private[1] will be destroyed
  - resource "aws_route_table_association" "private" {
      - id             = "rtbassoc-0dfdf06c56b879db3" -> null
      - route_table_id = "rtb-07bfe9cc9e0aaff90" -> null
      - subnet_id      = "subnet-04516a733d2088208" -> null
        # (1 unchanged attribute hidden)
    }

  # module.vpc.aws_route_table_association.public[0] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-02fcb8b002b37c001" -> null
      - route_table_id = "rtb-0b9aab65ac4e4a3ba" -> null
      - subnet_id      = "subnet-0e2b1c27fe01362e1" -> null
        # (1 unchanged attribute hidden)
    }

  # module.vpc.aws_route_table_association.public[1] will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-062fd51226d12561a" -> null
      - route_table_id = "rtb-0b9aab65ac4e4a3ba" -> null
      - subnet_id      = "subnet-07d6c3997d4cef561" -> null
        # (1 unchanged attribute hidden)
    }

  # module.vpc.aws_subnet.private[0] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                                            = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:subnet/subnet-082b0fed2e03ccecf" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "ap-south-1a" -> null
      - availability_zone_id                           = "aps1-az1" -> null
      - cidr_block                                     = "10.20.1.0/24" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-082b0fed2e03ccecf" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = false -> null
      - owner_id                                       = "[AWS_ACCOUNT_ID]" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - tags                                           = {
          - "Environment"                     = "dev"
          - "ManagedBy"                       = "Terraform"
          - "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1a"
          - "kubernetes.io/role/internal-elb" = "1"
        } -> null
      - tags_all                                       = {
          - "Environment"                     = "dev"
          - "ManagedBy"                       = "Terraform"
          - "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1a"
          - "kubernetes.io/role/internal-elb" = "1"
        } -> null
      - vpc_id                                         = "vpc-0b236660178acfe8c" -> null
        # (4 unchanged attributes hidden)
    }

  # module.vpc.aws_subnet.private[1] will be destroyed
  - resource "aws_subnet" "private" {
      - arn                                            = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:subnet/subnet-04516a733d2088208" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "ap-south-1b" -> null
      - availability_zone_id                           = "aps1-az3" -> null
      - cidr_block                                     = "10.20.2.0/24" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-04516a733d2088208" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = false -> null
      - owner_id                                       = "[AWS_ACCOUNT_ID]" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - tags                                           = {
          - "Environment"                     = "dev"
          - "ManagedBy"                       = "Terraform"
          - "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1b"
          - "kubernetes.io/role/internal-elb" = "1"
        } -> null
      - tags_all                                       = {
          - "Environment"                     = "dev"
          - "ManagedBy"                       = "Terraform"
          - "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1b"
          - "kubernetes.io/role/internal-elb" = "1"
        } -> null
      - vpc_id                                         = "vpc-0b236660178acfe8c" -> null
        # (4 unchanged attributes hidden)
    }

  # module.vpc.aws_subnet.public[0] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                                            = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:subnet/subnet-0e2b1c27fe01362e1" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "ap-south-1a" -> null
      - availability_zone_id                           = "aps1-az1" -> null
      - cidr_block                                     = "10.20.101.0/24" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-0e2b1c27fe01362e1" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = false -> null
      - owner_id                                       = "[AWS_ACCOUNT_ID]" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - tags                                           = {
          - "Environment"            = "dev"
          - "ManagedBy"              = "Terraform"
          - "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1a"
          - "kubernetes.io/role/elb" = "1"
        } -> null
      - tags_all                                       = {
          - "Environment"            = "dev"
          - "ManagedBy"              = "Terraform"
          - "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1a"
          - "kubernetes.io/role/elb" = "1"
        } -> null
      - vpc_id                                         = "vpc-0b236660178acfe8c" -> null
        # (4 unchanged attributes hidden)
    }

  # module.vpc.aws_subnet.public[1] will be destroyed
  - resource "aws_subnet" "public" {
      - arn                                            = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:subnet/subnet-07d6c3997d4cef561" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "ap-south-1b" -> null
      - availability_zone_id                           = "aps1-az3" -> null
      - cidr_block                                     = "10.20.102.0/24" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-07d6c3997d4cef561" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = false -> null
      - owner_id                                       = "[AWS_ACCOUNT_ID]" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - tags                                           = {
          - "Environment"            = "dev"
          - "ManagedBy"              = "Terraform"
          - "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1b"
          - "kubernetes.io/role/elb" = "1"
        } -> null
      - tags_all                                       = {
          - "Environment"            = "dev"
          - "ManagedBy"              = "Terraform"
          - "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1b"
          - "kubernetes.io/role/elb" = "1"
        } -> null
      - vpc_id                                         = "vpc-0b236660178acfe8c" -> null
        # (4 unchanged attributes hidden)
    }

  # module.vpc.aws_vpc.this[0] will be destroyed
  - resource "aws_vpc" "this" {
      - arn                                  = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:vpc/vpc-0b236660178acfe8c" -> null
      - assign_generated_ipv6_cidr_block     = false -> null
      - cidr_block                           = "10.20.0.0/16" -> null
      - default_network_acl_id               = "acl-041c4574a017016e1" -> null
      - default_route_table_id               = "rtb-09e2e3d49bb09de16" -> null
      - default_security_group_id            = "sg-0f6d08c531be0d121" -> null
      - dhcp_options_id                      = "dopt-04099746251bf6721" -> null
      - enable_dns_hostnames                 = true -> null
      - enable_dns_support                   = true -> null
      - enable_network_address_usage_metrics = false -> null
      - id                                   = "vpc-0b236660178acfe8c" -> null
      - instance_tenancy                     = "default" -> null
      - ipv6_netmask_length                  = 0 -> null
      - main_route_table_id                  = "rtb-09e2e3d49bb09de16" -> null
      - owner_id                             = "[AWS_ACCOUNT_ID]" -> null
      - tags                                 = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc"
        } -> null
      - tags_all                             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-campusfix-vpc"
        } -> null
        # (4 unchanged attributes hidden)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0] will be destroyed
  - resource "aws_eks_node_group" "this" {
      - ami_type               = "AL2023_x86_64_STANDARD" -> null
      - arn                    = "arn:aws:eks:ap-south-1:[AWS_ACCOUNT_ID]:nodegroup/sudhir-campusfix/main-20261013023027045600000010/f6d0998c-6930-ba0b-fee8-4b5bf127be5e" -> null
      - capacity_type          = "ON_DEMAND" -> null
      - cluster_name           = "sudhir-campusfix" -> null
      - disk_size              = 0 -> null
      - id                     = "sudhir-campusfix:main-20261013023027045600000010" -> null
      - instance_types         = [
          - "t3.medium",
        ] -> null
      - labels                 = {} -> null
      - node_group_name        = "main-20261013023027045600000010" -> null
      - node_group_name_prefix = "main-" -> null
      - node_role_arn          = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/main-eks-node-group-20261013022113872700000001" -> null
      - release_version        = "1.35.8-20261003" -> null
      - resources              = [
          - {
              - autoscaling_groups              = [
                  - {
                      - name = "eks-main-20261013023027045600000010-f6d0998c-6930-ba0b-fee8-4b5bf127be5e"
                    },
                ]
                # (1 unchanged attribute hidden)
            },
        ] -> null
      - status                 = "ACTIVE" -> null
      - subnet_ids             = [
          - "subnet-04516a733d2088208",
          - "subnet-082b0fed2e03ccecf",
        ] -> null
      - tags                   = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "main"
        } -> null
      - tags_all               = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "main"
        } -> null
      - version                = "1.35" -> null

      - launch_template {
          - id      = "lt-0c342f02f8398c6cc" -> null
          - name    = "main-2026101302302121020000000e" -> null
          - version = "1" -> null
        }

      - scaling_config {
          - desired_size = 2 -> null
          - max_size     = 3 -> null
          - min_size     = 1 -> null
        }

      - timeouts {}

      - update_config {
          - max_unavailable            = 0 -> null
          - max_unavailable_percentage = 33 -> null
        }
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0] will be destroyed
  - resource "aws_iam_role" "this" {
      - arn                   = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/main-eks-node-group-20261013022113872700000001" -> null
      - assume_role_policy    = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "sts:AssumeRole"
                      - Effect    = "Allow"
                      - Principal = {
                          - Service = "ec2.amazonaws.com"
                        }
                      - Sid       = "EKSNodeAssumeRole"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - create_date           = "2026-10-13T02:21:15Z" -> null
      - description           = "EKS managed node group IAM role" -> null
      - force_detach_policies = true -> null
      - id                    = "main-eks-node-group-20261013022113872700000001" -> null
      - managed_policy_arns   = [
          - "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
          - "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
          - "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
        ] -> null
      - max_session_duration  = 3600 -> null
      - name                  = "main-eks-node-group-20261013022113872700000001" -> null
      - name_prefix           = "main-eks-node-group-" -> null
      - path                  = "/" -> null
      - tags                  = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all              = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - unique_id             = "AROAQ3AHBKZX235YCQBX4" -> null
        # (1 unchanged attribute hidden)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"] will be destroyed
  - resource "aws_iam_role_policy_attachment" "this" {
      - id         = "main-eks-node-group-20261013022113872700000001-20261013022116283300000006" -> null
      - policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly" -> null
      - role       = "main-eks-node-group-20261013022113872700000001" -> null
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"] will be destroyed
  - resource "aws_iam_role_policy_attachment" "this" {
      - id         = "main-eks-node-group-20261013022113872700000001-20261013022116243100000005" -> null
      - policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy" -> null
      - role       = "main-eks-node-group-20261013022113872700000001" -> null
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"] will be destroyed
  - resource "aws_iam_role_policy_attachment" "this" {
      - id         = "main-eks-node-group-20261013022113872700000001-20261013022116235800000004" -> null
      - policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy" -> null
      - role       = "main-eks-node-group-20261013022113872700000001" -> null
    }

  # module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0] will be destroyed
  - resource "aws_launch_template" "this" {
      - arn                                  = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:launch-template/lt-0c342f02f8398c6cc" -> null
      - default_version                      = 1 -> null
      - description                          = "Custom launch template for main EKS managed node group" -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - id                                   = "lt-0c342f02f8398c6cc" -> null
      - latest_version                       = 1 -> null
      - name                                 = "main-2026101302302121020000000e" -> null
      - name_prefix                          = "main-" -> null
      - security_group_names                 = [] -> null
      - tags                                 = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - tags_all                             = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
        } -> null
      - update_default_version               = true -> null
      - vpc_security_group_ids               = [
          - "sg-0cc92304f43995481",
        ] -> null
        # (8 unchanged attributes hidden)

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_put_response_hop_limit = 2 -> null
          - http_tokens                 = "required" -> null
            # (2 unchanged attributes hidden)
        }

      - monitoring {
          - enabled = true -> null
        }

      - tag_specifications {
          - resource_type = "instance" -> null
          - tags          = {
              - "Environment" = "dev"
              - "ManagedBy"   = "Terraform"
              - "Name"        = "main"
            } -> null
        }
      - tag_specifications {
          - resource_type = "network-interface" -> null
          - tags          = {
              - "Environment" = "dev"
              - "ManagedBy"   = "Terraform"
              - "Name"        = "main"
            } -> null
        }
      - tag_specifications {
          - resource_type = "volume" -> null
          - tags          = {
              - "Environment" = "dev"
              - "ManagedBy"   = "Terraform"
              - "Name"        = "main"
            } -> null
        }
    }

  # module.eks.module.kms.aws_kms_alias.this["cluster"] will be destroyed
  - resource "aws_kms_alias" "this" {
      - arn            = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:alias/eks/sudhir-campusfix" -> null
      - id             = "alias/eks/sudhir-campusfix" -> null
      - name           = "alias/eks/sudhir-campusfix" -> null
      - target_key_arn = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:key/37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
      - target_key_id  = "37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
        # (1 unchanged attribute hidden)
    }

  # module.eks.module.kms.aws_kms_key.this[0] will be destroyed
  - resource "aws_kms_key" "this" {
      - arn                                = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:key/37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
      - bypass_policy_lockout_safety_check = false -> null
      - customer_master_key_spec           = "SYMMETRIC_DEFAULT" -> null
      - description                        = "sudhir-campusfix cluster encryption key" -> null
      - enable_key_rotation                = true -> null
      - id                                 = "37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
      - is_enabled                         = true -> null
      - key_id                             = "37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c" -> null
      - key_usage                          = "ENCRYPT_DECRYPT" -> null
      - multi_region                       = false -> null
      - policy                             = jsonencode(
            {
              - Statement = [
                  - {
                      - Action    = "kms:*"
                      - Effect    = "Allow"
                      - Principal = {
                          - AWS = "arn:aws:iam::[AWS_ACCOUNT_ID]:root"
                        }
                      - Resource  = "*"
                      - Sid       = "Default"
                    },
                  - {
                      - Action    = [
                          - "kms:Update*",
                          - "kms:UntagResource",
                          - "kms:TagResource",
                          - "kms:ScheduleKeyDeletion",
                          - "kms:Revoke*",
                          - "kms:ReplicateKey",
                          - "kms:Put*",
                          - "kms:List*",
                          - "kms:ImportKeyMaterial",
                          - "kms:Get*",
                          - "kms:Enable*",
                          - "kms:Disable*",
                          - "kms:Describe*",
                          - "kms:Delete*",
                          - "kms:Create*",
                          - "kms:CancelKeyDeletion",
                        ]
                      - Effect    = "Allow"
                      - Principal = {
                          - AWS = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli"
                        }
                      - Resource  = "*"
                      - Sid       = "KeyAdministration"
                    },
                  - {
                      - Action    = [
                          - "kms:ReEncrypt*",
                          - "kms:GenerateDataKey*",
                          - "kms:Encrypt",
                          - "kms:DescribeKey",
                          - "kms:Decrypt",
                        ]
                      - Effect    = "Allow"
                      - Principal = {
                          - AWS = "arn:aws:iam::[AWS_ACCOUNT_ID]:role/sudhir-campusfix-cluster-20261013022113872700000002"
                        }
                      - Resource  = "*"
                      - Sid       = "KeyUsage"
                    },
                ]
              - Version   = "2012-10-17"
            }
        ) -> null
      - rotation_period_in_days            = 365 -> null
      - tags                               = {
          - "Environment"           = "dev"
          - "ManagedBy"             = "Terraform"
          - "terraform-aws-modules" = "eks"
        } -> null
      - tags_all                           = {
          - "Environment"           = "dev"
          - "ManagedBy"             = "Terraform"
          - "terraform-aws-modules" = "eks"
        } -> null
        # (2 unchanged attributes hidden)
    }

  # module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr will be destroyed
  - resource "null_resource" "validate_cluster_service_cidr" {
      - id = "3032463307649055476" -> null
    }

Plan: 0 to add, 0 to change, 63 to destroy.

Changes to Outputs:
  - cluster_endpoint  = "https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com" -> null
  - cluster_name      = "sudhir-campusfix" -> null
  - configure_kubectl = "aws eks update-kubeconfig --region ap-south-1 --name sudhir-campusfix" -> null
  - vpc_id            = "vpc-0b236660178acfe8c" -> null
aws_iam_role_policy_attachment.ebs_csi: Destroying... [id=sudhir-campusfix-ebs-csi-2026101302300466330000000d]
module.eks.aws_eks_addon.this["kube-proxy"]: Destroying... [id=sudhir-campusfix:kube-proxy]
module.vpc.aws_route_table_association.public[0]: Destroying... [id=rtbassoc-02fcb8b002b37c001]
module.vpc.aws_default_security_group.this[0]: Destroying... [id=sg-0f6d08c531be0d121]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Destroying... [id=sg-00c2059b40e40b1b0,ManagedBy]
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Destroying... [id=sudhir-campusfix-cluster-20261013022113872700000002-2026101302214389440000000b]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Destroying... [id=sudhir-campusfix:aws-ebs-csi-driver]
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Destroying... [id=sudhir-campusfix#arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli#arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy]
module.vpc.aws_route_table_association.private[0]: Destroying... [id=rtbassoc-06f506a745155caff]
module.vpc.aws_route.public_internet_gateway[0]: Destroying... [id=r-rtb-0b9aab65ac4e4a3ba1080289494]
module.vpc.aws_default_security_group.this[0]: Destruction complete after 0s
module.eks.aws_eks_addon.this["coredns"]: Destroying... [id=sudhir-campusfix:coredns]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Destruction complete after 1s
module.vpc.aws_default_route_table.default[0]: Destroying... [id=rtb-09e2e3d49bb09de16]
module.vpc.aws_default_route_table.default[0]: Destruction complete after 0s
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Destruction complete after 1s
module.eks.aws_eks_addon.before_compute["vpc-cni"]: Destroying... [id=sudhir-campusfix:vpc-cni]
module.vpc.aws_route_table_association.public[0]: Destruction complete after 1s
module.vpc.aws_route_table_association.public[1]: Destroying... [id=rtbassoc-062fd51226d12561a]
module.vpc.aws_default_network_acl.this[0]: Destroying... [id=acl-041c4574a017016e1]
module.vpc.aws_default_network_acl.this[0]: Destruction complete after 0s
module.eks.aws_iam_role_policy_attachment.custom[0]: Destroying... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116581800000009]
module.vpc.aws_route_table_association.private[0]: Destruction complete after 1s
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Destroying... [id=sg-00c2059b40e40b1b0,Environment]
module.vpc.aws_route.public_internet_gateway[0]: Destruction complete after 1s
module.vpc.aws_route_table_association.public[1]: Destruction complete after 0s
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Destruction complete after 0s
module.eks.module.kms.aws_kms_alias.this["cluster"]: Destroying... [id=alias/eks/sudhir-campusfix]
module.vpc.aws_route.private_nat_gateway[0]: Destroying... [id=r-rtb-07bfe9cc9e0aaff901080289494]
module.vpc.aws_route_table_association.private[1]: Destroying... [id=rtbassoc-0dfdf06c56b879db3]
module.eks.module.kms.aws_kms_alias.this["cluster"]: Destruction complete after 0s
module.eks.aws_eks_access_entry.this["cluster_creator"]: Destroying... [id=sudhir-campusfix:arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.vpc.aws_route_table_association.private[1]: Destruction complete after 1s
module.vpc.aws_route_table.public[0]: Destroying... [id=rtb-0b9aab65ac4e4a3ba]
aws_iam_role_policy_attachment.ebs_csi: Destruction complete after 2s
module.vpc.aws_route.private_nat_gateway[0]: Destruction complete after 1s
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Destruction complete after 2s
module.vpc.aws_route_table.private[0]: Destroying... [id=rtb-07bfe9cc9e0aaff90]
module.eks.aws_iam_policy.cluster_encryption[0]: Destroying... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a]
module.vpc.aws_nat_gateway.this[0]: Destroying... [id=nat-0385c62146773d8ce]
module.eks.aws_eks_addon.this["kube-proxy"]: Destruction complete after 2s
module.eks.aws_eks_access_entry.this["cluster_creator"]: Destruction complete after 1s
module.eks.aws_iam_role_policy_attachment.custom[0]: Destruction complete after 1s
module.eks.aws_iam_policy.custom[0]: Destroying... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003]
module.vpc.aws_route_table.public[0]: Destruction complete after 0s
module.vpc.aws_route_table.private[0]: Destruction complete after 0s
module.eks.aws_iam_policy.cluster_encryption[0]: Destruction complete after 0s
module.eks.aws_iam_policy.custom[0]: Destruction complete after 1s
module.eks.aws_eks_addon.this["coredns"]: Destruction complete after 2s
module.eks.aws_eks_addon.before_compute["vpc-cni"]: Destruction complete after 2s
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Destruction complete after 8s
aws_iam_role.ebs_csi: Destroying... [id=sudhir-campusfix-ebs-csi]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Destroying... [id=sudhir-campusfix:main-20261013023027045600000010]
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Destroying... [id=3032463307649055476]
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Destruction complete after 0s
aws_iam_role.ebs_csi: Destruction complete after 1s
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Destroying... [id=arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5]
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Destruction complete after 1s
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 00m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 00m10s elapsed]
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 00m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 00m20s elapsed]
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 00m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 00m30s elapsed]
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 00m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 00m40s elapsed]
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 00m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 00m50s elapsed]
module.vpc.aws_nat_gateway.this[0]: Still destroying... [id=nat-0385c62146773d8ce, 01m00s elapsed]
module.vpc.aws_nat_gateway.this[0]: Destruction complete after 1m1s
module.vpc.aws_subnet.public[1]: Destroying... [id=subnet-07d6c3997d4cef561]
module.vpc.aws_subnet.public[0]: Destroying... [id=subnet-0e2b1c27fe01362e1]
module.vpc.aws_eip.nat[0]: Destroying... [id=eipalloc-04a90e0128a0fddda]
module.vpc.aws_eip.nat[0]: Destruction complete after 5s
module.vpc.aws_internet_gateway.this[0]: Destroying... [id=igw-040d3c722f60f7daa]
module.vpc.aws_subnet.public[0]: Destruction complete after 5s
module.vpc.aws_subnet.public[1]: Destruction complete after 5s
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m00s elapsed]
module.vpc.aws_internet_gateway.this[0]: Destruction complete after 0s
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 01m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 02m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 03m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 04m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 05m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 06m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 07m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 08m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still destroying... [id=sudhir-campusfix:main-20261013023027045600000010, 08m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Destruction complete after 8m17s
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Destroying... [id=lt-0c342f02f8398c6cc]
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Destruction complete after 4s
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Destroying... [id=main-eks-node-group-20261013022113872700000001-20261013022116235800000004]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Destroying... [id=main-eks-node-group-20261013022113872700000001-20261013022116243100000005]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Destroying... [id=main-eks-node-group-20261013022113872700000001-20261013022116283300000006]
module.eks.time_sleep.this[0]: Destroying... [id=2026-10-13T02:30:21Z]
module.eks.time_sleep.this[0]: Destruction complete after 0s
module.eks.aws_eks_cluster.this[0]: Destroying... [id=sudhir-campusfix]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Destruction complete after 2s
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Destruction complete after 2s
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Destruction complete after 2s
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Destroying... [id=main-eks-node-group-20261013022113872700000001]
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Destruction complete after 1s
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 00m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 00m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 00m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 00m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 00m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m11s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m21s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m31s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m41s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 01m51s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 02m01s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 02m11s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 02m21s elapsed]
module.eks.aws_eks_cluster.this[0]: Still destroying... [id=sudhir-campusfix, 02m31s elapsed]
module.eks.aws_eks_cluster.this[0]: Destruction complete after 2m33s
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Destroying... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116557100000007]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Destroying... [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116561000000008]
module.eks.aws_security_group_rule.node["egress_all"]: Destroying... [id=sgrule-390060527]
module.eks.aws_security_group_rule.node["ingress_http_self"]: Destroying... [id=sgrule-3554879769]
module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"]: Destroying... [id=sgrule-1777111604]
module.eks.aws_cloudwatch_log_group.this[0]: Destroying... [id=/aws/eks/sudhir-campusfix/cluster]
module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"]: Destroying... [id=sgrule-223191551]
module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"]: Destroying... [id=sgrule-2058399253]
module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"]: Destroying... [id=sgrule-1395389093]
module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"]: Destroying... [id=sgrule-4151595338]
module.eks.aws_cloudwatch_log_group.this[0]: Destruction complete after 1s
module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"]: Destroying... [id=sgrule-2163456516]
module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"]: Destruction complete after 1s
module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"]: Destroying... [id=sgrule-3019032963]
module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"]: Destruction complete after 1s
module.vpc.aws_subnet.private[1]: Destroying... [id=subnet-04516a733d2088208]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Destruction complete after 2s
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Destruction complete after 2s
module.eks.aws_security_group_rule.node["ingress_cluster_443"]: Destroying... [id=sgrule-4251643989]
module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"]: Destroying... [id=sgrule-3292919307]
module.eks.aws_security_group_rule.node["ingress_http_self"]: Destruction complete after 2s
module.vpc.aws_subnet.private[0]: Destroying... [id=subnet-082b0fed2e03ccecf]
module.vpc.aws_subnet.private[1]: Destruction complete after 0s
module.eks.module.kms.aws_kms_key.this[0]: Destroying... [id=37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c]
module.eks.aws_security_group_rule.node["egress_all"]: Destruction complete after 3s
module.eks.aws_security_group_rule.cluster["ingress_nodes_443"]: Destroying... [id=sgrule-3797039093]
module.vpc.aws_subnet.private[0]: Destruction complete after 1s
module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"]: Destruction complete after 3s
module.eks.aws_security_group_rule.cluster["ingress_nodes_443"]: Destruction complete after 0s
module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"]: Destruction complete after 4s
module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"]: Destruction complete after 4s
module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"]: Destruction complete after 4s
module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"]: Destruction complete after 4s
module.eks.aws_security_group_rule.node["ingress_cluster_443"]: Destruction complete after 3s
module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"]: Destruction complete after 4s
module.eks.aws_security_group.cluster[0]: Destroying... [id=sg-0522074d7a5b86fe2]
module.eks.aws_security_group.node[0]: Destroying... [id=sg-0cc92304f43995481]
module.eks.aws_security_group.cluster[0]: Destruction complete after 0s
module.eks.aws_security_group.node[0]: Destruction complete after 0s
module.vpc.aws_vpc.this[0]: Destroying... [id=vpc-0b236660178acfe8c]
module.vpc.aws_vpc.this[0]: Destruction complete after 1s
module.eks.module.kms.aws_kms_key.this[0]: Destruction complete after 8s
module.eks.aws_iam_role.this[0]: Destroying... [id=sudhir-campusfix-cluster-20261013022113872700000002]
module.eks.aws_iam_role.this[0]: Destruction complete after 1s

Destroy complete! Resources: 63 destroyed.

```

Exit code: 0
