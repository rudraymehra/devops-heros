#!/usr/bin/env bash
set -euo pipefail

project=hw8-network-lab
compose=(docker compose -p "$project" -f demo/docker-compose.yml)

if [[ -n "$("${compose[@]}" ps -q)" ]]; then
  echo "Compose project $project already has containers; stopping to avoid changing them." >&2
  exit 1
fi

cleanup() {
  "${compose[@]}" down --volumes --remove-orphans >/dev/null 2>&1 || true
}
trap cleanup EXIT

"${compose[@]}" up --build -d --wait --wait-timeout 120

echo '=== Compose service status ==='
"${compose[@]}" ps

echo '=== Frontend resolves backend ==='
"${compose[@]}" exec -T frontend getent hosts backend

echo '=== Backend resolves database ==='
"${compose[@]}" exec -T backend getent hosts database

echo '=== Compose networks ==='
docker network ls --filter "label=com.docker.compose.project=$project"
for network in frontend_net backend_net database_net; do
  docker network inspect "${project}_${network}" --format '{{.Name}} internal={{.Internal}} containers={{len .Containers}}'
done

response=
for attempt in {1..20}; do
  if response=$(curl --fail --silent --show-error --max-time 3 http://localhost:8080/api 2>/dev/null); then
    break
  fi
  sleep 1
done
if [[ -z "$response" ]]; then
  echo 'Frontend /api check failed; Compose logs follow:' >&2
  "${compose[@]}" logs >&2 || true
  exit 1
fi
echo '=== Frontend /api response ==='
printf '%s\n' "$response"
printf '%s\n' "$response" | grep -F 'Backend is working!'
printf '%s\n' "$response" | grep -F 'Hello from MySQL!'

echo 'Three-tier network lab passed; cleanup removes only this isolated Compose project.'
