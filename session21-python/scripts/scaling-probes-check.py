"""Observe autoscaling under real HTTP load, then exercise readiness/liveness."""
import json
import subprocess
import time

k = ["kubectl", "--context", "campusfix-eks", "--request-timeout=20s", "-n", "taskboard"]


def run(args, data=None):
    print("$", " ".join(k + args), flush=True)
    r = subprocess.run(k + args, input=data, text=True, capture_output=True, timeout=180)
    print(r.stdout, r.stderr, flush=True)
    r.check_returncode()
    return r.stdout


run(["delete", "pod", "campusfix-load", "--ignore-not-found=true", "--wait=true"])
run(["apply", "-f", "session21-python/scripts/cloud-load.yaml"])
run(["wait", "--for=condition=Ready", "pod/campusfix-load", "--timeout=120s"])
scaled = False
for _ in range(14):
    state = json.loads(run(["get", "hpa", "taskboard-backend", "-o", "json"]))
    scaled |= state.get("status", {}).get("desiredReplicas", 0) > 2
    run(["get", "pods", "-l", "app=taskboard-backend"])
    time.sleep(10)
run(["logs", "campusfix-load"])
run(["describe", "hpa", "taskboard-backend"])
assert scaled, "HPA did not request more than two replicas during the load window"
print("PASS: HPA requested additional replicas under real HTTP load.", flush=True)

pod = {"apiVersion": "v1", "kind": "Pod", "metadata": {"name": "campusfix-probes"},
       "spec": {"containers": [{
           "name": "web", "image": "nginx:1.28-alpine",
           "resources": {"requests": {"cpu": "20m", "memory": "32Mi"}},
           "lifecycle": {"postStart": {"exec": {"command": ["sh", "-c", "touch /usr/share/nginx/html/ready /usr/share/nginx/html/live"]}}},
           "readinessProbe": {"httpGet": {"path": "/ready", "port": 80}, "periodSeconds": 2, "failureThreshold": 1},
           "livenessProbe": {"httpGet": {"path": "/live", "port": 80}, "periodSeconds": 2, "failureThreshold": 2},
       }]}}
run(["apply", "-f", "-"], json.dumps(pod))
run(["wait", "--for=condition=Ready", "pod/campusfix-probes", "--timeout=120s"])
run(["exec", "campusfix-probes", "--", "rm", "/usr/share/nginx/html/ready"])
run(["wait", "--for=condition=Ready=false", "pod/campusfix-probes", "--timeout=30s"])
state = json.loads(run(["get", "pod", "campusfix-probes", "-o", "json"]))
assert state["status"]["containerStatuses"][0]["restartCount"] == 0
print("PASS: readiness failure removes readiness without restarting the process.")
run(["exec", "campusfix-probes", "--", "touch", "/usr/share/nginx/html/ready"])
run(["wait", "--for=condition=Ready", "pod/campusfix-probes", "--timeout=30s"])
run(["exec", "campusfix-probes", "--", "rm", "/usr/share/nginx/html/live"])
for _ in range(15):
    state = json.loads(run(["get", "pod", "campusfix-probes", "-o", "json"]))
    if state["status"]["containerStatuses"][0]["restartCount"] > 0:
        break
    time.sleep(3)
assert state["status"]["containerStatuses"][0]["restartCount"] > 0
run(["wait", "--for=condition=Ready", "pod/campusfix-probes", "--timeout=60s"])
run(["describe", "pod", "campusfix-probes"])
print("PASS: liveness failure restarts the container and it recovers readiness.")
run(["delete", "pod", "campusfix-probes", "campusfix-load", "--wait=true"])
