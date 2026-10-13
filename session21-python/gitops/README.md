# CampusFix GitOps

Argo CD watches this repository's Helm chart and `gitops/values.yaml`.
The Application lives outside the rendered chart, preventing recursive ownership.
`selfHeal` corrects drift; automatic pruning is disabled to protect lab storage.

After the repository is published and the images are loaded into the local cluster:

```bash
kubectl --context sudhir-devops apply -f session21-python/gitops/application.yaml
kubectl --context sudhir-devops get application campusfix -n argocd
kubectl --context sudhir-devops get pods -n taskboard
```

For GHCR deployment, put the passed pipeline's immutable commit SHA in both image
tags and use `ghcr.io/rudraymehra/campusfix-backend` and
`ghcr.io/rudraymehra/campusfix-frontend`. Commit that change. A successful sync
then reconciles the release. In a production cluster, supply the database and
registry Secrets outside Git and enable the EKS storage class from production values.

Choose either Argo CD or the manual CI deployment for a namespace. Running both
against different values causes Argo CD to undo imperative CI changes.
