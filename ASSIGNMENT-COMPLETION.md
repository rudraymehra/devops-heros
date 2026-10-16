# Assignment completion and verification
Rudray Mehra · 24 BCS 10425 · Batch B · rudray.24bcs10425@sst.scaler.com

All 20 submission fields have a README entry point in the
[submission guide](SUBMISSION-GUIDE.md). The results below identify actual runs;
course examples and expected output are not represented as executed work.

## 2026-10-16 submission update

- Corrected the student name to Rudray Mehra in authored submission headers and
  the CampusFix interface. Historical execution records retain the earlier label;
  see the [evidence identity note](session21-python/evidence/README.md).
- Added the user's original [Mac pytest screenshot](session21-python/evidence/terminal/README.md)
  unchanged, with its source checksum.
- Reran all 24 API tests successfully after the correction and rebuilt the frontend.
- Removed the capstone push path filter to meet the rubric's every-main-push
  requirement. This local change still requires a successful published CI run.
- Compared the supplied reference archive; its Flask/SQLite/EC2 capstone images
  do not demonstrate this FastAPI/React/PostgreSQL/EKS project. See
  [REFERENCE-COMPARISON.md](REFERENCE-COMPARISON.md).

These local updates do not mean that the final presentation, missing native/Console
screenshots, publication of this revision, or form submission have been completed.

## Verified results

| Work | Actual result and evidence |
|---|---|
| CampusFix application | Original campus-maintenance domain, workflow, UI and activity history; [desktop/mobile browser checks](session21-python/evidence/eks-browser/result.json) passed locally and on EKS |
| API tests | [24 passing tests](session21-python/evidence/pytest.md) |
| Docker | Three-service capstone stack ran locally; app images built, scanned and published by CI; seven earlier homework images passed fresh HTTP smoke checks |
| Kubernetes 9–12 | [Pods](submissions/09-kubernetes-fundamentals/OUTPUT.md), [replicas/rollouts](submissions/10-kubernetes-core-objects/OUTPUT.md), [Services/DNS](submissions/11-kubernetes-services/OUTPUT.md), [Ingress/configuration](submissions/12-kubernetes-config-ingress/OUTPUT.md) |
| Deployment strategies | [Blue/green, canary and Recreate passed](submissions/10-kubernetes-core-objects/STRATEGIES-SUCCESS.md); canary used 3 stable + 1 canary Pod to fit the lab |
| Storage, HPA, probes | [Report survived PostgreSQL Pod replacement](session21-python/evidence/eks-verification.md); [HPA scaled 2 → 4 → 6 with 30,291 successful requests and zero failed requests; readiness/liveness recovery passed](session21-python/evidence/scaling-and-probes.md) |
| Troubleshooting | [Five broken scenarios diagnosed and recovered](submissions/14-troubleshooting/OUTPUT.md), plus real HTTP security-group and CNI capacity issues encountered during the lab |
| Helm | [Install, upgrade, history, rollback and uninstall passed](submissions/15-helm/OUTPUT.md) |
| Session 16 | [Successful test/build/publish workflow](https://github.com/rudraymehra/devops-heros/actions/runs/38341620592) |
| Session 17 | [Successful tests, SAST, SCA, secrets, image security, publish and kind deployment](https://github.com/rudraymehra/devops-heros/actions/runs/38342666869) |
| Capstone CI | [Green workflow](https://github.com/rudraymehra/devops-heros/actions/runs/38342666849), SHA-tagged GHCR backend/frontend images, HIGH/CRITICAL Trivy gates |
| Terraform S3 | [Created private/encrypted/versioned bucket](submissions/18-terraform/OUTPUT.md); [DNS-related cleanup retry succeeded](submissions/18-terraform/DESTROY-RETRY.md) |
| Terraform EC2/VPC/S3 | [11 resources created, personalized Nginx webpage verified, all 11 destroyed](submissions/19-cloud/OUTPUT-SUCCESS.md) |
| EKS | [Plan](session21-python/evidence/aws-plan.md), [apply](session21-python/evidence/aws-apply-retry.md), [Helm deployment](session21-python/evidence/eks-helm-deploy.md), [63-resource destroy](session21-python/evidence/aws-destroy.md) |
| Monitoring/GitOps | [Live Prometheus, Grafana and Argo CD screenshots](session21-python/evidence/observability/); both API targets UP and deliberate ConfigMap drift self-healed |

Earlier Linux, shell, Git and Docker notes are preserved from the student's repository.
Fresh Linux, shell, Git, container networking, bind-mount and host-network checks
all passed in the [foundation workflow](https://github.com/rudraymehra/devops-heros/actions/runs/38372002674).
Its `foundation-command-evidence` artifact and job summary contain the actual commands
and output. All seven Hello World/multi-stage images also built and passed HTTP checks.
The capstone reuses the licensed course infrastructure scaffold; see [sources](SOURCES.md).

## Cloud cleanup

[Read-only AWS cleanup audit](session21-python/evidence/aws-cleanup-verification.md)
confirmed all three Terraform state resource lists are empty. No active lab EKS
cluster, EC2 instances, NAT, database disk, load balancer or S3 buckets remain.
The KMS key is disabled and scheduled for deletion on 2026-11-12, subject to AWS's
waiting period. Temporary cloud database reports were deleted; synthetic examples
can be recreated with the browser script. Code, images, screenshots and recordings remain.

The cloud demo URLs are intentionally no longer live. Actual charges can appear
later in AWS Billing; the testing budget was an estimate, not an enforced spending cap.

## What still requires the student

- Give the narrated presentation/live demonstration using
  [PRESENTATION.md](session21-python/PRESENTATION.md). Automated browser recordings
  are included but are not a narrated student presentation.
- Review and submit the [Section B form](https://forms.gle/pAuXQaokwVzhRzit6).
  This work has not submitted it on your behalf.
- The rubric explicitly asks for AWS Console screenshots and a Trivy job-log
  screenshot. Authenticated console/log screenshots were not captured. AWS CLI
  descriptions, complete plan/apply/destroy output, green scan jobs and package
  screenshots are provided instead. Confirm that this evidence format is accepted;
  a new live AWS console screenshot would require recreating the cleaned-up lab.
- A separately configured GitHub OIDC production-deploy job was not run. The
  application was deployed through Helm and reconciled by Argo CD instead.
