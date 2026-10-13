# Execution evidence index
Sudhir Mehra · 24 BCS 10425 · Batch B.

These are actual results from the student repository and approved AWS labs.
The application samples are synthetic maintenance reports, not real campus records.

## Application and CI
- [24 API tests](pytest.md) and [rendered actual test log](published/pytest-log-view.png).
  The rendered log is explicitly not a native-terminal screenshot.
- [Local browser checks](browser/result.json) and [local walkthrough](browser/browser-walkthrough.webm).
- [EKS browser checks](eks-browser/result.json), [desktop](eks-browser/desktop.png),
  [mobile](eks-browser/mobile.png), [cloud walkthrough](eks-browser/browser-walkthrough.webm).
- [Verified public CI run metadata](published/ci-runs.json).
- [Green foundation workflow](published/foundation-ci.png): Linux, shell, Git,
  seven Docker images, container networks, bind mounts and host networking.
- [Capstone CI screenshot](published/campusfix-ci.png), [Session 16](published/session16-ci.png),
  [Session 17](published/session17-ci.png), [commit history](published/commits.png).
- [Backend package](published/backend-package.png), [frontend package](published/frontend-package.png).

## EKS, storage and observability
- [Helm deployment](eks-helm-deploy.md).
- [Persistence and Argo self-healing](eks-verification.md).
- [Autoscaling and probe failure/recovery](scaling-and-probes.md).
- [Prometheus/Grafana/Argo observations and metrics](observability/result.json).
- [Prometheus targets](observability/prometheus-targets.png),
  [Grafana dashboard](observability/grafana-dashboard.png),
  [Argo CD synced](observability/argocd-synced.png).

## AWS lifecycle
- [Plan](aws-plan.md), [first apply attempt](aws-apply.md), [successful apply retry](aws-apply-retry.md).
- [Network-rule failure](aws-network-fix.md) and [successful targeted correction](aws-network-fix-retry.md).
- [Actual EKS description](aws-cluster-description.md), [VPC description](aws-vpc-description.md).
  These are CLI evidence, not AWS Console screenshots.
- [Kubernetes disk/LB cleanup](aws-kubernetes-cleanup.md).
- [Terraform destroy: 63 resources](aws-destroy.md).
- [Final independent cleanup audit](aws-cleanup-verification.md).
- S3 and EC2 assignment logs are under [Session 18](../../submissions/18-terraform/)
  and [Session 19](../../submissions/19-cloud/).

Failed attempts remain labelled with their exit codes. The automated browser videos
do not replace the student's spoken final presentation. The cloud lab was destroyed
after recording, so its temporary endpoints intentionally no longer respond.
