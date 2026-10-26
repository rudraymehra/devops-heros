#!/usr/bin/env bash
set -euo pipefail

profile=homework-k8s-strategies-20261023
tunnel_pid=
tunnel_log=
cluster_started=0

for command in docker minikube kubectl curl; do
  if ! command -v "$command" >/dev/null 2>&1; then
    echo "Required command '$command' is unavailable." >&2
    exit 1
  fi
done
if ! docker info >/dev/null 2>&1; then
  echo 'Docker is unavailable; start Docker Desktop and retry.' >&2
  exit 1
fi
profiles=$(minikube profile list -o json 2>/dev/null || true)
if printf '%s' "$profiles" | grep -Fq "$profile"; then
  echo "Minikube profile $profile already exists; stopping without changing it." >&2
  exit 1
fi

cleanup() {
  if [[ -n "$tunnel_pid" ]]; then
    kill "$tunnel_pid" >/dev/null 2>&1 || true
    wait "$tunnel_pid" 2>/dev/null || true
  fi
  if [[ -n "$tunnel_log" ]]; then rm -f "$tunnel_log"; fi
  if [[ "$cluster_started" -eq 1 ]]; then
    for manifest in 01-rolling-update 02-blue-green 03-canary 04-recreate; do
      kubectl --context "$profile" delete -f "$manifest" --ignore-not-found --wait=false >/dev/null 2>&1 || true
    done
    minikube delete --profile "$profile" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

cluster_started=1
minikube start --profile "$profile" --driver=docker
kubectl --context "$profile" wait --for=condition=Ready nodes --all --timeout=180s

start_service() {
  local name=$1
  tunnel_log=$(mktemp)
  minikube service --profile "$profile" "$name" --url >"$tunnel_log" 2>&1 &
  tunnel_pid=$!
  service_url=
  for attempt in {1..30}; do
    service_url=$(grep -Eo 'https?://[^[:space:]]+' "$tunnel_log" | sed -n '1p' || true)
    if [[ -n "$service_url" ]]; then return 0; fi
    sleep 1
  done
  echo "No URL returned for Service $name" >&2
  cat "$tunnel_log" >&2 || true
  return 1
}

stop_service() {
  if [[ -n "$tunnel_pid" ]]; then
    kill "$tunnel_pid" >/dev/null 2>&1 || true
    wait "$tunnel_pid" 2>/dev/null || true
    tunnel_pid=
  fi
  if [[ -n "$tunnel_log" ]]; then rm -f "$tunnel_log"; tunnel_log=; fi
}

check_version() {
  local label=$1 expected=$2 response=
  for attempt in {1..20}; do
    if response=$(curl --fail --silent --show-error --max-time 3 "$service_url" 2>/dev/null) && printf '%s\n' "$response" | grep -Fq "$expected"; then
      break
    fi
    sleep 1
  done
  if [[ -z "$response" ]] || ! printf '%s\n' "$response" | grep -Fq "$expected"; then
    echo "$label did not return expected text: $expected" >&2
    cat "$tunnel_log" >&2 || true
    return 1
  fi
  printf '%s: %s\n' "$label" "$expected"
}

echo '=== Rolling update: v1 to v2, then rollback ==='
kubectl --context "$profile" apply -f 01-rolling-update/deployment-v1.yaml
kubectl --context "$profile" apply -f 01-rolling-update/service.yaml
kubectl --context "$profile" rollout status deployment/app-rolling --timeout=180s
start_service app-rolling-service
check_version 'Rolling before update' 'VERSION: v1'
kubectl --context "$profile" apply -f 01-rolling-update/deployment-v2.yaml
kubectl --context "$profile" rollout status deployment/app-rolling --timeout=240s
kubectl --context "$profile" rollout history deployment/app-rolling
kubectl --context "$profile" get pods -l app=app-rolling -o wide
check_version 'Rolling after update' 'VERSION: v2'
kubectl --context "$profile" rollout undo deployment/app-rolling
kubectl --context "$profile" rollout status deployment/app-rolling --timeout=180s
check_version 'Rolling after rollback' 'VERSION: v1'
stop_service
kubectl --context "$profile" delete service app-rolling-service --wait=true
kubectl --context "$profile" delete deployment app-rolling --wait=true

echo '=== Blue-green: switch Service blue -> green -> blue ==='
kubectl --context "$profile" apply -f 02-blue-green/deployment-blue.yaml
kubectl --context "$profile" apply -f 02-blue-green/deployment-green.yaml
kubectl --context "$profile" rollout status deployment/app-blue --timeout=180s
kubectl --context "$profile" rollout status deployment/app-green --timeout=180s
kubectl --context "$profile" apply -f 02-blue-green/service-blue.yaml
start_service myapp-service
check_version 'Blue-green before switch' 'BLUE ENVIRONMENT'
kubectl --context "$profile" get endpoints myapp-service -o wide
kubectl --context "$profile" apply -f 02-blue-green/service-green.yaml
check_version 'Blue-green after switch' 'GREEN ENVIRONMENT'
kubectl --context "$profile" get endpoints myapp-service -o wide
kubectl --context "$profile" apply -f 02-blue-green/service-blue.yaml
check_version 'Blue-green after rollback' 'BLUE ENVIRONMENT'
stop_service
kubectl --context "$profile" delete service myapp-service --wait=true
kubectl --context "$profile" delete deployment app-blue app-green --wait=true

echo '=== Canary: stable/canary endpoints and promotion/rollback ==='
kubectl --context "$profile" apply -f 03-canary/deployment-stable.yaml
kubectl --context "$profile" rollout status deployment/app-stable --timeout=180s
kubectl --context "$profile" apply -f 03-canary/service.yaml
start_service myapp-canary-service
check_version 'Canary stable-only response' 'STABLE v1'
kubectl --context "$profile" apply -f 03-canary/deployment-canary.yaml
kubectl --context "$profile" rollout status deployment/app-canary --timeout=180s
kubectl --context "$profile" get pods -l app=myapp-canary --show-labels
kubectl --context "$profile" get endpoints myapp-canary-service -o wide
echo 'Canary sample (10 requests; distribution is naturally variable):'
for attempt in {1..10}; do
  if ! curl --fail --silent --show-error --max-time 3 "$service_url" | grep -oE 'STABLE v1|CANARY v2'; then echo 'request failed'; fi
done
kubectl --context "$profile" scale deployment app-canary --replicas=3
kubectl --context "$profile" scale deployment app-stable --replicas=7
kubectl --context "$profile" rollout status deployment/app-canary --timeout=180s
kubectl --context "$profile" rollout status deployment/app-stable --timeout=180s
kubectl --context "$profile" get endpoints myapp-canary-service -o wide
echo 'Canary at 30% sample (10 requests; distribution is naturally variable):'
for attempt in {1..10}; do
  if ! curl --fail --silent --show-error --max-time 3 "$service_url" | grep -oE 'STABLE v1|CANARY v2'; then echo 'request failed'; fi
done
kubectl --context "$profile" scale deployment app-canary --replicas=9
kubectl --context "$profile" scale deployment app-stable --replicas=0
kubectl --context "$profile" rollout status deployment/app-canary --timeout=180s
check_version 'Canary promoted to v2' 'CANARY v2'
kubectl --context "$profile" scale deployment app-canary --replicas=0
kubectl --context "$profile" scale deployment app-stable --replicas=9
kubectl --context "$profile" rollout status deployment/app-stable --timeout=180s
check_version 'Canary rolled back to v1' 'STABLE v1'
stop_service
kubectl --context "$profile" delete service myapp-canary-service --wait=true
kubectl --context "$profile" delete deployment app-canary app-stable --wait=true

echo '=== Recreate: v1, outage during replacement, v2, rollback ==='
kubectl --context "$profile" apply -f 04-recreate/deployment-v1.yaml
kubectl --context "$profile" apply -f 04-recreate/service.yaml
kubectl --context "$profile" rollout status deployment/app-recreate --timeout=180s
start_service app-recreate-service
check_version 'Recreate before update' 'VERSION: v1'
monitor_log=$(mktemp)
(
  for attempt in {1..24}; do
    if response=$(curl --fail --silent --max-time 1 "$service_url" 2>/dev/null); then
      printf '%s\n' "$response" | grep -oE 'VERSION: v[12]( \(UPGRADED\))?' || true
    else
      echo '[OUTAGE] Service unavailable during Recreate'
    fi
    sleep 0.5
  done
) >"$monitor_log" &
monitor_pid=$!
sleep 1
kubectl --context "$profile" apply -f 04-recreate/deployment-v2.yaml
kubectl --context "$profile" rollout status deployment/app-recreate --timeout=240s
wait "$monitor_pid"
cat "$monitor_log"
rm -f "$monitor_log"
check_version 'Recreate after update' 'VERSION: v2 (UPGRADED)'
kubectl --context "$profile" rollout undo deployment/app-recreate
kubectl --context "$profile" rollout status deployment/app-recreate --timeout=180s
check_version 'Recreate after rollback' 'VERSION: v1'
stop_service
kubectl --context "$profile" delete service app-recreate-service --wait=true
kubectl --context "$profile" delete deployment app-recreate --wait=true

echo 'All four deployment strategy demonstrations passed. Cleanup removes only this Minikube profile.'
