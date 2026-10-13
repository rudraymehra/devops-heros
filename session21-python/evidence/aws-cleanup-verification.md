# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T08:06:50.887050+00:00

Working directory: .

```text
$ python3 session21-python/scripts/verify-cloud-cleanup.py
$ /tmp/campusfix-tools.FCoLVB/terraform -chdir=/Users/rudraym/devops-heros/session21-python/terraform state list
 
$ /tmp/campusfix-tools.FCoLVB/terraform -chdir=/Users/rudraym/devops-heros/session18-terraform-iac/terraform-s3-demo state list
 
$ /tmp/campusfix-tools.FCoLVB/terraform -chdir=/Users/rudraym/devops-heros/session19-cloud-terraform/08-mini-project state list
 
$ aws eks describe-cluster --region ap-south-1 --name sudhir-campusfix
 
An error occurred (ResourceNotFoundException) when calling the DescribeCluster operation: No cluster found for name: sudhir-campusfix.

$ aws ec2 describe-vpcs --filters Name=vpc-id,Values=vpc-0b236660178acfe8c --query Vpcs --region ap-south-1 --output json
[]
 
$ aws ec2 describe-instances --filters Name=vpc-id,Values=vpc-0b236660178acfe8c --query Reservations[].Instances[?State.Name!='terminated'][] --region ap-south-1 --output json
[]
 
$ aws ec2 describe-instances --filters Name=tag:Session,Values=19 --query Reservations[].Instances[?State.Name!='terminated'][] --region ap-south-1 --output json
[]
 
$ aws ec2 describe-volumes --filters Name=volume-id,Values=vol-00e51cffb14918572 --query Volumes --region ap-south-1 --output json
[]
 
$ aws ec2 describe-nat-gateways --filter Name=vpc-id,Values=vpc-0b236660178acfe8c --query NatGateways[?State!='deleted'] --region ap-south-1 --output json
[]
 
$ aws elb describe-load-balancers --region ap-south-1 --query LoadBalancerDescriptions[?VPCId=='vpc-0b236660178acfe8c'] --output json
[]
 
$ aws elbv2 describe-load-balancers --region ap-south-1 --query LoadBalancers[?VpcId=='vpc-0b236660178acfe8c'] --output json
[]
 
$ aws s3api list-buckets --query Buckets[?Name=='sudhir-mehra-24bcs10425-lab-20261013-0738' || (starts_with(Name, 'session19-') && ends_with(Name, '-sudhir24bcs10425-20261013'))].Name --output json
[]
 
$ aws kms describe-key --region ap-south-1 --key-id 37fe050d-bcf3-4652-bcd2-2ad9cd2e1e4c --query KeyMetadata.{State:KeyState,DeletionDate:DeletionDate} --output json
{
    "State": "PendingDeletion",
    "DeletionDate": "2026-11-12T13:21:45.684000+05:30"
}
 
KMS uses AWS's mandatory deletion waiting period; key is disabled pending deletion.
PASS: all three Terraform states empty; no active lab cluster, instances, NAT, disk, load balancer or S3 buckets.

```

Exit code: 0
