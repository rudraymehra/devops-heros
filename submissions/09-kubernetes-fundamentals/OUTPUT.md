# Executed Kubernetes lab output

Context: `campusfix-eks`. Namespace: `rudray-devops-hw`.

```console
$ kubectl --context campusfix-eks --request-timeout=30s version --client
Client Version: v1.37.0
Kustomize Version: v5.8.1
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s cluster-info
Kubernetes control plane is running at https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com
CoreDNS is running at https://C8FE139F4147098CE5611530B3ADF3F5.gr7.ap-south-1.eks.amazonaws.com/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s get nodes -o wide
NAME                                         STATUS   ROLES    AGE   VERSION               INTERNAL-IP   EXTERNAL-IP   OS-IMAGE                        KERNEL-VERSION                     CONTAINER-RUNTIME
ip-10-20-1-116.ap-south-1.compute.internal   Ready    <none>   44m   v1.35.8-eks-3b4a6ca   10.20.1.116   <none>        Amazon Linux 2023.12.20260930   6.12.110-135.202.amzn2023.x86_64   containerd://2.2.7+unknown
ip-10-20-2-64.ap-south-1.compute.internal    Ready    <none>   44m   v1.35.8-eks-3b4a6ca   10.20.2.64    <none>        Amazon Linux 2023.12.20260930   6.12.110-135.202.amzn2023.x86_64   containerd://2.2.7+unknown
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s get pods -n kube-system
NAME                                 READY   STATUS    RESTARTS   AGE
aws-node-k9d4x                       2/2     Running   0          44m
aws-node-tksqv                       2/2     Running   0          44m
coredns-bf6759cdf-5qgzw              1/1     Running   0          49m
coredns-bf6759cdf-trvlr              1/1     Running   0          49m
ebs-csi-controller-d8875c947-skvdk   6/6     Running   0          44m
ebs-csi-controller-d8875c947-v67bm   6/6     Running   0          44m
ebs-csi-node-295dq                   3/3     Running   0          44m
ebs-csi-node-txmxq                   3/3     Running   0          44m
kube-proxy-8j5jp                     1/1     Running   0          44m
kube-proxy-schvb                     1/1     Running   0          44m
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/09-kubernetes-fundamentals/namespace.yaml
namespace/rudray-devops-hw created
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/09-kubernetes-fundamentals/pod.yaml
pod/hello-kubernetes created
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw wait --for=condition=Ready pod/hello-kubernetes --timeout=180s
pod/hello-kubernetes condition met
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pod hello-kubernetes -o wide
NAME               READY   STATUS    RESTARTS   AGE   IP           NODE                                         NOMINATED NODE   READINESS GATES
hello-kubernetes   1/1     Running   0          8s    10.20.1.53   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec hello-kubernetes -- wget -qO- http://127.0.0.1
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw logs hello-kubernetes --tail=10
2026/10/13 03:17:22 [notice] 1#1: using the "epoll" event method
2026/10/13 03:17:22 [notice] 1#1: nginx/1.28.3
2026/10/13 03:17:22 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/10/13 03:17:22 [notice] 1#1: OS: Linux 6.12.110-135.202.amzn2023.x86_64
2026/10/13 03:17:22 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 65536:1048576
2026/10/13 03:17:22 [notice] 1#1: start worker processes
2026/10/13 03:17:22 [notice] 1#1: start worker process 31
2026/10/13 03:17:22 [notice] 1#1: start worker process 32
10.20.1.116 - - [13/Oct/2026:03:17:23 +0000] "GET / HTTP/1.1" 200 615 "-" "kube-probe/1.35" "-"
127.0.0.1 - - [13/Oct/2026:03:17:25 +0000] "GET / HTTP/1.1" 200 615 "-" "Wget" "-"
[exit status: 0]
```

All checks in this topic completed successfully.
