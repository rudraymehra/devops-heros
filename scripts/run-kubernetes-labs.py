#!/usr/bin/env python3
"""Run the four Kubernetes labs and save actual command output per submission."""
import argparse
import json
from pathlib import Path
import shlex
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]
NS = "rudray-devops-hw"
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("--context", default="devops-homework", help="Local Minikube context")
parser.add_argument("--topic", choices=["all", "09", "10", "11", "12"], default="all")
args = parser.parse_args()
BASE = ["kubectl", "--context", args.context, "--request-timeout=30s"]
K = BASE + ["-n", NS]


class Evidence:
    def __init__(self, folder):
        self.folder = ROOT / "submissions" / folder
        self.text = ["# Executed Kubernetes lab output\n\n",
                     f"Context: `{args.context}`. Namespace: `{NS}`.\n\n"]
        self.path = self.folder / "OUTPUT.md"

    def run(self, command, expected=0):
        result = subprocess.run(command, cwd=ROOT, text=True,
                                stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self.text.append(f"```console\n$ {shlex.join(command)}\n{result.stdout}"
                         f"[exit status: {result.returncode}]\n```\n\n")
        self.path.write_text("".join(self.text))
        print(shlex.join(command), flush=True)
        print(result.stdout, end="", flush=True)
        if result.returncode != expected:
            raise RuntimeError(f"Command failed; see {self.path}")
        return result.stdout

    def apply(self, name):
        self.run(K + ["apply", "-f", str(self.folder.relative_to(ROOT) / name)])

    def complete(self):
        self.text.append("All checks in this topic completed successfully.\n")
        self.path.write_text("".join(self.text))


def rollout(e, name):
    e.run(K + ["rollout", "status", "deployment/" + name, "--timeout=180s"])


def fundamentals():
    e = Evidence("09-kubernetes-fundamentals")
    e.run(BASE + ["version", "--client"])
    e.run(BASE + ["cluster-info"])
    e.run(BASE + ["get", "nodes", "-o", "wide"])
    e.run(BASE + ["get", "pods", "-n", "kube-system"])
    e.apply("namespace.yaml")
    e.apply("pod.yaml")
    e.run(K + ["wait", "--for=condition=Ready", "pod/hello-kubernetes", "--timeout=180s"])
    e.run(K + ["get", "pod", "hello-kubernetes", "-o", "wide"])
    html = e.run(K + ["exec", "hello-kubernetes", "--", "wget", "-qO-", "http://127.0.0.1"])
    assert "Welcome to nginx!" in html
    e.run(K + ["logs", "hello-kubernetes", "--tail=10"])
    e.complete()


def core_objects():
    e = Evidence("10-kubernetes-core-objects")
    e.run(BASE + ["apply", "-f", "submissions/09-kubernetes-fundamentals/namespace.yaml"])
    e.apply("objects.yaml")
    e.run(K + ["wait", "--for=condition=Ready", "pod/standalone-web", "--timeout=180s"])
    e.run(K + ["wait", "--for=condition=Ready", "pod", "-l", "app=replica-web", "--timeout=180s"])
    rollout(e, "deployment-web")
    e.run(K + ["get", "pods,replicasets,deployments", "-o", "wide"])
    pods = json.loads(e.run(K + ["get", "pods", "-l", "app=replica-web", "-o", "json"]))
    old = pods["items"][0]["metadata"]["name"]
    e.run(K + ["delete", "pod", old, "--wait=true"])
    deadline = time.monotonic() + 120
    while True:
        current = json.loads(e.run(K + ["get", "pods", "-l", "app=replica-web", "-o", "json"]))
        if len(current["items"]) == 2 and all(p["metadata"]["name"] != old for p in current["items"]):
            break
        if time.monotonic() > deadline:
            raise RuntimeError("ReplicaSet did not replace the deleted Pod")
        time.sleep(2)
    e.run(K + ["wait", "--for=condition=Ready", "pod", "-l", "app=replica-web", "--timeout=180s"])
    e.run(K + ["get", "pods", "-l", "app=replica-web", "-o", "wide"])
    e.run(K + ["scale", "deployment/deployment-web", "--replicas=3"])
    rollout(e, "deployment-web")
    e.run(K + ["set", "image", "deployment/deployment-web", "nginx=nginx:1.28-alpine"])
    rollout(e, "deployment-web")
    e.run(K + ["rollout", "history", "deployment/deployment-web"])
    e.run(K + ["rollout", "undo", "deployment/deployment-web"])
    rollout(e, "deployment-web")
    image = e.run(K + ["get", "deployment", "deployment-web", "-o",
                      "jsonpath={.spec.template.spec.containers[0].image}"])
    assert image == "nginx:1.27-alpine"
    e.run(K + ["get", "pods,rs,deployments"])
    e.complete()


def services():
    e = Evidence("11-kubernetes-services")
    e.run(BASE + ["apply", "-f", "submissions/09-kubernetes-fundamentals/namespace.yaml"])
    e.apply("services.yaml")
    rollout(e, "service-web")
    e.run(K + ["wait", "--for=condition=Ready", "pod/network-client", "--timeout=180s"])
    e.run(K + ["get", "services", "-o", "wide"])
    e.run(K + ["get", "endpointslices", "-l", "kubernetes.io/service-name=web-clusterip"])
    for service in ["web-clusterip", "web-headless", "external-docs"]:
        host = f"{service}.{NS}.svc.cluster.local."
        e.run(K + ["exec", "network-client", "--", "nslookup", "-type=A", host])
    for host in ["web-clusterip", "web-nodeport", "web-loadbalancer"]:
        html = e.run(K + ["exec", "network-client", "--", "wget", "-qO-", "http://" + host])
        assert "Welcome to nginx!" in html
    node = json.loads(e.run(BASE + ["get", "nodes", "-o", "json"]))["items"][0]
    node_ip = next(a["address"] for a in node["status"]["addresses"] if a["type"] == "InternalIP")
    port = e.run(K + ["get", "service", "web-nodeport", "-o", "jsonpath={.spec.ports[0].nodePort}"])
    html = e.run(K + ["exec", "network-client", "--", "wget", "-qO-", f"http://{node_ip}:{port}"])
    assert "Welcome to nginx!" in html
    # A selector error removes all matching backend addresses, despite a healthy Deployment.
    e.run(K + ["patch", "service", "web-clusterip", "--type=merge", "-p",
               '{"spec":{"selector":{"app":"no-such-app"}}}'])
    try:
        deadline = time.monotonic() + 30
        while True:
            slices = json.loads(e.run(K + ["get", "endpointslices", "-l",
                                          "kubernetes.io/service-name=web-clusterip", "-o", "json"]))
            if all(not s.get("endpoints") for s in slices["items"]):
                break
            if time.monotonic() > deadline:
                raise RuntimeError("Wrong selector still has endpoints")
            time.sleep(2)
    finally:
        e.apply("services.yaml")
    e.complete()


def config_ingress():
    e = Evidence("12-kubernetes-config-ingress")
    e.run(BASE + ["apply", "-f", "submissions/09-kubernetes-fundamentals/namespace.yaml"])
    for name in ["configmap.yaml", "secret.yaml", "app.yaml", "ingress.yaml"]:
        e.apply(name)
    for name in ["homework-frontend", "homework-backend"]:
        rollout(e, name)
    e.run(K + ["get", "configmaps,secrets,deployments,services,ingresses"])
    e.run(K + ["describe", "secret", "homework-db"])
    for key in ["ENVIRONMENT", "DEFAULT_CURRENCY", "DB_USER"]:
        e.run(K + ["exec", "deployment/homework-backend", "--", "printenv", key])
    e.run(K + ["exec", "deployment/homework-backend", "--", "python3", "-c",
               'import os; print("DB_PASSWORD present:", bool(os.environ.get("DB_PASSWORD")))'])
    e.run(K + ["describe", "ingress", "homework-ingress"])
    # Test HTTP through the ingress controller, not a direct backend port-forward.
    e.run(BASE + ["-n", "ingress-nginx", "rollout", "status",
                  "deployment/ingress-nginx-controller", "--timeout=180s"])
    fetch = ('import urllib.request; '
             'r=urllib.request.Request("http://ingress-nginx-controller.ingress-nginx.svc.cluster.local%s", '
             'headers={"Host":"homework.local"}); '
             'print(urllib.request.urlopen(r, timeout=15).read().decode())')
    html = e.run(K + ["exec", "deployment/homework-backend", "--", "python3", "-c", fetch % "/"])
    assert "Hello World from Kubernetes" in html
    body = e.run(K + ["exec", "deployment/homework-backend", "--", "python3", "-c", fetch % "/api/health"])
    data = json.loads(body)
    assert data["environment"] == "production" and data["db_password_present"]
    assert data["path"] == "/api/health"
    e.complete()


if __name__ == "__main__":
    # Fail before replacing evidence if Docker/Minikube has not been started.
    subprocess.run(BASE + ["get", "nodes"], check=True)
    for topic, function in [("09", fundamentals), ("10", core_objects),
                            ("11", services), ("12", config_ingress)]:
        if args.topic in ["all", topic]:
            function()
