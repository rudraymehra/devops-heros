#!/usr/bin/env bash
set -euo pipefail

profile=homework-k8s-lifecycle-20261023
cluster_started=0
termination_log=
termination_pid=

for command in docker minikube kubectl; do
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
  if [[ -n "$termination_pid" ]]; then
    kill "$termination_pid" >/dev/null 2>&1 || true
    wait "$termination_pid" 2>/dev/null || true
  fi
  if [[ -n "$termination_log" ]]; then rm -f "$termination_log"; fi
  if [[ "$cluster_started" -eq 1 ]]; then
    kubectl --context "$profile" delete pods --all --ignore-not-found --wait=false >/dev/null 2>&1 || true
    minikube delete --profile "$profile" >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

cluster_started=1
minikube start --profile "$profile" --driver=docker
kubectl --context "$profile" wait --for=condition=Ready nodes --all --timeout=180s

apply_case() {
  local file=$1 pod=$2
  echo "=== ${file##*/} ==="
  kubectl --context "$profile" apply -f "pod-lifecycle/$file"
  printf 'Pod phase/status: '
  kubectl --context "$profile" get pod "$pod" -o 'custom-columns=NAME:.metadata.name,PHASE:.status.phase,READY:.status.containerStatuses[*].ready,RESTARTS:.status.containerStatuses[*].restartCount' --no-headers || true
}

inspect_case() {
  local pod=$1
  kubectl --context "$profile" describe pod "$pod" | tail -n 24 || true
}

remove_case() {
  kubectl --context "$profile" delete pod "$1" --ignore-not-found --wait=true --timeout=60s >/dev/null
}

apply_case 01-running.yaml lifecycle-running
kubectl --context "$profile" wait --for=condition=Ready pod/lifecycle-running --timeout=180s
kubectl --context "$profile" get pod lifecycle-running -o wide
inspect_case lifecycle-running
remove_case lifecycle-running

apply_case 02-pending.yaml lifecycle-pending
sleep 3
kubectl --context "$profile" get pod lifecycle-pending -o wide
inspect_case lifecycle-pending
remove_case lifecycle-pending

apply_case 03-succeeded.yaml lifecycle-succeeded
kubectl --context "$profile" wait --for=jsonpath='{.status.phase}'=Succeeded pod/lifecycle-succeeded --timeout=120s
kubectl --context "$profile" logs lifecycle-succeeded
kubectl --context "$profile" get pod lifecycle-succeeded
remove_case lifecycle-succeeded

apply_case 04-failed.yaml lifecycle-failed
kubectl --context "$profile" wait --for=jsonpath='{.status.phase}'=Failed pod/lifecycle-failed --timeout=120s
kubectl --context "$profile" logs lifecycle-failed || true
kubectl --context "$profile" get pod lifecycle-failed
remove_case lifecycle-failed

apply_case 05-crashloopbackoff.yaml lifecycle-crashloop
sleep 18
kubectl --context "$profile" get pod lifecycle-crashloop -o wide
inspect_case lifecycle-crashloop
kubectl --context "$profile" logs lifecycle-crashloop --previous || kubectl --context "$profile" logs lifecycle-crashloop || true
remove_case lifecycle-crashloop

apply_case 06-imagepullbackoff.yaml lifecycle-image-error
sleep 12
kubectl --context "$profile" get pod lifecycle-image-error -o wide
inspect_case lifecycle-image-error
remove_case lifecycle-image-error

apply_case 07-readiness.yaml lifecycle-readiness
kubectl --context "$profile" wait --for=jsonpath='{.status.phase}'=Running pod/lifecycle-readiness --timeout=180s
sleep 7
kubectl --context "$profile" get pod lifecycle-readiness -o wide
inspect_case lifecycle-readiness
remove_case lifecycle-readiness

apply_case 08-liveness.yaml lifecycle-liveness
sleep 34
kubectl --context "$profile" get pod lifecycle-liveness -o wide
inspect_case lifecycle-liveness
kubectl --context "$profile" logs lifecycle-liveness --previous || true
remove_case lifecycle-liveness

apply_case 09-startup.yaml lifecycle-startup
kubectl --context "$profile" wait --for=condition=Ready pod/lifecycle-startup --timeout=180s
kubectl --context "$profile" get pod lifecycle-startup -o wide
inspect_case lifecycle-startup
remove_case lifecycle-startup

apply_case 10-init-container.yaml lifecycle-init
kubectl --context "$profile" wait --for=condition=Ready pod/lifecycle-init --timeout=180s
kubectl --context "$profile" logs lifecycle-init -c setup
kubectl --context "$profile" get pod lifecycle-init -o wide
inspect_case lifecycle-init
remove_case lifecycle-init

apply_case 11-multi-container.yaml lifecycle-multi-container
kubectl --context "$profile" wait --for=condition=Ready pod/lifecycle-multi-container --timeout=180s
kubectl --context "$profile" get pod lifecycle-multi-container -o wide
kubectl --context "$profile" logs lifecycle-multi-container -c sidecar --tail=3
inspect_case lifecycle-multi-container
remove_case lifecycle-multi-container

apply_case 12-termination.yaml lifecycle-termination
kubectl --context "$profile" wait --for=jsonpath='{.status.phase}'=Running pod/lifecycle-termination --timeout=180s
kubectl --context "$profile" get pod lifecycle-termination -o wide
termination_log=$(mktemp)
kubectl --context "$profile" logs -f lifecycle-termination >"$termination_log" 2>&1 &
termination_pid=$!
sleep 2
kubectl --context "$profile" delete pod lifecycle-termination --wait=false
for attempt in {1..30}; do
  if grep -Fq 'Cleanup complete' "$termination_log"; then break; fi
  sleep 1
done
cat "$termination_log"
if ! grep -Fq 'Cleanup complete' "$termination_log"; then
  echo 'Graceful termination message was not observed.' >&2
  inspect_case lifecycle-termination
  exit 1
fi
kubectl --context "$profile" wait --for=delete pod/lifecycle-termination --timeout=60s
kill "$termination_pid" >/dev/null 2>&1 || true
wait "$termination_pid" 2>/dev/null || true
termination_pid=
rm -f "$termination_log"
termination_log=

echo 'All twelve Pod lifecycle examples completed. Cleanup removes only this Minikube profile.'
