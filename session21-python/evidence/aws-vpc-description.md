# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:38:40.572627+00:00

Working directory: .

```text
$ aws ec2 describe-vpcs --region ap-south-1 --vpc-ids vpc-0b236660178acfe8c --query 'Vpcs[].{Id:VpcId,State:State,CIDR:CidrBlock,Tags:Tags}' --output json
[
    {
        "Id": "vpc-0b236660178acfe8c",
        "State": "available",
        "CIDR": "10.20.0.0/16",
        "Tags": [
            {
                "Key": "ManagedBy",
                "Value": "Terraform"
            },
            {
                "Key": "Name",
                "Value": "sudhir-campusfix-vpc"
            },
            {
                "Key": "Environment",
                "Value": "dev"
            }
        ]
    }
]

```

Exit code: 0
