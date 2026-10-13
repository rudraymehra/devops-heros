# Kubernetes Fundamentals Homework

## Cluster installation and verification

```bash
minikube start --driver=docker
kubectl cluster-info
kubectl get nodes -o wide
kubectl get pods --all-namespaces
minikube status
```

`kubectl cluster-info` identifies the control-plane and DNS endpoints. A usable
single-node Minikube cluster should report its node as `Ready`.

## Architecture notes

The control plane maintains desired state:

- The API server validates and exposes the Kubernetes API.
- `etcd` stores cluster state.
- The scheduler assigns unscheduled Pods to nodes.
- Controller managers reconcile actual state toward desired state.

Each worker node runs a kubelet, a container runtime, and kube-proxy (or equivalent
networking implementation). The kubelet asks the runtime to run Pod containers and
reports their status to the API server.

```text
kubectl -> API server -> etcd
                    |-> scheduler -> node
                    |-> controllers

node: kubelet -> container runtime -> Pods
      kube-proxy/CNI -> Service and Pod networking
```

## Kubernetes Basics tutorial

```bash
kubectl create deployment kubernetes-bootcamp \
  --image=gcr.io/google-samples/kubernetes-bootcamp:v1
kubectl get deployments
kubectl get pods -o wide
kubectl expose deployment kubernetes-bootcamp --type=NodePort --port=8080
kubectl get services
minikube service kubernetes-bootcamp --url
kubectl scale deployment kubernetes-bootcamp --replicas=3
kubectl get pods
kubectl set image deployment/kubernetes-bootcamp \
  kubernetes-bootcamp=docker.io/jocatalin/kubernetes-bootcamp:v2
kubectl rollout status deployment/kubernetes-bootcamp
kubectl rollout undo deployment/kubernetes-bootcamp
kubectl delete service kubernetes-bootcamp
kubectl delete deployment kubernetes-bootcamp
```

## Core objects

| Object | Responsibility |
|---|---|
| Pod | Smallest schedulable unit; one or more tightly coupled containers |
| Deployment | Declarative rollout and lifecycle for stateless Pods |
| ReplicaSet | Maintains a requested number of matching Pods |
| Service | Stable networking endpoint for selected Pods |
| ConfigMap | Non-sensitive application configuration |
| Secret | Sensitive values requiring controlled distribution |
| Namespace | Logical grouping and policy boundary |

## Evidence checklist

- [ ] Add `minikube status` and `kubectl get nodes -o wide` output.
- [ ] Add screenshots for deploy, expose, scale, update, and rollback.
- [ ] Record observations for Pod replacement and Service stability.

## Resources

- <https://kubernetes.io/docs/tutorials/kubernetes-basics/>
- <https://minikube.sigs.k8s.io/docs/start/>
- <https://kubernetes.io/docs/concepts/architecture/>
