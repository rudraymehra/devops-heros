# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:42:11.133753+00:00

Working directory: session18-terraform-iac/terraform-s3-demo

```text
$ /tmp/campusfix-tools.FCoLVB/terraform destroy -no-color -auto-approve -var=bucket_name=sudhir-mehra-24bcs10425-lab-20261013-0738
aws_s3_bucket.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_public_access_block.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_versioning.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_server_side_encryption_configuration.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  - destroy

Terraform will perform the following actions:

  # aws_s3_bucket.devops553 will be destroyed
  - resource "aws_s3_bucket" "devops553" {
      - arn                         = "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - bucket                      = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - bucket_domain_name          = "sudhir-mehra-24bcs10425-lab-20261013-0738.s3.amazonaws.com" -> null
      - bucket_namespace            = "global" -> null
      - bucket_region               = "ap-south-1" -> null
      - bucket_regional_domain_name = "sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com" -> null
      - force_destroy               = false -> null
      - hosted_zone_id              = "Z11RGJOFQNVJUP" -> null
      - id                          = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - object_lock_enabled         = false -> null
      - region                      = "ap-south-1" -> null
      - request_payer               = "BucketOwner" -> null
      - tags                        = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
          - "Project"     = "Session18"
        } -> null
      - tags_all                    = {
          - "Environment" = "dev"
          - "ManagedBy"   = "Terraform"
          - "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
          - "Project"     = "Session18"
        } -> null
        # (3 unchanged attributes hidden)

      - grant {
          - id          = "51d9942c138bedd4ad540722650899405083b3914d09df588a131d0193bf14d2" -> null
          - permissions = [
              - "FULL_CONTROL",
            ] -> null
          - type        = "CanonicalUser" -> null
            # (1 unchanged attribute hidden)
        }

      - server_side_encryption_configuration {
          - rule {
              - bucket_key_enabled = false -> null

              - apply_server_side_encryption_by_default {
                  - sse_algorithm     = "AES256" -> null
                    # (1 unchanged attribute hidden)
                }
            }
        }

      - versioning {
          - enabled    = true -> null
          - mfa_delete = false -> null
        }
    }

  # aws_s3_bucket_public_access_block.devops553 will be destroyed
  - resource "aws_s3_bucket_public_access_block" "devops553" {
      - block_public_acls       = true -> null
      - block_public_policy     = true -> null
      - bucket                  = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - id                      = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - ignore_public_acls      = true -> null
      - region                  = "ap-south-1" -> null
      - restrict_public_buckets = true -> null
    }

  # aws_s3_bucket_server_side_encryption_configuration.devops553 will be destroyed
  - resource "aws_s3_bucket_server_side_encryption_configuration" "devops553" {
      - bucket                = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - id                    = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - region                = "ap-south-1" -> null
        # (1 unchanged attribute hidden)

      - rule {
          - blocked_encryption_types = [
              - "SSE-C",
            ] -> null
          - bucket_key_enabled       = false -> null

          - apply_server_side_encryption_by_default {
              - sse_algorithm     = "AES256" -> null
                # (1 unchanged attribute hidden)
            }
        }
    }

  # aws_s3_bucket_versioning.devops553 will be destroyed
  - resource "aws_s3_bucket_versioning" "devops553" {
      - bucket                = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - id                    = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
      - region                = "ap-south-1" -> null
        # (1 unchanged attribute hidden)

      - versioning_configuration {
          - mfa_delete = "Disabled" -> null
          - status     = "Enabled" -> null
        }
    }

Plan: 0 to add, 0 to change, 4 to destroy.

Changes to Outputs:
  - bucket_arn    = "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
  - bucket_name   = "sudhir-mehra-24bcs10425-lab-20261013-0738" -> null
  - bucket_region = "ap-south-1" -> null
aws_s3_bucket_public_access_block.devops553: Destroying... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_versioning.devops553: Destroying... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_server_side_encryption_configuration.devops553: Destroying... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_public_access_block.devops553: Destruction complete after 1s
aws_s3_bucket_server_side_encryption_configuration.devops553: Destruction complete after 1s
aws_s3_bucket_versioning.devops553: Destruction complete after 1s
aws_s3_bucket.devops553: Destroying... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket.devops553: Destruction complete after 1s

Destroy complete! Resources: 4 destroyed.

```

Exit code: 0
