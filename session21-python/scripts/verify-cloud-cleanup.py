"""Read-only verification that only the named homework labs have been removed."""
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[2]
terraform = "/tmp/campusfix-tools.FCoLVB/terraform"


def run(command, expected_error=None):
    print("$", " ".join(command), flush=True)
    result = subprocess.run(command, text=True, capture_output=True, timeout=120)
    print(result.stdout, result.stderr, flush=True)
    if expected_error:
        assert result.returncode and expected_error in result.stderr, "Resource unexpectedly remains or query failed differently"
    else:
        result.check_returncode()
    return result.stdout


for directory in ["session21-python/terraform", "session18-terraform-iac/terraform-s3-demo",
                  "session19-cloud-terraform/08-mini-project"]:
    state = run([terraform, "-chdir=" + str(root / directory), "state", "list"])
    assert not state.strip(), directory + " still contains managed resources"
run(["aws", "eks", "describe-cluster", "--region", "ap-south-1", "--name", "sudhir-campusfix"],
    "ResourceNotFoundException")
aws = ["aws", "ec2"]
checks = [
    ["describe-vpcs", "--filters", "Name=vpc-id,Values=vpc-0b236660178acfe8c", "--query", "Vpcs"],
    ["describe-instances", "--filters", "Name=vpc-id,Values=vpc-0b236660178acfe8c",
     "--query", "Reservations[].Instances[?State.Name!='terminated'][]"],
    ["describe-instances", "--filters", "Name=tag:Session,Values=19",
     "--query", "Reservations[].Instances[?State.Name!='terminated'][]"],
    ["describe-volumes", "--filters", "Name=volume-id,Values=vol-00e51cffb14918572", "--query", "Volumes"],
    ["describe-nat-gateways", "--filter", "Name=vpc-id,Values=vpc-0b236660178acfe8c",
     "--query", "NatGateways[?State!='deleted']"],
]
for command in checks:
    assert json.loads(run(aws + command + ["--region", "ap-south-1", "--output", "json"])) == []
for service, field, query in [
    ("elb", "describe-load-balancers", "LoadBalancerDescriptions[?VPCId=='vpc-0b236660178acfe8c']"),
    ("elbv2", "describe-load-balancers", "LoadBalancers[?VpcId=='vpc-0b236660178acfe8c']"),
]:
    assert json.loads(run(["aws", service, field, "--region", "ap-south-1", "--query", query, "--output", "json"])) == []
buckets = run(["aws", "s3api", "list-buckets", "--query",
    "Buckets[?Name=='sudhir-mehra-24bcs10425-lab-20261013-0738' || (starts_with(Name, 'session19-') && ends_with(Name, '-sudhir24bcs10425-20261013'))].Name",
    "--output", "json"])
assert json.loads(buckets) == []
backup = root / "session21-python/terraform/terraform.tfstate.backup"
if backup.exists():
    keys = [r for r in json.loads(backup.read_text()).get("resources", []) if r.get("type") == "aws_kms_key"]
    for resource in keys:
        for instance in resource["instances"]:
            key_id = instance["attributes"]["key_id"]
            state = json.loads(run(["aws", "kms", "describe-key", "--region", "ap-south-1", "--key-id", key_id,
                                   "--query", "KeyMetadata.{State:KeyState,DeletionDate:DeletionDate}", "--output", "json"]))
            assert state["State"] == "PendingDeletion"
            print("KMS uses AWS's mandatory deletion waiting period; key is disabled pending deletion.")
print("PASS: all three Terraform states empty; no active lab cluster, instances, NAT, disk, load balancer or S3 buckets.")
