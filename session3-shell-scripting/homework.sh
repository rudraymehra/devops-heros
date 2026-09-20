#!/bin/bash
# =============================================================================
#  homework.sh  -  System Information Script
#  Author : Rudray Mehra
#  Session: 3 - Shell Scripting (DevOps Heroes)
#
#  What this script does:
#    1. Prints the current date and time
#    2. Prints the hostname of the machine
#    3. Prints the username of the person running the script
#    4. Prints the disk usage (df -h)
#    5. Prints the currently running processes (ps)
#    6. Asks the user (read -p) for a directory name and a file name
#    7. Creates the directory with mkdir and the file with touch
#    8. Saves the full process list into that file using > redirection
#
#  Usage:
#    chmod +x homework.sh
#    ./homework.sh                       # interactive
#    printf 'logs\nps.txt\n' | ./homework.sh   # non-interactive (piped input)
# =============================================================================

set -euo pipefail

# -----------------------------------------------------------------------------
# 1. Store system information in variables
#    $(command) runs the command and captures its output into the variable.
# -----------------------------------------------------------------------------
CURRENT_DATE=$(date)          # current date and time
HOST_NAME=$(hostname)         # machine hostname
USER_NAME=$(whoami)           # user running the script
DISK_USAGE=$(df -h)           # disk usage in human readable format
PROCESS_COUNT=$(ps -e -o pid= | wc -l | tr -d ' ')   # number of running processes

# A small helper variable so the separators look the same everywhere
LINE="============================================================"

# -----------------------------------------------------------------------------
# 2. Print the basic system information using the variables above
# -----------------------------------------------------------------------------
echo "$LINE"
echo "          SYSTEM INFORMATION REPORT"
echo "$LINE"
echo "Date & Time : $CURRENT_DATE"
echo "Hostname    : $HOST_NAME"
echo "Username    : $USER_NAME"
echo "$LINE"

# -----------------------------------------------------------------------------
# 3. Disk usage
# -----------------------------------------------------------------------------
echo ""
echo "DISK USAGE (df -h)"
echo "$LINE"
echo "$DISK_USAGE"
echo "$LINE"

# -----------------------------------------------------------------------------
# 4. Running processes (only the top few are printed on screen so the output
#    stays readable; the complete list goes into the file later on)
# -----------------------------------------------------------------------------
echo ""
echo "RUNNING PROCESSES (ps aux | sed -n '1,10p')  -  total: $PROCESS_COUNT"
echo "$LINE"
ps aux | sed -n '1,10p'
echo "$LINE"

# -----------------------------------------------------------------------------
# 5. Take user input with read -p
#    ${VAR:-default} means: use VAR if it is set and not empty, otherwise use
#    the default value. This lets the script run non-interactively as well.
# -----------------------------------------------------------------------------
echo ""
read -r -p "Enter the directory name to create [default: system_logs]: " DIR_NAME || :
DIR_NAME=${DIR_NAME:-system_logs}

read -r -p "Enter the file name to store processes [default: processes.txt]: " FILE_NAME || :
FILE_NAME=${FILE_NAME:-processes.txt}
case "$FILE_NAME" in
    */*|.|..) echo "Enter a file name without directory separators." >&2; exit 1 ;;
esac

# Full path of the output file built from the two inputs
FILE_PATH="$DIR_NAME/$FILE_NAME"

# -----------------------------------------------------------------------------
# 6. Create the directory and the file
#    mkdir -p  -> create the directory (and parents), no error if it exists
#    touch     -> create an empty file (or update its timestamp if it exists)
# -----------------------------------------------------------------------------
echo ""
echo "Creating directory : $DIR_NAME"
mkdir -p -- "$DIR_NAME"

echo "Creating file      : $FILE_PATH"
touch -- "$FILE_PATH"

# -----------------------------------------------------------------------------
# 7. Store the running processes in the file using > output redirection
#    '>' sends the output of the command to the file instead of the screen
#    (it overwrites the file if it already has content).
# -----------------------------------------------------------------------------
echo "Saving process list to $FILE_PATH ..."
ps aux > "$FILE_PATH"

# -----------------------------------------------------------------------------
# 8. Confirmation / summary
# -----------------------------------------------------------------------------
SAVED_LINES=$(wc -l < "$FILE_PATH" | tr -d ' ')
FILE_SIZE=$(wc -c < "$FILE_PATH" | tr -d ' ')

echo ""
echo "$LINE"
echo "DONE"
echo "$LINE"
echo "Run by              : $USER_NAME on $HOST_NAME"
echo "Process file        : $FILE_PATH"
echo "Lines written       : $SAVED_LINES"
echo "File size           : $FILE_SIZE bytes"
echo "$LINE"
