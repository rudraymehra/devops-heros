# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T02:33:41.184456+00:00

Working directory: session21-python/terraform

```text
$ /tmp/campusfix-tools.FCoLVB/terraform apply -auto-approve -input=false -no-color
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Reading...
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.eks.data.aws_partition.current[0]: Reading...
module.eks.module.kms.data.aws_caller_identity.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Reading...
module.eks.module.kms.data.aws_partition.current[0]: Reading...
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Reading...
module.eks.data.aws_caller_identity.current[0]: Reading...
module.eks.aws_cloudwatch_log_group.this[0]: Refreshing state... [id=/aws/eks/sudhir-campusfix/cluster]
module.vpc.aws_vpc.this[0]: Refreshing state... [id=vpc-0b236660178acfe8c]
module.eks.data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2830595799]
module.eks.module.eks_managed_node_group["main"].data.aws_iam_policy_document.assume_role_policy[0]: Read complete after 0s [id=2560088296]
module.eks.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.module.eks_managed_node_group["main"].data.aws_partition.current: Read complete after 0s [id=aws]
module.eks.module.kms.data.aws_partition.current[0]: Read complete after 0s [id=aws]
module.eks.data.aws_iam_policy_document.custom[0]: Reading...
module.eks.data.aws_iam_policy_document.custom[0]: Read complete after 0s [id=513122117]
module.eks.data.aws_caller_identity.current[0]: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
module.eks.data.aws_iam_session_context.current[0]: Reading...
module.eks.data.aws_iam_session_context.current[0]: Read complete after 0s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.eks.module.kms.data.aws_caller_identity.current[0]: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
module.eks.module.eks_managed_node_group["main"].data.aws_caller_identity.current: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
module.vpc.aws_default_security_group.this[0]: Refreshing state... [id=sg-0f6d08c531be0d121]
module.vpc.aws_default_route_table.default[0]: Refreshing state... [id=rtb-09e2e3d49bb09de16]
module.eks.aws_security_group.node[0]: Refreshing state... [id=sg-0cc92304f43995481]
module.eks.aws_security_group.cluster[0]: Refreshing state... [id=sg-0522074d7a5b86fe2]
module.vpc.aws_route_table.public[0]: Refreshing state... [id=rtb-0b9aab65ac4e4a3ba]
module.vpc.aws_route_table.private[0]: Refreshing state... [id=rtb-07bfe9cc9e0aaff90]
module.vpc.aws_default_network_acl.this[0]: Refreshing state... [id=acl-041c4574a017016e1]
module.vpc.aws_internet_gateway.this[0]: Refreshing state... [id=igw-040d3c722f60f7daa]
module.vpc.aws_subnet.public[0]: Refreshing state... [id=subnet-0e2b1c27fe01362e1]
module.vpc.aws_subnet.public[1]: Refreshing state... [id=subnet-07d6c3997d4cef561]
module.vpc.aws_subnet.private[0]: Refreshing state... [id=subnet-082b0fed2e03ccecf]
module.vpc.aws_subnet.private[1]: Refreshing state... [id=subnet-04516a733d2088208]
module.eks.aws_security_group_rule.cluster["ingress_nodes_443"]: Refreshing state... [id=sgrule-3797039093]
module.eks.aws_security_group_rule.node["egress_all"]: Refreshing state... [id=sgrule-390060527]
module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"]: Refreshing state... [id=sgrule-2163456516]
module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"]: Refreshing state... [id=sgrule-1395389093]
module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"]: Refreshing state... [id=sgrule-1777111604]
module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"]: Refreshing state... [id=sgrule-223191551]
module.eks.aws_security_group_rule.node["ingress_cluster_443"]: Refreshing state... [id=sgrule-4251643989]
module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"]: Refreshing state... [id=sgrule-3292919307]
module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"]: Refreshing state... [id=sgrule-2058399253]
module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"]: Refreshing state... [id=sgrule-4151595338]
module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"]: Refreshing state... [id=sgrule-3019032963]
module.vpc.aws_route_table_association.public[0]: Refreshing state... [id=rtbassoc-02fcb8b002b37c001]
module.vpc.aws_route_table_association.public[1]: Refreshing state... [id=rtbassoc-062fd51226d12561a]
module.vpc.aws_route.public_internet_gateway[0]: Refreshing state... [id=r-rtb-0b9aab65ac4e4a3ba1080289494]
module.vpc.aws_eip.nat[0]: Refreshing state... [id=eipalloc-04a90e0128a0fddda]
module.vpc.aws_route_table_association.private[0]: Refreshing state... [id=rtbassoc-06f506a745155caff]
module.vpc.aws_route_table_association.private[1]: Refreshing state... [id=rtbassoc-0dfdf06c56b879db3]
module.vpc.aws_nat_gateway.this[0]: Refreshing state... [id=nat-0385c62146773d8ce]
module.vpc.aws_route.private_nat_gateway[0]: Refreshing state... [id=r-rtb-07bfe9cc9e0aaff901080289494]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create
 <= read (data resources)

Terraform will perform the following actions:

  # data.aws_iam_policy_document.ebs_csi_trust will be read during apply
  # (config refers to values not yet known)
 <= data "aws_iam_policy_document" "ebs_csi_trust" {
      + id            = (known after apply)
      + json          = (known after apply)
      + minified_json = (known after apply)

      + statement {
          + actions = [
              + "sts:AssumeRoleWithWebIdentity",
            ]

          + condition {
              + test     = "StringEquals"
              + values   = [
                  + "sts.amazonaws.com",
                ]
              + variable = (known after apply)
            }
          + condition {
              + test     = "StringEquals"
              + values   = [
                  + "system:serviceaccount:kube-system:ebs-csi-controller-sa",
                ]
              + variable = (known after apply)
            }

          + principals {
              + identifiers = [
                  + (known after apply),
                ]
              + type        = "Federated"
            }
        }
    }

  # aws_iam_role.ebs_csi will be created
  + resource "aws_iam_role" "ebs_csi" {
      + arn                   = (known after apply)
      + assume_role_policy    = (known after apply)
      + create_date           = (known after apply)
      + force_detach_policies = false
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = "sudhir-campusfix-ebs-csi"
      + name_prefix           = (known after apply)
      + path                  = "/"
      + tags_all              = (known after apply)
      + unique_id             = (known after apply)

      + inline_policy (known after apply)
    }

  # aws_iam_role_policy_attachment.ebs_csi will be created
  + resource "aws_iam_role_policy_attachment" "ebs_csi" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
      + role       = "sudhir-campusfix-ebs-csi"
    }

  # module.eks.data.aws_eks_addon_version.this["aws-ebs-csi-driver"] will be read during apply
  # (depends on a resource or a module with changes pending)
 <= data "aws_eks_addon_version" "this" {
      + addon_name         = "aws-ebs-csi-driver"
      + id                 = (known after apply)
      + kubernetes_version = "1.35"
      + version            = (known after apply)
    }

  # module.eks.data.aws_eks_addon_version.this["coredns"] will be read during apply
  # (depends on a resource or a module with changes pending)
 <= data "aws_eks_addon_version" "this" {
      + addon_name         = "coredns"
      + id                 = (known after apply)
      + kubernetes_version = "1.35"
      + version            = (known after apply)
    }

  # module.eks.data.aws_eks_addon_version.this["kube-proxy"] will be read during apply
  # (depends on a resource or a module with changes pending)
 <= data "aws_eks_addon_version" "this" {
      + addon_name         = "kube-proxy"
      + id                 = (known after apply)
      + kubernetes_version = "1.35"
      + version            = (known after apply)
    }

  # module.eks.data.aws_eks_addon_version.this["vpc-cni"] will be read during apply
  # (depends on a resource or a module with changes pending)
 <= data "aws_eks_addon_version" "this" {
      + addon_name         = "vpc-cni"
      + id                 = (known after apply)
      + kubernetes_version = "1.35"
      + version            = (known after apply)
    }

  # module.eks.data.tls_certificate.this[0] will be read during apply
  # (config refers to values not yet known)
 <= data "tls_certificate" "this" {
      + certificates = (known after apply)
      + id           = (known after apply)
      + url          = (known after apply)
    }

  # module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"] will be created
  + resource "aws_ec2_tag" "cluster_primary_security_group" {
      + id          = (known after apply)
      + key         = "Environment"
      + resource_id = (known after apply)
      + value       = "dev"
    }

  # module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"] will be created
  + resource "aws_ec2_tag" "cluster_primary_security_group" {
      + id          = (known after apply)
      + key         = "ManagedBy"
      + resource_id = (known after apply)
      + value       = "Terraform"
    }

  # module.eks.aws_eks_access_entry.this["cluster_creator"] will be created
  + resource "aws_eks_access_entry" "this" {
      + access_entry_arn  = (known after apply)
      + cluster_name      = (known after apply)
      + created_at        = (known after apply)
      + id                = (known after apply)
      + kubernetes_groups = (known after apply)
      + modified_at       = (known after apply)
      + principal_arn     = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli"
      + tags              = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all          = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + type              = "STANDARD"
      + user_name         = (known after apply)
    }

  # module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"] will be created
  + resource "aws_eks_access_policy_association" "this" {
      + associated_at = (known after apply)
      + cluster_name  = (known after apply)
      + id            = (known after apply)
      + modified_at   = (known after apply)
      + policy_arn    = "arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy"
      + principal_arn = "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli"

      + access_scope {
          + type = "cluster"
        }
    }

  # module.eks.aws_eks_addon.before_compute["vpc-cni"] will be created
  + resource "aws_eks_addon" "before_compute" {
      + addon_name                  = "vpc-cni"
      + addon_version               = (known after apply)
      + arn                         = (known after apply)
      + cluster_name                = (known after apply)
      + configuration_values        = (known after apply)
      + created_at                  = (known after apply)
      + id                          = (known after apply)
      + modified_at                 = (known after apply)
      + preserve                    = true
      + resolve_conflicts_on_create = "OVERWRITE"
      + resolve_conflicts_on_update = "OVERWRITE"
      + tags                        = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all                    = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }

      + timeouts {}
    }

  # module.eks.aws_eks_addon.this["aws-ebs-csi-driver"] will be created
  + resource "aws_eks_addon" "this" {
      + addon_name                  = "aws-ebs-csi-driver"
      + addon_version               = (known after apply)
      + arn                         = (known after apply)
      + cluster_name                = (known after apply)
      + configuration_values        = (known after apply)
      + created_at                  = (known after apply)
      + id                          = (known after apply)
      + modified_at                 = (known after apply)
      + preserve                    = true
      + resolve_conflicts_on_create = "OVERWRITE"
      + resolve_conflicts_on_update = "OVERWRITE"
      + service_account_role_arn    = (known after apply)
      + tags                        = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all                    = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }

      + timeouts {}
    }

  # module.eks.aws_eks_addon.this["coredns"] will be created
  + resource "aws_eks_addon" "this" {
      + addon_name                  = "coredns"
      + addon_version               = (known after apply)
      + arn                         = (known after apply)
      + cluster_name                = (known after apply)
      + configuration_values        = (known after apply)
      + created_at                  = (known after apply)
      + id                          = (known after apply)
      + modified_at                 = (known after apply)
      + preserve                    = true
      + resolve_conflicts_on_create = "OVERWRITE"
      + resolve_conflicts_on_update = "OVERWRITE"
      + tags                        = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all                    = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }

      + timeouts {}
    }

  # module.eks.aws_eks_addon.this["kube-proxy"] will be created
  + resource "aws_eks_addon" "this" {
      + addon_name                  = "kube-proxy"
      + addon_version               = (known after apply)
      + arn                         = (known after apply)
      + cluster_name                = (known after apply)
      + configuration_values        = (known after apply)
      + created_at                  = (known after apply)
      + id                          = (known after apply)
      + modified_at                 = (known after apply)
      + preserve                    = true
      + resolve_conflicts_on_create = "OVERWRITE"
      + resolve_conflicts_on_update = "OVERWRITE"
      + tags                        = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all                    = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }

      + timeouts {}
    }

  # module.eks.aws_eks_cluster.this[0] will be created
  + resource "aws_eks_cluster" "this" {
      + arn                           = (known after apply)
      + bootstrap_self_managed_addons = true
      + certificate_authority         = (known after apply)
      + cluster_id                    = (known after apply)
      + created_at                    = (known after apply)
      + enabled_cluster_log_types     = [
          + "api",
          + "audit",
          + "authenticator",
        ]
      + endpoint                      = (known after apply)
      + id                            = (known after apply)
      + identity                      = (known after apply)
      + name                          = "sudhir-campusfix"
      + platform_version              = (known after apply)
      + role_arn                      = (known after apply)
      + status                        = (known after apply)
      + tags                          = {
          + "Environment"           = "dev"
          + "ManagedBy"             = "Terraform"
          + "terraform-aws-modules" = "eks"
        }
      + tags_all                      = {
          + "Environment"           = "dev"
          + "ManagedBy"             = "Terraform"
          + "terraform-aws-modules" = "eks"
        }
      + version                       = "1.35"

      + access_config {
          + authentication_mode                         = "API_AND_CONFIG_MAP"
          + bootstrap_cluster_creator_admin_permissions = false
        }

      + encryption_config {
          + resources = [
              + "secrets",
            ]

          + provider {
              + key_arn = (known after apply)
            }
        }

      + kubernetes_network_config {
          + ip_family         = "ipv4"
          + service_ipv4_cidr = (known after apply)
          + service_ipv6_cidr = (known after apply)

          + elastic_load_balancing (known after apply)
        }

      + timeouts {}

      + upgrade_policy (known after apply)

      + vpc_config {
          + cluster_security_group_id = (known after apply)
          + endpoint_private_access   = true
          + endpoint_public_access    = true
          + public_access_cidrs       = [
              + "0.0.0.0/0",
            ]
          + security_group_ids        = [
              + "sg-0522074d7a5b86fe2",
            ]
          + subnet_ids                = [
              + "subnet-04516a733d2088208",
              + "subnet-082b0fed2e03ccecf",
            ]
          + vpc_id                    = (known after apply)
        }
    }

  # module.eks.aws_iam_openid_connect_provider.oidc_provider[0] will be created
  + resource "aws_iam_openid_connect_provider" "oidc_provider" {
      + arn             = (known after apply)
      + client_id_list  = [
          + "sts.amazonaws.com",
        ]
      + id              = (known after apply)
      + tags            = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-eks-irsa"
        }
      + tags_all        = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-eks-irsa"
        }
      + thumbprint_list = (known after apply)
      + url             = (known after apply)
    }

  # module.eks.aws_iam_policy.cluster_encryption[0] will be created
  + resource "aws_iam_policy" "cluster_encryption" {
      + arn              = (known after apply)
      + attachment_count = (known after apply)
      + description      = "Cluster encryption policy to allow cluster role to utilize CMK provided"
      + id               = (known after apply)
      + name             = (known after apply)
      + name_prefix      = "sudhir-campusfix-cluster-ClusterEncryption"
      + path             = "/"
      + policy           = (known after apply)
      + policy_id        = (known after apply)
      + tags             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all         = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
    }

  # module.eks.aws_iam_policy.custom[0] will be created
  + resource "aws_iam_policy" "custom" {
      + arn              = (known after apply)
      + attachment_count = (known after apply)
      + id               = (known after apply)
      + name             = (known after apply)
      + name_prefix      = "sudhir-campusfix-cluster-"
      + path             = "/"
      + policy           = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = [
                          + "ec2:RunInstances",
                          + "ec2:CreateLaunchTemplate",
                          + "ec2:CreateFleet",
                        ]
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                          + StringLike   = {
                              + "aws:RequestTag/eks:kubernetes-node-class-name" = "*"
                              + "aws:RequestTag/eks:kubernetes-node-pool-name"  = "*"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = "*"
                      + Sid       = "Compute"
                    },
                  + {
                      + Action    = [
                          + "ec2:CreateVolume",
                          + "ec2:CreateSnapshot",
                        ]
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = [
                          + "arn:aws:ec2:*:*:volume/*",
                          + "arn:aws:ec2:*:*:snapshot/*",
                        ]
                      + Sid       = "Storage"
                    },
                  + {
                      + Action    = "ec2:CreateNetworkInterface"
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name"         = "${aws:PrincipalTag/eks:eks-cluster-name}"
                              + "aws:RequestTag/eks:kubernetes-cni-node-name" = "*"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = "*"
                      + Sid       = "Networking"
                    },
                  + {
                      + Action    = [
                          + "elasticloadbalancing:CreateTargetGroup",
                          + "elasticloadbalancing:CreateRule",
                          + "elasticloadbalancing:CreateLoadBalancer",
                          + "elasticloadbalancing:CreateListener",
                          + "ec2:CreateSecurityGroup",
                        ]
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = "*"
                      + Sid       = "LoadBalancer"
                    },
                  + {
                      + Action    = "shield:CreateProtection"
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = "*"
                      + Sid       = "ShieldProtection"
                    },
                  + {
                      + Action    = "shield:TagResource"
                      + Condition = {
                          + StringEquals = {
                              + "aws:RequestTag/eks:eks-cluster-name" = "${aws:PrincipalTag/eks:eks-cluster-name}"
                            }
                        }
                      + Effect    = "Allow"
                      + Resource  = "arn:aws:shield::*:protection/*"
                      + Sid       = "ShieldTagResource"
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + policy_id        = (known after apply)
      + tags             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all         = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
    }

  # module.eks.aws_iam_role.this[0] will be created
  + resource "aws_iam_role" "this" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = [
                          + "sts:TagSession",
                          + "sts:AssumeRole",
                        ]
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "eks.amazonaws.com"
                        }
                      + Sid       = "EKSClusterAssumeRole"
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + force_detach_policies = true
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = (known after apply)
      + name_prefix           = "sudhir-campusfix-cluster-"
      + path                  = "/"
      + tags                  = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all              = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + unique_id             = (known after apply)

      + inline_policy (known after apply)
    }

  # module.eks.aws_iam_role_policy_attachment.cluster_encryption[0] will be created
  + resource "aws_iam_role_policy_attachment" "cluster_encryption" {
      + id         = (known after apply)
      + policy_arn = (known after apply)
      + role       = (known after apply)
    }

  # module.eks.aws_iam_role_policy_attachment.custom[0] will be created
  + resource "aws_iam_role_policy_attachment" "custom" {
      + id         = (known after apply)
      + policy_arn = (known after apply)
      + role       = (known after apply)
    }

  # module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"] will be created
  + resource "aws_iam_role_policy_attachment" "this" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSClusterPolicy"
      + role       = (known after apply)
    }

  # module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"] will be created
  + resource "aws_iam_role_policy_attachment" "this" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSVPCResourceController"
      + role       = (known after apply)
    }

  # module.eks.time_sleep.this[0] will be created
  + resource "time_sleep" "this" {
      + create_duration = "30s"
      + id              = (known after apply)
      + triggers        = {
          + "cluster_certificate_authority_data" = (known after apply)
          + "cluster_endpoint"                   = (known after apply)
          + "cluster_name"                       = (known after apply)
          + "cluster_service_cidr"               = (known after apply)
          + "cluster_version"                    = "1.35"
        }
    }

  # module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0] will be created
  + resource "aws_eks_node_group" "this" {
      + ami_type               = "AL2023_x86_64_STANDARD"
      + arn                    = (known after apply)
      + capacity_type          = (known after apply)
      + cluster_name           = (known after apply)
      + disk_size              = (known after apply)
      + id                     = (known after apply)
      + instance_types         = [
          + "t3.medium",
        ]
      + node_group_name        = (known after apply)
      + node_group_name_prefix = "main-"
      + node_role_arn          = (known after apply)
      + release_version        = (known after apply)
      + resources              = (known after apply)
      + status                 = (known after apply)
      + subnet_ids             = [
          + "subnet-04516a733d2088208",
          + "subnet-082b0fed2e03ccecf",
        ]
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "main"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "main"
        }
      + version                = "1.35"

      + launch_template {
          + id      = (known after apply)
          + name    = (known after apply)
          + version = (known after apply)
        }

      + node_repair_config (known after apply)

      + scaling_config {
          + desired_size = 2
          + max_size     = 3
          + min_size     = 1
        }

      + timeouts {}

      + update_config {
          + max_unavailable_percentage = 33
        }
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0] will be created
  + resource "aws_iam_role" "this" {
      + arn                   = (known after apply)
      + assume_role_policy    = jsonencode(
            {
              + Statement = [
                  + {
                      + Action    = "sts:AssumeRole"
                      + Effect    = "Allow"
                      + Principal = {
                          + Service = "ec2.amazonaws.com"
                        }
                      + Sid       = "EKSNodeAssumeRole"
                    },
                ]
              + Version   = "2012-10-17"
            }
        )
      + create_date           = (known after apply)
      + description           = "EKS managed node group IAM role"
      + force_detach_policies = true
      + id                    = (known after apply)
      + managed_policy_arns   = (known after apply)
      + max_session_duration  = 3600
      + name                  = (known after apply)
      + name_prefix           = "main-eks-node-group-"
      + path                  = "/"
      + tags                  = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all              = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + unique_id             = (known after apply)

      + inline_policy (known after apply)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"] will be created
  + resource "aws_iam_role_policy_attachment" "this" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
      + role       = (known after apply)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"] will be created
  + resource "aws_iam_role_policy_attachment" "this" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy"
      + role       = (known after apply)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"] will be created
  + resource "aws_iam_role_policy_attachment" "this" {
      + id         = (known after apply)
      + policy_arn = "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy"
      + role       = (known after apply)
    }

  # module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0] will be created
  + resource "aws_launch_template" "this" {
      + arn                    = (known after apply)
      + default_version        = (known after apply)
      + description            = "Custom launch template for main EKS managed node group"
      + id                     = (known after apply)
      + latest_version         = (known after apply)
      + name                   = (known after apply)
      + name_prefix            = "main-"
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
        }
      + update_default_version = true
      + vpc_security_group_ids = [
          + "sg-0cc92304f43995481",
        ]
        # (2 unchanged attributes hidden)

      + metadata_options {
          + http_endpoint               = "enabled"
          + http_protocol_ipv6          = (known after apply)
          + http_put_response_hop_limit = 2
          + http_tokens                 = "required"
          + instance_metadata_tags      = (known after apply)
        }

      + monitoring {
          + enabled = true
        }

      + tag_specifications {
          + resource_type = "instance"
          + tags          = {
              + "Environment" = "dev"
              + "ManagedBy"   = "Terraform"
              + "Name"        = "main"
            }
        }
      + tag_specifications {
          + resource_type = "network-interface"
          + tags          = {
              + "Environment" = "dev"
              + "ManagedBy"   = "Terraform"
              + "Name"        = "main"
            }
        }
      + tag_specifications {
          + resource_type = "volume"
          + tags          = {
              + "Environment" = "dev"
              + "ManagedBy"   = "Terraform"
              + "Name"        = "main"
            }
        }
    }

  # module.eks.module.kms.data.aws_iam_policy_document.this[0] will be read during apply
  # (config refers to values not yet known)
 <= data "aws_iam_policy_document" "this" {
      + id                        = (known after apply)
      + json                      = (known after apply)
      + minified_json             = (known after apply)
      + override_policy_documents = []
      + source_policy_documents   = []

      + statement {
          + actions   = [
              + "kms:*",
            ]
          + resources = [
              + "*",
            ]
          + sid       = "Default"

          + principals {
              + identifiers = [
                  + "arn:aws:iam::[AWS_ACCOUNT_ID]:root",
                ]
              + type        = "AWS"
            }
        }
      + statement {
          + actions   = [
              + "kms:CancelKeyDeletion",
              + "kms:Create*",
              + "kms:Delete*",
              + "kms:Describe*",
              + "kms:Disable*",
              + "kms:Enable*",
              + "kms:Get*",
              + "kms:ImportKeyMaterial",
              + "kms:List*",
              + "kms:Put*",
              + "kms:ReplicateKey",
              + "kms:Revoke*",
              + "kms:ScheduleKeyDeletion",
              + "kms:TagResource",
              + "kms:UntagResource",
              + "kms:Update*",
            ]
          + resources = [
              + "*",
            ]
          + sid       = "KeyAdministration"

          + principals {
              + identifiers = [
                  + "arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli",
                ]
              + type        = "AWS"
            }
        }
      + statement {
          + actions   = [
              + "kms:Decrypt",
              + "kms:DescribeKey",
              + "kms:Encrypt",
              + "kms:GenerateDataKey*",
              + "kms:ReEncrypt*",
            ]
          + resources = [
              + "*",
            ]
          + sid       = "KeyUsage"

          + principals {
              + identifiers = [
                  + (known after apply),
                ]
              + type        = "AWS"
            }
        }
    }

  # module.eks.module.kms.aws_kms_alias.this["cluster"] will be created
  + resource "aws_kms_alias" "this" {
      + arn            = (known after apply)
      + id             = (known after apply)
      + name           = "alias/eks/sudhir-campusfix"
      + name_prefix    = (known after apply)
      + target_key_arn = (known after apply)
      + target_key_id  = (known after apply)
    }

  # module.eks.module.kms.aws_kms_key.this[0] will be created
  + resource "aws_kms_key" "this" {
      + arn                                = (known after apply)
      + bypass_policy_lockout_safety_check = false
      + customer_master_key_spec           = "SYMMETRIC_DEFAULT"
      + description                        = "sudhir-campusfix cluster encryption key"
      + enable_key_rotation                = true
      + id                                 = (known after apply)
      + is_enabled                         = true
      + key_id                             = (known after apply)
      + key_usage                          = "ENCRYPT_DECRYPT"
      + multi_region                       = false
      + policy                             = (known after apply)
      + rotation_period_in_days            = (known after apply)
      + tags                               = {
          + "Environment"           = "dev"
          + "ManagedBy"             = "Terraform"
          + "terraform-aws-modules" = "eks"
        }
      + tags_all                           = {
          + "Environment"           = "dev"
          + "ManagedBy"             = "Terraform"
          + "terraform-aws-modules" = "eks"
        }
    }

  # module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr will be created
  + resource "null_resource" "validate_cluster_service_cidr" {
      + id = (known after apply)
    }

Plan: 29 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + cluster_endpoint  = (known after apply)
module.eks.aws_iam_policy.custom[0]: Creating...
module.eks.aws_iam_role.this[0]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Creating...
module.eks.aws_iam_policy.custom[0]: Creation complete after 2s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-20261013022113872700000003]
module.eks.module.eks_managed_node_group["main"].aws_iam_role.this[0]: Creation complete after 2s [id=main-eks-node-group-20261013022113872700000001]
module.eks.aws_iam_role.this[0]: Creation complete after 2s [id=sudhir-campusfix-cluster-20261013022113872700000002]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Creating...
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Creating...
module.eks.aws_iam_role_policy_attachment.custom[0]: Creating...
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Creating...
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Reading...
module.eks.module.kms.data.aws_iam_policy_document.this[0]: Read complete after 0s [id=729080925]
module.eks.module.kms.aws_kms_key.this[0]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKS_CNI_Policy"]: Creation complete after 1s [id=main-eks-node-group-20261013022113872700000001-20261013022116235800000004]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEKSWorkerNodePolicy"]: Creation complete after 1s [id=main-eks-node-group-20261013022113872700000001-20261013022116243100000005]
module.eks.module.eks_managed_node_group["main"].aws_iam_role_policy_attachment.this["AmazonEC2ContainerRegistryReadOnly"]: Creation complete after 1s [id=main-eks-node-group-20261013022113872700000001-20261013022116283300000006]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSVPCResourceController"]: Creation complete after 1s [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116557100000007]
module.eks.aws_iam_role_policy_attachment.this["AmazonEKSClusterPolicy"]: Creation complete after 1s [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116561000000008]
module.eks.aws_iam_role_policy_attachment.custom[0]: Creation complete after 1s [id=sudhir-campusfix-cluster-20261013022113872700000002-20261013022116581800000009]
module.eks.module.kms.aws_kms_key.this[0]: Still creating... [00m10s elapsed]
module.eks.module.kms.aws_kms_key.this[0]: Still creating... [00m20s elapsed]
module.eks.module.kms.aws_kms_key.this[0]: Creation complete after 27s [id=37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c]
module.eks.module.kms.aws_kms_alias.this["cluster"]: Creating...
module.eks.aws_iam_policy.cluster_encryption[0]: Creating...
module.eks.aws_eks_cluster.this[0]: Creating...
module.eks.module.kms.aws_kms_alias.this["cluster"]: Creation complete after 0s [id=alias/eks/sudhir-campusfix]
module.eks.aws_iam_policy.cluster_encryption[0]: Creation complete after 1s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:policy/sudhir-campusfix-cluster-ClusterEncryption2026101302214274200000000a]
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Creating...
module.eks.aws_iam_role_policy_attachment.cluster_encryption[0]: Creation complete after 0s [id=sudhir-campusfix-cluster-20261013022113872700000002-2026101302214389440000000b]
module.eks.aws_eks_cluster.this[0]: Still creating... [00m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [00m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [00m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [00m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [00m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [01m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [02m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [03m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [04m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [05m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [06m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m10s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m20s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m30s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m40s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [07m50s elapsed]
module.eks.aws_eks_cluster.this[0]: Still creating... [08m00s elapsed]
module.eks.aws_eks_cluster.this[0]: Creation complete after 8m8s [id=sudhir-campusfix]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Creating...
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Creating...
module.eks.aws_eks_access_entry.this["cluster_creator"]: Creating...
module.eks.time_sleep.this[0]: Creating...
module.eks.data.tls_certificate.this[0]: Reading...
module.eks.data.tls_certificate.this[0]: Read complete after 1s [id=1e3a331631939a1ae4a625cd4244a4963dabbfa2]
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Creating...
module.eks.aws_ec2_tag.cluster_primary_security_group["Environment"]: Creation complete after 1s [id=sg-00c2059b40e40b1b0,Environment]
module.eks.aws_ec2_tag.cluster_primary_security_group["ManagedBy"]: Creation complete after 1s [id=sg-00c2059b40e40b1b0,ManagedBy]
module.eks.aws_eks_access_entry.this["cluster_creator"]: Creation complete after 1s [id=sudhir-campusfix:arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli]
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Creating...
module.eks.aws_eks_access_policy_association.this["cluster_creator_admin"]: Creation complete after 0s [id=sudhir-campusfix#arn:aws:iam::[AWS_ACCOUNT_ID]:user/rudray-cli#arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy]
module.eks.time_sleep.this[0]: Still creating... [00m10s elapsed]
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Still creating... [00m10s elapsed]
module.eks.aws_iam_openid_connect_provider.oidc_provider[0]: Creation complete after 11s [id=arn:aws:iam::[AWS_ACCOUNT_ID]:oidc-provider/oidc.eks.ap-south-1.amazonaws.com/id/C8FE139F4147098CE5611530B3ADF3F5]
data.aws_iam_policy_document.ebs_csi_trust: Reading...
data.aws_iam_policy_document.ebs_csi_trust: Read complete after 0s [id=393383685]
aws_iam_role.ebs_csi: Creating...
aws_iam_role.ebs_csi: Creation complete after 1s [id=sudhir-campusfix-ebs-csi]
aws_iam_role_policy_attachment.ebs_csi: Creating...
module.eks.data.aws_eks_addon_version.this["coredns"]: Reading...
module.eks.data.aws_eks_addon_version.this["kube-proxy"]: Reading...
module.eks.data.aws_eks_addon_version.this["vpc-cni"]: Reading...
module.eks.data.aws_eks_addon_version.this["aws-ebs-csi-driver"]: Reading...
module.eks.data.aws_eks_addon_version.this["aws-ebs-csi-driver"]: Read complete after 0s [id=aws-ebs-csi-driver]
module.eks.data.aws_eks_addon_version.this["kube-proxy"]: Read complete after 1s [id=kube-proxy]
module.eks.data.aws_eks_addon_version.this["coredns"]: Read complete after 1s [id=coredns]
module.eks.data.aws_eks_addon_version.this["vpc-cni"]: Read complete after 1s [id=vpc-cni]
module.eks.aws_eks_addon.before_compute["vpc-cni"]: Creating...
aws_iam_role_policy_attachment.ebs_csi: Creation complete after 1s [id=sudhir-campusfix-ebs-csi-2026101302300466330000000d]
module.eks.time_sleep.this[0]: Still creating... [00m20s elapsed]
module.eks.aws_eks_addon.before_compute["vpc-cni"]: Creation complete after 7s [id=sudhir-campusfix:vpc-cni]
module.eks.time_sleep.this[0]: Still creating... [00m30s elapsed]
module.eks.time_sleep.this[0]: Creation complete after 30s [id=2026-10-13T02:30:21Z]
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Creating...
module.eks.module.eks_managed_node_group["main"].module.user_data.null_resource.validate_cluster_service_cidr: Creation complete after 0s [id=3032463307649055476]
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_launch_template.this[0]: Creation complete after 6s [id=lt-0c342f02f8398c6cc]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Creating...
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [00m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [00m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [00m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [00m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [00m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m30s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m40s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [01m50s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [02m00s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [02m10s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Still creating... [02m20s elapsed]
module.eks.module.eks_managed_node_group["main"].aws_eks_node_group.this[0]: Creation complete after 2m29s [id=sudhir-campusfix:main-20261013023027045600000010]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Creating...
module.eks.aws_eks_addon.this["kube-proxy"]: Creating...
module.eks.aws_eks_addon.this["coredns"]: Creating...
module.eks.aws_eks_addon.this["kube-proxy"]: Creation complete after 7s [id=sudhir-campusfix:kube-proxy]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Still creating... [00m10s elapsed]
module.eks.aws_eks_addon.this["coredns"]: Still creating... [00m10s elapsed]
module.eks.aws_eks_addon.this["coredns"]: Creation complete after 14s [id=sudhir-campusfix:coredns]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Still creating... [00m20s elapsed]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Still creating... [00m30s elapsed]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Still creating... [00m40s elapsed]
module.eks.aws_eks_addon.this["aws-ebs-csi-driver"]: Creation complete after 44s [id=sudhir-campusfix:aws-ebs-csi-driver]

Apply complete! Resources: 29 added, 0 changed, 0 destroyed.

Outputs:

cluster_endpoint = "https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com"
cluster_name = "sudhir-campusfix"
configure_kubectl = "aws eks update-kubeconfig --region ap-south-1 --name sudhir-campusfix"
vpc_id = "vpc-0b236660178acfe8c"

```

Exit code: 0
