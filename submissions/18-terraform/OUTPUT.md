# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:40:25.189588+00:00

Working directory: .

```text
$ python3 session21-python/scripts/small-cloud-lab.py 18 --terraform /tmp/campusfix-tools.FCoLVB/terraform
$ /tmp/campusfix-tools.FCoLVB/terraform init -no-color
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/aws from the dependency lock file
- Installing hashicorp/aws v6.66.0...
- Installed hashicorp/aws v6.66.0 (signed by HashiCorp)

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

 
$ /tmp/campusfix-tools.FCoLVB/terraform plan -no-color -out=/tmp/campusfix-session18.tfplan -var=bucket_name=sudhir-mehra-24bcs10425-lab-20261013-0738

Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_s3_bucket.devops553 will be created
  + resource "aws_s3_bucket" "devops553" {
      + acceleration_status         = (known after apply)
      + acl                         = (known after apply)
      + arn                         = (known after apply)
      + bucket                      = "sudhir-mehra-24bcs10425-lab-20261013-0738"
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
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
          + "Project"     = "Session18"
        }
      + tags_all                    = {
          + "Environment" = "dev"
          + "ManagedBy"   = "Terraform"
          + "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
          + "Project"     = "Session18"
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

  # aws_s3_bucket_public_access_block.devops553 will be created
  + resource "aws_s3_bucket_public_access_block" "devops553" {
      + block_public_acls       = true
      + block_public_policy     = true
      + bucket                  = (known after apply)
      + id                      = (known after apply)
      + ignore_public_acls      = true
      + region                  = "ap-south-1"
      + restrict_public_buckets = true
    }

  # aws_s3_bucket_server_side_encryption_configuration.devops553 will be created
  + resource "aws_s3_bucket_server_side_encryption_configuration" "devops553" {
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

  # aws_s3_bucket_versioning.devops553 will be created
  + resource "aws_s3_bucket_versioning" "devops553" {
      + bucket = (known after apply)
      + id     = (known after apply)
      + region = "ap-south-1"

      + versioning_configuration {
          + mfa_delete = (known after apply)
          + status     = "Enabled"
        }
    }

Plan: 4 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + bucket_arn    = (known after apply)
  + bucket_name   = "sudhir-mehra-24bcs10425-lab-20261013-0738"
  + bucket_region = "ap-south-1"

─────────────────────────────────────────────────────────────────────────────

Saved the plan to: /tmp/campusfix-session18.tfplan

To perform exactly these actions, run the following command to apply:
    terraform apply "/tmp/campusfix-session18.tfplan"
 
$ /tmp/campusfix-tools.FCoLVB/terraform apply -no-color -auto-approve /tmp/campusfix-session18.tfplan
aws_s3_bucket.devops553: Creating...
aws_s3_bucket.devops553: Still creating... [00m10s elapsed]
aws_s3_bucket.devops553: Creation complete after 10s [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_versioning.devops553: Creating...
aws_s3_bucket_public_access_block.devops553: Creating...
aws_s3_bucket_server_side_encryption_configuration.devops553: Creating...
aws_s3_bucket_public_access_block.devops553: Creation complete after 0s [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_server_side_encryption_configuration.devops553: Creation complete after 0s [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_versioning.devops553: Creation complete after 2s [id=sudhir-mehra-24bcs10425-lab-20261013-0738]

Apply complete! Resources: 4 added, 0 changed, 0 destroyed.

Outputs:

bucket_arn = "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738"
bucket_name = "sudhir-mehra-24bcs10425-lab-20261013-0738"
bucket_region = "ap-south-1"
 
$ /tmp/campusfix-tools.FCoLVB/terraform show -no-color
# aws_s3_bucket.devops553:
resource "aws_s3_bucket" "devops553" {
    acceleration_status         = null
    arn                         = "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738"
    bucket                      = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    bucket_domain_name          = "sudhir-mehra-24bcs10425-lab-20261013-0738.s3.amazonaws.com"
    bucket_namespace            = "global"
    bucket_prefix               = null
    bucket_region               = "ap-south-1"
    bucket_regional_domain_name = "sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com"
    force_destroy               = false
    hosted_zone_id              = "Z11RGJOFQNVJUP"
    id                          = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    object_lock_enabled         = false
    policy                      = null
    region                      = "ap-south-1"
    request_payer               = "BucketOwner"
    tags                        = {
        "Environment" = "dev"
        "ManagedBy"   = "Terraform"
        "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
        "Project"     = "Session18"
    }
    tags_all                    = {
        "Environment" = "dev"
        "ManagedBy"   = "Terraform"
        "Name"        = "sudhir-mehra-24bcs10425-lab-20261013-0738"
        "Project"     = "Session18"
    }

    grant {
        id          = "51d9942c138bedd4ad540722650899405083b3914d09df588a131d0193bf14d2"
        permissions = [
            "FULL_CONTROL",
        ]
        type        = "CanonicalUser"
        uri         = null
    }

    server_side_encryption_configuration {
        rule {
            bucket_key_enabled = false

            apply_server_side_encryption_by_default {
                kms_master_key_id = null
                sse_algorithm     = "AES256"
            }
        }
    }

    versioning {
        enabled    = false
        mfa_delete = false
    }
}

# aws_s3_bucket_public_access_block.devops553:
resource "aws_s3_bucket_public_access_block" "devops553" {
    block_public_acls       = true
    block_public_policy     = true
    bucket                  = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    id                      = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    ignore_public_acls      = true
    region                  = "ap-south-1"
    restrict_public_buckets = true
}

# aws_s3_bucket_server_side_encryption_configuration.devops553:
resource "aws_s3_bucket_server_side_encryption_configuration" "devops553" {
    bucket                = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    expected_bucket_owner = null
    id                    = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    region                = "ap-south-1"

    rule {
        blocked_encryption_types = [
            "SSE-C",
        ]
        bucket_key_enabled       = false

        apply_server_side_encryption_by_default {
            kms_master_key_id = null
            sse_algorithm     = "AES256"
        }
    }
}

# aws_s3_bucket_versioning.devops553:
resource "aws_s3_bucket_versioning" "devops553" {
    bucket                = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    expected_bucket_owner = null
    id                    = "sudhir-mehra-24bcs10425-lab-20261013-0738"
    region                = "ap-south-1"

    versioning_configuration {
        mfa_delete = "Disabled"
        status     = "Enabled"
    }
}


Outputs:

bucket_arn = "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738"
bucket_name = "sudhir-mehra-24bcs10425-lab-20261013-0738"
bucket_region = "ap-south-1"
 
$ /tmp/campusfix-tools.FCoLVB/terraform output -json
{
  "bucket_arn": {
    "sensitive": false,
    "type": "string",
    "value": "arn:aws:s3:::sudhir-mehra-24bcs10425-lab-20261013-0738"
  },
  "bucket_name": {
    "sensitive": false,
    "type": "string",
    "value": "sudhir-mehra-24bcs10425-lab-20261013-0738"
  },
  "bucket_region": {
    "sensitive": false,
    "type": "string",
    "value": "ap-south-1"
  }
}
 
PASS: private, encrypted, versioned S3 bucket created: sudhir-mehra-24bcs10425-lab-20261013-0738
$ /tmp/campusfix-tools.FCoLVB/terraform destroy -no-color -auto-approve -var=bucket_name=sudhir-mehra-24bcs10425-lab-20261013-0738
aws_s3_bucket.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_versioning.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_public_access_block.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
aws_s3_bucket_server_side_encryption_configuration.devops553: Refreshing state... [id=sudhir-mehra-24bcs10425-lab-20261013-0738]
 
Error: reading S3 Bucket Public Access Block (sudhir-mehra-24bcs10425-lab-20261013-0738): operation error S3: GetPublicAccessBlock, https response error StatusCode: 0, RequestID: , HostID: , request send failed, Get "https://sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com/?publicAccessBlock=": dial tcp: lookup sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com: no such host

  with aws_s3_bucket_public_access_block.devops553,
  on main.tf line 12, in resource "aws_s3_bucket_public_access_block" "devops553":
  12: resource "aws_s3_bucket_public_access_block" "devops553" {


Error: reading S3 Bucket Server-side Encryption Configuration (sudhir-mehra-24bcs10425-lab-20261013-0738): operation error S3: GetBucketEncryption, https response error StatusCode: 0, RequestID: , HostID: , request send failed, Get "https://sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com/?encryption=": dial tcp: lookup sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com: no such host

  with aws_s3_bucket_server_side_encryption_configuration.devops553,
  on main.tf line 21, in resource "aws_s3_bucket_server_side_encryption_configuration" "devops553":
  21: resource "aws_s3_bucket_server_side_encryption_configuration" "devops553" {


Error: reading S3 Bucket Versioning (sudhir-mehra-24bcs10425-lab-20261013-0738): operation error S3: GetBucketVersioning, https response error StatusCode: 0, RequestID: , HostID: , request send failed, Get "https://sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com/?versioning=": dial tcp: lookup sudhir-mehra-24bcs10425-lab-20261013-0738.s3.ap-south-1.amazonaws.com: no such host

  with aws_s3_bucket_versioning.devops553,
  on main.tf line 31, in resource "aws_s3_bucket_versioning" "devops553":
  31: resource "aws_s3_bucket_versioning" "devops553" {


Traceback (most recent call last):
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 54, in <module>
    run("destroy", "-no-color", "-auto-approve", *variables)
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/rudraym/devops-heros/session21-python/scripts/small-cloud-lab.py", line 25, in run
    result.check_returncode()
    ~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/homebrew/Cellar/python@3.14/3.14.7/Frameworks/Python.framework/Versions/3.14/lib/python3.14/subprocess.py", line 509, in check_returncode
    raise CalledProcessError(self.returncode, self.args, self.stdout,
                             self.stderr)
subprocess.CalledProcessError: Command '['/tmp/campusfix-tools.FCoLVB/terraform', 'destroy', '-no-color', '-auto-approve', '-var=bucket_name=sudhir-mehra-24bcs10425-lab-20261013-0738']' returned non-zero exit status 1.

```

Exit code: 1
