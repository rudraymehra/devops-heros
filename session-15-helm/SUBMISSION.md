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

- [ ] Successful lint and rendered YAML
- [ ] Installed release and running Pod
- [ ] Development-to-production upgrade
- [ ] Revision history and rollback
- [ ] Final cleanup
