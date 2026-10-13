"""Execute scoped strategy, troubleshooting and Helm labs on the selected context."""
import argparse
import json
import subprocess
import time
from pathlib import Path

import yaml

parser = argparse.ArgumentParser()
parser.add_argument("--context", required=True)
parser.add_argument("--topic", choices=["strategies", "troubleshooting", "helm"], required=True)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
namespace = "campusfix-" + args.topic
base = ["kubectl", "--context", args.context, "--request-timeout=30s"]
k = base + ["-n", namespace]


def run(command, data=None, check=True):
    print("$", " ".join(command), flush=True)
    result = subprocess.run(command, input=data, text=True, capture_output=True, cwd=root, timeout=240)
    print(result.stdout, result.stderr, "[exit:", result.returncode, "]", flush=True)
    if check and result.returncode:
        raise RuntimeError("Command failed")
    return result.stdout


def apply(path):
    run(k + ["apply", "-f", path])


def rollout(name):
    run(k + ["rollout", "status", "deployment/" + name, "--timeout=180s"])


def fetch(url):
    return run(k + ["exec", "client", "--", "wget", "-T", "10", "-qO-", url])


run(base + ["create", "namespace", namespace])
if args.topic == "strategies":
    run(k + ["run", "client", "--image=busybox:1.37", "--command", "--", "sleep", "3600"])
    run(k + ["wait", "--for=condition=Ready", "pod/client", "--timeout=180s"])
    prefix = "session10-k8s-core-objects/"
    for name in ["deployment-blue.yaml", "deployment-green.yaml", "service-blue.yaml"]:
        apply(prefix + "02-blue-green/" + name)
    rollout("app-blue")
    rollout("app-green")
    assert "BLUE ENVIRONMENT" in fetch("http://myapp-service")
    apply(prefix + "02-blue-green/service-green.yaml")
    time.sleep(3)
    assert "GREEN ENVIRONMENT" in fetch("http://myapp-service")
    run(k + ["get", "endpointslices", "-l", "kubernetes.io/service-name=myapp-service", "-o", "wide"])
    run(k + ["delete", "deployment", "app-blue", "app-green", "--wait=true"])
    for name in ["deployment-stable.yaml", "deployment-canary.yaml", "service.yaml"]:
        manifest = yaml.safe_load((root / (prefix + "03-canary/" + name)).read_text())
        if name == "deployment-stable.yaml":
            manifest["spec"]["replicas"] = 3
        run(k + ["apply", "-f", "-"], yaml.safe_dump(manifest))
    rollout("app-stable")
    rollout("app-canary")
    run(k + ["get", "pods", "-l", "app=myapp-canary", "-L", "track"])
    samples = run(k + ["exec", "client", "--", "sh", "-c",
                      "for i in $(seq 1 60); do wget -T 5 -qO- http://myapp-canary-service; done"])
    assert "STABLE" in samples and "CANARY" in samples
    print("Lab uses 3 stable + 1 canary to fit two t3.medium workers. Approximate 75/25 distribution, not an exact guarantee.")
    run(k + ["delete", "deployment", "app-stable", "app-canary", "--wait=true"])
    apply(prefix + "04-recreate/deployment-v1.yaml")
    apply(prefix + "04-recreate/service.yaml")
    rollout("app-recreate")
    run(k + ["get", "pods", "-l", "app=app-recreate", "-o", "wide"])
    apply(prefix + "04-recreate/deployment-v2.yaml")
    rollout("app-recreate")
    run(k + ["get", "pods", "-l", "app=app-recreate", "-L", "version"])
    run(k + ["get", "events", "--sort-by=.metadata.creationTimestamp"])
elif args.topic == "troubleshooting":
    run(k + ["create", "deployment", "dns-target", "--image=nginx:1.28-alpine"])
    run(k + ["expose", "deployment", "dns-target", "--port=80"])
    rollout("dns-target")
    paths = sorted((root / "session-14-kubernetes-troubleshooting/scenarios").glob("*/broken.yaml"))
    for path in paths:
        apply(str(path))
    deadline = time.monotonic() + 180
    while True:
        state = json.loads(run(k + ["get", "pods", "-l", "tier=triage-gauntlet", "-o", "json"]))
        statuses = {p["metadata"]["name"]: p.get("status", {}) for p in state["items"]}
        crash = str(statuses.get("fail-1-crashloop-pod", {}))
        image = str(statuses.get("fail-2-imagepull-pod", {}))
        oom = str(statuses.get("fail-5-oomkilled-pod", {}))
        if "exitCode" in crash and ("ErrImagePull" in image or "ImagePullBackOff" in image) and "OOMKilled" in oom:
            break
        if time.monotonic() > deadline:
            raise RuntimeError("Expected failure states not observed")
        time.sleep(5)
    run(k + ["get", "pods", "-o", "wide"])
    run(k + ["get", "events", "--sort-by=.metadata.creationTimestamp"])
    for path in paths:
        pod = yaml.safe_load(path.read_text())
        name = pod["metadata"]["name"]
        run(k + ["describe", "pod", name])
        run(k + ["logs", name, "--tail=20"], check=False)
        c = pod["spec"]["containers"][0]
        if "crashloop" in name:
            c["env"] = [{"name": "DATABASE_URL", "value": "postgresql://example.invalid/lab"}]
            c["command"] = ["python3", "-u", "-c", "import os,time; assert os.environ['DATABASE_URL']; print('Configuration present; service stays alive'); time.sleep(3600)"]
        elif "imagepull" in name:
            c["image"] = "nginx:1.28-alpine"
        elif "pending" in name:
            c["resources"] = {"requests": {"cpu": "20m", "memory": "32Mi"}}
        elif "dns-failure" in name:
            run(k + ["exec", name, "--", "curl", "-v", "--connect-timeout", "3",
                     "http://postgres-db-wrong-name.production.svc.cluster.local:5432"], check=False)
            c["args"] = ["curl --fail --show-error http://dns-target.campusfix-troubleshooting.svc.cluster.local; sleep 3600"]
        elif "oomkilled" in name:
            c["command"] = ["python3", "-u", "-c", "import time; data=bytearray(5*1024*1024); print('Bounded allocation: 5 MiB'); time.sleep(3600)"]
            c["resources"] = {"requests": {"memory": "32Mi"}, "limits": {"memory": "64Mi"}}
        run(k + ["delete", "pod", name, "--wait=true"])
        run(k + ["apply", "-f", "-"], yaml.safe_dump(pod))
        run(k + ["wait", "--for=condition=Ready", "pod/" + name, "--timeout=180s"])
        run(k + ["logs", name, "--tail=10"])
    run(k + ["get", "pods", "-o", "wide"])
elif args.topic == "helm":
    chart = "session-15-helm/mini-project/notes-chart"
    hb = ["helm", "--kube-context", args.context, "-n", namespace]
    run(["helm", "lint", chart])
    run(hb + ["install", "notes", chart, "--set", "image.tag=1.28-alpine", "--wait", "--timeout", "3m"])
    run(hb + ["upgrade", "notes", chart, "--set", "image.tag=1.28-alpine", "--set", "replicaCount=2", "--wait", "--timeout", "3m"])
    run(hb + ["history", "notes"])
    run(k + ["get", "deployments,services,configmaps"])
    run(hb + ["rollback", "notes", "1", "--wait", "--timeout", "3m"])
    run(hb + ["history", "notes"])
    run(k + ["get", "deployments"])
    run(hb + ["uninstall", "notes", "--wait"])
run(base + ["delete", "namespace", namespace, "--wait=true", "--timeout=180s"])
print("All checks in", args.topic, "passed; temporary namespace removed.")
