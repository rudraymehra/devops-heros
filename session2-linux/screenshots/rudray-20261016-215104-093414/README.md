# Fresh command evidence — reviewed index

Rudray Mehra | 24 BCS 10425 | Batch B

Raw logs and capture manifests are unchanged. Visual decisions are hash-bound in
[the review record](../../../evidence/coursework/native-review.json).
Rejected images remain local and are excluded from publication. A pass is only for the named command.

## Session 01-02 — real hard/symbolic links on this host

Execution: PASS.

[Original command output](01-links.txt)

Native capture: **not-captured**. No native image captured.

## Session 01-02 — actual OS/kernel

Execution: PASS.

[Original command output](02-host.txt)

Native capture: **accepted**. Actual uname output and Rudray heading visible; macOS host, not a Linux VM.

![Reviewed native window capture](02-host.png)

## Session 01-02 — actual disk usage

Execution: PASS.

[Original command output](03-disk.txt)

Native capture: **accepted**. Actual disk-usage output and Rudray heading visible.

![Reviewed native window capture](03-disk.png)

## Linux user management and journalctl

Execution: NOT RUN: Requires Linux/systemd; no host users created.

Native capture: **not-captured**. No native image captured.

## Reference-specific pending items

Execution: NOT RUN: Linux useradd/adduser and journalctl need a real Linux/systemd environment. macOS link tests are labelled macOS, not Linux VM results..

Native capture: **not-captured**. No native image captured.
