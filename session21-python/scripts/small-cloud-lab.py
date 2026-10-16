"""Run an approved Session 18/19 lab, record evidence, and always attempt teardown."""
import argparse
import json
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("topic", choices=["18", "19"])
parser.add_argument("--terraform", required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[2]
path = root / ("session18-terraform-iac/terraform-s3-demo" if args.topic == "18"
               else "session19-cloud-terraform/08-mini-project")
variables = ["-var=bucket_name=sudhir-mehra-24bcs10425-lab-20261013-0738"] if args.topic == "18" else ["-var=project_suffix=sudhir24bcs10425-20261013"]


def run(*arguments):
    command = [args.terraform, *arguments]
    print("$", " ".join(command), flush=True)
    result = subprocess.run(command, cwd=path, text=True, capture_output=True, timeout=900)
    print(result.stdout, result.stderr, flush=True)
    result.check_returncode()
    return result.stdout


run("init", "-no-color")
run("fmt", "-check")
run("validate", "-no-color")
run("plan", "-no-color", "-out=/tmp/campusfix-session" + args.topic + ".tfplan", *variables)
try:
    run("apply", "-no-color", "-auto-approve", "/tmp/campusfix-session" + args.topic + ".tfplan")
    run("show", "-no-color")
    output = json.loads(run("output", "-json"))
    if args.topic == "19":
        url = output["web_url"]["value"]
        deadline = time.monotonic() + 240
        while True:
            try:
                with urllib.request.urlopen(url, timeout=10) as response:
                    body = response.read().decode()
                assert "Rudray Mehra" in body and "24 BCS 10425" in body
                print("PASS: EC2 bootstrapped Nginx serves:", body, flush=True)
                break
            except (urllib.error.URLError, TimeoutError):
                if time.monotonic() > deadline:
                    raise
                time.sleep(5)
    else:
        print("PASS: private, encrypted, versioned S3 bucket created:", output["bucket_name"]["value"], flush=True)
finally:
    run("destroy", "-no-color", "-auto-approve", *variables)
    assert not run("state", "list").strip(), "Terraform still manages lab resources"
    print("PASS: lab resources destroyed and state resource list is empty.", flush=True)
