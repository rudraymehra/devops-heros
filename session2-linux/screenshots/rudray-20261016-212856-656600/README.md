# Fresh command evidence

Rudray Mehra | 24 BCS 10425 | Batch B

These commands were actually executed. Logs are not screenshots.
Native images, if present, are untouched user-selected macOS window captures.
Check each image visually before submission; file creation alone does not prove its contents.

| Check | Execution | Log | Native screenshot |
|---|---|---|---|
| Session 01-02 — real hard/symbolic links on this host | PASS | [Output](01-links.txt) | NOT CAPTURED |
| Session 01-02 — actual OS/kernel | PASS | [Output](02-host.txt) | NOT CAPTURED |
| Session 01-02 — actual disk usage | PASS | [Output](03-disk.txt) | NOT CAPTURED |
| Linux user management and journalctl | NOT RUN: Requires Linux/systemd; no host users created | — | NOT CAPTURED |
| Reference-specific pending items | NOT RUN: Linux useradd/adduser and journalctl need a real Linux/systemd environment. macOS link tests are labelled macOS, not Linux VM results. | — | NOT CAPTURED |

An exit code of zero proves only the named command succeeded.
Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.
No AWS resources were created or removed by this helper.
