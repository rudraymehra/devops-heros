# Session 10 Submission Checklist

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

- [ ] Rolling update output and version response
- [ ] Blue/green traffic switch output
- [ ] Stable/canary responses
- [ ] Recreate Pod termination/recreation output
- [ ] Status, events, and explanation for all lifecycle examples
