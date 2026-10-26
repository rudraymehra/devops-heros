# Session 16 Submission

The final project is
`session-16-github-actions/10-final-cicd-pipeline/`. It contains a Python
application, tests, build script, Dockerfile, and workflow. The repository-root
workflow `.github/workflows/session16-ci.yml` is the executable monorepo workflow;
nested `.github/workflows` files are examples and are not discovered by GitHub.

The pipeline performs test, build, artifact upload, Docker build, and a basic secret
filename check. A failing test blocks dependent build jobs.

## Evidence checklist

- [x] Successful Actions run URL: https://github.com/rudraymehra/devops-heros/actions/runs/40083432667
- [x] Test log: GitHub Actions `test` job passed all five tests
- [x] Uploaded `calculator-build` artifact (downloaded and confirmed `calculator.py` and `build-info.txt`)
- [x] Successful Docker image build in GitHub Actions and local Docker
- [x] Intentional failing-test behavior reproduced in an isolated temporary copy (1 failed, 4 passed); the working tree remained unchanged and the corrected GitHub Actions run passed

## Run notes

- Local dependencies were installed into the ignored `.venv/` directory. The local
  test run passed all five tests, `build.sh` created the build files, and Docker
  built `session16-calculator:local`.
- GitHub Actions was started with `workflow_dispatch` on `main`. The `test` and
  `build` jobs passed and uploaded the artifact. The `publish` job is push-only and
  did not run for this manual dispatch.
