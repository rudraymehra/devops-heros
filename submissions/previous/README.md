# DevOps Homework — Rudray Mehra

**Name:** Rudray Mehra
**Enrollment number:** 10425
**GitHub:** [rudraymehra](https://github.com/rudraymehra)
**Public repository:** [rudraymehra/devops-heros](https://github.com/rudraymehra/devops-heros)

## Submission links

Both submission forms say **“Share Readme.md file GitHub link only”** and provide separate fields for 11 topics. Copy the corresponding README URL below into each field; these are file links, not repository-folder links.

| Form field | README link | Evidence status |
| --- | --- | --- |
| Linux Fundamentals | [README](https://github.com/rudraymehra/devops-heros/blob/main/session2-linux/README.md) | Existing commands and output |
| Shell Scripting | [README](https://github.com/rudraymehra/devops-heros/blob/main/session3-shell-scripting/README.md) | Script, commands and output; error handling corrected |
| Networking | [README](https://github.com/rudraymehra/devops-heros/blob/main/session4-networking/README.md) | Existing commands, output and explanations |
| Git and GitHub | [README](https://github.com/rudraymehra/devops-heros/blob/main/session5-git-github/README.md) | Commit comparison and cherry-pick output |
| Docker Fundamentals | [README](https://github.com/rudraymehra/devops-heros/blob/main/session6-7-docker/README.md) | Six applications, Dockerfiles and recorded build/run output |
| Docker Images | [README](https://github.com/rudraymehra/devops-heros/blob/main/session6-7-docker/multi-stage-dockerfile/README.md) | Multi-stage app, port 8080 output and student details |
| Docker Networking | [README](https://github.com/rudraymehra/devops-heros/blob/main/session8-docker-networking-volume/README.md) | Recorded output present; required screenshots pending |
| Kubernetes Fundamentals | [README](https://github.com/rudraymehra/devops-heros/blob/main/submissions/09-kubernetes-fundamentals/README.md) | Manifests and exercises prepared; cluster run pending |
| Kubernetes Pods, ReplicaSets & Deployments | [README](https://github.com/rudraymehra/devops-heros/blob/main/submissions/10-kubernetes-core-objects/README.md) | Manifests and exercises prepared; cluster run pending |
| Kubernetes Networking & Services | [README](https://github.com/rudraymehra/devops-heros/blob/main/submissions/11-kubernetes-services/README.md) | Manifests and exercises prepared; cluster run pending |
| Kubernetes Ingress, ConfigMaps & Secrets | [README](https://github.com/rudraymehra/devops-heros/blob/main/submissions/12-kubernetes-config-ingress/README.md) | Manifests and exercises prepared; cluster run pending |

## Completion status

The original Linux-through-Docker submissions and their recorded September 3 command outputs are preserved. The enrollment number above was confirmed for this submission. The shell script and documentation corrections are included in this review.

**Remaining before a fully verified submission:** capture the required Docker networking screenshots and execute the four new Kubernetes labs. Docker Desktop and the local Minikube cluster were unavailable during this review. No Kubernetes runtime output has been fabricated. See [verification details](evidence/verification.md).

The linked homework document currently describes seven Linux-through-Docker topics. The live forms also require four Kubernetes topics. The added Kubernetes exercises follow the corresponding instructor repository sessions and clearly identify their execution status.

## Repository contents

- `session2-linux/`: links, user management, journald and Linux command practice.
- `session3-shell-scripting/homework.sh`: interactive system report with process output saved to a file.
- `session4-networking/`: networking command output and explanations.
- `session5-git-github/`: staging, `commit -a -m`, branches and cherry-pick practice.
- `session6-7-docker/`: `nodejs-app`, `python-app`, `java-app`, `Apache-app`, `React-app`, `nginx-app`, and the multi-stage app.
- `session8-docker-networking-volume/`: container connectivity, host networking, bind mounts and overlay networks.
- `submissions/09-*` through `submissions/12-*`: Kubernetes manifests, explanations and executable exercises.
- `scripts/run-kubernetes-labs.py`: captures real command output and verifies the four Kubernetes exercises.

## Running the Kubernetes exercises

Use Docker Desktop and a dedicated local Minikube profile:

```bash
minikube start -p devops-homework --driver=docker --cpus=2 --memory=3072
minikube addons enable ingress -p devops-homework
python3 scripts/run-kubernetes-labs.py --context devops-homework
```

Each topic's `OUTPUT.md` is created only when its commands execute. The runner exits on a command/check failure. Resource names are confined to `rudray-devops-hw`; cleanup is documented in each topic.

## Assignment and submission forms

- [Homework instructions](https://docs.google.com/document/d/1cjXFYf2Thm8cBEN-0C48B-v02cj3jGLd47lcO18prHE/edit?usp=sharing)
- [Section A submission form](https://forms.gle/ydjAJcwxjpjBXgxB8)
- [Section B submission form](https://forms.gle/pAuXQaokwVzhRzit6)
- [Instructor repository and session resources](https://github.com/Nency-Ravaliya/devops-heros)

Submit through the form for your section. The forms have not been submitted by this repository update.
