#!/usr/bin/env bash
set -euo pipefail

name=hw7-multistage

if docker container inspect "$name" >/dev/null 2>&1; then
  echo "Container $name already exists; stopping to avoid changing it." >&2
  exit 1
fi

cleanup() {
  docker rm -f "$name" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker build -t homework-multistage ./multi-stage-dockerfile
docker run -d --name "$name" -p 8080:8080 homework-multistage

response=
for attempt in {1..20}; do
  if response=$(curl --fail --silent --show-error --max-time 2 http://localhost:8080 2>/dev/null); then
    break
  fi
  sleep 1
done

if [[ -z "$response" ]]; then
  echo 'HTTP check did not become ready; container logs follow:' >&2
  docker logs "$name" >&2 || true
  exit 1
fi

printf '%s\n' "$response"
printf '%s\n' "$response" | grep -F 'Hello World from Docker Multi-Stage Build!'

docker ps --filter "name=$name"
echo 'Multi-stage HTTP check passed; temporary container will now be removed.'
