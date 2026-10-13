# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:57:31.084602+00:00

Working directory: .

```text
$ uv run --with pyyaml python scripts/run-advanced-kubernetes.py --context campusfix-eks --topic troubleshooting
$ kubectl --context campusfix-eks --request-timeout=30s create namespace campusfix-troubleshooting
namespace/campusfix-troubleshooting created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting create deployment dns-target --image=nginx:1.28-alpine
deployment.apps/dns-target created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting expose deployment dns-target --port=80
service/dns-target exposed
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting rollout status deployment/dns-target --timeout=180s
deployment "dns-target" successfully rolled out
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f /private/tmp/campusfix-publish/session-14-kubernetes-troubleshooting/scenarios/scenario-1-crashloop/broken.yaml
pod/fail-1-crashloop-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f /private/tmp/campusfix-publish/session-14-kubernetes-troubleshooting/scenarios/scenario-2-imagepull/broken.yaml
pod/fail-2-imagepull-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f /private/tmp/campusfix-publish/session-14-kubernetes-troubleshooting/scenarios/scenario-3-pending/broken.yaml
pod/fail-3-pending-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f /private/tmp/campusfix-publish/session-14-kubernetes-troubleshooting/scenarios/scenario-4-dns-failure/broken.yaml
pod/fail-4-dns-failure-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f /private/tmp/campusfix-publish/session-14-kubernetes-troubleshooting/scenarios/scenario-5-oomkilled/broken.yaml
pod/fail-5-oomkilled-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "21997",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "python-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                "phase": "Pending",
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22021",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ErrImagePull"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22029",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "message": "containers with unready status: [client]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "message": "containers with unready status: [client]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "curlimages/curl:8.6.0",
                        "imageID": "",
                        "lastState": {},
                        "name": "client",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "phase": "Pending",
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22035",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "False",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "memory-leaker",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                "phase": "Pending",
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22066",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:45Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:45Z"
                            }
                        },
                        "name": "python-app",
                        "ready": false,
                        "resources": {},
                        "restartCount": 1,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "back-off 10s restarting failed container=python-app pod=fail-1-crashloop-pod_campusfix-troubleshooting(a6eef282-59ba-4c26-830f-7e363842491e)",
                                "reason": "CrashLoopBackOff"
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
                                "name": "kube-api-access-cwzgq",
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
                "podIP": "10.20.1.70",
                "podIPs": [
                    {
                        "ip": "10.20.1.70"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22021",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ErrImagePull"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22067",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0",
                        "image": "docker.io/curlimages/curl:8.6.0",
                        "imageID": "docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b",
                        "lastState": {},
                        "name": "client",
                        "ready": true,
                        "resources": {},
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:51:46Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 101,
                                "supplementalGroups": [
                                    101
                                ],
                                "uid": 100
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "podIP": "10.20.1.42",
                "podIPs": [
                    {
                        "ip": "10.20.1.42"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22035",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "False",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "memory-leaker",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                "phase": "Pending",
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22066",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:45Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:45Z"
                            }
                        },
                        "name": "python-app",
                        "ready": false,
                        "resources": {},
                        "restartCount": 1,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "back-off 10s restarting failed container=python-app pod=fail-1-crashloop-pod_campusfix-troubleshooting(a6eef282-59ba-4c26-830f-7e363842491e)",
                                "reason": "CrashLoopBackOff"
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
                                "name": "kube-api-access-cwzgq",
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
                "podIP": "10.20.1.70",
                "podIPs": [
                    {
                        "ip": "10.20.1.70"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22021",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ErrImagePull"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22067",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0",
                        "image": "docker.io/curlimages/curl:8.6.0",
                        "imageID": "docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b",
                        "lastState": {},
                        "name": "client",
                        "ready": true,
                        "resources": {},
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:51:46Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 101,
                                "supplementalGroups": [
                                    101
                                ],
                                "uid": 100
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "podIP": "10.20.1.42",
                "podIPs": [
                    {
                        "ip": "10.20.1.42"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22035",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "False",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "memory-leaker",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                "phase": "Pending",
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22112",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:45Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:45Z"
                            }
                        },
                        "name": "python-app",
                        "ready": false,
                        "resources": {},
                        "restartCount": 2,
                        "started": false,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:56Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:56Z"
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
                                "name": "kube-api-access-cwzgq",
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
                "podIP": "10.20.1.70",
                "podIPs": [
                    {
                        "ip": "10.20.1.70"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22101",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "Back-off pulling image \"yatri-api-service:v999-invalid-tag-does-not-exist\": ErrImagePull: failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ImagePullBackOff"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22067",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0",
                        "image": "docker.io/curlimages/curl:8.6.0",
                        "imageID": "docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b",
                        "lastState": {},
                        "name": "client",
                        "ready": true,
                        "resources": {},
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:51:46Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 101,
                                "supplementalGroups": [
                                    101
                                ],
                                "uid": 100
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "podIP": "10.20.1.42",
                "podIPs": [
                    {
                        "ip": "10.20.1.42"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22035",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "False",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "memory-leaker",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                "phase": "Pending",
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22112",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:45Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:45Z"
                            }
                        },
                        "name": "python-app",
                        "ready": false,
                        "resources": {},
                        "restartCount": 2,
                        "started": false,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:56Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:56Z"
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
                                "name": "kube-api-access-cwzgq",
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
                "podIP": "10.20.1.70",
                "podIPs": [
                    {
                        "ip": "10.20.1.70"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22101",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "Back-off pulling image \"yatri-api-service:v999-invalid-tag-does-not-exist\": ErrImagePull: failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ImagePullBackOff"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22067",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0",
                        "image": "docker.io/curlimages/curl:8.6.0",
                        "imageID": "docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b",
                        "lastState": {},
                        "name": "client",
                        "ready": true,
                        "resources": {},
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:51:46Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 101,
                                "supplementalGroups": [
                                    101
                                ],
                                "uid": 100
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "podIP": "10.20.1.42",
                "podIPs": [
                    {
                        "ip": "10.20.1.42"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22035",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "False",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "python:3.11-alpine",
                        "imageID": "",
                        "lastState": {},
                        "name": "memory-leaker",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "reason": "ContainerCreating"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                "phase": "Pending",
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -l tier=triage-gauntlet -o json
{
    "apiVersion": "v1",
    "items": [
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"crashloop\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-1-crashloop-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"import os, sys\\ndb_url = os.environ.get(\\\"DATABASE_URL\\\")\\nif not db_url:\\n    print(\\\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\\\", file=sys.stderr)\\n    sys.exit(1)\\nprint(\\\"Application started successfully!\\\")\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"python-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:39Z",
                "generation": 1,
                "labels": {
                    "scenario": "crashloop",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-1-crashloop-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22112",
                "uid": "a6eef282-59ba-4c26-830f-7e363842491e"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "import os, sys\ndb_url = os.environ.get(\"DATABASE_URL\")\nif not db_url:\n    print(\"[FATAL ERROR]: DATABASE_URL environment variable is MISSING!\", file=sys.stderr)\n    sys.exit(1)\nprint(\"Application started successfully!\")\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "python-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-cwzgq",
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
                        "name": "kube-api-access-cwzgq",
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
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "message": "containers with unready status: [python-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:39Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://fd679722da6559292ad5a5dd741eab4f6b35a1136d4e3e08226b154ea9234adb",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:45Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:45Z"
                            }
                        },
                        "name": "python-app",
                        "ready": false,
                        "resources": {},
                        "restartCount": 2,
                        "started": false,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377",
                                "exitCode": 1,
                                "finishedAt": "2026-10-13T03:51:56Z",
                                "reason": "Error",
                                "startedAt": "2026-10-13T03:51:56Z"
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
                                "name": "kube-api-access-cwzgq",
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
                "podIP": "10.20.1.70",
                "podIPs": [
                    {
                        "ip": "10.20.1.70"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:39Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"imagepull\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-2-imagepull-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"yatri-api-service:v999-invalid-tag-does-not-exist\",\"name\":\"web-app\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:40Z",
                "generation": 1,
                "labels": {
                    "scenario": "imagepull",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-2-imagepull-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22182",
                "uid": "6fa1b709-b578-4a7e-a063-3513b086189f"
            },
            "spec": {
                "containers": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "web-app",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                        "name": "kube-api-access-l6gpl",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "message": "containers with unready status: [web-app]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:40Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "image": "yatri-api-service:v999-invalid-tag-does-not-exist",
                        "imageID": "",
                        "lastState": {},
                        "name": "web-app",
                        "ready": false,
                        "restartCount": 0,
                        "started": false,
                        "state": {
                            "waiting": {
                                "message": "failed to pull and unpack image \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": failed to resolve reference \"docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist\": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed",
                                "reason": "ErrImagePull"
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-l6gpl",
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
                "phase": "Pending",
                "podIP": "10.20.1.225",
                "podIPs": [
                    {
                        "ip": "10.20.1.225"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:40Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"pending\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-3-pending-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"image\":\"nginx:alpine\",\"name\":\"hungry-app\",\"resources\":{\"requests\":{\"cpu\":\"500\",\"memory\":\"1000Gi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:41Z",
                "generation": 1,
                "labels": {
                    "scenario": "pending",
                    "tier": "triage-gauntlet"
                },
                "name": "fail-3-pending-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22011",
                "uid": "073e7ab6-9483-4f1f-b602-c6b5b09e45ae"
            },
            "spec": {
                "containers": [
                    {
                        "image": "nginx:alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "hungry-app",
                        "resources": {
                            "requests": {
                                "cpu": "500",
                                "memory": "1000Gi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-k8pd8",
                                "readOnly": true
                            }
                        ]
                    }
                ],
                "dnsPolicy": "ClusterFirst",
                "enableServiceLinks": true,
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
                        "name": "kube-api-access-k8pd8",
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
                        "lastTransitionTime": "2026-10-13T03:51:41Z",
                        "message": "0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.",
                        "observedGeneration": 1,
                        "reason": "Unschedulable",
                        "status": "False",
                        "type": "PodScheduled"
                    }
                ],
                "phase": "Pending",
                "qosClass": "Burstable"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"dns-failure\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-4-dns-failure-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"args\":[\"echo \\\"Attempting connection to internal database...\\\";\\n# BUG: Incorrect internal hostname\\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\\necho \\\"Process sleeping...\\\";\\nsleep 3600\\n\"],\"command\":[\"sh\",\"-c\"],\"image\":\"curlimages/curl:8.6.0\",\"name\":\"client\"}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:42Z",
                "generation": 1,
                "labels": {
                    "scenario": "dns-failure",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-4-dns-failure-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22067",
                "uid": "bcbab84c-8c63-4b8c-b3e0-356f89206f98"
            },
            "spec": {
                "containers": [
                    {
                        "args": [
                            "echo \"Attempting connection to internal database...\";\n# BUG: Incorrect internal hostname\ncurl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true\necho \"Process sleeping...\";\nsleep 3600\n"
                        ],
                        "command": [
                            "sh",
                            "-c"
                        ],
                        "image": "curlimages/curl:8.6.0",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "client",
                        "resources": {},
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                        "name": "kube-api-access-6p79s",
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
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:47Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:42Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "containerID": "containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0",
                        "image": "docker.io/curlimages/curl:8.6.0",
                        "imageID": "docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b",
                        "lastState": {},
                        "name": "client",
                        "ready": true,
                        "resources": {},
                        "restartCount": 0,
                        "started": true,
                        "state": {
                            "running": {
                                "startedAt": "2026-10-13T03:51:46Z"
                            }
                        },
                        "user": {
                            "linux": {
                                "gid": 101,
                                "supplementalGroups": [
                                    101
                                ],
                                "uid": 100
                            }
                        },
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-6p79s",
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
                "podIP": "10.20.1.42",
                "podIPs": [
                    {
                        "ip": "10.20.1.42"
                    }
                ],
                "qosClass": "BestEffort",
                "startTime": "2026-10-13T03:51:42Z"
            }
        },
        {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "annotations": {
                    "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"labels\":{\"scenario\":\"oomkilled\",\"tier\":\"triage-gauntlet\"},\"name\":\"fail-5-oomkilled-pod\",\"namespace\":\"campusfix-troubleshooting\"},\"spec\":{\"containers\":[{\"command\":[\"python3\",\"-c\",\"# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\\nprint(\\\"Allocating memory rapidly...\\\")\\nchunks = []\\nfor i in range(100):\\n    chunks.append(b\\\"x\\\" * (10 * 1024 * 1024))\\n\"],\"image\":\"python:3.11-alpine\",\"name\":\"memory-leaker\",\"resources\":{\"limits\":{\"memory\":\"20Mi\"}}}]}}\n"
                },
                "creationTimestamp": "2026-10-13T03:51:43Z",
                "generation": 1,
                "labels": {
                    "scenario": "oomkilled",
                    "tier": "triage-gauntlet",
                    "topology.kubernetes.io/region": "ap-south-1",
                    "topology.kubernetes.io/zone": "ap-south-1a"
                },
                "name": "fail-5-oomkilled-pod",
                "namespace": "campusfix-troubleshooting",
                "resourceVersion": "22167",
                "uid": "c80874a3-a80c-40bc-b28a-f1defe4a88c1"
            },
            "spec": {
                "containers": [
                    {
                        "command": [
                            "python3",
                            "-c",
                            "# BUG: Rapidly allocates 200MB of RAM while limit is 20Mi\nprint(\"Allocating memory rapidly...\")\nchunks = []\nfor i in range(100):\n    chunks.append(b\"x\" * (10 * 1024 * 1024))\n"
                        ],
                        "image": "python:3.11-alpine",
                        "imagePullPolicy": "IfNotPresent",
                        "name": "memory-leaker",
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "terminationMessagePath": "/dev/termination-log",
                        "terminationMessagePolicy": "File",
                        "volumeMounts": [
                            {
                                "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                                "name": "kube-api-access-csqjh",
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
                        "name": "kube-api-access-csqjh",
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
                        "lastTransitionTime": "2026-10-13T03:52:07Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodReadyToStartContainers"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "Initialized"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "Ready"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "message": "containers with unready status: [memory-leaker]",
                        "observedGeneration": 1,
                        "reason": "ContainersNotReady",
                        "status": "False",
                        "type": "ContainersReady"
                    },
                    {
                        "lastProbeTime": null,
                        "lastTransitionTime": "2026-10-13T03:51:43Z",
                        "observedGeneration": 1,
                        "status": "True",
                        "type": "PodScheduled"
                    }
                ],
                "containerStatuses": [
                    {
                        "allocatedResources": {
                            "memory": "20Mi"
                        },
                        "containerID": "containerd://7ca826c4f5bcf9246df3d6d7320fad55ce1820330d6b03472a6f6c77c012834d",
                        "image": "docker.io/library/python:3.11-alpine",
                        "imageID": "docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929",
                        "lastState": {
                            "terminated": {
                                "containerID": "containerd://0ce21f5fc6a0666e98c3a7cd87efb857565e054138abad470e2a77517b3503b8",
                                "exitCode": 137,
                                "finishedAt": "2026-10-13T03:52:08Z",
                                "reason": "OOMKilled",
                                "startedAt": "2026-10-13T03:52:07Z"
                            }
                        },
                        "name": "memory-leaker",
                        "ready": false,
                        "resources": {
                            "limits": {
                                "memory": "20Mi"
                            },
                            "requests": {
                                "memory": "20Mi"
                            }
                        },
                        "restartCount": 1,
                        "started": false,
                        "state": {
                            "terminated": {
                                "containerID": "containerd://7ca826c4f5bcf9246df3d6d7320fad55ce1820330d6b03472a6f6c77c012834d",
                                "exitCode": 137,
                                "finishedAt": "2026-10-13T03:52:08Z",
                                "reason": "OOMKilled",
                                "startedAt": "2026-10-13T03:52:08Z"
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
                                "name": "kube-api-access-csqjh",
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
                "podIP": "10.20.1.53",
                "podIPs": [
                    {
                        "ip": "10.20.1.53"
                    }
                ],
                "qosClass": "Burstable",
                "startTime": "2026-10-13T03:51:43Z"
            }
        }
    ],
    "kind": "List",
    "metadata": {
        "resourceVersion": ""
    }
}
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -o wide
NAME                         READY   STATUS         RESTARTS      AGE   IP            NODE                                         NOMINATED NODE   READINESS GATES
dns-target-cb6d46759-v74z4   1/1     Running        0             36s   10.20.1.15    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-1-crashloop-pod         0/1     Error          2 (28s ago)   34s   10.20.1.70    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-2-imagepull-pod         0/1     ErrImagePull   0             33s   10.20.1.225   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-3-pending-pod           0/1     Pending        0             32s   <none>        <none>                                       <none>           <none>
fail-4-dns-failure-pod       1/1     Running        0             31s   10.20.1.42    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-5-oomkilled-pod         0/1     OOMKilled      1 (5s ago)    30s   10.20.1.53    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get events --sort-by=.metadata.creationTimestamp
LAST SEEN   TYPE      REASON                   OBJECT                            MESSAGE
37s         Normal    Scheduled                pod/dns-target-cb6d46759-v74z4    Successfully assigned campusfix-troubleshooting/dns-target-cb6d46759-v74z4 to ip-10-20-1-116.ap-south-1.compute.internal
37s         Normal    Pulled                   pod/dns-target-cb6d46759-v74z4    Container image "nginx:1.28-alpine" already present on machine and can be accessed by the pod
37s         Normal    SuccessfulCreate         replicaset/dns-target-cb6d46759   Created pod: dns-target-cb6d46759-v74z4
37s         Normal    ScalingReplicaSet        deployment/dns-target             Scaled up replica set dns-target-cb6d46759 from 0 to 1
36s         Normal    Created                  pod/dns-target-cb6d46759-v74z4    Container created
36s         Normal    Started                  pod/dns-target-cb6d46759-v74z4    Container started
35s         Normal    Scheduled                pod/fail-1-crashloop-pod          Successfully assigned campusfix-troubleshooting/fail-1-crashloop-pod to ip-10-20-1-116.ap-south-1.compute.internal
34s         Normal    Scheduled                pod/fail-2-imagepull-pod          Successfully assigned campusfix-troubleshooting/fail-2-imagepull-pod to ip-10-20-1-116.ap-south-1.compute.internal
34s         Normal    Pulling                  pod/fail-1-crashloop-pod          Pulling image "python:3.11-alpine"
33s         Warning   FailedScheduling         pod/fail-3-pending-pod            0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
18s         Normal    Pulling                  pod/fail-2-imagepull-pod          Pulling image "yatri-api-service:v999-invalid-tag-does-not-exist"
32s         Normal    Pulling                  pod/fail-4-dns-failure-pod        Pulling image "curlimages/curl:8.6.0"
32s         Normal    Scheduled                pod/fail-4-dns-failure-pod        Successfully assigned campusfix-troubleshooting/fail-4-dns-failure-pod to ip-10-20-1-116.ap-south-1.compute.internal
17s         Warning   Failed                   pod/fail-2-imagepull-pod          Failed to pull image "yatri-api-service:v999-invalid-tag-does-not-exist": failed to pull and unpack image "docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist": failed to resolve reference "docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
17s         Warning   Failed                   pod/fail-2-imagepull-pod          Error: ErrImagePull
2s          Normal    BackOff                  pod/fail-2-imagepull-pod          Back-off pulling image "yatri-api-service:v999-invalid-tag-does-not-exist"
2s          Warning   Failed                   pod/fail-2-imagepull-pod          Error: ImagePullBackOff
31s         Normal    Scheduled                pod/fail-5-oomkilled-pod          Successfully assigned campusfix-troubleshooting/fail-5-oomkilled-pod to ip-10-20-1-116.ap-south-1.compute.internal
31s         Warning   FailedCreatePodSandBox   pod/fail-5-oomkilled-pod          Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "bbcecb10a90aec50b47467e0176e0d2e3a0f691bb23f39767ade4b9e1203845b": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
30s         Normal    Pulled                   pod/fail-1-crashloop-pod          Successfully pulled image "python:3.11-alpine" in 4.408s (4.408s including waiting). Image size: 23003038 bytes.
18s         Normal    Started                  pod/fail-1-crashloop-pod          Container started
18s         Normal    Created                  pod/fail-1-crashloop-pod          Container created
18s         Normal    Pulled                   pod/fail-1-crashloop-pod          Container image "python:3.11-alpine" already present on machine and can be accessed by the pod
17s         Warning   BackOff                  pod/fail-1-crashloop-pod          Back-off restarting failed container python-app in pod fail-1-crashloop-pod_campusfix-troubleshooting(a6eef282-59ba-4c26-830f-7e363842491e)
28s         Normal    Pulled                   pod/fail-4-dns-failure-pod        Successfully pulled image "curlimages/curl:8.6.0" in 3.399s (3.399s including waiting). Image size: 7535333 bytes.
28s         Normal    Created                  pod/fail-4-dns-failure-pod        Container created
28s         Normal    Started                  pod/fail-4-dns-failure-pod        Container started
20s         Warning   FailedCreatePodSandBox   pod/fail-5-oomkilled-pod          Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "939a8ffabfbf545145af4700d77fd39e375bca4887cae40c0291de764de0a350": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
6s          Normal    Pulled                   pod/fail-5-oomkilled-pod          Container image "python:3.11-alpine" already present on machine and can be accessed by the pod
6s          Normal    Created                  pod/fail-5-oomkilled-pod          Container created
6s          Normal    Started                  pod/fail-5-oomkilled-pod          Container started
5s          Warning   BackOff                  pod/fail-5-oomkilled-pod          Back-off restarting failed container memory-leaker in pod fail-5-oomkilled-pod_campusfix-troubleshooting(c80874a3-a80c-40bc-b28a-f1defe4a88c1)
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting describe pod fail-1-crashloop-pod
Name:             fail-1-crashloop-pod
Namespace:        campusfix-troubleshooting
Priority:         0
Service Account:  default
Node:             ip-10-20-1-116.ap-south-1.compute.internal/10.20.1.116
Start Time:       Tue, 13 Oct 2026 09:21:39 +0530
Labels:           scenario=crashloop
                  tier=triage-gauntlet
                  topology.kubernetes.io/region=ap-south-1
                  topology.kubernetes.io/zone=ap-south-1a
Annotations:      <none>
Status:           Running
IP:               10.20.1.70
IPs:
  IP:  10.20.1.70
Containers:
  python-app:
    Container ID:  containerd://93e0c91f90cdcb0a00988b7b955f090a39c541ba78a8d5566ee63030e6f1e377
    Image:         python:3.11-alpine
    Image ID:      docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929
    Port:          <none>
    Host Port:     <none>
    Command:
      python3
      -c
      import os, sys
      db_url = os.environ.get("DATABASE_URL")
      if not db_url:
          print("[FATAL ERROR]: DATABASE_URL environment variable is MISSING!", file=sys.stderr)
          sys.exit(1)
      print("Application started successfully!")
      
    State:          Terminated
      Reason:       Error
      Exit Code:    1
      Started:      Tue, 13 Oct 2026 09:21:56 +0530
      Finished:     Tue, 13 Oct 2026 09:21:56 +0530
    Last State:     Terminated
      Reason:       Error
      Exit Code:    1
      Started:      Tue, 13 Oct 2026 09:21:45 +0530
      Finished:     Tue, 13 Oct 2026 09:21:45 +0530
    Ready:          False
    Restart Count:  2
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-cwzgq (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-cwzgq:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  35s                default-scheduler  Successfully assigned campusfix-troubleshooting/fail-1-crashloop-pod to ip-10-20-1-116.ap-south-1.compute.internal
  Normal   Pulling    34s                kubelet            spec.containers{python-app}: Pulling image "python:3.11-alpine"
  Normal   Pulled     30s                kubelet            spec.containers{python-app}: Successfully pulled image "python:3.11-alpine" in 4.408s (4.408s including waiting). Image size: 23003038 bytes.
  Normal   Created    18s (x3 over 30s)  kubelet            spec.containers{python-app}: Container created
  Normal   Started    18s (x3 over 30s)  kubelet            spec.containers{python-app}: Container started
  Normal   Pulled     18s (x2 over 29s)  kubelet            spec.containers{python-app}: Container image "python:3.11-alpine" already present on machine and can be accessed by the pod
  Warning  BackOff    17s (x3 over 28s)  kubelet            spec.containers{python-app}: Back-off restarting failed container python-app in pod fail-1-crashloop-pod_campusfix-troubleshooting(a6eef282-59ba-4c26-830f-7e363842491e)
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-1-crashloop-pod --tail=20
[FATAL ERROR]: DATABASE_URL environment variable is MISSING!
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting delete pod fail-1-crashloop-pod --wait=true
pod "fail-1-crashloop-pod" deleted from campusfix-troubleshooting namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f -
pod/fail-1-crashloop-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting wait --for=condition=Ready pod/fail-1-crashloop-pod --timeout=180s
pod/fail-1-crashloop-pod condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-1-crashloop-pod --tail=10
Configuration present; service stays alive
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting describe pod fail-2-imagepull-pod
Name:             fail-2-imagepull-pod
Namespace:        campusfix-troubleshooting
Priority:         0
Service Account:  default
Node:             ip-10-20-1-116.ap-south-1.compute.internal/10.20.1.116
Start Time:       Tue, 13 Oct 2026 09:21:40 +0530
Labels:           scenario=imagepull
                  tier=triage-gauntlet
                  topology.kubernetes.io/region=ap-south-1
                  topology.kubernetes.io/zone=ap-south-1a
Annotations:      <none>
Status:           Pending
IP:               10.20.1.225
IPs:
  IP:  10.20.1.225
Containers:
  web-app:
    Container ID:   
    Image:          yatri-api-service:v999-invalid-tag-does-not-exist
    Image ID:       
    Port:           <none>
    Host Port:      <none>
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-l6gpl (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-l6gpl:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  79s                default-scheduler  Successfully assigned campusfix-troubleshooting/fail-2-imagepull-pod to ip-10-20-1-116.ap-south-1.compute.internal
  Normal   Pulling    32s (x3 over 78s)  kubelet            spec.containers{web-app}: Pulling image "yatri-api-service:v999-invalid-tag-does-not-exist"
  Warning  Failed     31s (x3 over 77s)  kubelet            spec.containers{web-app}: Failed to pull image "yatri-api-service:v999-invalid-tag-does-not-exist": failed to pull and unpack image "docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist": failed to resolve reference "docker.io/library/yatri-api-service:v999-invalid-tag-does-not-exist": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  Warning  Failed     31s (x3 over 77s)  kubelet            spec.containers{web-app}: Error: ErrImagePull
  Normal   BackOff    4s (x4 over 77s)   kubelet            spec.containers{web-app}: Back-off pulling image "yatri-api-service:v999-invalid-tag-does-not-exist"
  Warning  Failed     4s (x4 over 77s)   kubelet            spec.containers{web-app}: Error: ImagePullBackOff
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-2-imagepull-pod --tail=20
 Error from server (BadRequest): container "web-app" in pod "fail-2-imagepull-pod" is waiting to start: trying and failing to pull image
 [exit: 1 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting delete pod fail-2-imagepull-pod --wait=true
pod "fail-2-imagepull-pod" deleted from campusfix-troubleshooting namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f -
pod/fail-2-imagepull-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting wait --for=condition=Ready pod/fail-2-imagepull-pod --timeout=180s
pod/fail-2-imagepull-pod condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-2-imagepull-pod --tail=10
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/10/13 03:53:44 [notice] 1#1: using the "epoll" event method
2026/10/13 03:53:44 [notice] 1#1: nginx/1.28.3
2026/10/13 03:53:44 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/10/13 03:53:44 [notice] 1#1: OS: Linux 6.12.110-135.202.amzn2023.x86_64
2026/10/13 03:53:44 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 65536:1048576
2026/10/13 03:53:44 [notice] 1#1: start worker processes
2026/10/13 03:53:44 [notice] 1#1: start worker process 29
2026/10/13 03:53:44 [notice] 1#1: start worker process 30
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting describe pod fail-3-pending-pod
Name:             fail-3-pending-pod
Namespace:        campusfix-troubleshooting
Priority:         0
Service Account:  default
Node:             <none>
Labels:           scenario=pending
                  tier=triage-gauntlet
Annotations:      <none>
Status:           Pending
IP:               
IPs:              <none>
Containers:
  hungry-app:
    Image:      nginx:alpine
    Port:       <none>
    Host Port:  <none>
    Requests:
      cpu:        500
      memory:     1000Gi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-k8pd8 (ro)
Conditions:
  Type           Status
  PodScheduled   False 
Volumes:
  kube-api-access-k8pd8:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age                 From               Message
  ----     ------            ----                ----               -------
  Warning  FailedScheduling  46s (x3 over 2m6s)  default-scheduler  0/2 nodes are available: 1 Too many pods, 2 Insufficient cpu, 2 Insufficient memory. no new claims to deallocate, preemption: 0/2 nodes are available: 2 Preemption is not helpful for scheduling.
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-3-pending-pod --tail=20
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting delete pod fail-3-pending-pod --wait=true
pod "fail-3-pending-pod" deleted from campusfix-troubleshooting namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f -
pod/fail-3-pending-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting wait --for=condition=Ready pod/fail-3-pending-pod --timeout=180s
pod/fail-3-pending-pod condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-3-pending-pod --tail=10
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/10/13 03:56:01 [notice] 1#1: using the "epoll" event method
2026/10/13 03:56:01 [notice] 1#1: nginx/1.31.6
2026/10/13 03:56:01 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/10/13 03:56:01 [notice] 1#1: OS: Linux 6.12.110-135.202.amzn2023.x86_64
2026/10/13 03:56:01 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 65536:1048576
2026/10/13 03:56:01 [notice] 1#1: start worker processes
2026/10/13 03:56:01 [notice] 1#1: start worker process 31
2026/10/13 03:56:01 [notice] 1#1: start worker process 32
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting describe pod fail-4-dns-failure-pod
Name:             fail-4-dns-failure-pod
Namespace:        campusfix-troubleshooting
Priority:         0
Service Account:  default
Node:             ip-10-20-1-116.ap-south-1.compute.internal/10.20.1.116
Start Time:       Tue, 13 Oct 2026 09:21:42 +0530
Labels:           scenario=dns-failure
                  tier=triage-gauntlet
                  topology.kubernetes.io/region=ap-south-1
                  topology.kubernetes.io/zone=ap-south-1a
Annotations:      <none>
Status:           Running
IP:               10.20.1.42
IPs:
  IP:  10.20.1.42
Containers:
  client:
    Container ID:  containerd://6f16ff72ffa2bf5ee886baca0e5687d11e8ab5d5c1acc8f4f1660ef13ebb59e0
    Image:         curlimages/curl:8.6.0
    Image ID:      docker.io/curlimages/curl@sha256:c3b8bee303c6c6beed656cfc921218c529d65aa61114eb9e27c62047a1271b9b
    Port:          <none>
    Host Port:     <none>
    Command:
      sh
      -c
    Args:
      echo "Attempting connection to internal database...";
      # BUG: Incorrect internal hostname
      curl -s --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432 || true
      echo "Process sleeping...";
      sleep 3600
      
    State:          Running
      Started:      Tue, 13 Oct 2026 09:21:46 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-6p79s (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-6p79s:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  4m21s  default-scheduler  Successfully assigned campusfix-troubleshooting/fail-4-dns-failure-pod to ip-10-20-1-116.ap-south-1.compute.internal
  Normal  Pulling    4m21s  kubelet            spec.containers{client}: Pulling image "curlimages/curl:8.6.0"
  Normal  Pulled     4m17s  kubelet            spec.containers{client}: Successfully pulled image "curlimages/curl:8.6.0" in 3.399s (3.399s including waiting). Image size: 7535333 bytes.
  Normal  Created    4m17s  kubelet            spec.containers{client}: Container created
  Normal  Started    4m17s  kubelet            spec.containers{client}: Container started
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-4-dns-failure-pod --tail=20
Attempting connection to internal database...
Process sleeping...
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting exec fail-4-dns-failure-pod -- curl -v --connect-timeout 3 http://postgres-db-wrong-name.production.svc.cluster.local:5432
   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* Could not resolve host: postgres-db-wrong-name.production.svc.cluster.local
* Closing connection
curl: (6) Could not resolve host: postgres-db-wrong-name.production.svc.cluster.local
command terminated with exit code 6
 [exit: 6 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting delete pod fail-4-dns-failure-pod --wait=true
pod "fail-4-dns-failure-pod" deleted from campusfix-troubleshooting namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f -
pod/fail-4-dns-failure-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting wait --for=condition=Ready pod/fail-4-dns-failure-pod --timeout=180s
pod/fail-4-dns-failure-pod condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-4-dns-failure-pod --tail=10

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>

  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   615  100   615    0     0  66307      0 --:--:-- --:--:-- --:--:-- 76875
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting describe pod fail-5-oomkilled-pod
Name:             fail-5-oomkilled-pod
Namespace:        campusfix-troubleshooting
Priority:         0
Service Account:  default
Node:             ip-10-20-1-116.ap-south-1.compute.internal/10.20.1.116
Start Time:       Tue, 13 Oct 2026 09:21:43 +0530
Labels:           scenario=oomkilled
                  tier=triage-gauntlet
                  topology.kubernetes.io/region=ap-south-1
                  topology.kubernetes.io/zone=ap-south-1a
Annotations:      <none>
Status:           Running
IP:               10.20.1.53
IPs:
  IP:  10.20.1.53
Containers:
  memory-leaker:
    Container ID:  containerd://2cc60583e1b666e4865854a5c0139795e0e4439d512e6c8b734526ff204b1750
    Image:         python:3.11-alpine
    Image ID:      docker.io/library/python@sha256:d9368b3a5ac59afea7b5d4f2e2aea0941dbf9fdee9c369c5bec00b98244bc929
    Port:          <none>
    Host Port:     <none>
    Command:
      python3
      -c
      # BUG: Rapidly allocates 200MB of RAM while limit is 20Mi
      print("Allocating memory rapidly...")
      chunks = []
      for i in range(100):
          chunks.append(b"x" * (10 * 1024 * 1024))
      
    State:          Waiting
      Reason:       CrashLoopBackOff
    Last State:     Terminated
      Reason:       OOMKilled
      Exit Code:    137
      Started:      Tue, 13 Oct 2026 09:24:56 +0530
      Finished:     Tue, 13 Oct 2026 09:24:56 +0530
    Ready:          False
    Restart Count:  5
    Limits:
      memory:  20Mi
    Requests:
      memory:     20Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-csqjh (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       False 
  ContainersReady             False 
  PodScheduled                True 
Volumes:
  kube-api-access-csqjh:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    Optional:                false
    DownwardAPI:             true
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason                  Age                   From               Message
  ----     ------                  ----                  ----               -------
  Normal   Scheduled               5m1s                  default-scheduler  Successfully assigned campusfix-troubleshooting/fail-5-oomkilled-pod to ip-10-20-1-116.ap-south-1.compute.internal
  Warning  FailedCreatePodSandBox  5m1s                  kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "bbcecb10a90aec50b47467e0176e0d2e3a0f691bb23f39767ade4b9e1203845b": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
  Warning  FailedCreatePodSandBox  4m50s                 kubelet            Failed to create pod sandbox: rpc error: code = Unknown desc = failed to setup network for sandbox "939a8ffabfbf545145af4700d77fd39e375bca4887cae40c0291de764de0a350": plugin type="aws-cni" name="aws-cni" failed (add): add cmd: failed to assign an IP address to container
  Normal   Pulled                  108s (x6 over 4m37s)  kubelet            spec.containers{memory-leaker}: Container image "python:3.11-alpine" already present on machine and can be accessed by the pod
  Normal   Created                 108s (x6 over 4m37s)  kubelet            spec.containers{memory-leaker}: Container created
  Normal   Started                 108s (x6 over 4m37s)  kubelet            spec.containers{memory-leaker}: Container started
  Warning  BackOff                 25s (x7 over 4m35s)   kubelet            spec.containers{memory-leaker}: Back-off restarting failed container memory-leaker in pod fail-5-oomkilled-pod_campusfix-troubleshooting(c80874a3-a80c-40bc-b28a-f1defe4a88c1)
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-5-oomkilled-pod --tail=20
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting delete pod fail-5-oomkilled-pod --wait=true
pod "fail-5-oomkilled-pod" deleted from campusfix-troubleshooting namespace
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting apply -f -
pod/fail-5-oomkilled-pod created
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting wait --for=condition=Ready pod/fail-5-oomkilled-pod --timeout=180s
pod/fail-5-oomkilled-pod condition met
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting logs fail-5-oomkilled-pod --tail=10
Bounded allocation: 5 MiB
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-troubleshooting get pods -o wide
NAME                         READY   STATUS    RESTARTS   AGE     IP            NODE                                         NOMINATED NODE   READINESS GATES
dns-target-cb6d46759-v74z4   1/1     Running   0          5m13s   10.20.1.15    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-1-crashloop-pod         1/1     Running   0          4m32s   10.20.1.70    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-2-imagepull-pod         1/1     Running   0          3m47s   10.20.1.225   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
fail-3-pending-pod           1/1     Running   0          3m      10.20.2.229   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
fail-4-dns-failure-pod       1/1     Running   0          13s     10.20.2.150   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
fail-5-oomkilled-pod         1/1     Running   0          3s      10.20.1.206   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s delete namespace campusfix-troubleshooting --wait=true --timeout=180s
namespace "campusfix-troubleshooting" deleted
  [exit: 0 ]
All checks in troubleshooting passed; temporary namespace removed.

```

Exit code: 0
