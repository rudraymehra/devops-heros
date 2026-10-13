output "cluster_name" {
  description = "EKS cluster name."
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "EKS Kubernetes API endpoint."
  value       = module.eks.cluster_endpoint
}

output "vpc_id" {
  description = "VPC created for the EKS cluster."
  value       = module.vpc.vpc_id
}

output "configure_kubectl" {
  description = "Command used to configure kubectl after apply."
  value       = "aws eks update-kubeconfig --region ${var.aws_region} --name ${module.eks.cluster_name}"
}
