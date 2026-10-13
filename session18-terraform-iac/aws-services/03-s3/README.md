# S3 — Simple Storage Service

S3 is regional object storage. A globally unique bucket contains objects addressed
by keys; it is not a mounted block filesystem. Storage classes trade retrieval time,
availability, and cost, including Standard, Intelligent-Tiering, Standard-IA,
One Zone-IA, and Glacier tiers.

Versioning preserves previous object versions and protects against accidental
overwrite or deletion. Lifecycle rules transition or expire versions. Server-side
encryption can use S3-managed keys (SSE-S3) or KMS keys (SSE-KMS). Bucket policies
are resource policies and should use explicit principals, narrow actions, and secure
transport conditions.

Best practices: enable Block Public Access by default, use IAM roles, encrypt data,
enable versioning for important data, configure lifecycle rules, log access where
required, and never place credentials inside objects or Terraform state.

Common uses include backups, logs, artifacts, static websites, data lakes, and
application uploads.
