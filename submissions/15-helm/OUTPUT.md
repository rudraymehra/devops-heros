# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:57:55.106290+00:00

Working directory: .

```text
$ uv run --with pyyaml python scripts/run-advanced-kubernetes.py --context campusfix-eks --topic helm
$ kubectl --context campusfix-eks --request-timeout=30s create namespace campusfix-helm
namespace/campusfix-helm created
  [exit: 0 ]
$ helm lint session-15-helm/mini-project/notes-chart
==> Linting session-15-helm/mini-project/notes-chart
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm install notes session-15-helm/mini-project/notes-chart --set image.tag=1.28-alpine --wait --timeout 3m
NAME: notes
LAST DEPLOYED: Tue Oct 13 09:27:37 2026
NAMESPACE: campusfix-helm
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm upgrade notes session-15-helm/mini-project/notes-chart --set image.tag=1.28-alpine --set replicaCount=2 --wait --timeout 3m
Release "notes" has been upgraded. Happy Helming!
NAME: notes
LAST DEPLOYED: Tue Oct 13 09:27:40 2026
NAMESPACE: campusfix-helm
STATUS: deployed
REVISION: 2
DESCRIPTION: Upgrade complete
TEST SUITE: None
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm history notes
REVISION	UPDATED                 	STATUS    	CHART            	APP VERSION	DESCRIPTION     
1       	Tue Oct 13 09:27:37 2026	superseded	notes-chart-0.1.0	1.0        	Install complete
2       	Tue Oct 13 09:27:40 2026	deployed  	notes-chart-0.1.0	1.0        	Upgrade complete
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-helm get deployments,services,configmaps
NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/notes-deploy   2/2     2            2           6s

NAME                TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/notes-svc   NodePort   172.20.76.80   <none>        80:30090/TCP   6s

NAME                         DATA   AGE
configmap/kube-root-ca.crt   1      8s
configmap/notes-config       2      6s
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm rollback notes 1 --wait --timeout 3m
Rollback was a success! Happy Helming!
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm history notes
REVISION	UPDATED                 	STATUS    	CHART            	APP VERSION	DESCRIPTION     
1       	Tue Oct 13 09:27:37 2026	superseded	notes-chart-0.1.0	1.0        	Install complete
2       	Tue Oct 13 09:27:40 2026	superseded	notes-chart-0.1.0	1.0        	Upgrade complete
3       	Tue Oct 13 09:27:44 2026	deployed  	notes-chart-0.1.0	1.0        	Rollback to 1   
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s -n campusfix-helm get deployments
NAME           READY   UP-TO-DATE   AVAILABLE   AGE
notes-deploy   1/1     1            1           9s
  [exit: 0 ]
$ helm --kube-context campusfix-eks -n campusfix-helm uninstall notes --wait
release "notes" uninstalled
  [exit: 0 ]
$ kubectl --context campusfix-eks --request-timeout=30s delete namespace campusfix-helm --wait=true --timeout=180s
namespace "campusfix-helm" deleted
  [exit: 0 ]
All checks in helm passed; temporary namespace removed.

```

Exit code: 0
