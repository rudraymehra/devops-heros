#!/usr/bin/env bash
set -euo pipefail

network=hw8-overlay-lab
swarm_started=0
network_created=0

cleanup() {
  if [[ "$network_created" -eq 1 ]]; then
    docker network rm "$network" >/dev/null 2>&1 || true
  fi
  if [[ "$swarm_started" -eq 1 ]]; then
    docker swarm leave --force >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

state=$(docker info --format '{{.Swarm.LocalNodeState}}')
if [[ "$state" != inactive ]]; then
  echo "Swarm state is '$state'; stopping without changing the existing Swarm." >&2
  exit 1
fi

if docker network inspect "$network" >/dev/null 2>&1; then
  echo "Network $network already exists; stopping without changing it." >&2
  exit 1
fi

echo '=== Swarm before lab ==='
docker info --format 'Swarm state: {{.Swarm.LocalNodeState}}'

if ! docker swarm init >/dev/null 2>&1; then
  echo 'Swarm initialization failed; no join tokens are shown by this helper.' >&2
  exit 1
fi
swarm_started=1

echo '=== Local Swarm node ==='
docker node ls

docker network create --driver overlay --attachable "$network"
network_created=1

echo '=== Overlay network inspection ==='
docker network inspect "$network" --format 'Name={{.Name}} Driver={{.Driver}} Scope={{.Scope}} Attachable={{.Attachable}} Internal={{.Internal}}'

echo 'Disposable overlay lab passed; cleanup removes its network and leaves its temporary Swarm.'
