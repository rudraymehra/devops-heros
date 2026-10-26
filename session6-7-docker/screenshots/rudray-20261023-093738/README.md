# Session 07 — build passed, HTTP check failed

Capture date: 2026-10-23 (Asia/Kolkata). The multi-stage Docker build completed successfully and the container launch returned an ID, but the immediate curl failed with `connection reset by peer`. This is an incomplete run and does not prove the application responded.

The helper now waits up to 20 seconds for the HTTP endpoint and prints container logs if readiness fails. Rerun `bash ./run-multistage-lab.sh` from `session6-7-docker` and capture the successful response and container listing.

- [Build and initial HTTP failure](01-build-passed-http-reset.png)
