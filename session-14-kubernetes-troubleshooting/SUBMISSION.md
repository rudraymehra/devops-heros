# Session 14 Submission

The numbered labs cover `get`, `describe`, `logs`, `exec`, events,
CrashLoopBackOff, ImagePullBackOff, Pending Pods, Service selectors, and DNS. The
`scenarios/` directory provides five deliberate failures, while `mini-project/`
combines Pod and Service diagnosis.

## Required troubleshooting record

| Problem | Symptom | Diagnostic command | Root cause | Fix |
|---|---|---|---|---|
| CrashLoopBackOff | `crash-demo` restarted; gauntlet Pod logged `[FATAL ERROR]: DATABASE_URL environment variable is MISSING!` | `kubectl logs --previous`, `kubectl describe pod` | Required `DATABASE_URL` was absent; the demo Pod also explicitly exited with code 1 | Set the env var or correct the failing command; fixed Pods reached `Running` |
| ImagePullBackOff | `ErrImagePull` then `ImagePullBackOff` | `kubectl describe pod` | Image/tag was unavailable; event included `pull access denied, repository does not exist` | Change to `nginx:1.27`; fixed Pods reached `Running` |
| Pending | `pending-demo` and gauntlet Pod stayed unscheduled | `kubectl describe pod` | Invalid node selector in `pending-demo`; gauntlet request exceeded available CPU and memory | Remove the invalid selector or lower requests; fixed Pods reached `Running` |
| Service has no endpoints | Endpoint list showed `<none>` and wget returned `Connection refused` | `kubectl get endpoints`, `kubectl get pods --show-labels`, `kubectl describe service` | Service selector did not match Pod label (`wrong-app` vs `troubleshooting-app`) | Restore matching selector; two endpoints returned and NGINX responded |
| DNS failure | curl returned exit code 6: `Could not resolve host: postgres-db-wrong-name.production.svc.cluster.local` | `curl -v`, `nslookup`, CoreDNS Pod/log checks | The requested Service hostname was incorrect; DNS resolved the valid `web-service.default.svc.cluster.local` name | Use the valid Service FQDN; DNS resolution and HTTP response succeeded |
| OOMKilled | Container's last termination reason was `OOMKilled`, exit code `137` | `kubectl get pod -o jsonpath=...`, `kubectl describe pod` | Process allocated about 200 MB with a `20Mi` memory limit | Use a bounded workload and suitable memory limit; corrected Pod reached `Running` |

Replace the generic observations above with the exact event text from your lab run.

## Evidence checklist

- [x] Before/after status for every scenario
- [x] Relevant events and logs
- [x] Root cause stated in your own words
- [x] Corrected resource and successful verification

## Run notes

- The working Service selector in `09-service-dns-troubleshooting/service.yaml`
  is `app: web`, matching the Deployment labels. The deliberately broken selector
  remains in `broken-service.yaml` for the failure demonstration.
- The DNS test Pod uses `busybox:1.36` because the referenced `dnsutils:1.3` image
  was unavailable from the registry during this run; BusyBox provides `nslookup`.
- Five corrected gauntlet manifests are in each `scenarios/scenario-*/fixed.yaml`.
