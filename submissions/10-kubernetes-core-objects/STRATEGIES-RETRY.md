# Command evidence

Student: Sudhir Mehra · 24 BCS 10425 · Batch B

Captured: 2026-10-13T03:46:55.567915+00:00

Working directory: .

```text
$ uv run --with pyyaml python scripts/run-advanced-kubernetes.py --context campusfix-eks --topic strategies
$ kubectl --context campusfix-eks --request-timeout=30s create namespace campusfix-strategies
 Error from server (AlreadyExists): object is being deleted: namespaces "campusfix-strategies" already exists
 [exit: 1 ]
Traceback (most recent call last):
  File "/private/tmp/campusfix-publish/scripts/run-advanced-kubernetes.py", line 41, in <module>
    run(base + ["create", "namespace", namespace])
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/private/tmp/campusfix-publish/scripts/run-advanced-kubernetes.py", line 25, in run
    raise RuntimeError("Command failed")
RuntimeError: Command failed

```

Exit code: 1
