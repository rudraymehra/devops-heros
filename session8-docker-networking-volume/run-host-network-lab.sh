#!/usr/bin/env bash
set -euo pipefail

project=hw8-host-network-lab
compose=(docker compose -p "$project" -f host-network/docker-compose.yml)

if [[ -n "$("${compose[@]}" ps -q)" ]]; then
  echo "Compose project $project already has containers; stopping to avoid changing them." >&2
  exit 1
fi

if command -v lsof >/dev/null 2>&1 && lsof -nP -iTCP:80 -sTCP:LISTEN >/dev/null 2>&1; then
  echo 'Host port 80 is already in use; stopping without changing the existing listener.' >&2
  lsof -nP -iTCP:80 -sTCP:LISTEN
  exit 1
fi

cleanup() {
  "${compose[@]}" down --remove-orphans >/dev/null 2>&1 || true
}
trap cleanup EXIT

"${compose[@]}" up -d
"${compose[@]}" ps

container=$("${compose[@]}" ps -q apache)
docker inspect "$container" --format 'NetworkMode={{.HostConfig.NetworkMode}}'
docker exec "$container" httpd -v

response=
for attempt in {1..15}; do
  if response=$(curl --fail --silent --show-error --max-time 2 http://localhost/ 2>/dev/null); then
    break
  fi
  sleep 1
done

if [[ -z "$response" ]]; then
  echo 'Host port 80 did not return an HTTP response. Docker Desktop host networking may need to be enabled in Docker Desktop settings.' >&2
  docker logs "$container" >&2 || true
  exit 1
fi

echo '=== HTTP response from localhost:80 ==='
printf '%s\n' "$response"
echo 'Host-network Apache check passed; the temporary Compose container will now be removed.'
