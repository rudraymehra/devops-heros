# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T07:39:26.053015+00:00

Working directory: .

```text
$ bash session21-python/scripts/cleanup-cloud.sh
No resources found
NAMESPACE   NAME                      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS    VOLUMEATTRIBUTESCLASS   AGE
taskboard   taskboard-postgres-data   Bound    pvc-2c1c6543-f3b2-45d2-91d4-eb3e1ee0a8ce   5Gi        RWO            campusfix-gp3   <unset>                 4h
application.argoproj.io "campusfix" deleted from argocd namespace
release "taskboard" uninstalled
namespace "taskboard" deleted
persistentvolume/pvc-2c1c6543-f3b2-45d2-91d4-eb3e1ee0a8ce condition met
No resources found
No resources found
[]
[]
Kubernetes-created disk and load balancer removed. Terraform teardown can proceed.

```

Exit code: 0
