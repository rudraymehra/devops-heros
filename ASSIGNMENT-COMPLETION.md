# Assignment completion and verification
Sudhir Mehra · 24 BCS 10425 · Batch B · rudray.24bcs10425@sst.scaler.com

All 20 form fields have source files and submission README entry points.
Implementation coverage does not mean every requested runtime screenshot exists.
See [submission links and instructions](SUBMISSION-GUIDE.md) and [sources](SOURCES.md).

## Verified during this work (2026-10-13)
- CampusFix: 24 API tests passed; [actual pytest output](session21-python/evidence/pytest.md).
- Docker Compose ran the PostgreSQL, API and frontend stack.
- Desktop/mobile browser exercised create, edit, resolve, reopen, search and delete,
  including preservation of an unsaved draft on a server error.
  [Screenshots, video and result](session21-python/evidence/browser/).
- Backend/frontend images passed HIGH/CRITICAL Trivy checks locally.
- Frontend production build, backend dependency audit, Bandit, Gitleaks,
  Helm rendering and GitHub Actions lint passed locally.
- AWS Terraform plan and apply created the EKS lab; the first failed attempt and
  successful retry are both preserved in [cloud evidence](session21-python/evidence/).
- Kubernetes sessions 9 and 10 ran on EKS: see their OUTPUT.md files.
- Earlier homework evidence and student Git history are retained; they are not
  presented as fresh executions.

## In progress / not yet claimed complete
- Published GitHub Actions runs and SHA-tagged GHCR images.
- EKS application, remaining Kubernetes labs, monitoring and GitOps runtime checks.
- AWS teardown confirmation.
- Exact screenshot-only rubric requirements where only terminal text is available.

## Student-only final steps
Give the narrated presentation/live demonstration described in
[the speaking guide](session21-python/PRESENTATION.md), review the evidence and
submit the [Section B form](https://forms.gle/pAuXQaokwVzhRzit6).
The automated browser video is not a narrated student presentation.
