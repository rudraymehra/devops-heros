# Session 03 — incomplete system information run

Rudray Mehra | 24 BCS 10425 | Batch B

Capture date: 2026-10-23, approximately 09:15 local time. Environment: macOS
Terminal.

The updated script stopped after printing the process list. With `set -o pipefail`,
`head` closed the `ps` pipe early and caused the script to exit before the input
prompts and process-file creation. The script now uses `sed -n '1,11p'`, which
reads all process output. This is an incomplete attempt, not completion evidence.

![Incomplete system information run](01-system-info-incomplete.png)
