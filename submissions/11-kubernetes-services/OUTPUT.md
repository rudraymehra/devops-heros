# Executed Kubernetes lab output

Context: `campusfix-eks`. Namespace: `rudray-devops-hw`.

```console
$ kubectl --context campusfix-eks --request-timeout=30s apply -f submissions/09-kubernetes-fundamentals/namespace.yaml
namespace/rudray-devops-hw unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/11-kubernetes-services/services.yaml
deployment.apps/service-web unchanged
service/web-clusterip unchanged
service/web-nodeport unchanged
service/web-loadbalancer unchanged
service/external-docs unchanged
service/web-headless unchanged
pod/network-client unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/service-web --timeout=180s
deployment "service-web" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw wait --for=condition=Ready pod/network-client --timeout=180s
pod/network-client condition met
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get services -o wide
NAME               TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE   SELECTOR
external-docs      ExternalName   <none>           kubernetes.io                                                             <none>         74s   <none>
web-clusterip      ClusterIP      172.20.221.62    <none>                                                                    80/TCP         74s   app=service-web
web-headless       ClusterIP      None             <none>                                                                    80/TCP         74s   app=service-web
web-loadbalancer   LoadBalancer   172.20.158.123   afc147309a5ce41248aa0272f3b8e839-278856017.ap-south-1.elb.amazonaws.com   80:32103/TCP   74s   app=service-web
web-nodeport       NodePort       172.20.64.104    <none>                                                                    80:32455/TCP   74s   app=service-web
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get endpointslices -l kubernetes.io/service-name=web-clusterip
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                 AGE
web-clusterip-svhp7   IPv4          80      10.20.1.206,10.20.2.150   75s
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- nslookup -type=A web-clusterip.rudray-devops-hw.svc.cluster.local.
Server:		172.20.0.10
Address:	172.20.0.10:53

Name:	web-clusterip.rudray-devops-hw.svc.cluster.local
Address: 172.20.221.62

[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- nslookup -type=A web-headless.rudray-devops-hw.svc.cluster.local.
Server:		172.20.0.10
Address:	172.20.0.10:53

Name:	web-headless.rudray-devops-hw.svc.cluster.local
Address: 10.20.2.150
Name:	web-headless.rudray-devops-hw.svc.cluster.local
Address: 10.20.1.206

[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- nslookup -type=A external-docs.rudray-devops-hw.svc.cluster.local.
Server:		172.20.0.10
Address:	172.20.0.10:53

external-docs.rudray-devops-hw.svc.cluster.local	canonical name = kubernetes.io
Name:	kubernetes.io
Address: 15.197.167.90
Name:	kubernetes.io
Address: 3.33.186.135

[exit status: 0]
```

