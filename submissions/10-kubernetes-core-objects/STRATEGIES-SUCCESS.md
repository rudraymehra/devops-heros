# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:51:35.875641+00:00

Working directory: .

```text
$ uv run --with pyyaml python scripts/run-advanced-kubernetes.py --context campusfix-eks --topic strategies
$ kubectl --context campusfix-eks --request-timeout=30s create namespace campusfix-strategies
namespace/campusfix-strategies created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies run client --image=busybox:1.37 --command -- sleep 3600
pod/client created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies wait --for=condition=Ready pod/client --timeout=180s
pod/client condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/02-blue-green/deployment-blue.yaml
deployment.apps/app-blue created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/02-blue-green/deployment-green.yaml
deployment.apps/app-green created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/02-blue-green/service-blue.yaml
service/myapp-service created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-blue --timeout=180s
Waiting for deployment "app-blue" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "app-blue" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "app-blue" rollout to finish: 2 of 3 updated replicas are available...
deployment "app-blue" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-green --timeout=180s
Waiting for deployment "app-green" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "app-green" rollout to finish: 2 of 3 updated replicas are available...
deployment "app-green" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies exec client -- wget -T 10 -qO- http://myapp-service
<html><body style="background:#003566;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>BLUE ENVIRONMENT</p>
<p style="font-size:0.5em">Version: v1 | Slot: BLUE (LIVE)</p>
</body></html>
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/02-blue-green/service-green.yaml
service/myapp-service configured
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies exec client -- wget -T 10 -qO- http://myapp-service
<html><body style="background:#1b4332;color:#95d5b2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>GREEN ENVIRONMENT</p>
<p style="font-size:0.5em">Version: v2 | Slot: GREEN (STANDBY -> PROMOTED)</p>
</body></html>
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies get endpointslices -l kubernetes.io/service-name=myapp-service -o wide
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                            AGE
myapp-service-bpssq   IPv4          80      10.20.1.42,10.20.1.206,10.20.2.167   13s
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies delete deployment app-blue app-green --wait=true
deployment.apps "app-blue" deleted from campusfix-strategies namespace
deployment.apps "app-green" deleted from campusfix-strategies namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f -
deployment.apps/app-stable created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f -
deployment.apps/app-canary created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f -
service/myapp-canary-service created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-stable --timeout=180s
Waiting for deployment "app-stable" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 2 of 3 updated replicas are available...
deployment "app-stable" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-canary --timeout=180s
deployment "app-canary" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies get pods -l app=myapp-canary -L track
NAME                          READY   STATUS    RESTARTS   AGE   TRACK
app-canary-9bd67fcfc-7vbfh    1/1     Running   0          47s   canary
app-stable-848f547c48-6hcqf   1/1     Running   0          48s   stable
app-stable-848f547c48-vls5r   1/1     Running   0          48s   stable
app-stable-848f547c48-wpjc4   1/1     Running   0          48s   stable
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies exec client -- sh -c for i in $(seq 1 60); do wget -T 5 -qO- http://myapp-canary-service; done
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#7b2d00;color:#ffd60a;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>CANARY v2</p>
<p style="font-size:0.4em;color:#ff9f1c">Track: canary | 10% of traffic (1 of 10 pods)</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
<html><body style="background:#1a1a2e;color:#e2e2e2;font-family:monospace;font-size:3em;text-align:center;padding-top:20vh">
<p>STABLE v1</p>
<p style="font-size:0.4em;color:#888">Track: stable | 90% of traffic</p>
</body></html>
  [exit: 0 ]
Lab uses 3 stable + 1 canary to fit two t3.medium workers. Approximate 75/25 distribution, not an exact guarantee.
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies delete deployment app-stable app-canary --wait=true
deployment.apps "app-stable" deleted from campusfix-strategies namespace
deployment.apps "app-canary" deleted from campusfix-strategies namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/04-recreate/deployment-v1.yaml
deployment.apps/app-recreate created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/04-recreate/service.yaml
service/app-recreate-service created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-recreate --timeout=180s
Waiting for deployment "app-recreate" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "app-recreate" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "app-recreate" rollout to finish: 2 of 3 updated replicas are available...
deployment "app-recreate" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies get pods -l app=app-recreate -o wide
NAME                            READY   STATUS    RESTARTS   AGE   IP            NODE                                         NOMINATED NODE   READINESS GATES
app-recreate-5fdc578485-46mbm   1/1     Running   0          46s   10.20.1.42    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
app-recreate-5fdc578485-ddwlm   1/1     Running   0          46s   10.20.1.70    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
app-recreate-5fdc578485-wwlz8   1/1     Running   0          46s   10.20.1.225   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/04-recreate/deployment-v2.yaml
deployment.apps/app-recreate configured
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-recreate --timeout=180s
Waiting for deployment "app-recreate" rollout to finish: 0 out of 3 new replicas have been updated...
Waiting for deployment "app-recreate" rollout to finish: 0 of 3 updated replicas are available...
Waiting for deployment "app-recreate" rollout to finish: 1 of 3 updated replicas are available...
Waiting for deployment "app-recreate" rollout to finish: 2 of 3 updated replicas are available...
deployment "app-recreate" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies get pods -l app=app-recreate -L version
NAME                            READY   STATUS    RESTARTS   AGE   VERSION
app-recreate-75f5965c97-nl8j8   1/1     Running   0          44s   v2
app-recreate-75f5965c97-qjfzm   1/1     Running   0          44s   v2
app-recreate-75f5965c97-s96wl   1/1     Running   0          44s   v2
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies get events --sort-by=.metadata.creationTimestamp
LAST SEEN   TYPE      REASON                   OBJECT                               MESSAGE
2m46s       Normal    Scheduled                pod/client                           Successfully assigned campusfix-strategies/client to ip-10-20-1-116.ap-south-1.compute.internal
2m45s       Normal    Pulling                  pod/client                           Pulling image "busybox:1.37"
2m42s       Normal    Started                  pod/client                           Container started
2m42s       Normal    Created                  pod/client                           Container created
2m42s       Normal    Pulled                   pod/client                           Successfully pulled image "busybox:1.37" in 3.349s (3.349s including waiting). Image size: 2222118 bytes.
2m40s       Normal    Scheduled                pod/app-blue-75d775cc67-nhrd7        Successfully assigned campusfix-strategies/app-blue-75d775cc67-nhrd7 to ip-10-20-2-64.ap-south-1.compute.internal
2m40s       Normal    SuccessfulCreate         replicaset/app-blue-75d775cc67       Created pod: app-blue-75d775cc67-jkp94
2m40s       Normal    Scheduled                pod/app-blue-75d775cc67-jkp94        Successfully assigned campusfix-strategies/app-blue-75d775cc67-jkp94 to ip-10-20-1-116.ap-south-1.compute.internal
2m40s       Normal    Scheduled                pod/app-blue-75d775cc67-7vlwl        Successfully assigned campusfix-strategies/app-blue-75d775cc67-7vlwl to ip-10-20-1-116.ap-south-1.compute.internal
2m40s       Normal    ScalingReplicaSet        deployment/app-blue                  Scaled up replica set app-blue-75d775cc67 from 0 to 3
2m40s       Normal    SuccessfulCreate         replicaset/app-blue-75d775cc67       Created pod: app-blue-75d775cc67-7vlwl
2m40s       Normal    SuccessfulCreate         replicaset/app-blue-75d775cc67       Created pod: app-blue-75d775cc67-nhrd7
2m39s       Normal    Pulled                   pod/app-blue-75d775cc67-7vlwl        Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
2m39s       Normal    SuccessfulCreate         replicaset/app-green-5dbb4f5d8d      Created pod: app-green-5dbb4f5d8d-jd8q2
2m39s       Normal    Scheduled                pod/app-green-5dbb4f5d8d-mvmf4       Successfully assigned campusfix-strategies/app-green-5dbb4f5d8d-mvmf4 to ip-10-20-1-116.ap-south-1.compute.internal
2m39s       Normal    Created                  pod/app-blue-75d775cc67-nhrd7        Container created
2m39s       Normal    Pulled                   pod/app-blue-75d775cc67-nhrd7        Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
2m39s       Normal    Scheduled                pod/app-green-5dbb4f5d8d-jd8q2       Successfully assigned campusfix-strategies/app-green-5dbb4f5d8d-jd8q2 to ip-10-20-2-64.ap-south-1.compute.internal
2m39s       Normal    Scheduled                pod/app-green-5dbb4f5d8d-6vwxm       Successfully assigned campusfix-strategies/app-green-5dbb4f5d8d-6vwxm to ip-10-20-1-116.ap-south-1.compute.internal
2m39s       Normal    Started                  pod/app-blue-75d775cc67-jkp94        Container started
2m39s       Normal    Created                  pod/app-blue-75d775cc67-jkp94        Container created
2m39s       Normal    SuccessfulCreate         replicaset/app-green-5dbb4f5d8d      Created pod: app-green-5dbb4f5d8d-mvmf4
2m39s       Normal    Started                  pod/app-blue-75d775cc67-7vlwl        Container started
2m39s       Normal    Created                  pod/app-blue-75d775cc67-7vlwl        Container created
2m39s       Normal    Pulled                   pod/app-blue-75d775cc67-jkp94        Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
2m39s       Normal    ScalingReplicaSet        deployment/app-green                 Scaled up replica set app-green-5dbb4f5d8d from 0 to 3
2m39s       Normal    SuccessfulCreate         replicaset/app-green-5dbb4f5d8d      Created pod: app-green-5dbb4f5d8d-6vwxm
2m39s       Normal    Started                  pod/app-blue-75d775cc67-nhrd7        Container started
2m38s       Normal    Started                  pod/app-green-5dbb4f5d8d-jd8q2       Container started
2m38s       Normal    Pulled                   pod/app-green-5dbb4f5d8d-jd8q2       Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
2m38s       Normal    Pulled                   pod/app-green-5dbb4f5d8d-6vwxm       Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
2m38s       Normal    Created                  pod/app-green-5dbb4f5d8d-6vwxm       Container created
2m38s       Normal    Started                  pod/app-green-5dbb4f5d8d-6vwxm       Container started
2m38s       Normal    Started                  pod/app-green-5dbb4f5d8d-mvmf4       Container started
2m38s       Normal    Created                  pod/app-green-5dbb4f5d8d-mvmf4       Container created
2m38s       Normal    Pulled                   pod/app-green-5dbb4f5d8d-mvmf4       Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
2m38s       Normal    Created                  pod/app-green-5dbb4f5d8d-jd8q2       Container created
2m24s       Normal    Killing                  pod/app-blue-75d775cc67-7vlwl        Stopping container web
2m24s       Normal    Killing                  pod/app-green-5dbb4f5d8d-mvmf4       Stopping container web
2m24s       Normal    Killing                  pod/app-blue-75d775cc67-nhrd7        Stopping container web
2m24s       Normal    Killing                  pod/app-green-5dbb4f5d8d-jd8q2       Stopping container web
2m24s       Normal    Killing                  pod/app-blue-75d775cc67-jkp94        Stopping container web
2m24s       Normal    Killing                  pod/app-green-5dbb4f5d8d-6vwxm       Stopping container web
2m22s       Normal    ScalingReplicaSet        deployment/app-stable                Scaled up replica set app-stable-848f547c48 from 0 to 3
2m22s       Normal    SuccessfulCreate         replicaset/app-stable-848f547c48     Created pod: app-stable-848f547c48-wpjc4
2m22s       Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-vls5r      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "eb4d60258f1ef45b2b25f67d57d7ff24927d3830a7c3421bae07f9a88e90de56": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m22s       Normal    Scheduled                pod/app-stable-848f547c48-wpjc4      Successfully assigned campusfix-strategies/app-stable-848f547c48-wpjc4 to ip-10-20-1-116.ap-south-1.compute.internal
2m22s       Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-wpjc4      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "511546c6206b6b10e7db283dfd9aa67da4b4ab70875113bbd617b92ea710aa89": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m22s       Normal    Scheduled                pod/app-stable-848f547c48-6hcqf      Successfully assigned campusfix-strategies/app-stable-848f547c48-6hcqf to ip-10-20-2-64.ap-south-1.compute.internal
2m22s       Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-6hcqf      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "ebc3a61051603f4fcc97522b0e44e2264ad908243fc71656697e5de8aac83641": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m22s       Normal    SuccessfulCreate         replicaset/app-stable-848f547c48     Created pod: app-stable-848f547c48-vls5r
2m22s       Normal    Scheduled                pod/app-stable-848f547c48-vls5r      Successfully assigned campusfix-strategies/app-stable-848f547c48-vls5r to ip-10-20-1-116.ap-south-1.compute.internal
2m22s       Normal    SuccessfulCreate         replicaset/app-stable-848f547c48     Created pod: app-stable-848f547c48-6hcqf
2m21s       Normal    ScalingReplicaSet        deployment/app-canary                Scaled up replica set app-canary-9bd67fcfc from 0 to 1
2m21s       Normal    Scheduled                pod/app-canary-9bd67fcfc-7vbfh       Successfully assigned campusfix-strategies/app-canary-9bd67fcfc-7vbfh to ip-10-20-1-116.ap-south-1.compute.internal
2m21s       Normal    SuccessfulCreate         replicaset/app-canary-9bd67fcfc      Created pod: app-canary-9bd67fcfc-7vbfh
2m21s       Warning   FailedCreatePodSandBox   pod/app-canary-9bd67fcfc-7vbfh       Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "846f36ada29125aa6bfbc01393e5c273b5e5d743e6e26d45a641551eeccb91ae": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m10s       Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-wpjc4      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "73ac83ab15972a9c4b2e5cf2fef47c2082366ac575d149934cdaf9d5f6d81400": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m9s        Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-vls5r      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "e023477fe9f80768215cbfda9d638b8ff7bc1f5202f5d4a511658972ef5d7a7a": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m8s        Warning   FailedCreatePodSandBox   pod/app-canary-9bd67fcfc-7vbfh       Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "1b8444c8885eb408dced0a1dc90e6586d0b0c9f05ad20cd153df199dc278ddf9": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
2m8s        Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-6hcqf      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "5439efae9477910d012cf6679a6937f3a79c4aae793aeda698e597f43469b205": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
118s        Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-vls5r      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "4662a55415b701667843f12ff2c6613395ce72dc7f6fea8863fc228d61775d9a": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
117s        Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-wpjc4      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "39f7da2403c44bab657a1678cfdf571cd9b58cd0d42c0f2b817d35ae7808a9b4": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
117s        Warning   FailedCreatePodSandBox   pod/app-stable-848f547c48-6hcqf      Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "ce4ce2af2f3a16daccb1ad336e05faa78fb99aeee8bca9bf1218e428207f0e48": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
114s        Warning   FailedCreatePodSandBox   pod/app-canary-9bd67fcfc-7vbfh       Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "26de876cecf9599db273e12b0b68ad202c0cb00d9a70db49ebe93ee9c23a2adf": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
105s        Normal    Started                  pod/app-stable-848f547c48-wpjc4      Container started
105s        Normal    Created                  pod/app-stable-848f547c48-wpjc4      Container created
105s        Normal    Pulled                   pod/app-stable-848f547c48-wpjc4      Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
105s        Normal    Started                  pod/app-stable-848f547c48-vls5r      Container started
105s        Normal    Created                  pod/app-stable-848f547c48-vls5r      Container created
105s        Normal    Pulled                   pod/app-stable-848f547c48-vls5r      Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
102s        Normal    Pulled                   pod/app-stable-848f547c48-6hcqf      Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
102s        Normal    Created                  pod/app-stable-848f547c48-6hcqf      Container created
102s        Normal    Started                  pod/app-stable-848f547c48-6hcqf      Container started
101s        Normal    Pulled                   pod/app-canary-9bd67fcfc-7vbfh       Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
101s        Normal    Created                  pod/app-canary-9bd67fcfc-7vbfh       Container created
101s        Normal    Started                  pod/app-canary-9bd67fcfc-7vbfh       Container started
92s         Normal    Killing                  pod/app-stable-848f547c48-wpjc4      Stopping container web
92s         Normal    Killing                  pod/app-stable-848f547c48-vls5r      Stopping container web
92s         Normal    Killing                  pod/app-stable-848f547c48-6hcqf      Stopping container web
92s         Normal    Killing                  pod/app-canary-9bd67fcfc-7vbfh       Stopping container web
91s         Normal    Scheduled                pod/app-recreate-5fdc578485-46mbm    Successfully assigned campusfix-strategies/app-recreate-5fdc578485-46mbm to ip-10-20-1-116.ap-south-1.compute.internal
91s         Normal    Scheduled                pod/app-recreate-5fdc578485-wwlz8    Successfully assigned campusfix-strategies/app-recreate-5fdc578485-wwlz8 to ip-10-20-1-116.ap-south-1.compute.internal
91s         Normal    SuccessfulCreate         replicaset/app-recreate-5fdc578485   Created pod: app-recreate-5fdc578485-wwlz8
91s         Normal    SuccessfulCreate         replicaset/app-recreate-5fdc578485   Created pod: app-recreate-5fdc578485-46mbm
91s         Normal    ScalingReplicaSet        deployment/app-recreate              Scaled up replica set app-recreate-5fdc578485 from 0 to 3
91s         Normal    Scheduled                pod/app-recreate-5fdc578485-ddwlm    Successfully assigned campusfix-strategies/app-recreate-5fdc578485-ddwlm to ip-10-20-1-116.ap-south-1.compute.internal
91s         Normal    SuccessfulCreate         replicaset/app-recreate-5fdc578485   Created pod: app-recreate-5fdc578485-ddwlm
90s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-ddwlm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "dc3985289de7e6f3d42983d5fe602afbabdfc946b74d615c68f44bc367706644": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
90s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-wwlz8    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "23af71631c3e0421274fa8fce1a14092262c80d27953a09d3e929b402f78c40b": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
90s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-46mbm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "a92744a14064c997a7686d0e4339649ab6cb169eeba70e4959a26545720528c5": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
80s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-wwlz8    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "ec49b88fefdcf1b90e361e16da5cbd619995451e278915357ce19a50945855d0": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
79s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-46mbm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "ed2f7ac2aa0f59bcd86648e0d3c5076cc558ac594dc377c078eef7a396fc1b45": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
78s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-ddwlm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "0e1a4386a0c6bc8c816cb0af0535ecd38bf0d84b070cda281a4e284e6035e285": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
66s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-ddwlm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "645b7356800310e404e8cf2ae12e108d59aaaf9c81f8a9d308973fac6d9d2659": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
66s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-wwlz8    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "4fba764885f1dadb433ad3f5cd7821f58fb9482f690c94e07268b0a53fed9f4d": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
63s         Warning   FailedCreatePodSandBox   pod/app-recreate-5fdc578485-46mbm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "ac1445403901717acb50d0b8eaa2c06f58065b7eff47e9222b7ae5308371a185": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
52s         Normal    Pulled                   pod/app-recreate-5fdc578485-wwlz8    Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
52s         Normal    Started                  pod/app-recreate-5fdc578485-wwlz8    Container started
52s         Normal    Pulled                   pod/app-recreate-5fdc578485-ddwlm    Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
52s         Normal    Created                  pod/app-recreate-5fdc578485-ddwlm    Container created
52s         Normal    Started                  pod/app-recreate-5fdc578485-ddwlm    Container started
52s         Normal    Created                  pod/app-recreate-5fdc578485-wwlz8    Container created
47s         Normal    Pulled                   pod/app-recreate-5fdc578485-46mbm    Container image "nginx:1.24-alpine" already present on machine and can be accessed by the pod
47s         Normal    Created                  pod/app-recreate-5fdc578485-46mbm    Container created
47s         Normal    Started                  pod/app-recreate-5fdc578485-46mbm    Container started
44s         Normal    SuccessfulDelete         replicaset/app-recreate-5fdc578485   Deleted pod: app-recreate-5fdc578485-ddwlm
44s         Normal    SuccessfulCreate         replicaset/app-recreate-75f5965c97   Created pod: app-recreate-75f5965c97-nl8j8
44s         Normal    Scheduled                pod/app-recreate-75f5965c97-nl8j8    Successfully assigned campusfix-strategies/app-recreate-75f5965c97-nl8j8 to ip-10-20-1-116.ap-south-1.compute.internal
44s         Normal    Scheduled                pod/app-recreate-75f5965c97-s96wl    Successfully assigned campusfix-strategies/app-recreate-75f5965c97-s96wl to ip-10-20-1-116.ap-south-1.compute.internal
44s         Normal    SuccessfulCreate         replicaset/app-recreate-75f5965c97   Created pod: app-recreate-75f5965c97-qjfzm
44s         Normal    SuccessfulCreate         replicaset/app-recreate-75f5965c97   Created pod: app-recreate-75f5965c97-s96wl
44s         Normal    Killing                  pod/app-recreate-5fdc578485-46mbm    Stopping container web
44s         Normal    ScalingReplicaSet        deployment/app-recreate              Scaled down replica set app-recreate-5fdc578485 from 3 to 0
44s         Normal    ScalingReplicaSet        deployment/app-recreate              Scaled up replica set app-recreate-75f5965c97 from 0 to 3
44s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-nl8j8    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "d6df40d9859fc58a2ad52a74f2a17c8419ac663629221a4ed4e3b29c020adc6c": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
44s         Normal    Scheduled                pod/app-recreate-75f5965c97-qjfzm    Successfully assigned campusfix-strategies/app-recreate-75f5965c97-qjfzm to ip-10-20-1-116.ap-south-1.compute.internal
44s         Normal    Killing                  pod/app-recreate-5fdc578485-ddwlm    Stopping container web
44s         Normal    Killing                  pod/app-recreate-5fdc578485-wwlz8    Stopping container web
44s         Normal    SuccessfulDelete         replicaset/app-recreate-5fdc578485   Deleted pod: app-recreate-5fdc578485-46mbm
44s         Normal    SuccessfulDelete         replicaset/app-recreate-5fdc578485   Deleted pod: app-recreate-5fdc578485-wwlz8
43s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-qjfzm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "fef3e813c26de4b52e2ea2d7757f0d8c32b6457ec2f2872eead19a3ee8a2cfdd": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
43s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-s96wl    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "f91616ba6ba6a7b13cf26e9f5f6319a04e576a67e426ea5647225f9d2fb54c84": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
32s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-qjfzm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "4dfe3ca00f6152cebf77543155e886c607686bf3639cb24544e13abda1f2d236": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
32s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-s96wl    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "d5eb569c09716eb3bf4640f2bbc9896553cf74d78d31b5c3bfee0c1638a72881": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
32s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-nl8j8    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "94b4959895caed987e6900114825e11cfe3e928ec1455182f81b2258e7349072": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
20s         Normal    Pulled                   pod/app-recreate-75f5965c97-nl8j8    Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
20s         Normal    Created                  pod/app-recreate-75f5965c97-nl8j8    Container created
20s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-s96wl    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "10d91047299d926db7a8c6cf2ac0371f8e7459a62119c35f36e7cc3861195c96": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
20s         Normal    Started                  pod/app-recreate-75f5965c97-nl8j8    Container started
17s         Warning   FailedCreatePodSandBox   pod/app-recreate-75f5965c97-qjfzm    Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "c9078ac44a1e59772d4f333f92f84474a286768c435b71ce5e6ab27606531355": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
5s          Normal    Created                  pod/app-recreate-75f5965c97-s96wl    Container created
5s          Normal    Pulled                   pod/app-recreate-75f5965c97-s96wl    Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
5s          Normal    Started                  pod/app-recreate-75f5965c97-s96wl    Container started
3s          Normal    Pulled                   pod/app-recreate-75f5965c97-qjfzm    Container image "nginx:1.25-alpine" already present on machine and can be accessed by the pod
2s          Normal    Created                  pod/app-recreate-75f5965c97-qjfzm    Container created
2s          Normal    Started                  pod/app-recreate-75f5965c97-qjfzm    Container started
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s delete namespace campusfix-strategies --wait=true --timeout=180s
namespace "campusfix-strategies" deleted
  [exit: 0 ]
All checks in strategies passed; temporary namespace removed.

```

Exit code: 0
