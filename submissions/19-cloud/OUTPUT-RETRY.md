# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:41:56.281775+00:00

Working directory: .

```text
$ python3 session21-python/scripts/small-cloud-lab.py 19 --terraform /tmp/campusfix-tools.FCoLVB/terraform
$ /tmp/campusfix-tools.FCoLVB/terraform init -no-color
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/aws v6.68.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
 
$ /tmp/campusfix-tools.FCoLVB/terraform fmt -check
 
$ /tmp/campusfix-tools.FCoLVB/terraform validate -no-color
Success! The configuration is valid.

 
$ /tmp/campusfix-tools.FCoLVB/terraform plan -no-color -out=/tmp/campusfix-session19.tfplan -var=project_suffix=sudhir24bcs10425-20261013
data.aws_ami.amazon_linux: Reading...
data.aws_caller_identity.current: Reading...
data.aws_caller_identity.current: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
data.aws_ami.amazon_linux: Read complete after 1s [id=ami-0324b92f52e4d7a4a]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_instance.web will be created
  + resource "aws_instance" "web" {
      + ami                                  = "ami-0324b92f52e4d7a4a"
      + arn                                  = (known after apply)
      + associate_public_ip_address          = true
      + availability_zone                    = (known after apply)
      + disable_api_stop                     = (known after apply)
      + disable_api_termination              = (known after apply)
      + ebs_optimized                        = (known after apply)
      + enable_primary_ipv6                  = (known after apply)
      + force_destroy                        = false
      + get_password_data                    = false
      + host_id                              = (known after apply)
      + host_resource_group_arn              = (known after apply)
      + iam_instance_profile                 = (known after apply)
      + id                                   = (known after apply)
      + instance_initiated_shutdown_behavior = (known after apply)
      + instance_lifecycle                   = (known after apply)
      + instance_state                       = (known after apply)
      + instance_type                        = "t3.micro"
      + ipv6_address_count                   = (known after apply)
      + ipv6_addresses                       = (known after apply)
      + key_name                             = (known after apply)
      + monitoring                           = (known after apply)
      + outpost_arn                          = (known after apply)
      + password_data                        = (known after apply)
      + placement_group                      = (known after apply)
      + placement_group_id                   = (known after apply)
      + placement_partition_number           = (known after apply)
      + primary_network_interface_id         = (known after apply)
      + private_dns                          = (known after apply)
      + private_ip                           = (known after apply)
      + public_dns                           = (known after apply)
      + public_ip                            = (known after apply)
      + region                               = "ap-south-1"
      + secondary_private_ips                = (known after apply)
      + security_groups                      = (known after apply)
      + source_dest_check                    = true
      + spot_instance_request_id             = (known after apply)
      + subnet_id                            = (known after apply)
      + tags                                 = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-web"
          + "Session"   = "19"
        }
      + tags_all                             = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-web"
          + "Session"   = "19"
        }
      + tenancy                              = (known after apply)
      + user_data                            = <<-EOT
            #!/bin/bash
            set -eux
            dnf install -y nginx
            echo '<h1>Sudhir Mehra: Terraform Cloud Lab</h1><p>24 BCS 10425 | Batch B</p>' > /usr/share/nginx/html/index.html
            systemctl enable --now nginx
        EOT
      + user_data_base64                     = (known after apply)
      + user_data_replace_on_change          = false
      + vpc_security_group_ids               = (known after apply)

      + capacity_reservation_specification (known after apply)

      + cpu_options (known after apply)

      + ebs_block_device (known after apply)

      + enclave_options (known after apply)

      + ephemeral_block_device (known after apply)

      + instance_market_options (known after apply)

      + maintenance_options (known after apply)

      + metadata_options {
          + http_endpoint               = "enabled"
          + http_protocol_ipv6          = "disabled"
          + http_put_response_hop_limit = (known after apply)
          + http_tokens                 = "required"
          + instance_metadata_tags      = (known after apply)
        }

      + network_interface (known after apply)

      + primary_network_interface (known after apply)

      + private_dns_name_options (known after apply)

      + root_block_device {
          + delete_on_termination = true
          + device_name           = (known after apply)
          + encrypted             = true
          + iops                  = (known after apply)
          + kms_key_id            = (known after apply)
          + tags_all              = (known after apply)
          + throughput            = (known after apply)
          + volume_id             = (known after apply)
          + volume_size           = 8
          + volume_type           = "gp3"
        }

      + secondary_network_interface (known after apply)
    }

  # aws_internet_gateway.main will be created
  + resource "aws_internet_gateway" "main" {
      + arn      = (known after apply)
      + id       = (known after apply)
      + owner_id = (known after apply)
      + region   = "ap-south-1"
      + tags     = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-igw"
          + "Session"   = "19"
        }
      + tags_all = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-igw"
          + "Session"   = "19"
        }
      + vpc_id   = (known after apply)
    }

  # aws_route_table.public will be created
  + resource "aws_route_table" "public" {
      + arn              = (known after apply)
      + id               = (known after apply)
      + owner_id         = (known after apply)
      + propagating_vgws = (known after apply)
      + region           = "ap-south-1"
      + route            = [
          + {
              + cidr_block                 = "0.0.0.0/0"
              + gateway_id                 = (known after apply)
                # (12 unchanged attributes hidden)
            },
        ]
      + tags             = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-public-rt"
          + "Session"   = "19"
        }
      + tags_all         = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-public-rt"
          + "Session"   = "19"
        }
      + vpc_id           = (known after apply)
    }

  # aws_route_table_association.public will be created
  + resource "aws_route_table_association" "public" {
      + id             = (known after apply)
      + region         = "ap-south-1"
      + route_table_id = (known after apply)
      + subnet_id      = (known after apply)
    }

  # aws_s3_bucket.artifacts will be created
  + resource "aws_s3_bucket" "artifacts" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "session19-[AWS_ACCOUNT_ID]-sudhir24bcs10425-20261013"
      + bucket_domain_name          = (known after apply)
      + bucket_namespace            = (known after apply)
      + bucket_prefix               = (known after apply)
      + bucket_region               = (known after apply)
      + bucket_regional_domain_name = (known after apply)
      + force_destroy               = false
      + hosted_zone_id              = (known after apply)
      + id                          = (known after apply)
      + object_lock_enabled         = (known after apply)
      + policy                      = (known after apply)
      + region                      = "ap-south-1"
      + request_payer               = (known after apply)
      + tags                        = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-artifacts"
          + "Session"   = "19"
        }
      + tags_all                    = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-artifacts"
          + "Session"   = "19"
        }
      + website_domain              = (known after apply)
      + website_endpoint            = (known after apply)

      + cors_rule (known after apply)

      + grant (known after apply)

      + lifecycle_rule (known after apply)

      + logging (known after apply)

      + object_lock_configuration (known after apply)

      + replication_configuration (known after apply)

      + server_side_encryption_configuration (known after apply)

      + versioning (known after apply)

      + website (known after apply)
    }

  # aws_s3_bucket_public_access_block.artifacts will be created
  + resource "aws_s3_bucket_public_access_block" "artifacts" {
      + block_public_acls       = true
      + block_public_policy     = true
      + bucket                  = (known after apply)
      + id                      = (known after apply)
      + ignore_public_acls      = true
      + region                  = "ap-south-1"
      + restrict_public_buckets = true
    }

  # aws_s3_bucket_server_side_encryption_configuration.artifacts will be created
  + resource "aws_s3_bucket_server_side_encryption_configuration" "artifacts" {
      + bucket = (known after apply)
      + id     = (known after apply)
      + region = "ap-south-1"

      + rule {
          + blocked_encryption_types = (known after apply)
          + bucket_key_enabled       = (known after apply)

          + apply_server_side_encryption_by_default {
              + kms_master_key_id = (known after apply)
              + sse_algorithm     = "AES256"
            }
        }
    }

  # aws_s3_bucket_versioning.artifacts will be created
  + resource "aws_s3_bucket_versioning" "artifacts" {
      + bucket = (known after apply)
      + id     = (known after apply)
      + region = "ap-south-1"

      + versioning_configuration {
          + mfa_delete = (known after apply)
          + status     = "Enabled"
        }
    }

  # aws_security_group.web will be created
  + resource "aws_security_group" "web" {
      + arn                    = (known after apply)
      + description            = "Allow HTTP and HTTPS for Session 19"
      + egress                 = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = "Allow outbound IPv4"
              + from_port        = 0
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "-1"
              + security_groups  = []
              + self             = false
              + to_port          = 0
            },
        ]
      + id                     = (known after apply)
      + ingress                = [
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = "HTTP"
              + from_port        = 80
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 80
            },
          + {
              + cidr_blocks      = [
                  + "0.0.0.0/0",
                ]
              + description      = "HTTPS"
              + from_port        = 443
              + ipv6_cidr_blocks = []
              + prefix_list_ids  = []
              + protocol         = "tcp"
              + security_groups  = []
              + self             = false
              + to_port          = 443
            },
        ]
      + name                   = "session19-mini-web-sg"
      + name_prefix            = (known after apply)
      + owner_id               = (known after apply)
      + region                 = "ap-south-1"
      + revoke_rules_on_delete = false
      + tags                   = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-web-sg"
          + "Session"   = "19"
        }
      + tags_all               = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-web-sg"
          + "Session"   = "19"
        }
      + vpc_id                 = (known after apply)
    }

  # aws_subnet.public will be created
  + resource "aws_subnet" "public" {
      + arn                                            = (known after apply)
      + assign_ipv6_address_on_creation                = false
      + availability_zone                              = "ap-south-1a"
      + availability_zone_id                           = (known after apply)
      + cidr_block                                     = "10.20.1.0/24"
      + enable_dns64                                   = false
      + enable_resource_name_dns_a_record_on_launch    = false
      + enable_resource_name_dns_aaaa_record_on_launch = false
      + id                                             = (known after apply)
      + ipv6_cidr_block                                = (known after apply)
      + ipv6_cidr_block_association_id                 = (known after apply)
      + ipv6_native                                    = false
      + map_public_ip_on_launch                        = true
      + owner_id                                       = (known after apply)
      + private_dns_hostname_type_on_launch            = (known after apply)
      + region                                         = "ap-south-1"
      + tags                                           = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-public-subnet"
          + "Session"   = "19"
        }
      + tags_all                                       = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-public-subnet"
          + "Session"   = "19"
        }
      + vpc_id                                         = (known after apply)
    }

  # aws_vpc.main will be created
  + resource "aws_vpc" "main" {
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
      + region                               = "ap-south-1"
      + tags                                 = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-vpc"
          + "Session"   = "19"
        }
      + tags_all                             = {
          + "ManagedBy" = "Terraform"
          + "Name"      = "session19-mini-vpc"
          + "Session"   = "19"
        }
    }

Plan: 11 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + artifact_bucket   = (known after apply)
  + instance_id       = (known after apply)
  + security_group_id = (known after apply)
  + subnet_id         = (known after apply)
  + vpc_cidr          = "10.20.0.0/16"
  + vpc_id            = (known after apply)
  + web_url           = (known after apply)

─────────────────────────────────────────────────────────────────────────────

Saved the plan to: /tmp/campusfix-session19.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "/tmp/campusfix-session19.tfplan"
 
$ /tmp/campusfix-tools.FCoLVB/terraform apply -no-color -auto-approve /tmp/campusfix-session19.tfplan
aws_vpc.main: Creating...
aws_s3_bucket.artifacts: Creating...
aws_vpc.main: Creation complete after 2s [id=vpc-0cdb1457b728a6edc]
aws_internet_gateway.main: Creating...
aws_subnet.public: Creating...
aws_security_group.web: Creating...
aws_internet_gateway.main: Creation complete after 1s [id=igw-0a6a8ae0298651b24]
aws_route_table.public: Creating...
aws_route_table.public: Creation complete after 1s [id=rtb-001b44ddfd8d0f27d]
aws_security_group.web: Creation complete after 3s [id=sg-0f135e74b803e1f28]
aws_subnet.public: Still creating... [00m10s elapsed]
aws_subnet.public: Creation complete after 11s [id=subnet-0e18b80de695af470]
aws_route_table_association.public: Creating...
aws_instance.web: Creating...
aws_route_table_association.public: Creation complete after 1s [id=rtbassoc-0e6183b1f82980703]
aws_instance.web: Still creating... [00m10s elapsed]
aws_instance.web: Creation complete after 13s [id=i-0a2f302d38bc2b6fc]
 
Error: creating S3 Bucket (session19-[AWS_ACCOUNT_ID]-sudhir24bcs10425-20261013): operation error S3: CreateBucket, https response error StatusCode: 0, RequestID: , HostID: , request send failed, Put "https://session19-[AWS_ACCOUNT_ID]-sudhir24bcs10425-20261013.s3.ap-south-1.amazonaws.com/": dial tcp: lookup session19-[AWS_ACCOUNT_ID]-sudhir24bcs10425-20261013.s3.ap-south-1.amazonaws.com: no such host

  with aws_s3_bucket.artifacts,
  on main.tf line 142, in resource "aws_s3_bucket" "artifacts":
 142: resource "aws_s3_bucket" "artifacts" {


$ /tmp/campusfix-tools.FCoLVB/terraform destroy -no-color -auto-approve -var=project_suffix=sudhir24bcs10425-20261013
data.aws_caller_identity.current: Reading...
data.aws_ami.amazon_linux: Reading...
aws_vpc.main: Refreshing state... [id=vpc-0cdb1457b728a6edc]
data.aws_caller_identity.current: Read complete after 0s [id=[AWS_ACCOUNT_ID]]
data.aws_ami.amazon_linux: Read complete after 0s [id=ami-0324b92f52e4d7a4a]
aws_internet_gateway.main: Refreshing state... [id=igw-0a6a8ae0298651b24]
aws_subnet.public: Refreshing state... [id=subnet-0e18b80de695af470]
aws_security_group.web: Refreshing state... [id=sg-0f135e74b803e1f28]
aws_route_table.public: Refreshing state... [id=rtb-001b44ddfd8d0f27d]
aws_instance.web: Refreshing state... [id=i-0a2f302d38bc2b6fc]
aws_route_table_association.public: Refreshing state... [id=rtbassoc-0e6183b1f82980703]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_instance.web will be destroyed
  - resource "aws_instance" "web" {
      - ami                                  = "ami-0324b92f52e4d7a4a" -> null
      - arn                                  = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:instance/i-0a2f302d38bc2b6fc" -> null
      - associate_public_ip_address          = true -> null
      - availability_zone                    = "ap-south-1a" -> null
      - disable_api_stop                     = false -> null
      - disable_api_termination              = false -> null
      - ebs_optimized                        = false -> null
      - force_destroy                        = false -> null
      - get_password_data                    = false -> null
      - hibernation                          = false -> null
      - id                                   = "i-0a2f302d38bc2b6fc" -> null
      - instance_initiated_shutdown_behavior = "stop" -> null
      - instance_state                       = "running" -> null
      - instance_type                        = "t3.micro" -> null
      - ipv6_address_count                   = 0 -> null
      - ipv6_addresses                       = [] -> null
      - monitoring                           = false -> null
      - placement_partition_number           = 0 -> null
      - primary_network_interface_id         = "eni-065628742eea88158" -> null
      - private_dns                          = "ip-10-20-1-183.ap-south-1.compute.internal" -> null
      - private_ip                           = "10.20.1.183" -> null
      - public_dns                           = "ec2-13-234-231-160.ap-south-1.compute.amazonaws.com" -> null
      - public_ip                            = "13.234.231.160" -> null
      - region                               = "ap-south-1" -> null
      - secondary_private_ips                = [] -> null
      - security_groups                      = [] -> null
      - source_dest_check                    = true -> null
      - subnet_id                            = "subnet-0e18b80de695af470" -> null
      - tags                                 = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-web"
          - "Session"   = "19"
        } -> null
      - tags_all                             = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-web"
          - "Session"   = "19"
        } -> null
      - tenancy                              = "default" -> null
      - user_data                            = <<-EOT
            #!/bin/bash
            set -eux
            dnf install -y nginx
            echo '<h1>Sudhir Mehra: Terraform Cloud Lab</h1><p>24 BCS 10425 | Batch B</p>' > /usr/share/nginx/html/index.html
            systemctl enable --now nginx
        EOT -> null
      - user_data_replace_on_change          = false -> null
      - vpc_security_group_ids               = [
          - "sg-0f135e74b803e1f28",
        ] -> null
        # (9 unchanged attributes hidden)

      - capacity_reservation_specification {
          - capacity_reservation_preference = "open" -> null
        }

      - cpu_options {
          - core_count            = 1 -> null
          - threads_per_core      = 2 -> null
            # (2 unchanged attributes hidden)
        }

      - credit_specification {
          - cpu_credits = "unlimited" -> null
        }

      - enclave_options {
          - enabled = false -> null
        }

      - maintenance_options {
          - auto_recovery = "default" -> null
        }

      - metadata_options {
          - http_endpoint               = "enabled" -> null
          - http_protocol_ipv6          = "disabled" -> null
          - http_put_response_hop_limit = 2 -> null
          - http_tokens                 = "required" -> null
          - instance_metadata_tags      = "disabled" -> null
        }

      - primary_network_interface {
          - delete_on_termination = true -> null
          - network_interface_id  = "eni-065628742eea88158" -> null
        }

      - private_dns_name_options {
          - enable_resource_name_dns_a_record    = false -> null
          - enable_resource_name_dns_aaaa_record = false -> null
          - hostname_type                        = "ip-name" -> null
        }

      - root_block_device {
          - delete_on_termination = true -> null
          - device_name           = "/dev/xvda" -> null
          - encrypted             = true -> null
          - iops                  = 3000 -> null
          - kms_key_id            = "arn:aws:kms:ap-south-1:[AWS_ACCOUNT_ID]:key/49853920-ab0b-48b7-a3fc-cb08c3e2e07c" -> null
          - tags                  = {} -> null
          - tags_all              = {} -> null
          - throughput            = 125 -> null
          - volume_id             = "vol-0d6d185959ac14196" -> null
          - volume_size           = 8 -> null
          - volume_type           = "gp3" -> null
        }
    }

  # aws_internet_gateway.main will be destroyed
  - resource "aws_internet_gateway" "main" {
      - arn      = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:internet-gateway/igw-0a6a8ae0298651b24" -> null
      - id       = "igw-0a6a8ae0298651b24" -> null
      - owner_id = "[AWS_ACCOUNT_ID]" -> null
      - region   = "ap-south-1" -> null
      - tags     = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-igw"
          - "Session"   = "19"
        } -> null
      - tags_all = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-igw"
          - "Session"   = "19"
        } -> null
      - vpc_id   = "vpc-0cdb1457b728a6edc" -> null
    }

  # aws_route_table.public will be destroyed
  - resource "aws_route_table" "public" {
      - arn              = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:route-table/rtb-001b44ddfd8d0f27d" -> null
      - id               = "rtb-001b44ddfd8d0f27d" -> null
      - owner_id         = "[AWS_ACCOUNT_ID]" -> null
      - propagating_vgws = [] -> null
      - region           = "ap-south-1" -> null
      - route            = [
          - {
              - cidr_block                 = "0.0.0.0/0"
              - gateway_id                 = "igw-0a6a8ae0298651b24"
                # (12 unchanged attributes hidden)
            },
        ] -> null
      - tags             = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-public-rt"
          - "Session"   = "19"
        } -> null
      - tags_all         = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-public-rt"
          - "Session"   = "19"
        } -> null
      - vpc_id           = "vpc-0cdb1457b728a6edc" -> null
    }

  # aws_route_table_association.public will be destroyed
  - resource "aws_route_table_association" "public" {
      - id             = "rtbassoc-0e6183b1f82980703" -> null
      - region         = "ap-south-1" -> null
      - route_table_id = "rtb-001b44ddfd8d0f27d" -> null
      - subnet_id      = "subnet-0e18b80de695af470" -> null
        # (1 unchanged attribute hidden)
    }

  # aws_security_group.web will be destroyed
  - resource "aws_security_group" "web" {
      - arn                    = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:security-group/sg-0f135e74b803e1f28" -> null
      - description            = "Allow HTTP and HTTPS for Session 19" -> null
      - egress                 = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = "Allow outbound IPv4"
              - from_port        = 0
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "-1"
              - security_groups  = []
              - self             = false
              - to_port          = 0
            },
        ] -> null
      - id                     = "sg-0f135e74b803e1f28" -> null
      - ingress                = [
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = "HTTP"
              - from_port        = 80
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 80
            },
          - {
              - cidr_blocks      = [
                  - "0.0.0.0/0",
                ]
              - description      = "HTTPS"
              - from_port        = 443
              - ipv6_cidr_blocks = []
              - prefix_list_ids  = []
              - protocol         = "tcp"
              - security_groups  = []
              - self             = false
              - to_port          = 443
            },
        ] -> null
      - name                   = "session19-mini-web-sg" -> null
      - owner_id               = "[AWS_ACCOUNT_ID]" -> null
      - region                 = "ap-south-1" -> null
      - revoke_rules_on_delete = false -> null
      - tags                   = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-web-sg"
          - "Session"   = "19"
        } -> null
      - tags_all               = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-web-sg"
          - "Session"   = "19"
        } -> null
      - vpc_id                 = "vpc-0cdb1457b728a6edc" -> null
        # (1 unchanged attribute hidden)
    }

  # aws_subnet.public will be destroyed
  - resource "aws_subnet" "public" {
      - arn                                            = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:subnet/subnet-0e18b80de695af470" -> null
      - assign_ipv6_address_on_creation                = false -> null
      - availability_zone                              = "ap-south-1a" -> null
      - availability_zone_id                           = "aps1-az1" -> null
      - cidr_block                                     = "10.20.1.0/24" -> null
      - enable_dns64                                   = false -> null
      - enable_lni_at_device_index                     = 0 -> null
      - enable_resource_name_dns_a_record_on_launch    = false -> null
      - enable_resource_name_dns_aaaa_record_on_launch = false -> null
      - id                                             = "subnet-0e18b80de695af470" -> null
      - ipv6_native                                    = false -> null
      - map_customer_owned_ip_on_launch                = false -> null
      - map_public_ip_on_launch                        = true -> null
      - owner_id                                       = "[AWS_ACCOUNT_ID]" -> null
      - private_dns_hostname_type_on_launch            = "ip-name" -> null
      - region                                         = "ap-south-1" -> null
      - tags                                           = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-public-subnet"
          - "Session"   = "19"
        } -> null
      - tags_all                                       = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-public-subnet"
          - "Session"   = "19"
        } -> null
      - vpc_id                                         = "vpc-0cdb1457b728a6edc" -> null
        # (4 unchanged attributes hidden)
    }

  # aws_vpc.main will be destroyed
  - resource "aws_vpc" "main" {
      - arn                                  = "arn:aws:ec2:ap-south-1:[AWS_ACCOUNT_ID]:vpc/vpc-0cdb1457b728a6edc" -> null
      - assign_generated_ipv6_cidr_block     = false -> null
      - cidr_block                           = "10.20.0.0/16" -> null
      - default_network_acl_id               = "acl-0ddd1a17f21b4440d" -> null
      - default_route_table_id               = "rtb-028496100e6e39b41" -> null
      - default_security_group_id            = "sg-007beb0230af67f74" -> null
      - dhcp_options_id                      = "dopt-04099746251bf6721" -> null
      - enable_dns_hostnames                 = true -> null
      - enable_dns_support                   = true -> null
      - enable_network_address_usage_metrics = false -> null
      - id                                   = "vpc-0cdb1457b728a6edc" -> null
      - instance_tenancy                     = "default" -> null
      - ipv6_netmask_length                  = 0 -> null
      - main_route_table_id                  = "rtb-028496100e6e39b41" -> null
      - owner_id                             = "[AWS_ACCOUNT_ID]" -> null
      - region                               = "ap-south-1" -> null
      - tags                                 = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-vpc"
          - "Session"   = "19"
        } -> null
      - tags_all                             = {
          - "ManagedBy" = "Terraform"
          - "Name"      = "session19-mini-vpc"
          - "Session"   = "19"
        } -> null
        # (4 unchanged attributes hidden)
    }

Plan: 0 to add, 0 to change, 7 to destroy.

Changes to Outputs:
  - instance_id       = "i-0a2f302d38bc2b6fc" -> null
  - security_group_id = "sg-0f135e74b803e1f28" -> null
  - subnet_id         = "subnet-0e18b80de695af470" -> null
  - vpc_cidr          = "10.20.0.0/16" -> null
  - vpc_id            = "vpc-0cdb1457b728a6edc" -> null
  - web_url           = "http://13.234.231.160" -> null
aws_route_table_association.public: Destroying... [id=rtbassoc-0e6183b1f82980703]
aws_instance.web: Destroying... [id=i-0a2f302d38bc2b6fc]
aws_route_table_association.public: Destruction complete after 1s
aws_route_table.public: Destroying... [id=rtb-001b44ddfd8d0f27d]
aws_route_table.public: Destruction complete after 0s
aws_internet_gateway.main: Destroying... [id=igw-0a6a8ae0298651b24]
aws_instance.web: Still destroying... [id=i-0a2f302d38bc2b6fc, 00m10s elapsed]
aws_internet_gateway.main: Still destroying... [id=igw-0a6a8ae0298651b24, 00m10s elapsed]
aws_instance.web: Still destroying... [id=i-0a2f302d38bc2b6fc, 00m20s elapsed]
aws_internet_gateway.main: Destruction complete after 20s
aws_instance.web: Still destroying... [id=i-0a2f302d38bc2b6fc, 00m30s elapsed]
aws_instance.web: Destruction complete after 30s
aws_subnet.public: Destroying... [id=subnet-0e18b80de695af470]
aws_security_group.web: Destroying... [id=sg-0f135e74b803e1f28]
aws_subnet.public: Destruction complete after 0s
aws_security_group.web: Destruction complete after 1s
aws_vpc.main: Destroying... [id=vpc-0cdb1457b728a6edc]
aws_vpc.main: Destruction complete after 0s

Destroy complete! Resources: 7 destroyed.
 
$ /tmp/campusfix-tools.FCoLVB/terraform state list
 
PASS: lab resources destroyed and state resource list is empty.
Traceback (most recent call last):
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 34, in <module>
    run("apply", "-no-color", "-auto-approve", "/tmp/campusfix-session" + args.topic + ".tfplan")
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 25, in run
    result.check_returncode()
    ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 509, in check_returncode
    raise CalledProcessError(self.returncode, self.args, self.stdout,
                             self.stderr)
subprocess.CalledProcessError: Command '['/tmp/campusfix-tools.FCoLVB/terraform', 'apply', '-no-color', '-auto-approve', '/tmp/campusfix-session19.tfplan']' returned non-zero exit status 1.

```

Exit code: 1
