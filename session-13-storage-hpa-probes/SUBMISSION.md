# Session 13 Submission

## Completed deliverables

- `01-volumes/volume.md` documents `emptyDir`, `hostPath`, PV, PVC, StorageClass,
  and dynamic provisioning, with runnable examples.
- `04-hpa/` contains the Deployment, Service, HPA, and load-test instructions.
- `05-probes/` demonstrates startup, readiness, and liveness probes.
- `mini-project/` combines storage, probes, resources, a Service, and autoscaling.

## Verification

```bash
kubectl apply -f mini-project/namespace.yaml
kubectl apply -f mini-project/pvc.yaml
kubectl apply -f mini-project/deployment.yaml
kubectl apply -f mini-project/service.yaml
kubectl apply -f mini-project/hpa.yaml
kubectl get pods,pvc,service,hpa -n production-webapp
kubectl top pods -n production-webapp
```

## Evidence checklist

- [x] PVC reaches `Bound`
- [x] Data remains after a Pod replacement
- [x] HPA changes replica count under load
- [x] Probe failure/recovery appears in events
- [x] Cleanup output

## Run notes

- The static `student-pvc` sets `storageClassName: ""` so it binds to the manually
  defined `student-pv` instead of Minikube's default dynamic StorageClass.
- The NGINX request loop produced no measurable CPU in this Minikube run. For the
  scaling demonstration, a temporary BusyBox CPU-load sidecar drove the capstone HPA
  from 2 to 4 replicas at `100%` against its `50%` target; deleting the project
  namespace removed that temporary workload.
