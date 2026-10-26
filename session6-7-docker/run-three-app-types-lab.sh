#!/usr/bin/env bash
set -euo pipefail

names=(hwms-verify-node hwms-verify-python hwms-verify-java)

for name in "${names[@]}"; do
  if docker container inspect "$name" >/dev/null 2>&1; then
    echo "Container $name already exists; stopping to avoid changing it." >&2
    exit 1
  fi
done

cleanup() {
  docker rm -f "${names[@]}" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker build -t hwms-verify-node ./nodejs-app
docker build -t hwms-verify-python ./python-app
docker build -t hwms-verify-java ./java-app

docker run -d --name hwms-verify-node -p 127.0.0.1::3000 hwms-verify-node
docker run -d --name hwms-verify-python -p 127.0.0.1::8000 hwms-verify-python
docker run -d --name hwms-verify-java -p 127.0.0.1::8080 hwms-verify-java

check_app() {
  name=$1
  container_port=$2
  expected=$3
  host_port=$(docker port "$name" "$container_port/tcp" | sed -n '1s/.*://p')
  if [[ -z "$host_port" ]]; then
    echo "Could not determine published port for $name" >&2
    return 1
  fi

  response=
  for attempt in {1..20}; do
    if response=$(curl --fail --silent --show-error --max-time 2 "http://127.0.0.1:$host_port" 2>/dev/null); then
      break
    fi
    sleep 1
  done
  if [[ -z "$response" ]]; then
    echo "HTTP check failed for $name; container logs follow:" >&2
    docker logs "$name" >&2 || true
    return 1
  fi

  printf '\n=== %s on localhost:%s ===\n%s\n' "$name" "$host_port" "$response"
  printf '%s\n' "$response" | grep -F "$expected"
}

check_app hwms-verify-node 3000 'Hello World from Node.js!'
check_app hwms-verify-python 8000 'Hello World from Python + Docker!'
check_app hwms-verify-java 8080 'Hello World from Java + Docker!'

printf '\n=== Running containers ===\n'
docker ps --filter name=hwms-verify-
printf '\n=== Image sizes ===\n'
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}' | grep -E 'REPOSITORY|hwms-verify-'
echo 'All three application checks passed; temporary containers will now be removed.'
