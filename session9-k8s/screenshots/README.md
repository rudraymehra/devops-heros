# Session 09 — evidence and screenshots

Fresh captures are kept by actual run date. Failed or incomplete attempts stay labeled as such; they are not completion evidence.

## Fresh run records

### [rudray-20261023-220036](rudray-20261023-220036/README.md)

- PASS. Minikube node Ready; deployment and NodePort Service created; three replicas reached Ready; the service returned v1 initially and after scale, v2 after update, and v1 after rollback.
- Pod listings show new ReplicaSet pods replacing the prior set; the service remained reachable through all stages.
- [Cluster, deployment, scale, and update](rudray-20261023-220036/01-cluster-deploy-scale-update.png)
- [Update and rollback back to v1](rudray-20261023-220036/02-rollout-rollback-v1.png)

### [rudray-20261023-215445](rudray-20261023-215445/README.md)

- Minikube node became Ready; deploy, NodePort, scale to three replicas, update to v2, and `rollout undo` all completed.
- The initial and scaled app responses showed v1; update showed v2. After rollback, the endpoint still returned v2 while old pods were terminating, so rollback is not yet verified at the app response level.
- [Cluster, deployment, and scale](rudray-20261023-215445/01-cluster-deploy-and-scale.png)
- [Image update and rollback attempt](rudray-20261023-215445/02-update-and-rollback-attempt.png)

### [rudray-20261023-213319](rudray-20261023-213319/README.md)

- Minikube profile startup and deployment creation succeeded; the initial NodePort request returned HTTP 200.
- The request during scale returned `connection reset by peer`, so update/rollback were not reached. This run is incomplete.
- [Cluster and initial scale attempt](rudray-20261023-213319/01-cluster-and-initial-scale-attempt.png)
- [Scale service reset](rudray-20261023-213319/02-scale-service-reset.png)
