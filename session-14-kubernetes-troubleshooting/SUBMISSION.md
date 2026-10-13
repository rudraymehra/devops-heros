# Session 14 Submission

The numbered labs cover `get`, `describe`, `logs`, `exec`, events,
CrashLoopBackOff, ImagePullBackOff, Pending Pods, Service selectors, and DNS. The
`scenarios/` directory provides five deliberate failures, while `mini-project/`
combines Pod and Service diagnosis.

## Required troubleshooting record

| Problem | Symptom | Diagnostic command | Root cause | Fix |
|---|---|---|---|---|
| CrashLoopBackOff | Repeated restarts | `kubectl logs --previous` | Process exits unsuccessfully | Correct command/configuration |
| ImagePullBackOff | Image cannot be downloaded | `kubectl describe pod` | Invalid image or registry access | Correct image/tag or pull secret |
| Pending | Pod is unscheduled | `kubectl describe pod` | Unsatisfied resources/constraints | Correct requests or provide capacity |
| Service has no endpoints | Requests time out | `kubectl get endpoints` | Selector does not match Pod labels | Align selector and labels |
| DNS failure | Name does not resolve | `nslookup`, CoreDNS logs | Wrong name/policy/DNS health | Correct name or DNS/network policy |

Replace the generic observations above with the exact event text from your lab run.

## Evidence checklist

- [ ] Before/after status for every scenario
- [ ] Relevant events and logs
- [ ] Root cause stated in your own words
- [ ] Corrected resource and successful verification
