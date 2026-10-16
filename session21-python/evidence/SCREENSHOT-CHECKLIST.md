# Screenshot audit — Rudray Mehra

24 BCS 10425 · Batch B · 2026-10-16.

**Not all requested screenshots are captured.** This checklist distinguishes
historical runs, fresh command logs, native images, and still-missing evidence.
Image count in a friend's repository is not proof that these rubric items passed.

| Rubric | Existing evidence | Exact remaining capture/action |
|---|---|---|
| M1 application | Historical local/EKS browser screenshots | Rebuild and capture current localhost UI showing Rudray Mehra |
| M2 pytest | Original native Mac image with 24 passes; fresh 24-pass log | Fresh native image with corrected full-name heading |
| M3 Git | Historical commit-history image; meaningful repository history | Verify latest published revision and history in GitHub |
| M4 Compose | Historical execution record; current stack definition | Native `up --build`, all three services, non-root UIDs, and localhost browser |
| M5 Actions/GHCR | Earlier green run and both package screenshots | Verify green run/images for the new revision; capture SHA tags |
| M6 Trivy | Earlier green gates and written explanation | Actual report screenshot for BOTH images; workflow now prints both reports |
| M7 Terraform plan | Complete original plan log and labelled rendered excerpt | Native plan output; optional helper flag runs a fresh read-only plan |
| M7 AWS Console | Original CLI VPC/EKS descriptions | No authenticated live Console captures exist; old lab was destroyed |
| M7 Terraform destroy | Original successful destroy log and labelled excerpt | Original native capture was not taken; do not represent a new empty-state destroy as the original teardown |
| M8 Kubernetes | Original Pods/Services/Helm/Ingress logs and EKS browser image | Native live `get pods`, `get svc`, `helm list`, ingress browser; explicit live context required |
| M9 metrics | Original metrics data and actual Prometheus/Grafana browser captures | Native curl metrics; original cluster screenshots remain historical |
| M10 presentation | README, presentation outline, automated app recordings | Student's narrated change → pipeline → deployment demo, live or recorded |

## Capture real local output on the Mac

Open Docker Desktop and maximize Terminal. From the repository root:

```bash
/opt/homebrew/bin/python3.13 session21-python/scripts/capture-native-evidence.py \
  --screenshots --compose \
  --terraform /private/tmp/campusfix-tools.FCoLVB/terraform
```

This exact Terraform path is the student's previously downloaded local tool, not
a portable dependency. On another machine, install Terraform and use its PATH
entry or provide a valid `--terraform` path. Python must be the working Homebrew
3.13 interpreter, not the previously broken standalone symlink.

The helper:

1. Runs real isolated API tests, the frontend build, Helm lint and Terraform validation.
2. Checks Docker with a 20-second timeout. If unavailable, records the error and
   skips dependent work; it does not hang forever or delete Docker data.
3. Builds/starts only Compose project `campusfix`, then shows actual service
   status, non-root users, Alembic revision, health/readiness/API and metrics.
4. Prints Rudray Mehra, roll and batch above/below actual command output.
5. Asks you to select the specific Terminal window using native macOS capture.
   Do not select a private window or desktop. Maximize/zoom out enough to include
   the command and result. Press `s` to skip, or Escape to cancel a capture.
6. Opens localhost:3000 for a separate browser-window capture. Confirm the current
   app profile says Rudray Mehra. Existing database reports are not rewritten;
   if you need new examples, create a clearly synthetic report under the correct
   name and filter to it. Do not relabel someone else's records.
7. Saves a new timestamped directory under `evidence/terminal/`, with an index,
   untouched PNGs, command logs, exit codes and SHA-256 checksums. Old runs are
   never overwritten. Review every image: selecting the wrong window does not
   satisfy the rubric even when a PNG file was created.

macOS may request Screen Recording permission for Terminal. If it denies access,
allow it in System Settings → Privacy & Security → Screen Recording (or Screen &
System Audio Recording), reopen Terminal if macOS asks, then rerun. Do not
disable macOS security. Only the selected window is captured.

The helper keeps the local database volume and leaves the stack running for the
demo. Afterward, from `session21-python`, run `docker compose -p campusfix down`
to stop it while keeping data. Do not add `-v` unless you intend to erase reports.

## Optional real infrastructure evidence

- Add `--terraform-plan` after logging in to AWS locally to run a real **read-only**
  plan. No `apply` or `destroy` is executed. A plan is not proof of provisioned AWS
  resources, and `validate` alone is not a plan.
- Add `--kube-context rudray-devops` only if that local cluster is already running
  with CampusFix deployed. It collects read-only Pod/Deployment/Service/Ingress
  and Helm output. Check all app Pods are Running, both Deployments have at least
  two ready replicas, and the Helm release is deployed. An empty `get`/`list`
  returning exit 0 is not a completed deployment.
- The helper does not create a cluster or restart a paid AWS lab. Capturing a new
  live VPC/EKS Console view would require a separately approved new cloud run and
  cleanup, or instructor acceptance of the existing historical CLI evidence.

## CI/security screenshot steps

1. Open [CampusFix Actions](https://github.com/rudraymehra/devops-heros/actions/workflows/session21-capstone.yml).
2. Select the run for the exact commit being submitted; do not confuse an older
   green run with verification of the newest changes.
3. Open each `build-scan-push` matrix job (backend and frontend), then expand
   **Display actual Trivy report for screenshot evidence**. Capture its real
   report and the run URL/SHA. This step becomes available after this update is
   pushed; existing historical runs cannot gain a new step retroactively.
4. Capture both published GHCR package pages and their commit-SHA tags.
   Do not infer publication merely from a successful build.

For old runs, the `trivy-backend` and `trivy-frontend` artifacts contain the actual
reports. Preserve the run URL and commit provenance if displaying those files.
See [security explanation](../security/README.md).

## Current automation limitation

In this editing session, macOS Terminal access was denied and the approval service
failed with HTTP 404; native GUI capture could not execute. Docker explicitly
returned socket `operation not permitted`. Terraform provider handshakes failed
in this sandbox. None of those failures is labelled a successful current run.
The [fresh local verification](terminal/rudray-local-verification-2026-10-16/README.md)
contains actual passing test/build/lint logs and the failed validation output,
**not newly captured screenshots**. Run the helper interactively on the Mac to
collect native evidence, then review it before publishing.
