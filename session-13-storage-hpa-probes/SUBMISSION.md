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

- [ ] PVC reaches `Bound`
- [ ] Data remains after a Pod replacement
- [ ] HPA changes replica count under load
- [ ] Probe failure/recovery appears in events
- [ ] Cleanup output
