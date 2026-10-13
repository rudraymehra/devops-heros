# IAM — Identity and Access Management

IAM controls who can perform which actions on which AWS resources under what
conditions. It is a global service.

- A user represents a person or legacy workload with long-term identity.
- A group applies policies to multiple users.
- A role has permissions but no long-term credentials; trusted identities assume it
  to receive temporary credentials.
- A policy is a JSON permission document. Identity policies attach to principals;
  resource policies attach to supported resources.
- An explicit deny wins over any allow. Otherwise an action is denied unless an
  applicable policy explicitly allows it.

Least privilege means granting only required actions, resources, conditions, and
duration. Prefer federation/Identity Center and roles over access keys, require MFA,
rotate or remove unused credentials, review access with IAM Access Analyzer, protect
the root account, and never commit credentials.

Common uses include human workforce access, EC2 instance roles, CI deployment roles,
cross-account access, and tightly scoped application access to S3 or DynamoDB.
