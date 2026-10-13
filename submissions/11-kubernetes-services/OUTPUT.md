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
NAME                TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE   SELECTOR
external-docs       ExternalName   <none>           kubernetes.io                                                             <none>         16m   <none>
homework-backend    ClusterIP      172.20.114.137   <none>                                                                    80/TCP         13m   app=homework-backend
homework-frontend   ClusterIP      172.20.213.198   <none>                                                                    80/TCP         13m   app=homework-frontend
web-clusterip       ClusterIP      172.20.221.62    <none>                                                                    80/TCP         16m   app=service-web
web-headless        ClusterIP      None             <none>                                                                    80/TCP         16m   app=service-web
web-loadbalancer    LoadBalancer   172.20.158.123   afc147309a5ce41248aa0272f3b8e839-278856017.ap-south-1.elb.amazonaws.com   80:32103/TCP   16m   app=service-web
web-nodeport        NodePort       172.20.64.104    <none>                                                                    80:32455/TCP   16m   app=service-web
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get endpointslices -l kubernetes.io/service-name=web-clusterip
NAME                  ADDRESSTYPE   PORTS   ENDPOINTS                 AGE
web-clusterip-svhp7   IPv4          80      10.20.1.206,10.20.2.150   16m
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

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- wget -qO- http://web-clusterip
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
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- wget -qO- http://web-nodeport
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
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- wget -qO- http://web-loadbalancer
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
$ kubectl --context campusfix-eks --request-timeout=30s get nodes -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Node",
            "metadata": {
                "annotations": {
                    "alpha.kubernetes.io/provided-node-ip": "10.20.1.116",
                    "csi.volume.kubernetes.io/nodeid": "{\"ebs.csi.aws.com\":\"i-096b380e79a7e15f1\"}",
                    "node.alpha.kubernetes.io/ttl": "0",
                    "volumes.kubernetes.io/controller-managed-attach-detach": "true"
                },
                "creationTimestamp": "2026-10-13T02:32:18Z",
                "labels": {
                    "beta.kubernetes.io/arch": "amd64",
                    "beta.kubernetes.io/instance-type": "t3.medium",
                    "beta.kubernetes.io/os": "linux",
                    "eks.amazonaws.com/capacityType": "ON_DEMAND",
                    "eks.amazonaws.com/nodegroup": "main-20261013023027045600000010",
                    "eks.amazonaws.com/nodegroup-image": "ami-06d47e8116d74df53",
                    "eks.amazonaws.com/sourceLaunchTemplateId": "lt-0c342f02f8398c6cc",
                    "eks.amazonaws.com/sourceLaunchTemplateVersion": "1",
                    "failure-domain.beta.kubernetes.io/region": "ap-south-1",
                    "failure-domain.beta.kubernetes.io/zone": "ap-south-1a",
                    "k8s.io/cloud-provider-aws": "0ba41e04bb886255ed68795bdbc0fd67",
                    "kubernetes.io/arch": "amd64",
                    "kubernetes.io/hostname": "ip-10-20-1-116.ap-south-1.compute.internal",
                    "kubernetes.io/os": "linux",
                    "node.kubernetes.io/instance-type": "t3.medium",
                    "topology.ebs.csi.aws.com/zone": "ap-south-1a",
                    "topology.k8s.aws/zone-id": "aps1-az1",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "ip-10-20-1-116.ap-south-1.compute.internal",
                "resourceVersion": "15080",
                "uid": "c6fed8fa-8088-48a6-b6a2-57e5ddf56b67"
            },
            "spec": {
                "providerID": "aws:///ap-south-1a/i-096b380e79a7e15f1"
            },
            "status": {
                "addresses": [
                    {
                        "address": "10.20.1.116",
                        "type": "InternalIP"
                    },
                    {
                        "address": "ip-10-20-1-116.ap-south-1.compute.internal",
                        "type": "InternalDNS"
                    },
                    {
                        "address": "ip-10-20-1-116.ap-south-1.compute.internal",
                        "type": "Hostname"
                    }
                ],
                "allocatable": {
                    "cpu": "1930m",
                    "ephemeral-storage": "18181869946",
                    "hugepages-1Gi": "0",
                    "hugepages-2Mi": "0",
                    "memory": "3371528Ki",
                    "pods": "17"
                },
                "capacity": {
                    "cpu": "2",
                    "ephemeral-storage": "20893676Ki",
                    "hugepages-1Gi": "0",
                    "hugepages-2Mi": "0",
                    "memory": "3926536Ki",
                    "pods": "17"
                },
                "conditions": [
                    {
                        "lastHeartbeatTime": "2026-10-13T03:31:00Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has sufficient memory available",
                        "reason": "KubeletHasSufficientMemory",
                        "status": "False",
                        "type": "MemoryPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:31:00Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has no disk pressure",
                        "reason": "KubeletHasNoDiskPressure",
                        "status": "False",
                        "type": "DiskPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:31:00Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has sufficient PID available",
                        "reason": "KubeletHasSufficientPID",
                        "status": "False",
                        "type": "PIDPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:31:00Z",
                        "lastTransitionTime": "2026-10-13T02:32:29Z",
                        "message": "kubelet is posting ready status",
                        "reason": "KubeletReady",
                        "status": "True",
                        "type": "Ready"
                    }
                ],
                "daemonEndpoints": {
                    "kubeletEndpoint": {
                        "Port": 10250
                    }
                },
                "features": {
                    "supplementalGroupsPolicy": true
                },
                "images": [
                    {
                        "names": [
                            "registry.k8s.io/ingress-nginx/controller@sha256:594ceea76b01c592858f803f9ff4d2cb40542cae2060410b2c95f75907d659e1"
                        ],
                        "sizeBytes": 115975561
                    },
                    {
                        "names": [
                            "quay.io/prometheus/prometheus@sha256:b2a413d5a03ea6a76782a508d1c7947440bba3b973931a25676e278431891b01",
                            "quay.io/prometheus/prometheus:v3.15.0-distroless"
                        ],
                        "sizeBytes": 113793870
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni-init@sha256:57866ee72791f6564a316a8e9ad5df0737200f64cbfcbf6ad4153b5bc80f4fb6",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni-init:v1.22.4-eksbuild.3"
                        ],
                        "sizeBytes": 69724381
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni@sha256:7ba0bb50de053432467d1cc629dfc846de4e534f00b73828a1ff33fcee70c8e7",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni:v1.22.4-eksbuild.3"
                        ],
                        "sizeBytes": 57915596
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-provisioner@sha256:344672a6d3a794c1fb8eea8b586c66cac3f1936341aa9c8e222dcd85e7c039be",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-provisioner:v6.3.0-eksbuild.7"
                        ],
                        "sizeBytes": 42745381
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-snapshotter@sha256:1a0c4c40c14e632ab8fd1eba0e2d1363089bf11e4207461c4cc4285c81afceaf",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-snapshotter:v8.6.0-eksbuild.8"
                        ],
                        "sizeBytes": 40766717
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-resizer@sha256:3e9480a608a19f903541ab91e44b2c2e4da7b45dece01601630fc837425c2a81",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-resizer:v2.2.1-eksbuild.6"
                        ],
                        "sizeBytes": 40518352
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-attacher@sha256:f12da9edb687581e282e7e2a9ad34fa3a542f6c23610d06820da0802291d76ff",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-attacher:v4.12.0-eksbuild.8"
                        ],
                        "sizeBytes": 40511344
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/aws-ebs-csi-driver@sha256:e2564165048c1706a4c64a648d982c974bd07280ab27c7cce4b6c7906afb0c5d",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/aws-ebs-csi-driver:v1.66.0"
                        ],
                        "sizeBytes": 36722260
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon/aws-network-policy-agent@sha256:c8555b6f2aed6d795a1637e0fe7f1f47cca2465354438157bdc8d8a6beb61045",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon/aws-network-policy-agent:v1.4.0-eksbuild.1"
                        ],
                        "sizeBytes": 33957519
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/kube-proxy@sha256:da92e0b7ab61a4959a73b63ab1bddbca69533d591e9a6f1258f60cd193ada9de",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/kube-proxy:v1.35.3-eksbuild.29"
                        ],
                        "sizeBytes": 31964133
                    },
                    {
                        "names": [
                            "registry.k8s.io/ingress-nginx/kube-webhook-certgen@sha256:01038e7de14b78d702d2849c3aad72fd25903c4765af63cf16aa3398f5d5f2dd"
                        ],
                        "sizeBytes": 26543532
                    },
                    {
                        "names": [
                            "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                            "docker.io/library/nginx:1.28-alpine"
                        ],
                        "sizeBytes": 25976042
                    },
                    {
                        "names": [
                            "quay.io/prometheus-operator/prometheus-operator@sha256:7c88d4e7bae63bd8d0f8da986054337c23b4472fa8d3c6817f5bc4b8407a2d6a",
                            "quay.io/prometheus-operator/prometheus-operator:v0.94.1"
                        ],
                        "sizeBytes": 22572616
                    },
                    {
                        "names": [
                            "docker.io/library/nginx@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10",
                            "docker.io/library/nginx:1.27-alpine"
                        ],
                        "sizeBytes": 20984244
                    },
                    {
                        "names": [
                            "docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4",
                            "docker.io/library/python:3.12-alpine"
                        ],
                        "sizeBytes": 20643193
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/livenessprobe@sha256:2ec65c594fe3283d4376697a8c05a832391d5e4403bc5142617cb9d7004d54c5",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/livenessprobe:v2.19.0-eksbuild.7"
                        ],
                        "sizeBytes": 17696607
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-node-driver-registrar@sha256:8222182e244554a46ac820b6e99a841b4b50c43e6524ea55e3669462564cc0a1",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-node-driver-registrar:v2.17.0-eksbuild.7"
                        ],
                        "sizeBytes": 17558434
                    },
                    {
                        "names": [
                            "quay.io/prometheus-operator/prometheus-config-reloader@sha256:06b52bd4dbe3ed6dd5905aadaf8b9987d9da4c31d37bb86deaadae68cee2d26b",
                            "quay.io/prometheus-operator/prometheus-config-reloader:v0.94.1"
                        ],
                        "sizeBytes": 14893664
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.us-west-2.amazonaws.com/eks/pause:3.10",
                            "localhost/kubernetes/pause:latest"
                        ],
                        "sizeBytes": 318731
                    }
                ],
                "nodeInfo": {
                    "architecture": "amd64",
                    "bootID": "1f4855f7-5ed0-4dbc-8a9e-ff5318701c81",
                    "containerRuntimeVersion": "containerd://2.2.7+unknown",
                    "kernelVersion": "6.12.110-135.202.amzn2023.x86_64",
                    "kubeProxyVersion": "",
                    "kubeletVersion": "v1.35.8-eks-3b4a6ca",
                    "machineID": "ec254c613bcfbaa1f5991dbb7fdf9dd7",
                    "operatingSystem": "linux",
                    "osImage": "Amazon Linux 2023.12.20260930",
                    "systemUUID": "ec254c61-3bcf-baa1-f599-1dbb7fdf9dd7"
                },
                "runtimeHandlers": [
                    {
                        "features": {
                            "recursiveReadOnlyMounts": true,
                            "userNamespaces": true
                        },
                        "name": ""
                    },
                    {
                        "features": {
                            "recursiveReadOnlyMounts": true,
                            "userNamespaces": true
                        },
                        "name": "runc"
                    }
                ]
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Node",
            "metadata": {
                "annotations": {
                    "alpha.kubernetes.io/provided-node-ip": "10.20.2.64",
                    "csi.volume.kubernetes.io/nodeid": "{\"ebs.csi.aws.com\":\"i-08a35a8a3aec48622\"}",
                    "node.alpha.kubernetes.io/ttl": "0",
                    "volumes.kubernetes.io/controller-managed-attach-detach": "true"
                },
                "creationTimestamp": "2026-10-13T02:32:15Z",
                "labels": {
                    "beta.kubernetes.io/arch": "amd64",
                    "beta.kubernetes.io/instance-type": "t3.medium",
                    "beta.kubernetes.io/os": "linux",
                    "eks.amazonaws.com/capacityType": "ON_DEMAND",
                    "eks.amazonaws.com/nodegroup": "main-20261013023027045600000010",
                    "eks.amazonaws.com/nodegroup-image": "ami-06d47e8116d74df53",
                    "eks.amazonaws.com/sourceLaunchTemplateId": "lt-0c342f02f8398c6cc",
                    "eks.amazonaws.com/sourceLaunchTemplateVersion": "1",
                    "failure-domain.beta.kubernetes.io/region": "ap-south-1",
                    "failure-domain.beta.kubernetes.io/zone": "ap-south-1b",
                    "k8s.io/cloud-provider-aws": "0ba41e04bb886255ed68795bdbc0fd67",
                    "kubernetes.io/arch": "amd64",
                    "kubernetes.io/hostname": "ip-10-20-2-64.ap-south-1.compute.internal",
                    "kubernetes.io/os": "linux",
                    "node.kubernetes.io/instance-type": "t3.medium",
                    "topology.ebs.csi.aws.com/zone": "ap-south-1b",
                    "topology.k8s.aws/zone-id": "aps1-az3",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1b"
                },
                "name": "ip-10-20-2-64.ap-south-1.compute.internal",
                "resourceVersion": "15962",
                "uid": "7de7ae63-75ac-4543-87f7-b60b56888f3c"
            },
            "spec": {
                "providerID": "aws:///ap-south-1b/i-08a35a8a3aec48622"
            },
            "status": {
                "addresses": [
                    {
                        "address": "10.20.2.64",
                        "type": "InternalIP"
                    },
                    {
                        "address": "ip-10-20-2-64.ap-south-1.compute.internal",
                        "type": "InternalDNS"
                    },
                    {
                        "address": "ip-10-20-2-64.ap-south-1.compute.internal",
                        "type": "Hostname"
                    }
                ],
                "allocatable": {
                    "cpu": "1930m",
                    "ephemeral-storage": "18181869946",
                    "hugepages-1Gi": "0",
                    "hugepages-2Mi": "0",
                    "memory": "3371532Ki",
                    "pods": "17"
                },
                "capacity": {
                    "cpu": "2",
                    "ephemeral-storage": "20893676Ki",
                    "hugepages-1Gi": "0",
                    "hugepages-2Mi": "0",
                    "memory": "3926540Ki",
                    "pods": "17"
                },
                "conditions": [
                    {
                        "lastHeartbeatTime": "2026-10-13T03:34:49Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has sufficient memory available",
                        "reason": "KubeletHasSufficientMemory",
                        "status": "False",
                        "type": "MemoryPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:34:49Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has no disk pressure",
                        "reason": "KubeletHasNoDiskPressure",
                        "status": "False",
                        "type": "DiskPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:34:49Z",
                        "lastTransitionTime": "2026-10-13T02:32:12Z",
                        "message": "kubelet has sufficient PID available",
                        "reason": "KubeletHasSufficientPID",
                        "status": "False",
                        "type": "PIDPressure"
                    },
                    {
                        "lastHeartbeatTime": "2026-10-13T03:34:49Z",
                        "lastTransitionTime": "2026-10-13T02:32:25Z",
                        "message": "kubelet is posting ready status",
                        "reason": "KubeletReady",
                        "status": "True",
                        "type": "Ready"
                    }
                ],
                "daemonEndpoints": {
                    "kubeletEndpoint": {
                        "Port": 10250
                    }
                },
                "features": {
                    "supplementalGroupsPolicy": true
                },
                "images": [
                    {
                        "names": [
                            "docker.io/grafana/grafana@sha256:202e5d5b3f8499e70ccac7991eea6d7da72d2790eb2e0597e7987acf724e7180",
                            "docker.io/grafana/grafana:13.2.3-distroless"
                        ],
                        "sizeBytes": 463753316
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni-init@sha256:57866ee72791f6564a316a8e9ad5df0737200f64cbfcbf6ad4153b5bc80f4fb6",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni-init:v1.22.4-eksbuild.3"
                        ],
                        "sizeBytes": 69724381
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni@sha256:7ba0bb50de053432467d1cc629dfc846de4e534f00b73828a1ff33fcee70c8e7",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon-k8s-cni:v1.22.4-eksbuild.3"
                        ],
                        "sizeBytes": 57915596
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-provisioner@sha256:344672a6d3a794c1fb8eea8b586c66cac3f1936341aa9c8e222dcd85e7c039be",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-provisioner:v6.3.0-eksbuild.7"
                        ],
                        "sizeBytes": 42745381
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-snapshotter@sha256:1a0c4c40c14e632ab8fd1eba0e2d1363089bf11e4207461c4cc4285c81afceaf",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-snapshotter:v8.6.0-eksbuild.8"
                        ],
                        "sizeBytes": 40766717
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-resizer@sha256:3e9480a608a19f903541ab91e44b2c2e4da7b45dece01601630fc837425c2a81",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-resizer:v2.2.1-eksbuild.6"
                        ],
                        "sizeBytes": 40518352
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-attacher@sha256:f12da9edb687581e282e7e2a9ad34fa3a542f6c23610d06820da0802291d76ff",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-attacher:v4.12.0-eksbuild.8"
                        ],
                        "sizeBytes": 40511344
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/aws-ebs-csi-driver@sha256:e2564165048c1706a4c64a648d982c974bd07280ab27c7cce4b6c7906afb0c5d",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/aws-ebs-csi-driver:v1.66.0"
                        ],
                        "sizeBytes": 36722260
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon/aws-network-policy-agent@sha256:c8555b6f2aed6d795a1637e0fe7f1f47cca2465354438157bdc8d8a6beb61045",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/amazon/aws-network-policy-agent:v1.4.0-eksbuild.1"
                        ],
                        "sizeBytes": 33957519
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/kube-proxy@sha256:da92e0b7ab61a4959a73b63ab1bddbca69533d591e9a6f1258f60cd193ada9de",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/kube-proxy:v1.35.3-eksbuild.29"
                        ],
                        "sizeBytes": 31964133
                    },
                    {
                        "names": [
                            "quay.io/kiwigrid/k8s-sidecar@sha256:092dbe0c335fba9af414a27630ca68f34df6185784fa847d9954187e69dbfdd7",
                            "quay.io/kiwigrid/k8s-sidecar:2.14.1"
                        ],
                        "sizeBytes": 29200776
                    },
                    {
                        "names": [
                            "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                            "docker.io/library/nginx:1.28-alpine"
                        ],
                        "sizeBytes": 25976042
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/coredns@sha256:7d706ec4be5c8acff3802dfdd70aa23e7875efee5cbb3130c2dcef77a2a1fd05",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/coredns:v1.13.2-eksbuild.50"
                        ],
                        "sizeBytes": 25614614
                    },
                    {
                        "names": [
                            "registry.k8s.io/metrics-server/metrics-server@sha256:d9862115e7c7881280d3d75ca26bda8ffc0fc213315979575bf23ce9826205c0",
                            "registry.k8s.io/metrics-server/metrics-server:v0.9.0"
                        ],
                        "sizeBytes": 23258428
                    },
                    {
                        "names": [
                            "docker.io/library/nginx@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10",
                            "docker.io/library/nginx:1.27-alpine"
                        ],
                        "sizeBytes": 20984244
                    },
                    {
                        "names": [
                            "docker.io/library/python@sha256:1b668429b3511ab407d8e00648891631b0b1a4d7e15e3ca70f38ab5b91ad4ab4",
                            "docker.io/library/python:3.12-alpine"
                        ],
                        "sizeBytes": 20643193
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/livenessprobe@sha256:2ec65c594fe3283d4376697a8c05a832391d5e4403bc5142617cb9d7004d54c5",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/livenessprobe:v2.19.0-eksbuild.7"
                        ],
                        "sizeBytes": 17696607
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-node-driver-registrar@sha256:8222182e244554a46ac820b6e99a841b4b50c43e6524ea55e3669462564cc0a1",
                            "602401143452.dkr.ecr.ap-south-1.amazonaws.com/eks/csi-node-driver-registrar:v2.17.0-eksbuild.7"
                        ],
                        "sizeBytes": 17558434
                    },
                    {
                        "names": [
                            "ghcr.io/jkroepke/kube-webhook-certgen@sha256:58e4ac2e15bf7785eb00ac90d03f9be1ff3f2fe0add6c71b54af6e5c80031148",
                            "ghcr.io/jkroepke/kube-webhook-certgen:1.8.9"
                        ],
                        "sizeBytes": 9485580
                    },
                    {
                        "names": [
                            "docker.io/library/busybox@sha256:bdf57e528e45e4433820e045b29b4597825a1c9e38353532d90a01445013f82e",
                            "docker.io/library/busybox:1.37"
                        ],
                        "sizeBytes": 2222118
                    },
                    {
                        "names": [
                            "602401143452.dkr.ecr.us-west-2.amazonaws.com/eks/pause:3.10",
                            "localhost/kubernetes/pause:latest"
                        ],
                        "sizeBytes": 318731
                    }
                ],
                "nodeInfo": {
                    "architecture": "amd64",
                    "bootID": "b039e132-8586-4d71-b0fa-80a943150d2e",
                    "containerRuntimeVersion": "containerd://2.2.7+unknown",
                    "kernelVersion": "6.12.110-135.202.amzn2023.x86_64",
                    "kubeProxyVersion": "",
                    "kubeletVersion": "v1.35.8-eks-3b4a6ca",
                    "machineID": "ec26061fe8ca5386223713727e9a9954",
                    "operatingSystem": "linux",
                    "osImage": "Amazon Linux 2023.12.20260930",
                    "systemUUID": "ec26061f-e8ca-5386-2237-13727e9a9954"
                },
                "runtimeHandlers": [
                    {
                        "features": {
                            "recursiveReadOnlyMounts": true,
                            "userNamespaces": true
                        },
                        "name": ""
                    },
                    {
                        "features": {
                            "recursiveReadOnlyMounts": true,
                            "userNamespaces": true
                        },
                        "name": "runc"
                    }
                ]
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get service web-nodeport -o 'jsonpath={.spec.ports[0].nodePort}'
32455[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec network-client -- wget -qO- http://10.20.1.116:32455
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
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw patch service web-clusterip --type=merge -p '{"spec":{"selector":{"app":"no-such-app"}}}'
service/web-clusterip patched
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get endpointslices -l kubernetes.io/service-name=web-clusterip -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "addressType": "IPv4",
            "apiVersion": "discovery.k8s.io/v1",
            "endpoints": null,
            "kind": "EndpointSlice",
            "metadata": {
                "creationTimestamp": "2026-10-13T03:18:01Z",
                "generateName": "web-clusterip-",
                "generation": 6,
                "labels": {
                    "endpointslice.kubernetes.io/managed-by": "endpointslice-controller.k8s.io",
                    "kubernetes.io/service-name": "web-clusterip"
                },
                "name": "web-clusterip-svhp7",
                "namespace": "rudray-devops-hw",
                "ownerReferences": [
                    {
                        "apiVersion": "v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "Service",
                        "name": "web-clusterip",
                        "uid": "5ffa246e-158e-4bbc-9ff6-d9d09ad6f054"
                    }
                ],
                "resourceVersion": "16025",
                "uid": "b5b635af-14b2-4294-99b8-c951fc545f98"
            },
            "ports": null
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/11-kubernetes-services/services.yaml
deployment.apps/service-web unchanged
service/web-clusterip configured
service/web-nodeport unchanged
service/web-loadbalancer unchanged
service/external-docs unchanged
service/web-headless unchanged
pod/network-client unchanged
[exit status: 0]
```

All checks in this topic completed successfully.
