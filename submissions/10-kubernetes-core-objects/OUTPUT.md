# Executed Kubernetes lab output

Context: `campusfix-eks`. Namespace: `rudray-devops-hw`.

```console
$ kubectl --context campusfix-eks --request-timeout=30s apply -f submissions/09-kubernetes-fundamentals/namespace.yaml
namespace/rudray-devops-hw unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/10-kubernetes-core-objects/objects.yaml
pod/standalone-web created
replicaset.apps/replica-web created
deployment.apps/deployment-web created
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw wait --for=condition=Ready pod/standalone-web --timeout=180s
pod/standalone-web condition met
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw wait --for=condition=Ready pod -l app=replica-web --timeout=180s
pod/replica-web-bhmrf condition met
pod/replica-web-jbkvj condition met
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/deployment-web --timeout=180s
Waiting for deployment "deployment-web" rollout to finish: 0 of 2 updated replicas are available...
Waiting for deployment "deployment-web" rollout to finish: 1 of 2 updated replicas are available...
deployment "deployment-web" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pods,replicasets,deployments -o wide
NAME                                  READY   STATUS    RESTARTS   AGE   IP            NODE                                         NOMINATED NODE   READINESS GATES
pod/deployment-web-858f686f95-9fk56   1/1     Running   0          7s    10.20.2.198   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/deployment-web-858f686f95-b2qt7   1/1     Running   0          7s    10.20.1.70    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/hello-kubernetes                  1/1     Running   0          20s   10.20.1.53    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/replica-web-bhmrf                 1/1     Running   0          7s    10.20.2.204   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/replica-web-jbkvj                 1/1     Running   0          7s    10.20.1.225   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/standalone-web                    1/1     Running   0          8s    10.20.1.15    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>

NAME                                        DESIRED   CURRENT   READY   AGE   CONTAINERS   IMAGES              SELECTOR
replicaset.apps/deployment-web-858f686f95   2         2         2       7s    nginx        nginx:1.27-alpine   app=deployment-web,pod-template-hash=858f686f95
replicaset.apps/replica-web                 2         2         2       8s    nginx        nginx:1.28-alpine   app=replica-web

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES              SELECTOR
deployment.apps/deployment-web   2/2     2            2           7s    nginx        nginx:1.27-alpine   app=deployment-web
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pods -l app=replica-web -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2026-10-13T03:17:29Z",
                "generateName": "replica-web-",
                "generation": 1,
                "labels": {
                    "app": "replica-web",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1b"
                },
                "name": "replica-web-bhmrf",
                "namespace": "rudray-devops-hw",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "replica-web",
                        "uid": "42b62083-5833-4e2a-94ac-19e6fc66fb5e"
                    }
                ],
                "resourceVersion": "11335",
                "uid": "d50d523f-244b-4742-9815-f30360be8cf7"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:1.28-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "nginx",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6z87",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "nodeName": "ip-10-20-2-64.ap-south-1.compute.internal",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "default",
                "serviceAccountName": "default",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-l6z87",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:34Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:34Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "allocatedResources": {
                            "cpu": "25m",
                            "memory": "32Mi"
                        },
                        "containerID": "containerd://2a9a4dc5e2c8783f55f0c6ab8ac0a717e1f582093103fa503ca25dfa41d2b0fc",
                        "image": "docker.io/library/nginx:1.28-alpine",
                        "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                        "lastState": {},
                        "name": "nginx",
                        "ready": true,
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:17:34Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 0,
                                "supplementalGroups": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    6,
                                    10,
                                    11,
                                    20,
                                    26,
                                    27
                                ],
                                "uid": 0
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6z87",
                                "readOnly": true,
                                "recursiveReadOnly": "Disabled"
                            }
                        ]
                    }
                ],
                "hostIP": "10.20.2.64",
                "hostIPs": [
                    {
                        "ip": "10.20.2.64"
                    }
                ],
                "observedGeneration": 1,
                "phase": "Running",
                "podIP": "10.20.2.204",
                "podIPs": [
                    {
                        "ip": "10.20.2.204"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:17:29Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2026-10-13T03:17:29Z",
                "generateName": "replica-web-",
                "generation": 1,
                "labels": {
                    "app": "replica-web",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "replica-web-jbkvj",
                "namespace": "rudray-devops-hw",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "replica-web",
                        "uid": "42b62083-5833-4e2a-94ac-19e6fc66fb5e"
                    }
                ],
                "resourceVersion": "11310",
                "uid": "ed1526ad-6a2f-47b8-a1f9-464922c3a54e"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:1.28-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "nginx",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-g8dhf",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "nodeName": "ip-10-20-1-116.ap-south-1.compute.internal",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "default",
                "serviceAccountName": "default",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-g8dhf",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:30Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:30Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "allocatedResources": {
                            "cpu": "25m",
                            "memory": "32Mi"
                        },
                        "containerID": "containerd://fc80efe8aaf25d724fe4bfd3d34a0962f04cf38017bfb1ac0d2cace139c4064b",
                        "image": "docker.io/library/nginx:1.28-alpine",
                        "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                        "lastState": {},
                        "name": "nginx",
                        "ready": true,
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:17:29Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 0,
                                "supplementalGroups": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    6,
                                    10,
                                    11,
                                    20,
                                    26,
                                    27
                                ],
                                "uid": 0
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-g8dhf",
                                "readOnly": true,
                                "recursiveReadOnly": "Disabled"
                            }
                        ]
                    }
                ],
                "hostIP": "10.20.1.116",
                "hostIPs": [
                    {
                        "ip": "10.20.1.116"
                    }
                ],
                "observedGeneration": 1,
                "phase": "Running",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:17:29Z"
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
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw delete pod replica-web-bhmrf --wait=true
pod "replica-web-bhmrf" deleted from rudray-devops-hw namespace
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pods -l app=replica-web -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2026-10-13T03:17:37Z",
                "generateName": "replica-web-",
                "generation": 1,
                "labels": {
                    "app": "replica-web",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1b"
                },
                "name": "replica-web-cb7zx",
                "namespace": "rudray-devops-hw",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "replica-web",
                        "uid": "42b62083-5833-4e2a-94ac-19e6fc66fb5e"
                    }
                ],
                "resourceVersion": "11390",
                "uid": "6d427233-2def-4207-960b-7a837e89b2ff"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:1.28-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "nginx",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-f2srf",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "nodeName": "ip-10-20-2-64.ap-south-1.compute.internal",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "default",
                "serviceAccountName": "default",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-f2srf",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:38Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:37Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:38Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:38Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:37Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "allocatedResources": {
                            "cpu": "25m",
                            "memory": "32Mi"
                        },
                        "containerID": "containerd://52fc046ec0767c8037340ff2b7b2d7e880ce0a37e8990dd6917fd153b670d472",
                        "image": "docker.io/library/nginx:1.28-alpine",
                        "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                        "lastState": {},
                        "name": "nginx",
                        "ready": true,
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:17:38Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 0,
                                "supplementalGroups": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    6,
                                    10,
                                    11,
                                    20,
                                    26,
                                    27
                                ],
                                "uid": 0
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-f2srf",
                                "readOnly": true,
                                "recursiveReadOnly": "Disabled"
                            }
                        ]
                    }
                ],
                "hostIP": "10.20.2.64",
                "hostIPs": [
                    {
                        "ip": "10.20.2.64"
                    }
                ],
                "observedGeneration": 1,
                "phase": "Running",
                "podIP": "10.20.2.55",
                "podIPs": [
                    {
                        "ip": "10.20.2.55"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:17:37Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "creationTimestamp": "2026-10-13T03:17:29Z",
                "generateName": "replica-web-",
                "generation": 1,
                "labels": {
                    "app": "replica-web",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "replica-web-jbkvj",
                "namespace": "rudray-devops-hw",
                "ownerReferences": [
                    {
                        "apiVersion": "apps/v1",
                        "blockOwnerDeletion": true,
                        "controller": true,
                        "kind": "ReplicaSet",
                        "name": "replica-web",
                        "uid": "42b62083-5833-4e2a-94ac-19e6fc66fb5e"
                    }
                ],
                "resourceVersion": "11310",
                "uid": "ed1526ad-6a2f-47b8-a1f9-464922c3a54e"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:1.28-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "nginx",
                        "ports": [
                            {
                                "containerPort": 80,
                                "protocol": "TCP"
                            }
                        ],
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-g8dhf",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
                "nodeName": "ip-10-20-1-116.ap-south-1.compute.internal",
                "preemptionPolicy": "PreemptLowerPriority",
                "priority": 0,
                "restartPolicy": "Always",
                "schedulerName": "default-scheduler",
                "securityContext": {},
                "serviceAccount": "default",
                "serviceAccountName": "default",
                "terminationGracePeriodSeconds": 30,
                "tolerations": [
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/not-ready",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    },
                    {
                        "effect": "NoExecute",
                        "key": "node.kubernetes.io/unreachable",
                        "operator": "Exists",
                        "tolerationSeconds": 300
                    }
                ],
                "volumes": [
                    {
                        "name": "kube-api-access-g8dhf",
                        "projected": {
                            "defaultMode": 420,
                            "sources": [
                                {
                                    "serviceAccountToken": {
                                        "expirationSeconds": 3607,
                                        "path": "token"
                                    }
                                },
                                {
                                    "configMap": {
                                        "items": [
                                            {
                                                "key": "ca.crt",
                                                "path": "ca.crt"
                                            }
                                        ],
                                        "name": "kube-root-ca.crt"
                                    }
                                },
                                {
                                    "downwardAPI": {
                                        "items": [
                                            {
                                                "fieldRef": {
                                                    "apiVersion": "v1",
                                                    "fieldPath": "metadata.namespace"
                                                },
                                                "path": "namespace"
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                ]
            },
            "status": {
                "conditions": [
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:30Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:30Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:17:29Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "allocatedResources": {
                            "cpu": "25m",
                            "memory": "32Mi"
                        },
                        "containerID": "containerd://fc80efe8aaf25d724fe4bfd3d34a0962f04cf38017bfb1ac0d2cace139c4064b",
                        "image": "docker.io/library/nginx:1.28-alpine",
                        "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                        "lastState": {},
                        "name": "nginx",
                        "ready": true,
                        "resources": {
                            "limits": {
                                "cpu": "100m",
                                "memory": "64Mi"
                            },
                            "requests": {
                                "cpu": "25m",
                                "memory": "32Mi"
                            }
                        },
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:17:29Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 0,
                                "supplementalGroups": [
                                    0,
                                    1,
                                    2,
                                    3,
                                    4,
                                    6,
                                    10,
                                    11,
                                    20,
                                    26,
                                    27
                                ],
                                "uid": 0
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-g8dhf",
                                "readOnly": true,
                                "recursiveReadOnly": "Disabled"
                            }
                        ]
                    }
                ],
                "hostIP": "10.20.1.116",
                "hostIPs": [
                    {
                        "ip": "10.20.1.116"
                    }
                ],
                "observedGeneration": 1,
                "phase": "Running",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:17:29Z"
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
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw wait --for=condition=Ready pod -l app=replica-web --timeout=180s
pod/replica-web-cb7zx condition met
pod/replica-web-jbkvj condition met
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pods -l app=replica-web -o wide
NAME                READY   STATUS    RESTARTS   AGE   IP            NODE                                         NOMINATED NODE   READINESS GATES
replica-web-cb7zx   1/1     Running   0          3s    10.20.2.55    ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
replica-web-jbkvj   1/1     Running   0          11s   10.20.1.225   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw scale deployment/deployment-web --replicas=3
deployment.apps/deployment-web scaled
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/deployment-web --timeout=180s
Waiting for deployment "deployment-web" rollout to finish: 2 of 3 updated replicas are available...
deployment "deployment-web" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw set image deployment/deployment-web nginx=nginx:1.28-alpine
deployment.apps/deployment-web image updated
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/deployment-web --timeout=180s
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
deployment "deployment-web" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout history deployment/deployment-web
deployment.apps/deployment-web 
REVISION  CHANGE-CAUSE
1         <none>
2         <none>

[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout undo deployment/deployment-web
Warning: resource deployments/deployment-web was previously managed with 'kubectl apply'. Rolling back will not update the kubectl.kubernetes.io/last-applied-configuration annotation, which may cause unexpected behavior on future 'kubectl apply' operations. Consider using 'kubectl apply' with your previous configuration file instead.
deployment.apps/deployment-web rolled back
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/deployment-web --timeout=180s
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 2 out of 3 new replicas have been updated...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
Waiting for deployment "deployment-web" rollout to finish: 1 old replicas are pending termination...
deployment "deployment-web" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get deployment deployment-web -o 'jsonpath={.spec.template.spec.containers[0].image}'
nginx:1.27-alpine[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get pods,rs,deployments
NAME                                  READY   STATUS    RESTARTS   AGE
pod/deployment-web-858f686f95-9vlkq   1/1     Running   0          8s
pod/deployment-web-858f686f95-qndwh   1/1     Running   0          6s
pod/deployment-web-858f686f95-r5h4r   1/1     Running   0          4s
pod/hello-kubernetes                  1/1     Running   0          43s
pod/replica-web-cb7zx                 1/1     Running   0          22s
pod/replica-web-jbkvj                 1/1     Running   0          30s
pod/standalone-web                    1/1     Running   0          31s

NAME                                        DESIRED   CURRENT   READY   AGE
replicaset.apps/deployment-web-84b596885b   0         0         0       15s
replicaset.apps/deployment-web-858f686f95   3         3         3       30s
replicaset.apps/replica-web                 2         2         2       31s

NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deployment-web   3/3     3            3           30s
[exit status: 0]
```

All checks in this topic completed successfully.
