#!/usr/bin/env bash
set -euo pipefail

current_date=$(date)
host_name=$(hostname)
user_name=$(whoami)
disk_usage=$(df -h)
process_count=$(ps -e | wc -l | tr -d ' ')

printf '%s\n' '=============================================='
printf '%s\n' '        SYSTEM INFORMATION REPORT'
printf '%s\n' '=============================================='
printf 'Current date: %s\n' "$current_date"
printf 'Hostname: %s\n' "$host_name"
printf 'Username: %s\n' "$user_name"
printf 'Process count (including ps header): %s\n' "$process_count"
printf '\nDisk usage (df -h):\n%s\n' "$disk_usage"
printf '\nRunning processes (first 10 by PID):\n'
# Omit process arguments because they may contain tokens or passwords.
# sed reads the full process list; head would close the pipe early and make
# ps report SIGPIPE under the script's `set -o pipefail` setting.
ps -eo pid,user,%cpu,%mem,comm | sed -n '1,11p'

read -r -p 'Enter your name: ' student_name
read -r -p 'Enter your roll number: ' roll_number
read -r -p 'Enter a directory name to create: ' output_directory

if [[ -z "$output_directory" || "$output_directory" == "/" || "$output_directory" == "." ]]; then
  printf 'Choose a non-empty directory name other than / or .\n' >&2
  exit 1
fi

mkdir -p "$output_directory"
process_file="${output_directory%/}/process.log"
touch "$process_file"
ps -eo pid,user,%cpu,%mem,comm > "$process_file"

printf '\nHello %s (roll number %s).\n' "$student_name" "$roll_number"
printf 'Created directory: %s\n' "$output_directory"
printf 'Saved running processes to %s using > redirection.\n' "$process_file"
printf '\nPreview of %s (first 5 lines):\n' "$process_file"
head -n 5 "$process_file"
printf 'Total lines in %s: %s\n' "$process_file" "$(wc -l < "$process_file" | tr -d ' ')"
printf '%s\n' 'Script finished successfully.'
