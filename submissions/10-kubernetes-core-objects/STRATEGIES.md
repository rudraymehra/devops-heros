# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:43:04.451014+00:00

Working directory: .

```text
$ uv run --with pyyaml python scripts/run-advanced-kubernetes.py --context campusfix-eks --topic strategies
Installed 1 package in 3ms
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
Waiting for deployment "app-green" rollout to finish: 0 of 3 updated replicas are available...
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
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                           AGE
myapp-service-87djx   IPv4          80      10.20.1.42,10.20.2.167,10.20.1.15   45s
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies delete deployment app-blue app-green --wait=true
deployment.apps "app-blue" deleted from campusfix-strategies namespace
deployment.apps "app-green" deleted from campusfix-strategies namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/03-canary/deployment-stable.yaml
deployment.apps/app-stable created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/03-canary/deployment-canary.yaml
deployment.apps/app-canary created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies apply -f session10-k8s-core-objects/03-canary/service.yaml
service/myapp-canary-service created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-strategies rollout status deployment/app-stable --timeout=180s
Waiting for deployment "app-stable" rollout to finish: 0 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 1 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 2 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 3 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 4 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 5 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 6 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 7 of 9 updated replicas are available...
Waiting for deployment "app-stable" rollout to finish: 8 of 9 updated replicas are available...
 error: timed out waiting for the condition
 [exit: 1 ]
Traceback (most recent call last):
  File "/private/tmp/campusfix-publish/scripts/run-advanced-kubernetes.py", line 58, in <module>
    rollout("app-stable")
    ~~~~~~~^^^^^^^^^^^^^^
  File "/private/tmp/campusfix-publish/scripts/run-advanced-kubernetes.py", line 34, in rollout
    run(k + ["rollout", "status", "deployment/" + name, "--timeout=180s"])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/campusfix-publish/scripts/run-advanced-kubernetes.py", line 25, in run
    raise RuntimeError("Command failed")
RuntimeError: Command failed

```

Exit code: 1
