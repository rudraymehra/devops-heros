# Session 15 Submission

The numbered directories demonstrate chart structure, values, templates, install,
upgrade, history, rollback, and application deployment. `mini-project/notes-chart`
is the final chart with development and production values.

```bash
helm lint mini-project/notes-chart
helm template notes-dev mini-project/notes-chart
helm upgrade --install notes-dev mini-project/notes-chart
helm upgrade notes-dev mini-project/notes-chart \
  -f mini-project/notes-chart/values-prod.yaml
helm history notes-dev
helm rollback notes-dev 1
helm status notes-dev
helm uninstall notes-dev
```

## Evidence checklist

- [x] Successful lint and rendered YAML
- [x] Installed release and running Pod
- [x] Development-to-production upgrade
- [x] Revision history and rollback
- [x] Final cleanup

## Run notes

- `helm lint` passed with only the optional chart icon recommendation.
- The release upgraded from one development replica to three production replicas.
- A deliberately invalid image tag produced `ErrImagePull`; rollback to revision 2
  restored three Ready Pods. Helm history recorded the rollback as revision 4.
- `helm uninstall notes-dev` removed the release. The remaining Minikube Pods belong
  to Session 12 and were left running.
