# Submission verification

Name: Rudray Mehra
Enrollment number: 10425

## Existing evidence

The repository already contained the original Linux, shell, networking, Git and Docker outputs. Those records are preserved and have not been relabelled as fresh executions.

## Runtime prerequisites

Docker check performed during this review:

```console
$ docker version --format '{{.Server.Version}}'
Cannot connect to the Docker daemon at unix:///Users/rudraym/.docker/run/docker.sock. Is the docker daemon running?
```

The configured Minikube API also refused connections. New Kubernetes manifests are accompanied by an executable runner, but a successful cluster execution is not claimed. Docker networking still needs screenshots of the running exercises.

## Checks in this review

- **Passed:** all 20 new Kubernetes objects validate against the standalone strict Kubernetes v1.32 JSON schemas. This verifies document structure, not admission or runtime behaviour on a cluster.
- **Passed:** workload selectors match template labels, namespaced resources use `rudray-devops-hw`, and embedded Python application code parses successfully.
- **Passed:** 32 submission file links resolve in the checkout.
- **Passed:** Bash syntax check and Python runner compilation.
- **Passed:** shell script tests for directory names containing spaces, correct process count, EOF/default input, rejected file-path traversal and directory creation errors.
- **Passed:** `git diff --check`.

The shell functional checks used a controlled `ps` stub. The environment blocked the real `/bin/ps` with `Operation not permitted`, so these checks validate script input/error/file behaviour rather than live host process output. No stub output is presented as assignment execution evidence.

The Kubernetes runner has not completed a cluster run. Static schema checks do not prove image pulls, scheduling, service routing or ingress behaviour.
