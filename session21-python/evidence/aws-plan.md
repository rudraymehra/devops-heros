# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T02:05:44.082556+00:00

Working directory: session21-python/terraform

```text
$ /tmp/campusfix-tools.FCoLVB/terraform show -no-color /tmp/campusfix.tfplan

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

  # module.eks.aws_cloudwatch_log_group.this[0] will be created
  + resource "aws_cloudwatch_log_group" "this" {
      + arn               = (known after apply)
      + id                = (known after apply)
      + log_group_class   = (known after apply)
      + name              = "/aws/eks/sudhir-campusfix/cluster"
      + name_prefix       = (known after apply)
      + retention_in_days = 90
      + skip_destroy      = false
      + tags              = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "/aws/eks/sudhir-campusfix/cluster"
        }
      + tags_all          = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "/aws/eks/sudhir-campusfix/cluster"
        }
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
          + security_group_ids        = (known after apply)
          + subnet_ids                = (known after apply)
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

  # module.eks.aws_security_group.cluster[0] will be created
  + resource "aws_security_group" "cluster" {
      + arn                    = (known after apply)
      + description            = "EKS cluster security group"
      + egress                 = (known after apply)
      + id                     = (known after apply)
      + ingress                = (known after apply)
      + name                   = (known after apply)
      + name_prefix            = "sudhir-campusfix-cluster-"
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-cluster"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-cluster"
        }
      + vpc_id                 = (known after apply)
    }

  # module.eks.aws_security_group.node[0] will be created
  + resource "aws_security_group" "node" {
      + arn                    = (known after apply)
      + description            = "EKS node shared security group"
      + egress                 = (known after apply)
      + id                     = (known after apply)
      + ingress                = (known after apply)
      + name                   = (known after apply)
      + name_prefix            = "sudhir-campusfix-node-"
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags                   = {
          + "Environment"                            = "dev"
          + "ManagedBy"                              = "Terraform"
          + "Name"                                   = "sudhir-campusfix-node"
          + "kubernetes.io/cluster/sudhir-campusfix" = "owned"
        }
      + tags_all               = {
          + "Environment"                            = "dev"
          + "ManagedBy"                              = "Terraform"
          + "Name"                                   = "sudhir-campusfix-node"
          + "kubernetes.io/cluster/sudhir-campusfix" = "owned"
        }
      + vpc_id                 = (known after apply)
    }

  # module.eks.aws_security_group_rule.cluster["ingress_nodes_443"] will be created
  + resource "aws_security_group_rule" "cluster" {
      + description              = "Node groups to cluster API"
      + from_port                = 443
      + id                       = (known after apply)
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["egress_all"] will be created
  + resource "aws_security_group_rule" "node" {
      + cidr_blocks              = [
          + "0.0.0.0/0",
        ]
      + description              = "Allow all egress"
      + from_port                = 0
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "-1"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 0
      + type                     = "egress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_443"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node groups"
      + from_port                = 443
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_4443_webhook"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node 4443/tcp webhook"
      + from_port                = 4443
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 4443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_6443_webhook"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node 6443/tcp webhook"
      + from_port                = 6443
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 6443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_8443_webhook"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node 8443/tcp webhook"
      + from_port                = 8443
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 8443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_9443_webhook"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node 9443/tcp webhook"
      + from_port                = 9443
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 9443
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_cluster_kubelet"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Cluster API to node kubelets"
      + from_port                = 10250
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = false
      + source_security_group_id = (known after apply)
      + to_port                  = 10250
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_nodes_ephemeral"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Node to node ingress on ephemeral ports"
      + from_port                = 1025
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = true
      + source_security_group_id = (known after apply)
      + to_port                  = 65535
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_self_coredns_tcp"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Node to node CoreDNS"
      + from_port                = 53
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "tcp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = true
      + source_security_group_id = (known after apply)
      + to_port                  = 53
      + type                     = "ingress"
    }

  # module.eks.aws_security_group_rule.node["ingress_self_coredns_udp"] will be created
  + resource "aws_security_group_rule" "node" {
      + description              = "Node to node CoreDNS UDP"
      + from_port                = 53
      + id                       = (known after apply)
      + prefix_list_ids          = []
      + protocol                 = "udp"
      + security_group_id        = (known after apply)
      + security_group_rule_id   = (known after apply)
      + self                     = true
      + source_security_group_id = (known after apply)
      + to_port                  = 53
      + type                     = "ingress"
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

  # module.vpc.aws_default_network_acl.this[0] will be created
  + resource "aws_default_network_acl" "this" {
      + arn                    = (known after apply)
      + default_network_acl_id = (known after apply)
      + id                     = (known after apply)
      + owner_id               = (known after apply)
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + vpc_id                 = (known after apply)

      + egress {
          + action          = "allow"
          + from_port       = 0
          + ipv6_cidr_block = "::/0"
          + protocol        = "-1"
          + rule_no         = 101
          + to_port         = 0
            # (1 unchanged attribute hidden)
        }
      + egress {
          + action          = "allow"
          + cidr_block      = "0.0.0.0/0"
          + from_port       = 0
          + protocol        = "-1"
          + rule_no         = 100
          + to_port         = 0
            # (1 unchanged attribute hidden)
        }

      + ingress {
          + action          = "allow"
          + from_port       = 0
          + ipv6_cidr_block = "::/0"
          + protocol        = "-1"
          + rule_no         = 101
          + to_port         = 0
            # (1 unchanged attribute hidden)
        }
      + ingress {
          + action          = "allow"
          + cidr_block      = "0.0.0.0/0"
          + from_port       = 0
          + protocol        = "-1"
          + rule_no         = 100
          + to_port         = 0
            # (1 unchanged attribute hidden)
        }
    }

  # module.vpc.aws_default_route_table.default[0] will be created
  + resource "aws_default_route_table" "default" {
      + arn                    = (known after apply)
      + default_route_table_id = (known after apply)
      + id                     = (known after apply)
      + owner_id               = (known after apply)
      + route                  = (known after apply)
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + vpc_id                 = (known after apply)

      + timeouts {
          + create = "5m"
          + update = "5m"
        }
    }

  # module.vpc.aws_default_security_group.this[0] will be created
  + resource "aws_default_security_group" "this" {
      + arn                    = (known after apply)
      + description            = (known after apply)
      + egress                 = (known after apply)
      + id                     = (known after apply)
      + ingress                = (known after apply)
      + name                   = (known after apply)
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + revoke_rules_on_delete = false
      + tags                   = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + tags_all               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-default"
        }
      + vpc_id                 = (known after apply)
    }

  # module.vpc.aws_eip.nat[0] will be created
  + resource "aws_eip" "nat" {
      + allocation_id        = (known after apply)
      + arn                  = (known after apply)
      + association_id       = (known after apply)
      + carrier_ip           = (known after apply)
      + customer_owned_ip    = (known after apply)
      + domain               = "vpc"
      + id                   = (known after apply)
      + instance             = (known after apply)
      + ipam_pool_id         = (known after apply)
      + network_border_group = (known after apply)
      + network_interface    = (known after apply)
      + private_dns          = (known after apply)
      + private_ip           = (known after apply)
      + ptr_record           = (known after apply)
      + public_dns           = (known after apply)
      + public_ip            = (known after apply)
      + public_ipv4_pool     = (known after apply)
      + tags                 = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        }
      + tags_all             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        }
      + vpc                  = (known after apply)
    }

  # module.vpc.aws_internet_gateway.this[0] will be created
  + resource "aws_internet_gateway" "this" {
      + arn      = (known after apply)
      + id       = (known after apply)
      + owner_id = (known after apply)
      + tags     = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc"
        }
      + tags_all = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc"
        }
      + vpc_id   = (known after apply)
    }

  # module.vpc.aws_nat_gateway.this[0] will be created
  + resource "aws_nat_gateway" "this" {
      + allocation_id                      = (known after apply)
      + association_id                     = (known after apply)
      + connectivity_type                  = "public"
      + id                                 = (known after apply)
      + network_interface_id               = (known after apply)
      + private_ip                         = (known after apply)
      + public_ip                          = (known after apply)
      + secondary_private_ip_address_count = (known after apply)
      + secondary_private_ip_addresses     = (known after apply)
      + subnet_id                          = (known after apply)
      + tags                               = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        }
      + tags_all                           = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-ap-south-1a"
        }
    }

  # module.vpc.aws_route.private_nat_gateway[0] will be created
  + resource "aws_route" "private_nat_gateway" {
      + destination_cidr_block = "0.0.0.0/0"
      + id                     = (known after apply)
      + instance_id            = (known after apply)
      + instance_owner_id      = (known after apply)
      + nat_gateway_id         = (known after apply)
      + network_interface_id   = (known after apply)
      + origin                 = (known after apply)
      + route_table_id         = (known after apply)
      + state                  = (known after apply)

      + timeouts {
          + create = "5m"
        }
    }

  # module.vpc.aws_route.public_internet_gateway[0] will be created
  + resource "aws_route" "public_internet_gateway" {
      + destination_cidr_block = "0.0.0.0/0"
      + gateway_id             = (known after apply)
      + id                     = (known after apply)
      + instance_id            = (known after apply)
      + instance_owner_id      = (known after apply)
      + network_interface_id   = (known after apply)
      + origin                 = (known after apply)
      + route_table_id         = (known after apply)
      + state                  = (known after apply)

      + timeouts {
          + create = "5m"
        }
    }

  # module.vpc.aws_route_table.private[0] will be created
  + resource "aws_route_table" "private" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + route            = (known after apply)
      + tags             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-private"
        }
      + tags_all         = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-private"
        }
      + vpc_id           = (known after apply)
    }

  # module.vpc.aws_route_table.public[0] will be created
  + resource "aws_route_table" "public" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + route            = (known after apply)
      + tags             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-public"
        }
      + tags_all         = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc-public"
        }
      + vpc_id           = (known after apply)
    }

  # module.vpc.aws_route_table_association.private[0] will be created
  + resource "aws_route_table_association" "private" {
      + id             = (known after apply)
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # module.vpc.aws_route_table_association.private[1] will be created
  + resource "aws_route_table_association" "private" {
      + id             = (known after apply)
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # module.vpc.aws_route_table_association.public[0] will be created
  + resource "aws_route_table_association" "public" {
      + id             = (known after apply)
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # module.vpc.aws_route_table_association.public[1] will be created
  + resource "aws_route_table_association" "public" {
      + id             = (known after apply)
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # module.vpc.aws_subnet.private[0] will be created
  + resource "aws_subnet" "private" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "ap-south-1a"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.20.1.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags                                           = {
          + "Environment"                     = "dev"
          + "ManagedBy"                       = "Terraform"
          + "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1a"
          + "kubernetes.io/role/internal-elb" = "1"
        }
      + tags_all                                       = {
          + "Environment"                     = "dev"
          + "ManagedBy"                       = "Terraform"
          + "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1a"
          + "kubernetes.io/role/internal-elb" = "1"
        }
      + vpc_id                                         = (known after apply)
    }

  # module.vpc.aws_subnet.private[1] will be created
  + resource "aws_subnet" "private" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "ap-south-1b"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.20.2.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags                                           = {
          + "Environment"                     = "dev"
          + "ManagedBy"                       = "Terraform"
          + "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1b"
          + "kubernetes.io/role/internal-elb" = "1"
        }
      + tags_all                                       = {
          + "Environment"                     = "dev"
          + "ManagedBy"                       = "Terraform"
          + "Name"                            = "sudhir-campusfix-vpc-private-ap-south-1b"
          + "kubernetes.io/role/internal-elb" = "1"
        }
      + vpc_id                                         = (known after apply)
    }

  # module.vpc.aws_subnet.public[0] will be created
  + resource "aws_subnet" "public" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "ap-south-1a"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.20.101.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags                                           = {
          + "Environment"            = "dev"
          + "ManagedBy"              = "Terraform"
          + "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1a"
          + "kubernetes.io/role/elb" = "1"
        }
      + tags_all                                       = {
          + "Environment"            = "dev"
          + "ManagedBy"              = "Terraform"
          + "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1a"
          + "kubernetes.io/role/elb" = "1"
        }
      + vpc_id                                         = (known after apply)
    }

  # module.vpc.aws_subnet.public[1] will be created
  + resource "aws_subnet" "public" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "ap-south-1b"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.20.102.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = false
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + tags                                           = {
          + "Environment"            = "dev"
          + "ManagedBy"              = "Terraform"
          + "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1b"
          + "kubernetes.io/role/elb" = "1"
        }
      + tags_all                                       = {
          + "Environment"            = "dev"
          + "ManagedBy"              = "Terraform"
          + "Name"                   = "sudhir-campusfix-vpc-public-ap-south-1b"
          + "kubernetes.io/role/elb" = "1"
        }
      + vpc_id                                         = (known after apply)
    }

  # module.vpc.aws_vpc.this[0] will be created
  + resource "aws_vpc" "this" {
      + arn                                  = (known after apply)
      + cidr_block                           = "10.20.0.0/16"
      + default_network_acl_id               = (known after apply)
      + default_route_table_id               = (known after apply)
      + default_security_group_id            = (known after apply)
      + dhcp_options_id                      = (known after apply)
      + enable_dns_hostnames                 = true
      + enable_dns_support                   = true
      + enable_network_address_usage_metrics = (known after apply)
      + id                                   = (known after apply)
      + instance_tenancy                     = "default"
      + ipv6_association_id                  = (known after apply)
      + ipv6_cidr_block                      = (known after apply)
      + ipv6_cidr_block_network_border_group = (known after apply)
      + main_route_table_id                  = (known after apply)
      + owner_id                             = (known after apply)
      + tags                                 = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc"
        }
      + tags_all                             = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-campusfix-vpc"
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
      + subnet_ids             = (known after apply)
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
      + vpc_security_group_ids = (known after apply)
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

Plan: 62 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + cluster_endpoint  = (known after apply)
  + cluster_name      = "sudhir-campusfix"
  + configure_kubectl = "aws eks update-kubeconfig --region ap-south-1 --name sudhir-campusfix"
  + vpc_id            = (known after apply)

```

Exit code: 0
