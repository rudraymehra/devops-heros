# Session 01–02 — Task 2 attempt

Rudray Mehra | 24 BCS 10425 | Batch B

Capture date: 2026-10-23, approximately 08:58 local time. Environment: Ubuntu
24.04 container.

![Incomplete user-management attempt](02-user-management-attempt.png)

`adduser` created `devopsdemo` and its home directory. The run then stopped because
`deluser --remove-home` requires `perl`; the script used `set -e`, so the `useradd`
demonstration and cleanup verification did not run. This is a recorded failed
attempt, not a completed Task 2 result. The container was launched with `--rm` and
was removed when the command exited.
