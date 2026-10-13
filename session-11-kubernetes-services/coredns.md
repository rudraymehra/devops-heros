# CoreDNS and Kubernetes Service Discovery

CoreDNS is Kubernetes' default cluster DNS server. Pods normally receive the
cluster DNS Service address in `/etc/resolv.conf`. CoreDNS watches Kubernetes
Services and EndpointSlices and serves records such as:

```text
<service>.<namespace>.svc.cluster.local
```

For a headless Service, DNS returns Pod addresses instead of one ClusterIP. An
`ExternalName` Service returns a CNAME pointing to the configured external name.

## Resolution flow

1. An application asks the resolver for `api`.
2. The Pod search suffix expands it to `api.default.svc.cluster.local`.
3. The query reaches the `kube-dns` Service.
4. CoreDNS' `kubernetes` plugin answers using current Service/EndpointSlice state.

## Configuration and troubleshooting

```bash
kubectl get deployment,pods,service -n kube-system -l k8s-app=kube-dns
kubectl get configmap coredns -n kube-system -o yaml
kubectl logs -n kube-system -l k8s-app=kube-dns
kubectl exec client-pod -- cat /etc/resolv.conf
kubectl exec client-pod -- nslookup kubernetes.default.svc.cluster.local
kubectl get service,endpoints,endpointslices
```

If name resolution fails, verify the queried name and namespace, the Pod's resolver
configuration, CoreDNS health/logs, the `kube-dns` Service, and any NetworkPolicy
blocking UDP/TCP port 53. If DNS works but traffic fails, inspect Service selectors,
EndpointSlices, readiness, and `targetPort`.
