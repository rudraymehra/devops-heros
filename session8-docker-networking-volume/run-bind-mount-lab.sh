#!/usr/bin/env bash
set -euo pipefail

project=hw8-bind-mount-lab
compose=(docker compose -p "$project" -f bind-mount/docker-compose.yml)
site_file=bind-mount/site/index.html
backup=$(mktemp)
cp "$site_file" "$backup"
started=0

cleanup() {
  cp "$backup" "$site_file"
  rm -f "$backup"
  if [[ "$started" -eq 1 ]]; then
    "${compose[@]}" down --remove-orphans >/dev/null 2>&1 || true
  fi
}
trap cleanup EXIT

if [[ -n "$("${compose[@]}" ps -q)" ]]; then
  echo "Compose project $project already has containers; stopping to avoid changing them." >&2
  exit 1
fi

started=1
"${compose[@]}" up -d
"${compose[@]}" ps

echo '=== Initial page from bind mount ==='
curl --fail --silent --show-error --retry 10 --retry-connrefused --retry-delay 1 http://localhost:8088
curl --fail --silent --show-error http://localhost:8088 | grep -F 'Hello students'

cat > "$site_file" <<'HTML'
<!doctype html>
<html lang="en">
  <head><meta charset="utf-8"><title>Bind Mount Updated</title></head>
  <body><h1>Live bind-mount update</h1><p>Served without rebuilding or restarting the container.</p></body>
</html>
HTML

echo '=== Updated page, served without rebuild/restart ==='
updated=$(curl --fail --silent --show-error --retry 10 --retry-connrefused --retry-delay 1 http://localhost:8088)
printf '%s\n' "$updated"
printf '%s\n' "$updated" | grep -F 'Live bind-mount update'

echo '=== Container remained running during host-file edit ==='
"${compose[@]}" ps
echo 'Bind-mount update passed; cleanup restores the original tracked page and removes the container.'
