# Session 21 Final Capstone Submission

**Student:** Sudhir Mehra | **Roll number:** 24 BCS 10425 | **Batch:** B

CampusFix is a full-stack campus-maintenance application used to demonstrate an
end-to-end DevOps delivery path. It includes a React frontend, FastAPI CRUD API,
PostgreSQL, Alembic migration, automated tests, containers, CI/CD, security scanning,
Terraform, Kubernetes, Helm, autoscaling, Ingress, metrics, and troubleshooting labs.

## Local acceptance checks

```bash
docker compose up --build -d
docker compose ps
curl --fail http://localhost:8000/health
curl --fail http://localhost:8000/api/requests
open http://localhost:3000
docker compose down
```

Backend tests:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -v
```

Frontend and Helm:

```bash
cd frontend && npm ci && npm run build && cd ..
helm lint helm/taskboard
helm template taskboard helm/taskboard -f helm/taskboard/values-dev.yaml
```

## Cloud safety

The Terraform project creates a NAT Gateway, EKS control plane, and EC2 worker nodes,
all of which can incur charges. Review the plan in a lab account, set a budget alert,
and run `terraform destroy` after evaluation. No command in this repository embeds
AWS credentials.

## Final evidence checklist

- [ ] Browser screenshot showing the working application
- [ ] `pytest -v` with at least five passing API tests
- [ ] At least ten meaningful Git commits
- [ ] `docker compose` output and frontend/backend images
- [ ] Successful GitHub Actions URL and GHCR SHA-tagged packages
- [ ] Trivy results and explanation
- [ ] Terraform plan, VPC/EKS console views, and destroy output
- [ ] Running Kubernetes Pods, Services, Helm release, and Ingress response
- [ ] Prometheus target `UP` and a Grafana panel with live metrics
- [ ] Troubleshooting demonstration and resolution

The production GitHub environment must define `AWS_ROLE_TO_ASSUME` (OIDC IAM role),
`GHCR_PULL_TOKEN` (read-packages token), and `TASKBOARD_DB_PASSWORD`. Store them as
GitHub environment secrets; never put their values in this repository. Production
deployment is deliberately manual: run the **Session 21 Capstone** workflow with its
`deploy` input enabled after reviewing the build and security-scan results.
