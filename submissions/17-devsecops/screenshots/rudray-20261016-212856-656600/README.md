# Fresh command evidence

Rudray Mehra | 24 BCS 10425 | Batch B

These commands were actually executed. Logs are not screenshots.
Native images, if present, are untouched user-selected macOS window captures.
Check each image visually before submission; file creation alone does not prove its contents.

| Check | Execution | Log | Native screenshot |
|---|---|---|---|
| Session 17 — actual project tests | FAILED / BLOCKED | [Output](01-pytest.txt) | NOT CAPTURED |
| Session 17 — actual source scan | PASS | [Output](02-bandit.txt) | NOT CAPTURED |
| CI/image/security/deployment screenshots | NOT RUN: Use actual jobs for the submitted SHA; local test success alone is not CI success | — | NOT CAPTURED |
| Reference-specific pending items | NOT RUN: Capture real unit/SAST/SCA/secret/image scan and deployment results. Before/after findings must come from real revisions; never invent a vulnerable scan. | — | NOT CAPTURED |

An exit code of zero proves only the named command succeeded.
Helm lint is not a deployment; Terraform validate is not a plan/apply/destroy.
No AWS resources were created or removed by this helper.
