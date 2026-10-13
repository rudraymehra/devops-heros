resource "aws_s3_bucket" "devops553" {
  bucket        = var.bucket_name
  force_destroy = false
  tags = {
    Name        = var.bucket_name
    Environment = "dev"
    ManagedBy   = "Terraform"
    Project     = "Session18"
  }
}

resource "aws_s3_bucket_public_access_block" "devops553" {
  bucket = aws_s3_bucket.devops553.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "devops553" {
  bucket = aws_s3_bucket.devops553.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_versioning" "devops553" {
  bucket = aws_s3_bucket.devops553.id

  versioning_configuration {
    status = "Enabled"
  }
}
