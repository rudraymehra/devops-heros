# CampusFix presentation guide

Sudhir Mehra · 24 BCS 10425 · Batch B.

Use this as a speaking outline and demonstrate your own running environment.
The saved automated browser video can illustrate the app, but the rubric also
asks for a live pipeline demonstration or a recorded walkthrough you present.

## Suggested eight-minute walkthrough

1. **Problem (45 seconds):** campus maintenance reports need a location, urgency,
   repair status and a record of the actual fix. Show CampusFix's desk.
2. **Application (90 seconds):** report an electrical problem; start work; show
   that resolution requires notes; resolve and reopen it. Show activity updates.
3. **Data and tests (60 seconds):** explain the two new tables and migration.
   Show the 24 tests, isolated test database and one invalid transition test.
4. **Containers (45 seconds):** show three Compose services, non-root app users
   and the frontend's multi-stage build. Explain why PostgreSQL has no host port.
5. **Delivery and security (90 seconds):** show a real GitHub Actions run and both
   SHA-tagged GHCR packages. Explain why a failed test or high/critical image
   finding blocks publication. Describe the Debian-base finding and Alpine fix.
6. **Infrastructure (60 seconds):** show the actual Terraform plan/apply results,
   EKS nodes, Helm release, Services and Ingress. Explain the PVC and EBS CSI.
7. **Observe and troubleshoot (60 seconds):** generate requests, show Prometheus
   scraping and a Grafana panel; demonstrate one broken Service selector and fix.
8. **GitOps and cleanup (30 seconds):** explain the Argo CD Application and show
   a real sync if available. Show the completed Terraform destroy log.

## Questions to be ready for

- Why can liveness be UP while readiness is failing?
- Why do two replicas need serialized database migrations?
- Why are database credentials Secret references instead of literal Pod values?
- How does a Service selector differ from an Ingress route?
- Why is a commit-SHA image tag safer than `latest` for rollback?
- What does a clean vulnerability scan prove, and what does it not prove?
- Why can Argo CD undo a manual `kubectl` or Helm change?
- What data survives Pod replacement, and what does `docker compose down -v` erase?

## Before recording

Use the links in the submission guide, avoid showing credentials, and clearly
identify any failed or unavailable step. The final spoken recording must reflect
the checks that actually completed.
