# Sessions 1–20: evidence and native screenshot capture

**Rudray Mehra · 24 BCS 10425 · Batch B**

[Session-by-session audit](evidence/coursework/README.md) ·
[All submission README links](SUBMISSION-GUIDE.md)

All **19 homework entry points** (Sessions 1 and 2 share one) were compared against
the **179 images** in Vivek's supplied ZIP. Every session now has a `screenshots/`
page listing the exact reference filenames, our core implementation files,
our existing historical evidence, fresh command results and remaining capture gaps.
No reference image was copied, retouched or used as evidence of Rudray's execution.

## What was actually verified in this update

- Local hard/symbolic links passed on macOS, explicitly not described as Linux VM evidence.
- The shell script passes syntax checking. Its actual run is blocked here by macOS
  process-inspection permissions; no process-list screenshot is claimed.
- Git `commit -a` and cherry-pick exercises passed in a newly created disposable
  repository, with Rudray Mehra as the actual local commit author. The coursework
  repository's existing Git history/index was not used for that exercise.
- The Session 15 notes chart passes Helm lint and renders correctly; that is not
  an install/upgrade/rollback demonstration.
- All **5 Session 16 calculator tests pass**.
- Session 17 Bandit scanning completes with no issues identified. Its unit suite
  could not collect because Flask is missing from the selected local interpreter;
  that failure is recorded, not treated as a test pass. No new pip-audit/Trivy
  result is asserted without an actual scan.
- Both Sessions 18 and 19 pass Terraform format checks. Provider-schema handshakes
  fail in the editing sandbox, so fresh validation is marked failed/blocked.
- [42 Python/shell source files](evidence/coursework/source-syntax.md) pass non-executing
  syntax checks. All three homework workflow files pass actionlint.
- The 8 coursework-audit tests and 9 native-recorder tests pass. The recorder now
  rejects `Operation not permitted` even when a macOS command returns exit 0.

**No new native screenshots were captured by this editing session.** macOS Terminal
access and Docker access are restricted, and the approval service previously
failed with HTTP 404. Native PNGs must be taken in the user's interactive Terminal.
Raw LAN-neighbour output was withheld from publication; the narrower default-route
check is used instead. No private process arguments or decoded credentials are
needed in screenshots.

## One command for genuine local screenshots

Open Terminal and maximize it. From the repository root:

```bash
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py run --screenshots \
  --terraform /private/tmp/campusfix-tools.FCoLVB/terraform
```

The working Homebrew Python 3.13 and previously downloaded Terraform paths above
are specific to this Mac. The helper runs actual commands, prints Rudray's name,
roll and batch, then asks you to select **only the relevant Terminal window**.
Press Enter and click the window; `s` skips a screenshot. Keep the command and
result visible, and check no private information appears. macOS may request
Screen Recording permission for Terminal in System Settings.

Files go to a separate timestamped directory inside each submission's
`screenshots/` folder. Logs, exit codes, untouched native PNGs and SHA-256 checksums
are retained together. The session pages embed captured PNGs automatically.
Selecting the wrong window can still create a PNG, so review each image yourself.
An error screenshot documents a failure; it does not complete that exercise.

For fewer prompts, choose sessions:

```bash
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py run \
  --screenshots --sessions 01-02,03,04,05,15,16
```

## Docker screenshots (Sessions 6–8)

Open Docker Desktop first, then add `--docker-labs`:

```bash
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py run \
  --sessions 06,07,08 --screenshots --docker-labs
```

This builds and requests the six Hello World apps and the multi-stage app, offers
browser-window captures, then stops/removes only the uniquely named temporary
containers it created. Images remain for reuse. Session 8 starts its dedicated
`rudray-hw08` Compose project, captures networks/connectivity, and stops it while
preserving the database volume. It never prunes Docker or deletes unrelated work.
The host-network and bind-mount-change exercises remain separately identified gaps.

At the latest check, the Mac had only about **6.9 GiB free**. The helper requires
8 GiB free before these image builds. Free space deliberately first; this tool does
not erase anything to make room. Do not delete Docker's disk image to force it.
If interrupted during Session 8, stop only this lab with:

```bash
docker compose -p rudray-hw08 -f session8-docker-networking-volume/demo/docker-compose.yml down
```

## Kubernetes, Helm and monitoring screenshots

To read an **existing** local homework cluster, explicitly supply its context:

```bash
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py run \
  --sessions 09,10,11,12,13,14,15,20 --screenshots --kube-context devops-homework
```

The helper does not create a cluster or overwrite historical `OUTPUT.md` files.
It captures current state only. Empty lists, missing namespaces, a successful
`kubectl get`, or Helm lint alone do not prove the exercise succeeded. Actual
lifecycle/rollout/failure/recovery/scaling sequences still need their own runs.
The original EKS lab was destroyed, including temporary troubleshooting/Helm
namespaces. Do not expect a fresh cluster or empty context to contain them.

Session 20's real historical Prometheus/Grafana/Argo images are linked directly
from its evidence page. Do not change their pixels or timestamps. Extra reference
items such as cAdvisor and firing/recovering alerts are not certified by those
three images.

## Session 17 local dependencies

The helper accepts `--python17 /path/to/python` for an interpreter with the project
requirements, pytest and Bandit installed. If no project environment exists yet,
create a new one only after checking that `.venv` is absent:

```bash
cd session-17-devsecops/demo
/opt/homebrew/bin/python3.13 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt bandit pip-audit
cd ../..
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py run --sessions 17 \
  --screenshots --python17 /Users/rudraym/devops-heros/session-17-devsecops/demo/.venv/bin/python
```

These dependency downloads require working network access. Do not claim a clean
SCA or Trivy scan based only on Bandit; they check different things. Use the actual
GitHub Actions steps/artifacts for each gate and the exact submitted commit SHA.

## AWS and publication

The Session 18 S3 and Session 19 VPC/EC2/S3 labs have their own actual historical
apply/destroy logs, but native screenshots were not taken during those runs.
The capture helper never applies/destroys AWS resources, and a new empty-state
destroy would not prove the original teardown. New paid runs require separate
approval, or the instructor must accept the existing log format.

After checking new screenshots, ask for their review and inclusion in the publishing
clone. Running the capture helper does **not** automatically commit or push PNGs.
The push command provided with this update publishes only the already committed
revision; captures made afterward require another reviewed commit.

To refresh the inventory without executing labs:

```bash
/opt/homebrew/bin/python3.13 scripts/coursework-evidence.py audit
```

Historical identities and logs are preserved. New commands and current instructions
use Rudray Mehra. File presence, a filename matching Vivek's ZIP, or a generated
log view is never counted as a completed native screenshot.
