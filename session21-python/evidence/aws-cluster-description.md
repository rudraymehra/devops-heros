# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:38:35.383551+00:00

Working directory: .

```text
$ aws eks describe-cluster --region ap-south-1 --name sudhir-campusfix --query 'cluster.{Name:name,Status:status,Version:version,Created:createdAt,Vpc:resourcesVpcConfig.vpcId,Subnets:resourcesVpcConfig.subnetIds}' --output json
{
    "Name": "sudhir-campusfix",
    "Status": "ACTIVE",
    "Version": "1.35",
    "Created": "2026-10-13T07:51:49.867000+05:30",
    "Vpc": "vpc-0b236660178acfe8c",
    "Subnets": [
        "subnet-04516a733d2088208",
        "subnet-082b0fed2e03ccecf"
    ]
}

```

Exit code: 0
