# Session 10 Submission Checklist

For a fresh live run of Task 1, execute `bash ./run-deployment-strategies-lab.sh`
from this directory. The helper uses a separate Minikube profile and removes only
that profile after verifying the four strategies.

For a fresh live run of Task 2, execute `bash ./run-pod-lifecycle-lab.sh` from
this directory. It walks through the twelve examples in order, prints status,
events, and relevant logs, then removes only its separate Minikube profile.

## Task 1: deployment strategies

The four implementations are under `01-rolling-update/`, `02-blue-green/`,
`03-canary/`, and `04-recreate/`. Follow each directory's README and capture:

- `kubectl get deployments,pods,services -o wide`
- the application response before and after switching/updating
- `kubectl rollout status` and `kubectl rollout history` where applicable

Key observations:

- Rolling update replaces Pods gradually while retaining availability.
- Blue-green runs two complete versions and switches a Service selector.
- Canary runs stable and canary versions together behind a shared Service.
- Recreate terminates the old ReplicaSet before starting the replacement.

## Task 2: Pod lifecycle

The `pod-lifecycle/` directory contains twelve runnable cases: Running, Pending,
Succeeded, Failed, CrashLoopBackOff, ImagePullBackOff, readiness, liveness, startup,
init containers, multi-container Pods, and graceful termination.

```bash
kubectl apply -f pod-lifecycle/01-running.yaml
kubectl get pod lifecycle-running -o wide
kubectl describe pod lifecycle-running
kubectl delete -f pod-lifecycle/01-running.yaml
```

Repeat with each manifest as explained in `pod-lifecycle/README.md`.

## Evidence checklist

- [x] Rolling update output and version response
- [x] Blue/green traffic switch output
- [x] Stable/canary responses
- [x] Recreate Pod termination/recreation output
- [x] Status, events, and explanation for all lifecycle examples

Lifecycle evidence is saved under `screenshots/rudray-20261023-224618/`. The
liveness capture shows failed probes and the kubelet starting a restart; the
status snapshot was taken before the restart count advanced, so the immediate
`--previous` log query reported that no previous container was available yet.
