#!/usr/bin/env bash
set -euo pipefail

output_file="network-command-output.txt"

{
  printf 'Collected: %s\n\n' "$(date -u '+%Y-%m-%dT%H:%M:%SZ')"
  printf '## Interfaces and addresses\n'
  if command -v ip >/dev/null 2>&1; then ip addr; else ifconfig; fi
  printf '\n## Routing table\n'
  if command -v ip >/dev/null 2>&1; then ip route; else netstat -rn; fi
  printf '\n## Listening sockets\n'
  if command -v ss >/dev/null 2>&1; then ss -tuln; else netstat -an; fi
  printf '\n## DNS lookup\n'
  if command -v dig >/dev/null 2>&1; then dig +short example.com; else nslookup example.com; fi
  printf '\n## Connectivity\n'
  ping -c 4 1.1.1.1
  printf '\n## HTTP headers\n'
  curl --head --max-time 10 https://example.com
} > "$output_file" 2>&1

printf 'Network evidence written to %s\n' "$output_file"
