# Session 3 - Shell Scripting Homework: System Information Script

**Name:** Rudray Mehra
**GitHub:** [rudraymehra](https://github.com/rudraymehra)
**Script:** [`homework.sh`](./homework.sh)

## The task

Write a shell script that:

- prints the current date
- prints the hostname
- prints the username
- prints the disk usage
- prints the running processes
- uses variables to store and reuse data
- takes user input with `read -p`
- creates a directory with `mkdir`
- creates a file with `touch`
- stores the running-process list in that file using `>` output redirection

Commands that had to be used: `mkdir`, `touch`, `echo`, `df`, `ps`, `read -p`, variables and `>` redirection.

## How I approached it

I split the script into small numbered blocks so that each requirement from the task maps to one block:

1. Capture system information into variables with `$(command)` substitution.
2. Print the variables with `echo`.
3. Print `df -h`.
4. Print the first 10 lines of `ps aux` on screen (the complete list goes into the file later, so the terminal does not get flooded).
5. Ask the user for a directory name and a file name using `read -p`. Both prompts have a default (`${VAR:-default}`) so the script also works when it is run non-interactively, for example in a pipeline or from another script.
6. `mkdir -p` the directory and `touch` the file.
7. `ps aux > file` to write the full process list.
8. Print a short summary (lines written, file size).

I deliberately did not put `clear` at the top of the script, because it wipes the terminal history of whoever runs it and it breaks when the output is redirected to a file.

## The script

```bash
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
```

## Commands used and what each one does

| Command / feature | Where it is used in the script | What it does |
|---|---|---|
| `#!/bin/bash` | line 1 | Shebang. Tells the OS to run the file with bash when executed directly (`./homework.sh`). |
| Variables (`NAME=value`, `$NAME`) | `CURRENT_DATE`, `HOST_NAME`, `USER_NAME`, `DISK_USAGE`, `DIR_NAME`, `FILE_NAME`, `FILE_PATH`, ... | Store a value once and reuse it. No spaces around `=`. I always quote `"$VAR"` when using it so names with spaces do not break the script. |
| `$(command)` | `CURRENT_DATE=$(date)` etc. | Command substitution: runs the command and puts its output into the variable. |
| `date` | block 1 | Prints the current date and time. |
| `hostname` | block 1 | Prints the name of the machine. |
| `whoami` | block 1 | Prints the user that is running the script. `$USER` would also work, but `whoami` is more reliable under `sudo`. |
| `echo` | everywhere | Prints text and variable values to standard output. `echo ""` prints an empty line. |
| `df -h` | block 3 | Shows disk usage of all mounted filesystems. `-h` = human readable (G, M instead of raw 1K blocks). |
| `ps aux` | blocks 4 and 7 | Lists running processes. `a` = all users, `u` = user-oriented format (CPU, MEM), `x` = include processes without a terminal (daemons). |
| `ps -e \| wc -l` | block 1 | `-e` lists every process; piping to `wc -l` counts the lines, which gives me the total process count for the header. |
| `head -n 10` | block 4 | Shows only the first 10 lines so the screen output stays short. |
| `read -p "prompt" VAR` | block 5 | Prints the prompt and waits for the user to type a line, storing it in `VAR`. |
| `${VAR:-default}` | block 5 | Parameter expansion with a default. If the user just hits Enter (or stdin is empty), the default is used. |
| `mkdir -p DIR` | block 6 | Creates the directory. `-p` also creates parent directories and does not error if it already exists. |
| `touch FILE` | block 6 | Creates an empty file (or just updates the modification time if it already exists). |
| `>` | block 7 (`ps aux > "$FILE_PATH"`) | Output redirection: sends stdout of the command into the file instead of the terminal. It **overwrites** the file. (`>>` would append instead.) |
| `wc -l < FILE`, `wc -c < FILE` | block 8 | Counts lines / bytes of the file. Using `<` (input redirection) instead of passing the filename makes `wc` print only the number, without the file name. |
| `chmod +x homework.sh` | before running | Gives the file the execute permission so it can be run as `./homework.sh`. |

## Running the script

### Making it executable

```bash
chmod +x homework.sh
ls -l homework.sh
```

```text
-rwxr-xr-x@ 1 rudraym  staff  4870 Sep  3 19:52 homework.sh
```

### Full run (Ubuntu 22.04)

I ran the script in a fresh Ubuntu 22.04 container on my laptop (`docker run ... ubuntu:22.04`) so the `df` and `ps` output is in the standard Linux format that we see on servers. I started a few dummy background processes (`sleep`, `tail -f /dev/null`, a `while` loop) so there was something to see in the process list. The inputs `hw_logs` and `process.log` were piped into the script, which is why the two `read -p` prompts do not show a typed answer in the output below.

```bash
printf 'hw_logs\nprocess.log\n' | ./homework.sh
```

```text
============================================================
          SYSTEM INFORMATION REPORT
============================================================
Date & Time : Thu Sep  3 14:23:24 UTC 2026
Hostname    : 084f10f5e6af
Username    : root
============================================================

DISK USAGE (df -h)
============================================================
Filesystem              Size  Used Avail Use% Mounted on
overlay                 224G   24G  189G  12% /
tmpfs                    64M     0   64M   0% /dev
shm                      64M     0   64M   0% /dev/shm
/run/host_mark/private  229G  199G   30G  87% /root/homework.sh
/dev/vda1               224G   24G  189G  12% /etc/hosts
tmpfs                   2.5G     0  2.5G   0% /proc/scsi
tmpfs                   2.5G     0  2.5G   0% /sys/firmware
============================================================

RUNNING PROCESSES (ps aux | head -n 10)  -  total: 12
============================================================
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2224   888 ?        Ss   14:23   0:00 sleep infinity
root         7  0.0  0.0   2224   888 ?        Ss   14:23   0:00 sleep 3600
root        13  0.0  0.0   2256   904 ?        Ss   14:23   0:00 tail -f /dev/null
root        19  0.0  0.0   3876  2628 ?        Ss   14:23   0:00 bash -c while true; do sleep 5; done
root        25  0.0  0.0   2224  1012 ?        S    14:23   0:00 sleep 5
root        26  0.0  0.0   3876  2512 ?        Ss   14:23   0:00 bash -c printf "hw_logs\nprocess.log\n" | ./homework.sh
root        33  0.0  0.0   3876  2760 ?        S    14:23   0:00 /bin/bash ./homework.sh
root        42  0.0  0.0   6444  2412 ?        R    14:23   0:00 ps aux
============================================================

Enter the directory name to create [default: system_logs]: Enter the file name to store processes [default: processes.txt]:
Creating directory : hw_logs
Creating file      : hw_logs/process.log
Saving process list to hw_logs/process.log ...

============================================================
DONE
============================================================
Run by              : root on 084f10f5e6af
Process file        : hw_logs/process.log
Lines written       : 9
File size           : 769 bytes
============================================================
```

### Verifying the directory and the file that were created

```bash
ls -la hw_logs
```

```text
total 12
drwxr-xr-x 2 root root 4096 Sep  3 14:23 .
drwx------ 1 root root 4096 Sep  3 14:23 ..
-rw-r--r-- 1 root root  769 Sep  3 14:23 process.log
```

```bash
head -n 10 hw_logs/process.log
```

```text
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0   2224   888 ?        Ss   14:23   0:00 sleep infinity
root         7  0.0  0.0   2224   888 ?        Ss   14:23   0:00 sleep 3600
root        13  0.0  0.0   2256   904 ?        Ss   14:23   0:00 tail -f /dev/null
root        19  0.0  0.0   3876  2628 ?        Ss   14:23   0:00 bash -c while true; do sleep 5; done
root        25  0.0  0.0   2224  1012 ?        S    14:23   0:00 sleep 5
root        26  0.0  0.0   3876  2512 ?        Ss   14:23   0:00 bash -c printf "hw_logs\nprocess.log\n" | ./homework.sh
root        33  0.0  0.0   3876  2760 ?        S    14:23   0:00 /bin/bash ./homework.sh
root        46  0.0  0.0   6444  2412 ?        R    14:23   0:00 ps aux
```

```bash
wc -l hw_logs/process.log
```

```text
9 hw_logs/process.log
```

The `ps aux` that is saved in the file is a separate run from the one shown on screen, so its own PID (46 vs 42) is different. Everything else matches.

### Running with the defaults (just pressing Enter / empty stdin)

```bash
./homework.sh < /dev/null | tail -n 7
ls -la system_logs
```

```text
DONE
============================================================
Run by              : root on 084f10f5e6af
Process file        : system_logs/processes.txt
Lines written       : 10
File size           : 853 bytes
============================================================
total 12
drwxr-xr-x 2 root root 4096 Sep  3 14:23 .
drwx------ 1 root root 4096 Sep  3 14:23 ..
-rw-r--r-- 1 root root  853 Sep  3 14:23 processes.txt
```

Because of `${VAR:-default}`, an empty answer falls back to `system_logs/processes.txt` instead of failing on an empty path.

### Same script directly on macOS

The script is plain POSIX-friendly bash, so it also runs unchanged on my Mac (bash 3.2). Only the `df`/`ps` column layout differs slightly because the macOS versions of those tools are the BSD ones. Header and disk section from that run:

```bash
printf 'hw_logs\nprocess.log\n' | ./homework.sh
```

```text
============================================================
          SYSTEM INFORMATION REPORT
============================================================
Date & Time : Thu Sep  3 19:52:37 IST 2026
Hostname    : MacBook-Air-9.local
Username    : rudraym
============================================================

DISK USAGE (df -h)
============================================================
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   228Gi    17Gi    31Gi    36%    426k  325M    0%   /
devfs            223Ki   223Ki     0Bi   100%     770     0  100%   /dev
/dev/disk3s6     228Gi   8.0Gi    31Gi    21%       8  325M    0%   /System/Volumes/VM
/dev/disk3s2     228Gi    16Gi    31Gi    34%    2.0k  325M    0%   /System/Volumes/Preboot
/dev/disk3s4     228Gi   751Mi    31Gi     3%     330  325M    0%   /System/Volumes/Update
/dev/disk1s2     500Mi   6.0Mi   482Mi     2%       1  4.9M    0%   /System/Volumes/xarts
/dev/disk1s1     500Mi   5.6Mi   482Mi     2%      34  4.9M    0%   /System/Volumes/iSCPreboot
/dev/disk1s3     500Mi   1.2Mi   482Mi     1%      68  4.9M    0%   /System/Volumes/Hardware
/dev/disk3s5     228Gi   153Gi    31Gi    84%    2.1M  325M    1%   /System/Volumes/Data
map auto_home      0Bi     0Bi     0Bi   100%       0     0     -   /System/Volumes/Data/home
/dev/disk2s1     5.0Gi   1.7Gi   3.2Gi    35%      66   34M    0%   /System/Volumes/Update/SFR/mnt1
/dev/disk3s1     228Gi    17Gi    31Gi    36%    459k  325M    0%   /System/Volumes/Update/mnt1
============================================================

RUNNING PROCESSES (ps aux | head -n 10)  -  total: 480
...
Process file        : hw_logs/process.log
Lines written       : 477
File size           : 109134 bytes
============================================================
```

(The macOS process lines are several hundred characters long because of GUI app arguments, so I have cut that block from the README; the file `hw_logs/process.log` contained 477 process lines / 109 KB.)

## What I understood

- **Variables + `$(...)`** let me run a command once and reuse the result in several places (for example `$USER_NAME` and `$HOST_NAME` appear both in the header and in the summary).
- **`read -p`** is how a script becomes interactive, and `${VAR:-default}` is the standard way to make that input optional so the script still works in cron jobs or pipelines where nobody is there to type.
- **`>` vs `>>`**: `>` truncates the file and writes fresh content; `>>` appends. Because I use `>`, running the script twice with the same file name simply refreshes the process snapshot instead of growing the file.
- **`mkdir -p` and `touch` are idempotent**: re-running the script does not fail if the directory or file already exists, which is the behaviour you want from an automation script.
- **`df -h` and `ps aux`** are the two everyday commands for checking "is the disk full?" and "what is running?" on a server. `ps aux` output on Linux (procps) and macOS (BSD) has slightly different columns, but the flags are the same.
- Always **quote variables** (`"$DIR_NAME"`) so a name with a space does not turn into two arguments to `mkdir`.

## Submission review

The current script excludes the `ps` header from its process count, accepts literal backslashes with `read -r -p`, and exits on command, directory or file errors. File names cannot escape the selected output directory. The full process list is still written with `>` redirection. Earlier terminal output above is retained as the original run record. Current input and file-handling checks used controlled process data because the review sandbox blocks reading host processes; see [verification](../evidence/verification.md).
