variable "aws_region" {
  description = "AWS region for the Session 19 mini project."
  type        = string
  default     = "ap-south-1"
}

variable "instance_type" {
  description = "Small EC2 instance type used by the web demonstration."
  type        = string
  default     = "t3.micro"
}

variable "project_suffix" {
  description = "Lowercase suffix used in the globally unique S3 bucket name."
  type        = string
  default     = "devops-homework"

  validation {
    condition     = can(regex("^[a-z0-9][a-z0-9-]{1,30}[a-z0-9]$", var.project_suffix))
    error_message = "project_suffix must contain 3-32 lowercase letters, digits, or hyphens."
  }
}
