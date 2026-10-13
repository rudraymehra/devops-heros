"""Verify persistence, probes and GitOps; capture real command/API responses."""
import json
import subprocess
import time
import urllib.request

K = ["kubectl", "--context", "campusfix-eks", "--request-timeout=30s"]


def run(arguments):
    print("$", " ".join(K + arguments), flush=True)
    result = subprocess.run(K + arguments, capture_output=True, text=True, timeout=240)
    print(result.stdout, result.stderr, flush=True)
    result.check_returncode()
    return result.stdout


def api(path, data=None):
    req = urllib.request.Request("http://127.0.0.1:8088" + path,
        data=json.dumps(data).encode() if data else None,
        headers={"Host": "campusfix.local", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=15) as response:
        result = json.load(response)
        print(path, json.dumps(result), flush=True)
        return result


run(["get", "nodes", "-o", "wide"])
run(["get", "pods,svc,pvc,hpa,ingress", "-n", "taskboard", "-o", "wide"])
before = api("/api/requests", {"title": "Persistence verification", "location": "Cloud lab",
                             "description": "Synthetic report retained across database Pod replacement.",
                             "category": "OTHER", "urgency": "NORMAL", "reporter": "Sudhir Mehra"})
run(["delete", "pod", "-n", "taskboard", "-l", "app=taskboard-postgres", "--wait=true"])
run(["rollout", "status", "deployment/taskboard-postgres", "-n", "taskboard", "--timeout=180s"])
time.sleep(5)
after = api("/api/requests/" + str(before["id"]))
assert after["id"] == before["id"] and after["title"] == before["title"]
print("PASS: PostgreSQL PVC retains the exact report after database Pod replacement.", flush=True)
run(["get", "pvc", "-n", "taskboard"])
run(["get", "deployment/taskboard-backend", "-n", "taskboard", "-o",
     "jsonpath={.spec.template.spec.containers[0].readinessProbe} {.spec.template.spec.containers[0].livenessProbe}"])

# Change managed configuration, not HPA-owned replica counts.
run(["patch", "configmap", "taskboard-config", "-n", "taskboard", "--type=merge", "-p",
     json.dumps({"data": {"APP_NAME": "temporary-drift-test"}})])
run(["annotate", "application", "campusfix", "-n", "argocd", "argocd.argoproj.io/refresh=hard", "--overwrite"])
deadline = time.monotonic() + 180
while True:
    current = run(["get", "configmap", "taskboard-config", "-n", "taskboard", "-o", "json"])
    if json.loads(current)["data"].get("APP_NAME") == "CampusFix API":
        break
    if time.monotonic() > deadline:
        raise RuntimeError("Argo CD did not heal the configuration drift")
    time.sleep(5)
print("PASS: Argo CD restored the committed application name after an intentional live edit.", flush=True)
run(["get", "application", "campusfix", "-n", "argocd"])
run(["get", "pods", "-n", "monitoring"])
with urllib.request.urlopen("http://127.0.0.1:9090/api/v1/targets", timeout=15) as response:
    targets = [t for t in json.load(response)["data"]["activeTargets"] if t["labels"].get("namespace") == "taskboard"]
assert len(targets) >= 2 and all(t["health"] == "up" for t in targets)
print("PASS: backend Prometheus targets:", json.dumps(targets, indent=2), flush=True)
