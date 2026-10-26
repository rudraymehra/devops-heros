# Linux Homework

## Task 1: soft links and hard links

A symbolic (soft) link stores a path to another file. It may cross file systems and
may point to a directory, but it becomes broken when its target is removed. A hard
link is another directory entry for the same inode. It must remain on the same file
system and normally cannot point to a directory. Removing one hard-link name does
not remove the data while another hard link still exists.

```bash
mkdir -p link-lab && cd link-lab
printf 'DevOps link lab\n' > original.txt
ln -s original.txt soft-link.txt
ln original.txt hard-link.txt
ls -li original.txt soft-link.txt hard-link.txt
readlink soft-link.txt
rm soft-link.txt
rm hard-link.txt original.txt
cd .. && rmdir link-lab
```

`original.txt` and `hard-link.txt` have the same inode number. The symbolic link
has its own inode and displays `-> original.txt` in `ls -li` output.

## Task 2: `adduser` versus `useradd`

`useradd` is the low-level, portable account-creation utility. It uses command-line
flags and system defaults. On Debian and Ubuntu, `adduser` is a friendlier wrapper:
it prompts for account information, creates the home directory, and applies local
policy. For interactive account creation on Ubuntu, `adduser` is usually preferred.

```bash
sudo adduser devopsdemo
id devopsdemo
getent passwd devopsdemo
sudo deluser --remove-home devopsdemo
```

For a non-interactive service account, `useradd` is appropriate:

```bash
sudo useradd --system --no-create-home --shell /usr/sbin/nologin demo-service
sudo userdel demo-service
```

## Task 3: `journalctl`

`journalctl` queries logs collected by `systemd-journald`.

```bash
journalctl --boot
journalctl --priority=err --boot
journalctl --unit=ssh --since "1 hour ago"
journalctl --follow
journalctl --disk-usage
```

Useful interview distinction: `systemctl status nginx` shows a service summary and
recent messages, while `journalctl -u nginx` provides searchable historical logs.

## Task 4: command practice

| Purpose | Commands practiced |
|---|---|
| Navigation | `pwd`, `ls -la`, `cd` |
| Files | `touch`, `cp`, `mv`, `rm`, `find` |
| Text | `cat`, `less`, `head`, `tail`, `grep`, `sort`, `wc` |
| Permissions | `chmod`, `chown`, `umask` |
| Processes | `ps`, `top`, `kill` |
| Storage | `df -h`, `du -sh` |
| Networking | `ip addr`, `ss -tulpn`, `curl` |
| Archives | `tar`, `gzip`, `unzip` |

Run commands only in a disposable practice directory. Commands requiring `sudo`
should be performed on a lab VM, not a shared or production machine.

## Evidence checklist

- [x] Add terminal output for the link inode comparison: [2026-10-23 macOS capture](screenshots/rudray-20261023-085600/01-links.png). This proves the link behavior on macOS, not Linux.
- [x] Add terminal output showing both account types and cleanup in an Ubuntu 24.04 container: [capture 1](screenshots/rudray-20261023-090351/02-user-management-setup.png) · [capture 2](screenshots/rudray-20261023-090351/03-user-management-result.png).
- [x] Add `journalctl` output from a systemd-enabled Ubuntu 24.04 container: [2026-10-23 capture](screenshots/rudray-20261023-090745/04-journalctl.png). It shows system and cron logs, a generated test entry, journal disk usage, and container cleanup.
- [x] Add a command-practice transcript covering the listed command groups in Ubuntu 24.04: [commands](screenshots/rudray-20261023-090932/05-command-practice-commands.png) · [results](screenshots/rudray-20261023-090932/06-command-practice-results.png).
