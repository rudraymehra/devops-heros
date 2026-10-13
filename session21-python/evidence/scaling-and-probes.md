# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:38:13.549186+00:00

Working directory: .

```text
$ python3 session21-python/scripts/scaling-probes-check.py
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard delete pod campusfix-load --ignore-not-found=true --wait=true
pod "campusfix-load" deleted from taskboard namespace
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard apply -f session21-python/scripts/cloud-load.yaml
pod/campusfix-load created
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard wait --for=condition=Ready pod/campusfix-load --timeout=120s
pod/campusfix-load condition met
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72138",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is less than the minimum replica count",
                "reason": "TooFewReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 2,
                        "averageValue": "2m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 2,
        "desiredReplicas": 2,
        "lastScaleTime": "2026-10-13T03:55:24Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h57m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h57m
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72261",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is less than the minimum replica count",
                "reason": "TooFewReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 3,
                        "averageValue": "3m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 2,
        "desiredReplicas": 2,
        "lastScaleTime": "2026-10-13T03:55:24Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h57m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h57m
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72319",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "the HPA controller was able to update the target scale to 4",
                "reason": "SucceededRescale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is increasing faster than the maximum scale rate",
                "reason": "ScaleUpLimit",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 196,
                        "averageValue": "196m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 2,
        "desiredReplicas": 4,
        "lastScaleTime": "2026-10-13T07:35:27Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS              RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   0/1     ContainerCreating   0          1s
taskboard-backend-b6b57c5cf-5pf4x   0/1     ContainerCreating   0          1s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running             0          3h57m
taskboard-backend-b6b57c5cf-d26md   1/1     Running             0          3h57m
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72319",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "the HPA controller was able to update the target scale to 4",
                "reason": "SucceededRescale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is increasing faster than the maximum scale rate",
                "reason": "ScaleUpLimit",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 196,
                        "averageValue": "196m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 2,
        "desiredReplicas": 4,
        "lastScaleTime": "2026-10-13T07:35:27Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          12s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          12s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72421",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "the HPA controller was able to update the target scale to 6",
                "reason": "SucceededRescale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 449,
                        "averageValue": "449m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 4,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          24s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          24s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-fwjfh   0/1     Running   0          9s
taskboard-backend-b6b57c5cf-l4ghc   0/1     Running   0          9s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72518",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recent recommendations were higher than current one, applying the highest recent recommendation",
                "reason": "ScaleDownStabilized",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 405,
                        "averageValue": "405m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          35s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          35s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          20s
taskboard-backend-b6b57c5cf-l4ghc   0/1     Running   0          20s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72581",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 358,
                        "averageValue": "358m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          46s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          46s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          31s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          31s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72581",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 358,
                        "averageValue": "358m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          58s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          58s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          43s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          43s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72636",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 348,
                        "averageValue": "348m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          69s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          69s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h58m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          54s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          54s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72693",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 316,
                        "averageValue": "316m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          84s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          84s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          69s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          69s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72748",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 331,
                        "averageValue": "331m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          96s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          96s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          81s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          81s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72810",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 333,
                        "averageValue": "333m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          107s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          107s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          92s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          92s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72810",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recommended size matches current size",
                "reason": "ReadyForNewScale",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 333,
                        "averageValue": "333m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          119s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          119s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          3h59m
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          104s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          104s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get hpa taskboard-backend -o json
{
    "apiVersion": "autoscaling/v2",
    "kind": "HorizontalPodAutoscaler",
    "metadata": {
        "annotations": {
            "argocd.argoproj.io/tracking-id": "campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend",
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"autoscaling/v2\",\"kind\":\"HorizontalPodAutoscaler\",\"metadata\":{\"annotations\":{\"argocd.argoproj.io/tracking-id\":\"campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend\"},\"name\":\"taskboard-backend\",\"namespace\":\"taskboard\"},\"spec\":{\"maxReplicas\":6,\"metrics\":[{\"resource\":{\"name\":\"cpu\",\"target\":{\"averageUtilization\":60,\"type\":\"Utilization\"}},\"type\":\"Resource\"}],\"minReplicas\":2,\"scaleTargetRef\":{\"apiVersion\":\"apps/v1\",\"kind\":\"Deployment\",\"name\":\"taskboard-backend\"}}}\n",
            "meta.helm.sh/release-name": "taskboard",
            "meta.helm.sh/release-namespace": "taskboard"
        },
        "creationTimestamp": "2026-10-13T03:37:38Z",
        "labels": {
            "app.kubernetes.io/managed-by": "Helm"
        },
        "name": "taskboard-backend",
        "namespace": "taskboard",
        "resourceVersion": "72864",
        "uid": "1ed4b20f-613f-4296-8095-538ff8541890"
    },
    "spec": {
        "maxReplicas": 6,
        "metrics": [
            {
                "resource": {
                    "name": "cpu",
                    "target": {
                        "averageUtilization": 60,
                        "type": "Utilization"
                    }
                },
                "type": "Resource"
            }
        ],
        "minReplicas": 2,
        "scaleTargetRef": {
            "apiVersion": "apps/v1",
            "kind": "Deployment",
            "name": "taskboard-backend"
        }
    },
    "status": {
        "conditions": [
            {
                "lastTransitionTime": "2026-10-13T03:37:53Z",
                "message": "recent recommendations were higher than current one, applying the highest recent recommendation",
                "reason": "ScaleDownStabilized",
                "status": "True",
                "type": "AbleToScale"
            },
            {
                "lastTransitionTime": "2026-10-13T03:39:53Z",
                "message": "the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)",
                "reason": "ValidMetricFound",
                "status": "True",
                "type": "ScalingActive"
            },
            {
                "lastTransitionTime": "2026-10-13T03:55:24Z",
                "message": "the desired replica count is more than the maximum replica count",
                "reason": "TooManyReplicas",
                "status": "True",
                "type": "ScalingLimited"
            }
        ],
        "currentMetrics": [
            {
                "resource": {
                    "current": {
                        "averageUtilization": 170,
                        "averageValue": "170m"
                    },
                    "name": "cpu"
                },
                "type": "Resource"
            }
        ],
        "currentReplicas": 6,
        "desiredReplicas": 6,
        "lastScaleTime": "2026-10-13T07:35:42Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pods -l app=taskboard-backend
NAME                                READY   STATUS    RESTARTS   AGE
taskboard-backend-b6b57c5cf-24gjc   1/1     Running   0          2m11s
taskboard-backend-b6b57c5cf-5pf4x   1/1     Running   0          2m11s
taskboard-backend-b6b57c5cf-9sn7x   1/1     Running   0          4h
taskboard-backend-b6b57c5cf-d26md   1/1     Running   0          4h
taskboard-backend-b6b57c5cf-fwjfh   1/1     Running   0          116s
taskboard-backend-b6b57c5cf-l4ghc   1/1     Running   0          116s
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard logs campusfix-load
{'successful_requests': 30291, 'failed_requests': 0}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard describe hpa taskboard-backend
Name:                                                  taskboard-backend
Namespace:                                             taskboard
Labels:                                                app.kubernetes.io/managed-by=Helm
Annotations:                                           argocd.argoproj.io/tracking-id: campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend
                                                       meta.helm.sh/release-name: taskboard
                                                       meta.helm.sh/release-namespace: taskboard
CreationTimestamp:                                     Tue, 13 Oct 2026 09:07:38 +0530
Reference:                                             Deployment/taskboard-backend
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  60% (60m) / 60%
Min replicas:                                          2
Max replicas:                                          6
Deployment pods:                                       6 current / 6 desired
Conditions:
  Type            Status  Reason               Message
  ----            ------  ------               -------
  AbleToScale     True    ScaleDownStabilized  recent recommendations were higher than current one, applying the highest recent recommendation
  ScalingActive   True    ValidMetricFound     the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
  ScalingLimited  True    TooManyReplicas      the desired replica count is more than the maximum replica count
Events:
  Type    Reason             Age                    From                       Message
  ----    ------             ----                   ----                       -------
  Normal  SuccessfulRescale  2m28s (x2 over 3h49m)  horizontal-pod-autoscaler  New size: 4; reason: cpu resource utilization (percentage of request) above target
  Normal  SuccessfulRescale  2m13s (x2 over 3h49m)  horizontal-pod-autoscaler  New size: 6; reason: cpu resource utilization (percentage of request) above target
 
PASS: HPA requested additional replicas under real HTTP load.
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard apply -f -
pod/campusfix-probes created
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard wait --for=condition=Ready pod/campusfix-probes --timeout=120s
pod/campusfix-probes condition met
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard exec campusfix-probes -- rm /usr/share/nginx/html/ready
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard wait --for=condition=Ready=false pod/campusfix-probes --timeout=30s
pod/campusfix-probes condition met
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pod campusfix-probes -o json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"name\":\"campusfix-probes\",\"namespace\":\"taskboard\"},\"spec\":{\"containers\":[{\"image\":\"nginx:1.28-alpine\",\"lifecycle\":{\"postStart\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"touch /usr/share/nginx/html/ready /usr/share/nginx/html/live\"]}}},\"livenessProbe\":{\"failureThreshold\":2,\"httpGet\":{\"path\":\"/live\",\"port\":80},\"periodSeconds\":2},\"name\":\"web\",\"readinessProbe\":{\"failureThreshold\":1,\"httpGet\":{\"path\":\"/ready\",\"port\":80},\"periodSeconds\":2},\"resources\":{\"requests\":{\"cpu\":\"20m\",\"memory\":\"32Mi\"}}}]}}\n"
        },
        "creationTimestamp": "2026-10-13T07:37:56Z",
        "generation": 1,
        "labels": {
            "topology.kubernetes.io/region": "ap-south-1",
            "topology.kubernetes.io/zone": "ap-south-1a"
        },
        "name": "campusfix-probes",
        "namespace": "taskboard",
        "resourceVersion": "72998",
        "uid": "b1d4628d-9694-4312-98c2-74efef4616f4"
    },
    "spec": {
        "containers": [
            {
                "image": "nginx:1.28-alpine",
                "imagePullPolicy": "IfNotPresent",
                "lifecycle": {
                    "postStart": {
                        "exec": {
                            "command": [
                                "sh",
                                "-c",
                                "touch /usr/share/nginx/html/ready /usr/share/nginx/html/live"
                            ]
                        }
                    }
                },
                "livenessProbe": {
                    "failureThreshold": 2,
                    "httpGet": {
                        "path": "/live",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "name": "web",
                "readinessProbe": {
                    "failureThreshold": 1,
                    "httpGet": {
                        "path": "/ready",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-q4h2r",
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
                "name": "kube-api-access-q4h2r",
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
                "lastTransitionTime": "2026-10-13T07:37:57Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodReadyToStartContainers"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "Initialized"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:00Z",
                "message": "containers with unready status: [web]",
                "observedGeneration": 1,
                "reason": "ContainersNotReady",
                "status": "False",
                "type": "Ready"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:00Z",
                "message": "containers with unready status: [web]",
                "observedGeneration": 1,
                "reason": "ContainersNotReady",
                "status": "False",
                "type": "ContainersReady"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodScheduled"
            }
        ],
        "containerStatuses": [
            {
                "allocatedResources": {
                    "cpu": "20m",
                    "memory": "32Mi"
                },
                "containerID": "containerd://a996e49ee58d1d8d3d4c658f56a1a61c3d3b91d7f49a6a200a23c4d1dc87925d",
                "image": "docker.io/library/nginx:1.28-alpine",
                "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                "lastState": {},
                "name": "web",
                "ready": false,
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "restartCount": 0,
                "started": true,
                "state": {
                    "running": {
                        "startedAt": "2026-10-13T07:37:57Z"
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
                        "name": "kube-api-access-q4h2r",
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
        "podIP": "10.20.1.15",
        "podIPs": [
            {
                "ip": "10.20.1.15"
            }
        ],
        "qosClass": "Burstable",
        "startTime": "2026-10-13T07:37:56Z"
    }
}
 
PASS: readiness failure removes readiness without restarting the process.
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard exec campusfix-probes -- touch /usr/share/nginx/html/ready
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard wait --for=condition=Ready pod/campusfix-probes --timeout=30s
pod/campusfix-probes condition met
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard exec campusfix-probes -- rm /usr/share/nginx/html/live
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pod campusfix-probes -o json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"name\":\"campusfix-probes\",\"namespace\":\"taskboard\"},\"spec\":{\"containers\":[{\"image\":\"nginx:1.28-alpine\",\"lifecycle\":{\"postStart\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"touch /usr/share/nginx/html/ready /usr/share/nginx/html/live\"]}}},\"livenessProbe\":{\"failureThreshold\":2,\"httpGet\":{\"path\":\"/live\",\"port\":80},\"periodSeconds\":2},\"name\":\"web\",\"readinessProbe\":{\"failureThreshold\":1,\"httpGet\":{\"path\":\"/ready\",\"port\":80},\"periodSeconds\":2},\"resources\":{\"requests\":{\"cpu\":\"20m\",\"memory\":\"32Mi\"}}}]}}\n"
        },
        "creationTimestamp": "2026-10-13T07:37:56Z",
        "generation": 1,
        "labels": {
            "topology.kubernetes.io/region": "ap-south-1",
            "topology.kubernetes.io/zone": "ap-south-1a"
        },
        "name": "campusfix-probes",
        "namespace": "taskboard",
        "resourceVersion": "73013",
        "uid": "b1d4628d-9694-4312-98c2-74efef4616f4"
    },
    "spec": {
        "containers": [
            {
                "image": "nginx:1.28-alpine",
                "imagePullPolicy": "IfNotPresent",
                "lifecycle": {
                    "postStart": {
                        "exec": {
                            "command": [
                                "sh",
                                "-c",
                                "touch /usr/share/nginx/html/ready /usr/share/nginx/html/live"
                            ]
                        }
                    }
                },
                "livenessProbe": {
                    "failureThreshold": 2,
                    "httpGet": {
                        "path": "/live",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "name": "web",
                "readinessProbe": {
                    "failureThreshold": 1,
                    "httpGet": {
                        "path": "/ready",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-q4h2r",
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
                "name": "kube-api-access-q4h2r",
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
                "lastTransitionTime": "2026-10-13T07:37:57Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodReadyToStartContainers"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "Initialized"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:03Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "Ready"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:03Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "ContainersReady"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodScheduled"
            }
        ],
        "containerStatuses": [
            {
                "allocatedResources": {
                    "cpu": "20m",
                    "memory": "32Mi"
                },
                "containerID": "containerd://a996e49ee58d1d8d3d4c658f56a1a61c3d3b91d7f49a6a200a23c4d1dc87925d",
                "image": "docker.io/library/nginx:1.28-alpine",
                "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                "lastState": {},
                "name": "web",
                "ready": true,
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "restartCount": 0,
                "started": true,
                "state": {
                    "running": {
                        "startedAt": "2026-10-13T07:37:57Z"
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
                        "name": "kube-api-access-q4h2r",
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
        "podIP": "10.20.1.15",
        "podIPs": [
            {
                "ip": "10.20.1.15"
            }
        ],
        "qosClass": "Burstable",
        "startTime": "2026-10-13T07:37:56Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard get pod campusfix-probes -o json
{
    "apiVersion": "v1",
    "kind": "Pod",
    "metadata": {
        "annotations": {
            "kubectl.kubernetes.io/last-applied-configuration": "{\"apiVersion\":\"v1\",\"kind\":\"Pod\",\"metadata\":{\"annotations\":{},\"name\":\"campusfix-probes\",\"namespace\":\"taskboard\"},\"spec\":{\"containers\":[{\"image\":\"nginx:1.28-alpine\",\"lifecycle\":{\"postStart\":{\"exec\":{\"command\":[\"sh\",\"-c\",\"touch /usr/share/nginx/html/ready /usr/share/nginx/html/live\"]}}},\"livenessProbe\":{\"failureThreshold\":2,\"httpGet\":{\"path\":\"/live\",\"port\":80},\"periodSeconds\":2},\"name\":\"web\",\"readinessProbe\":{\"failureThreshold\":1,\"httpGet\":{\"path\":\"/ready\",\"port\":80},\"periodSeconds\":2},\"resources\":{\"requests\":{\"cpu\":\"20m\",\"memory\":\"32Mi\"}}}]}}\n"
        },
        "creationTimestamp": "2026-10-13T07:37:56Z",
        "generation": 1,
        "labels": {
            "topology.kubernetes.io/region": "ap-south-1",
            "topology.kubernetes.io/zone": "ap-south-1a"
        },
        "name": "campusfix-probes",
        "namespace": "taskboard",
        "resourceVersion": "73039",
        "uid": "b1d4628d-9694-4312-98c2-74efef4616f4"
    },
    "spec": {
        "containers": [
            {
                "image": "nginx:1.28-alpine",
                "imagePullPolicy": "IfNotPresent",
                "lifecycle": {
                    "postStart": {
                        "exec": {
                            "command": [
                                "sh",
                                "-c",
                                "touch /usr/share/nginx/html/ready /usr/share/nginx/html/live"
                            ]
                        }
                    }
                },
                "livenessProbe": {
                    "failureThreshold": 2,
                    "httpGet": {
                        "path": "/live",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "name": "web",
                "readinessProbe": {
                    "failureThreshold": 1,
                    "httpGet": {
                        "path": "/ready",
                        "port": 80,
                        "scheme": "HTTP"
                    },
                    "periodSeconds": 2,
                    "successThreshold": 1,
                    "timeoutSeconds": 1
                },
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "terminationMessagePath": "/dev/termination-log",
                "terminationMessagePolicy": "File",
                "volumeMounts": [
                    {
                        "mountPath": "/var/run/secrets/kubernetes.io/serviceaccount",
                        "name": "kube-api-access-q4h2r",
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
                "name": "kube-api-access-q4h2r",
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
                "lastTransitionTime": "2026-10-13T07:37:57Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodReadyToStartContainers"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "Initialized"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:07Z",
                "message": "containers with unready status: [web]",
                "observedGeneration": 1,
                "reason": "ContainersNotReady",
                "status": "False",
                "type": "Ready"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:38:07Z",
                "message": "containers with unready status: [web]",
                "observedGeneration": 1,
                "reason": "ContainersNotReady",
                "status": "False",
                "type": "ContainersReady"
            },
            {
                "lastProbeTime": null,
                "lastTransitionTime": "2026-10-13T07:37:56Z",
                "observedGeneration": 1,
                "status": "True",
                "type": "PodScheduled"
            }
        ],
        "containerStatuses": [
            {
                "allocatedResources": {
                    "cpu": "20m",
                    "memory": "32Mi"
                },
                "containerID": "containerd://c82147747539f37d2f187984510b8d1180e8e7156b39645e6e8a93c7e48a88fa",
                "image": "docker.io/library/nginx:1.28-alpine",
                "imageID": "docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236",
                "lastState": {
                    "terminated": {
                        "containerID": "containerd://a996e49ee58d1d8d3d4c658f56a1a61c3d3b91d7f49a6a200a23c4d1dc87925d",
                        "exitCode": 0,
                        "finishedAt": "2026-10-13T07:38:07Z",
                        "reason": "Completed",
                        "startedAt": "2026-10-13T07:37:57Z"
                    }
                },
                "name": "web",
                "ready": false,
                "resources": {
                    "requests": {
                        "cpu": "20m",
                        "memory": "32Mi"
                    }
                },
                "restartCount": 1,
                "started": true,
                "state": {
                    "running": {
                        "startedAt": "2026-10-13T07:38:07Z"
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
                        "name": "kube-api-access-q4h2r",
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
        "podIP": "10.20.1.15",
        "podIPs": [
            {
                "ip": "10.20.1.15"
            }
        ],
        "qosClass": "Burstable",
        "startTime": "2026-10-13T07:37:56Z"
    }
}
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard wait --for=condition=Ready pod/campusfix-probes --timeout=60s
pod/campusfix-probes condition met
 
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard describe pod campusfix-probes
Name:             campusfix-probes
Namespace:        taskboard
Priority:         0
Service Account:  default
Node:             ip-10-20-1-116.ap-south-1.compute.internal/10.20.1.116
Start Time:       Tue, 13 Oct 2026 13:07:56 +0530
Labels:           topology.kubernetes.io/region=ap-south-1
                  topology.kubernetes.io/zone=ap-south-1a
Annotations:      <none>
Status:           Running
IP:               10.20.1.15
IPs:
  IP:  10.20.1.15
Containers:
  web:
    Container ID:   containerd://c82147747539f37d2f187984510b8d1180e8e7156b39645e6e8a93c7e48a88fa
    Image:          nginx:1.28-alpine
    Image ID:       docker.io/library/nginx@sha256:a8b39bd9cf0f83869a2162827a0caf6137ddf759d50a171451b335cecc87d236
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Tue, 13 Oct 2026 13:08:07 +0530
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Tue, 13 Oct 2026 13:07:57 +0530
      Finished:     Tue, 13 Oct 2026 13:08:07 +0530
    Ready:          True
    Restart Count:  1
    Requests:
      cpu:        20m
      memory:     32Mi
    Liveness:     http-get http://:80/live delay=0s timeout=1s period=2s successThreshold=1 failureThreshold=2
    Readiness:    http-get http://:80/ready delay=0s timeout=1s period=2s successThreshold=1 failureThreshold=1
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-q4h2r (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-q4h2r:
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
  Type     Reason     Age                From               Message
  ----     ------     ----               ----               -------
  Normal   Scheduled  15s                default-scheduler  Successfully assigned taskboard/campusfix-probes to ip-10-20-1-116.ap-south-1.compute.internal
  Warning  Unhealthy  10s (x3 over 11s)  kubelet            spec.containers{web}: Readiness probe failed: HTTP probe failed with statuscode: 404
  Normal   Pulled     4s (x2 over 14s)   kubelet            spec.containers{web}: Container image "nginx:1.28-alpine" already present on machine and can be accessed by the pod
  Normal   Created    4s (x2 over 14s)   kubelet            spec.containers{web}: Container created
  Normal   Started    4s (x2 over 14s)   kubelet            spec.containers{web}: Container started
  Warning  Unhealthy  4s (x2 over 6s)    kubelet            spec.containers{web}: Liveness probe failed: HTTP probe failed with statuscode: 404
  Normal   Killing    4s                 kubelet            spec.containers{web}: Container web failed liveness probe, will be restarted
  Warning  Unhealthy  4s                 kubelet            spec.containers{web}: Readiness probe failed: Get "http://10.20.1.15:80/ready": dial tcp 10.20.1.15:80: connect: connection refused
 
PASS: liveness failure restarts the container and it recovers readiness.
$ kubectl --context campusfix-eks --request-timeout=20s -n taskboard delete pod campusfix-probes campusfix-load --wait=true
pod "campusfix-probes" deleted from taskboard namespace
pod "campusfix-load" deleted from taskboard namespace
 

```

Exit code: 0
