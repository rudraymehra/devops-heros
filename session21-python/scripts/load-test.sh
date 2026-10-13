#!/usr/bin/env bash
set -euo pipefail
URL="${URL:-http://taskboard.local/api/tasks}"
for _ in $(seq 1 500); do curl -s "$URL" >/dev/null || true; done
echo "Load test completed"
