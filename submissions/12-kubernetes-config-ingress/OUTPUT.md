# Executed Kubernetes lab output

Context: `campusfix-eks`. Namespace: `rudray-devops-hw`.

```console
$ kubectl --context campusfix-eks --request-timeout=30s apply -f submissions/09-kubernetes-fundamentals/namespace.yaml
namespace/rudray-devops-hw unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/12-kubernetes-config-ingress/configmap.yaml
configmap/homework-config unchanged
configmap/homework-pages unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/12-kubernetes-config-ingress/secret.yaml
secret/homework-db configured
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/12-kubernetes-config-ingress/app.yaml
deployment.apps/homework-frontend unchanged
deployment.apps/homework-backend unchanged
service/homework-frontend unchanged
service/homework-backend unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw apply -f submissions/12-kubernetes-config-ingress/ingress.yaml
ingress.networking.k8s.io/homework-ingress unchanged
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/homework-frontend --timeout=180s
deployment "homework-frontend" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw rollout status deployment/homework-backend --timeout=180s
deployment "homework-backend" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw get configmaps,secrets,deployments,services,ingresses
NAME                         DATA   AGE
configmap/homework-config    3      13m
configmap/homework-pages     1      13m
configmap/kube-root-ca.crt   1      18m

NAME                 TYPE     DATA   AGE
secret/homework-db   Opaque   3      13m

NAME                                READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/deployment-web      3/3     3            3           17m
deployment.apps/homework-backend    2/2     2            2           13m
deployment.apps/homework-frontend   2/2     2            2           13m
deployment.apps/service-web         2/2     2            2           17m

NAME                        TYPE           CLUSTER-IP       EXTERNAL-IP                                                               PORT(S)        AGE
service/external-docs       ExternalName   <none>           kubernetes.io                                                             <none>         17m
service/homework-backend    ClusterIP      172.20.114.137   <none>                                                                    80/TCP         13m
service/homework-frontend   ClusterIP      172.20.213.198   <none>                                                                    80/TCP         13m
service/web-clusterip       ClusterIP      172.20.221.62    <none>                                                                    80/TCP         17m
service/web-headless        ClusterIP      None             <none>                                                                    80/TCP         17m
service/web-loadbalancer    LoadBalancer   172.20.158.123   afc147309a5ce41248aa0272f3b8e839-278856017.ap-south-1.elb.amazonaws.com   80:32103/TCP   17m
service/web-nodeport        NodePort       172.20.64.104    <none>                                                                    80:32455/TCP   17m

NAME                                         CLASS   HOSTS            ADDRESS         PORTS   AGE
ingress.networking.k8s.io/homework-ingress   nginx   homework.local   172.20.98.234   80      13m
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw describe secret homework-db
Name:         homework-db
Namespace:    rudray-devops-hw
Labels:       <none>
Annotations:  <none>

Type:  Opaque

Data
====
DB_NAME:      11 bytes
DB_PASSWORD:  29 bytes
DB_USER:      13 bytes
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- printenv ENVIRONMENT
production
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- printenv DEFAULT_CURRENCY
INR
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- printenv DB_USER
homework_user
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- python3 -c 'import os; print("DB_PASSWORD present:", bool(os.environ.get("DB_PASSWORD")))'
DB_PASSWORD present: True
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw describe ingress homework-ingress
Name:             homework-ingress
Labels:           <none>
Namespace:        rudray-devops-hw
Address:          172.20.98.234
Ingress Class:    nginx
Default backend:  <default>
Rules:
  Host            Path  Backends
  ----            ----  --------
  homework.local  
                  /api   homework-backend:80 (10.20.1.70:5000,10.20.2.198:5000)
                  /      homework-frontend:80 (10.20.1.60:80,10.20.2.204:80)
Annotations:      <none>
Events:
  Type    Reason  Age                From                      Message
  ----    ------  ----               ----                      -------
  Normal  Sync    12m (x2 over 13m)  nginx-ingress-controller  Scheduled for sync
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n ingress-nginx rollout status deployment/ingress-nginx-controller --timeout=180s
deployment "ingress-nginx-controller" successfully rolled out
[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- python3 -c 'import urllib.request; r=urllib.request.Request("http://ingress-nginx-controller.ingress-nginx.svc.cluster.local/", headers={"Host":"homework.local"}); print(urllib.request.urlopen(r, timeout=15).read().decode())'
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>DevOps Homework</title></head>
<body><h1>Hello World from Kubernetes</h1><p>Rudray Mehra — 10425</p></body></html>

[exit status: 0]
```

```console
$ kubectl --context campusfix-eks --request-timeout=30s -n rudray-devops-hw exec deployment/homework-backend -- python3 -c 'import urllib.request; r=urllib.request.Request("http://ingress-nginx-controller.ingress-nginx.svc.cluster.local/api/health", headers={"Host":"homework.local"}); print(urllib.request.urlopen(r, timeout=15).read().decode())'
{"message": "Hello World from Kubernetes backend", "path": "/api/health", "environment": "production", "currency": "INR", "db_user": "homework_user", "db_password_present": true}
[exit status: 0]
```

All checks in this topic completed successfully.
