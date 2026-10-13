# Session 16 Submission

The final project is
`session-16-github-actions/10-final-cicd-pipeline/`. It contains a Python
application, tests, build script, Dockerfile, and workflow. The repository-root
workflow `.github/workflows/session16-ci.yml` is the executable monorepo workflow;
nested `.github/workflows` files are examples and are not discovered by GitHub.

The pipeline performs test, build, artifact upload, Docker build, and a basic secret
filename check. A failing test blocks dependent build jobs.

## Evidence checklist

- [ ] Successful Actions run URL
- [ ] Test log
- [ ] Uploaded `calculator-build` artifact
- [ ] Successful Docker image build
- [ ] Intentional failing-test screenshot followed by corrected run
