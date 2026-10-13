# Session 11 Submission Checklist

## Service demonstrations

This session contains runnable examples for all five required Service forms:

1. `01-clusterip/`
2. `02-nodeport/`
3. `03-loadbalancer/`
4. `04-externalname/`
5. `05-headless/`

For every example, follow its README and capture `kubectl get`, `kubectl describe`,
connectivity/DNS tests, and cleanup output.

## Object comparisons

| Comparison | Main distinction |
|---|---|
| Deployment vs ReplicaSet | A Deployment owns ReplicaSets and adds declarative rollouts and rollback. |
| Deployment vs DaemonSet | Deployment controls replica count; DaemonSet normally runs one Pod per eligible node. |
| Deployment vs StatefulSet | StatefulSet gives stable identity, ordered rollout, and per-Pod storage. |
| ReplicaSet vs Service | ReplicaSet maintains Pods; Service gives selected ready Pods stable networking. |

Detailed Service behavior is documented in `service.md`; Kubernetes naming is in
`fqdn.md`; DNS internals and diagnostics are in `coredns.md`.

## Evidence checklist

- [ ] YAML and output for all five Service forms
- [ ] Connectivity checks from client Pods
- [ ] `nslookup` output for short name and FQDN
- [ ] CoreDNS configuration/log inspection
- [ ] Empty-endpoints failure, diagnosis, and fix
