#!/usr/bin/env bash
# Only the explicitly named, user-approved CampusFix lab is targeted.
set -euo pipefail
export KUBECONFIG=/tmp/campusfix-eks.kubeconfig
kubectl --context campusfix-eks get svc -A --field-selector spec.type=LoadBalancer
kubectl --context campusfix-eks get pvc -A
kubectl --context campusfix-eks delete application campusfix -n argocd --wait=true
helm --kube-context campusfix-eks uninstall taskboard -n taskboard --wait --timeout 3m
kubectl --context campusfix-eks delete namespace taskboard --wait=true --timeout=180s
kubectl --context campusfix-eks wait --for=delete pv/pvc-2c1c6543-f3b2-45d2-91d4-eb3e1ee0a8ce --timeout=180s
aws ec2 wait volume-deleted --region ap-south-1 --volume-ids vol-00e51cffb14918572
kubectl --context campusfix-eks get pv
kubectl --context campusfix-eks get svc -A --field-selector spec.type=LoadBalancer
aws elb describe-load-balancers --region ap-south-1 --query "LoadBalancerDescriptions[?VPCId=='vpc-0b236660178acfe8c'].LoadBalancerName"
aws elbv2 describe-load-balancers --region ap-south-1 --query "LoadBalancers[?VpcId=='vpc-0b236660178acfe8c'].LoadBalancerArn"
echo "Kubernetes-created disk and load balancer removed. Terraform teardown can proceed."
