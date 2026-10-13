# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:33:17.764865+00:00

Working directory: .

```text
$ kubectl --context campusfix-eks get hpa,pods -n taskboard -o wide
NAME                                                    REFERENCE                      TARGETS       MINPODS   MAXPODS   REPLICAS   AGE
horizontalpodautoscaler.autoscaling/taskboard-backend   Deployment/taskboard-backend   cpu: 2%/60%   2         6         2          3h55m

NAME                                      READY   STATUS      RESTARTS   AGE     IP            NODE                                         NOMINATED NODE   READINESS GATES
pod/campusfix-load                        0/1     Completed   0          3h45m   10.20.1.15    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/taskboard-backend-b6b57c5cf-9sn7x     1/1     Running     0          3h55m   10.20.1.224   ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/taskboard-backend-b6b57c5cf-d26md     1/1     Running     0          3h55m   10.20.2.198   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/taskboard-frontend-66967b946f-69khs   1/1     Running     0          3h55m   10.20.1.60    ip-10-20-1-116.ap-south-1.compute.internal   <none>           <none>
pod/taskboard-frontend-66967b946f-qpkbd   1/1     Running     0          3h55m   10.20.2.204   ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>
pod/taskboard-postgres-5c4567ddcb-9tzpd   1/1     Running     0          3h45m   10.20.2.55    ip-10-20-2-64.ap-south-1.compute.internal    <none>           <none>

```

Exit code: 0
