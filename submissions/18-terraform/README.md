# Session 18: Terraform & Infrastructure as Code

**Sudhir Mehra · 24 BCS 10425 · Batch B**

[Implementation and session files](../../session18-terraform-iac/) ·
[Deliverables and evidence checklist](../../session18-terraform-iac/SUBMISSION.md)

This README is the submission entry point for the named form field. The linked
checklist maps the required work to its files. Runtime results, when available,
are linked from the [completion report](../../ASSIGNMENT-COMPLETION.md).
Course examples with expected output are retained as references and are not
claimed as executed evidence.

## Verified execution — 2026-10-13

[S3 init/validate/plan/apply/show/output](OUTPUT.md) created the encrypted, versioned, non-public bucket. The first destroy hit a DNS failure; [the regional-endpoint retry destroyed all four resources](DESTROY-RETRY.md). [Final audit](../../session21-python/evidence/aws-cleanup-verification.md) confirms the bucket is gone.
