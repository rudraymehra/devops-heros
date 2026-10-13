#!/usr/bin/env bash
set -euo pipefail

read -r -p "Enter your name: " student_name
read -r -p "Enter your enrollment number: " enrollment_number

output_directory="system-info-output"
process_file="${output_directory}/processes.txt"
report_file="${output_directory}/report.txt"

mkdir -p "$output_directory"
touch "$process_file" "$report_file"
printf 'Running processes:\n'
ps aux | tee "$process_file"

{
  printf 'Student: %s\n' "$student_name"
  printf 'Enrollment number: %s\n' "$enrollment_number"
  printf 'Current date: %s\n' "$(date)"
  printf 'Hostname: %s\n' "$(hostname)"
  printf 'Username: %s\n' "$(whoami)"
  printf '\nDisk usage:\n'
  df -h
  printf '\nProcess list saved to: %s\n' "$process_file"
} | tee "$report_file"

printf 'Report created successfully: %s\n' "$report_file"
