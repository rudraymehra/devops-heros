# Session 10 screenshots

## Task 1: deployment strategies

- [01-rolling-update.png](rudray-20261023-222751/01-rolling-update.png)
- [02-blue-green-and-canary.png](rudray-20261023-222751/02-blue-green-and-canary.png)
- [03-canary-promotion-and-recreate.png](rudray-20261023-222751/03-canary-promotion-and-recreate.png)
- [04-recreate-and-cleanup.png](rudray-20261023-222751/04-recreate-and-cleanup.png)

The captures are native terminal screenshots from the live Minikube run on 2026-10-23. The final capture shows all four strategy demonstrations passed and isolated-profile cleanup.

## Task 2: Pod lifecycle

The native terminal captures show the twelve lifecycle cases from the isolated Minikube run on 2026-10-23. The liveness output records failed probes and the kubelet restart action; its snapshot preceded the restart counter increment.

- [01-running-and-pending.png](rudray-20261023-224618/01-running-and-pending.png)
- [02-completed-failed-crashloop-imagepull.png](rudray-20261023-224618/02-completed-failed-crashloop-imagepull.png)
- [03-readiness-liveness-startup.png](rudray-20261023-224618/03-readiness-liveness-startup.png)
- [04-startup-init-multicontainer.png](rudray-20261023-224618/04-startup-init-multicontainer.png)
- [05-init-multicontainer-termination-cleanup.png](rudray-20261023-224618/05-init-multicontainer-termination-cleanup.png)
