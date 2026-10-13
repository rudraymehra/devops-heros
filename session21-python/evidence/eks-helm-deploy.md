# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:39:54.790932+00:00

Working directory: .

```text
$ helm upgrade --install taskboard session21-python/helm/taskboard --namespace taskboard --create-namespace -f session21-python/helm/taskboard/values-prod.yaml --set backend.tag=0a1c12a5cbb3bb649b77f1be3b515357eca0d30e --set frontend.tag=0a1c12a5cbb3bb649b77f1be3b515357eca0d30e --wait --timeout 5m
Release "taskboard" does not exist. Installing it now.
NAME: taskboard
LAST DEPLOYED: Tue Oct 13 09:07:35 2026
NAMESPACE: taskboard
STATUS: deployed
REVISION: 1
DESCRIPTION: Install complete
TEST SUITE: None

```

Exit code: 0
