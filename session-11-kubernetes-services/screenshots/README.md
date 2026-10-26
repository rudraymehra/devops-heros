# Session 11 screenshots

## ClusterIP

Captures from the ClusterIP walkthrough on 2026-10-23. Three backend replicas became Ready, the Service exposed all three endpoints, and requests by short Service name and FQDN returned the NGINX page. The follow-up terminal output also confirmed the Service IP request succeeded and the resources were cleaned up.

- [01-clusterip-instructions.png](rudray-20261023-235102/01-clusterip-instructions.png)
- [02-clusterip-manifests-and-setup.png](rudray-20261023-235102/02-clusterip-manifests-and-setup.png)
- [03-clusterip-endpoints-and-dns-tests.png](rudray-20261023-235102/03-clusterip-endpoints-and-dns-tests.png)
- [04-clusterip-tests-and-cleanup-instructions.png](rudray-20261023-235102/04-clusterip-tests-and-cleanup-instructions.png)
- [05-clusterip-deploy-and-dns-response.png](rudray-20261023-235102/05-clusterip-deploy-and-dns-response.png)
- [06-clusterip-response.png](rudray-20261023-235102/06-clusterip-response.png)

## LoadBalancer

The native terminal captures show Minikube tunnel running and the LoadBalancer Service assigned external IP `127.0.0.1` on 2026-10-24. The follow-up terminal output confirmed HTTP 200 and the NGINX page from `127.0.0.1`.

- [01-minikube-tunnel-running.png](rudray-20261024-021721/01-minikube-tunnel-running.png)
- [02-loadbalancer-external-ip.png](rudray-20261024-021721/02-loadbalancer-external-ip.png)

## ExternalName

The terminal capture shows the Service targeting `api.github.com`, a DNS CNAME lookup resolving to that hostname, and a successful GitHub API response. `nslookup` emitted NXDOMAIN for search suffixes before resolving the full Service DNS name.

- [01-externalname-cname-and-github-response.png](rudray-20261024-022930/01-externalname-cname-and-github-response.png)

## Headless Service

The native terminal capture shows the Service IP as `None`, all three StatefulSet Pods Ready, DNS returning the three Pod addresses and the individual `web-stateful-0` address, and a successful NGINX response from that Pod.

- [01-headless-dns-and-pod-response.png](rudray-20261024-023304/01-headless-dns-and-pod-response.png)

## CoreDNS and empty endpoints

CoreDNS had two Ready Pods. Its ConfigMap and logs were inspected; Pod resolver settings pointed to `10.96.0.10`, and the Kubernetes Service FQDN resolved. The empty-endpoints failure showed selector `app=wrong-backend-name` against backend labels `app=yatri-backend`, followed by a failed connection. The selector was patched to `app=yatri-backend`; the Service then populated all three endpoints on port `5000`, and curl returned the backend response.

- [01-coredns-and-empty-endpoints.png](rudray-20261024-043051/01-coredns-and-empty-endpoints.png)
- [02-selector-mismatch-and-failed-curl.png](rudray-20261024-043051/02-selector-mismatch-and-failed-curl.png)

The final troubleshooting capture verifies the repaired selector, three restored endpoints, and successful backend response.

- [01-selector-fixed-and-endpoints-restored.png](rudray-20261024-043513/01-selector-fixed-and-endpoints-restored.png)
