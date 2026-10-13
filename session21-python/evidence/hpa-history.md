# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:34:11.008037+00:00

Working directory: .

```text
$ kubectl --context campusfix-eks describe hpa taskboard-backend -n taskboard
Name:                                                  taskboard-backend
Namespace:                                             taskboard
Labels:                                                app.kubernetes.io/managed-by=Helm
Annotations:                                           argocd.argoproj.io/tracking-id: campusfix:autoscaling/HorizontalPodAutoscaler:taskboard/taskboard-backend
                                                       meta.helm.sh/release-name: taskboard
                                                       meta.helm.sh/release-namespace: taskboard
CreationTimestamp:                                     Tue, 13 Oct 2026 09:07:38 +0530
Reference:                                             Deployment/taskboard-backend
Metrics:                                               ( current / target )
  resource cpu on pods  (as a percentage of request):  2% (2m) / 60%
Min replicas:                                          2
Max replicas:                                          6
Deployment pods:                                       2 current / 2 desired
Conditions:
  Type            Status  Reason            Message
  ----            ------  ------            -------
  AbleToScale     True    ReadyForNewScale  recommended size matches current size
  ScalingActive   True    ValidMetricFound  the HPA was able to successfully calculate a replica count from cpu resource utilization (percentage of request)
  ScalingLimited  True    TooFewReplicas    the desired replica count is less than the minimum replica count
Events:           <none>

```

Exit code: 0
