# Reference comparison — Rudray Mehra

24 BCS 10425 · Batch B · Compared on 2026-10-16.

The supplied `Devops_Final_Assignment_N_Project-main.zip` was inspected as a
reference, not imported as CampusFix execution evidence. It contains 204 image
files across the coursework, including 25 in its capstone.

Archive SHA-256: `bba4a044dbe172e2371ea91d45c3cc2bddca5f02f95e1512d79760fb9d17698a`.
Its archive comment identifies commit `a96f00cdd6bcd4d827ae6f3d129dea31d68c971d`.

## Important capstone differences

| Area | Supplied ZIP: TaskBoard Lite | This submission: CampusFix |
|---|---|---|
| Domain | General task board | Campus maintenance reports, repair workflow and activity history |
| Backend | Flask | FastAPI |
| Frontend | Server-rendered HTML | React, built separately and served by Nginx |
| Database | SQLite | PostgreSQL with Alembic migrations; isolated SQLite only for API tests |
| Tests | README records 17 passing tests | 24 passing tests; user's native Mac screenshot retained |
| Compose | App, Prometheus and Grafana | Frontend, backend and PostgreSQL |
| Terraform | EC2, S3, VPC and one public subnet; no EKS resource/module in capstone main.tf | EKS, managed worker nodes, VPC with two public/two private subnets and EBS CSI |
| Kubernetes environment | Colima/Minikube in the reference records | Local lab and actual AWS EKS lab recorded separately |
| Identity | ZIP identifies Vivek Singh Solanki, 24bcs10338 | Rudray Mehra, 24 BCS 10425, Batch B |

The supplied rubric specifically asks for FastAPI, a separate frontend/backend,
PostgreSQL/Alembic and EKS. Images of the reference's stack do not demonstrate
those CampusFix requirements, even if sharing the reference is permitted.

The inspected `04-docker-compose-01.png` also includes a port-9090 allocation
failure. It cannot serve as evidence that all three CampusFix services started.
No reference image has been renamed, retouched or included as a CampusFix run.

## Coursework coverage

The ZIP contains session folders for all 20 submission fields (Sessions 1 and 2
share a field). Our corresponding README entry points are listed in
[SUBMISSION-GUIDE.md](SUBMISSION-GUIDE.md). The existing completion report links
actual foundation CI output and Kubernetes/cloud lab records. This comparison
does not certify every exercise by screenshot count; execution records and the
instructor's own rubric take precedence over another submission's layout.

## Evidence packaging and remaining requirements

- The user's original 2026-10-13 Mac pytest screenshot is stored unchanged at
  [the terminal evidence page](session21-python/evidence/terminal/README.md).
- [Recorded log views](session21-python/evidence/recorded-log-views/README.md)
  show excerpts of our own execution records with source checksums and line numbers.
  They are not represented as native terminal or AWS Console screenshots.
- Current authored documentation and the UI use Rudray Mehra. Older records used
  the earlier supplied label, Sudhir Mehra; those originals are preserved and the
  correction is documented in the evidence index.
- The capstone workflow now triggers on every push to main. A successful run of
  this revision remains to be verified after publication.
- Still required: native Compose/Trivy/Kubernetes/metrics evidence where the
  instructor insists on that format; AWS Console evidence or explicit acceptance
  of the existing CLI records; the student's narrated change-to-deployment demo;
  and final form review/submission.

Cloud resources were cleaned up after the recorded lab. This packaging work
does not recreate AWS resources or claim a currently live cloud URL.

## Local verification of this update

- CampusFix API: 24 tests passed, one existing deprecation warning.
- Frontend: production build passed after the visible name correction.
- Workflow: actionlint and an every-main-push/test-gate assertion passed.
- Six generated PNGs: valid PNG headers and matching source hashes verified.
- Native test screenshot: checksum matches the user's supplied file exactly.
- New evidence/comparison Markdown links resolve locally.
- The Session 17 greeting test's sample name was corrected too, but rerunning
  that suite was blocked by missing local Flask/pytest dependencies and unavailable
  offline packages. Its updated suite must be checked in CI after publication.
