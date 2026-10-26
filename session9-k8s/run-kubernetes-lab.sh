#!/usr/bin/env bash
set -euo pipefail

profile=homework-k8s-20261023
deployment=kubernetes-bootcamp
service=$deployment
cluster_started=0
service_tunnel_pid=
service_log=

for command in docker minikube kubectl curl; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command '$command' is unavailable. Install it before running this lab." >&2
    exit 1
  fi
done

if ! docker info >/dev/null 2>&1; then
  echo 'Docker is not available; start Docker Desktop, then rerun this lab.' >&2
  exit 1
fi

profiles=$(minikube profile list -o json 2>/dev/null || true)
if printf '%s' "$profiles" | grep -Fq "$profile"; then
  echo "Minikube profile $profile already exists; stopping without changing it." >&2
  exit 1
fi

cleanup() {
  if [[ -n "$service_tunnel_pid" ]]; then
    kill "$service_tunnel_pid" >/dev/null 2>&1 || true
    wait "$service_tunnel_pid" 2>/dev/null || true
  fi
  if [[ -n "$service_log" ]]; then rm -f "$service_log"; fi
  if [[ "$cluster_started" -eq 1 ]]; then
    kubectl --context "$profile" delete service "$service" --ignore-not-found --wait=false >/dev/null 2>&1 || true
    kubectl --context "$profile" delete deployment "$deployment" --ignore-not-found --wait=false >/dev/null 2>&1 || true
    minikube delete --profile "$profile" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

service_log=$(mktemp)
cluster_started=1
minikube start --profile "$profile" --driver=docker
kubectl --context "$profile" wait --for=condition=Ready nodes --all --timeout=180s

echo '=== Cluster information ==='
kubectl --context "$profile" cluster-info
kubectl --context "$profile" get nodes -o wide
kubectl --context "$profile" get pods --all-namespaces
minikube status --profile "$profile"

echo '=== Create deployment and NodePort Service ==='
kubectl --context "$profile" create deployment "$deployment" --image=gcr.io/google-samples/kubernetes-bootcamp:v1
kubectl --context "$profile" rollout status deployment/"$deployment" --timeout=180s
kubectl --context "$profile" expose deployment "$deployment" --type=NodePort --port=8080
kubectl --context "$profile" get services

minikube service --profile "$profile" "$service" --url >"$service_log" 2>&1 &
service_tunnel_pid=$!
service_url=
for attempt in {1..30}; do
  service_url=$(grep -Eo 'https?://[^[:space:]]+' "$service_log" | sed -n '1p' || true)
  if [[ -n "$service_url" ]]; then break; fi
  sleep 1
done
if [[ -z "$service_url" ]]; then
  echo 'Minikube did not provide a NodePort service URL; service output follows:' >&2
  cat "$service_log" >&2 || true
  exit 1
fi
echo "NodePort service URL: $service_url"

check_service() {
  local label=$1 expected_version=$2 response=
  for attempt in {1..20}; do
    if response=$(curl --fail --silent --show-error --max-time 5 "$service_url" 2>/dev/null); then
      if printf '%s\n' "$response" | grep -Fq "$expected_version"; then break; fi
    fi
    sleep 1
  done
  if [[ -z "$response" ]] || ! printf '%s\n' "$response" | grep -Fq "$expected_version"; then
    echo "Service check failed at stage: $label" >&2
    cat "$service_log" >&2 || true
    kubectl --context "$profile" get pods -o wide >&2 || true
    return 1
  fi
  printf '%s: HTTP %s\n' "$label" "$(curl --silent --output /dev/null --write-out '%{http_code}' "$service_url")"
  printf '%s\n' "$response" | sed -n '1,5p'
}

echo '=== Initial service and pods ==='
check_service initial 'v=1'
kubectl --context "$profile" get pods -o wide

echo '=== Scale to three replicas ==='
kubectl --context "$profile" scale deployment/"$deployment" --replicas=3
kubectl --context "$profile" rollout status deployment/"$deployment" --timeout=180s
kubectl --context "$profile" get pods -o wide
check_service scaled 'v=1'

echo '=== Update image to v2 ==='
kubectl --context "$profile" set image deployment/"$deployment" "$deployment"=docker.io/jocatalin/kubernetes-bootcamp:v2
kubectl --context "$profile" rollout status deployment/"$deployment" --timeout=240s
kubectl --context "$profile" rollout history deployment/"$deployment"
kubectl --context "$profile" get pods -o wide
check_service updated 'v=2'

echo '=== Roll back to the previous image ==='
kubectl --context "$profile" rollout undo deployment/"$deployment"
kubectl --context "$profile" rollout status deployment/"$deployment" --timeout=180s
kubectl --context "$profile" rollout history deployment/"$deployment"
kubectl --context "$profile" get deployment "$deployment" -o=jsonpath='{.spec.template.spec.containers[0].image}{"\n"}'
kubectl --context "$profile" get pods -o wide
check_service rollback 'v=1'

echo 'Kubernetes deployment, Service, scale, update, and rollback checks passed.'
echo "Cleanup will remove only the isolated Minikube profile: $profile"
