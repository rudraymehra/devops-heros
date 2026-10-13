variable "aws_region" {
  description = "AWS region in which to create the VPC and EKS cluster."
  type        = string
  default     = "ap-south-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster."
  type        = string
  default     = "sudhir-campusfix"
}

variable "environment" {
  description = "Environment tag applied to managed resources."
  type        = string
  default     = "dev"
}

variable "kubernetes_version" {
  description = "EKS Kubernetes version supported in the selected region."
  type        = string
  default     = "1.35"
}

variable "node_instance_type" {
  description = "EC2 instance type for the managed worker group."
  type        = string
  default     = "t3.medium"
}
