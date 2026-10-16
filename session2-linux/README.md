# Session 2 - Linux Fundamentals Homework

## Screenshot evidence audit — 2026-10-16

See [this session's screenshot inventory and actual capture results](screenshots/README.md).
Missing native captures remain marked pending; historical logs are not relabelled as fresh screenshots.

**Name:** Rudray Mehra · **Roll number:** 24 BCS 10425 · **Batch:** B
**GitHub:** [rudraymehra](https://github.com/rudraymehra)

This file preserves the Linux homework evidence already present in the student's
repository. Its original account labels and command output have not been rewritten
to imply a fresh execution. The recorded environment was an Ubuntu 22.04 container
on macOS, with a systemd-based image for journal checks. Expected-output examples
remain examples, not verified runs from the current completion pass.

---

## Task 1: Soft Link & Hard Link

### What is the difference?

A file on Linux has two parts: the **inode** (the on-disk metadata plus pointers to the data blocks) and one or more **directory entries** (names) that point at that inode.

- A **hard link** is simply a second name for the same inode. Both names are equal; there is no "original" and "copy". The inode keeps a link count, and the data is only freed when the count drops to 0.
- A **soft link** (symbolic link / symlink) is a separate small file whose content is a *path* to another file. It has its own inode, and the kernel follows the path every time the link is accessed.

| Feature | Soft link (`ln -s`) | Hard link (`ln`) |
| :--- | :--- | :--- |
| Inode | Own inode, different from the target | Same inode as the target |
| What it stores | The target's path (a string) | Nothing extra - it *is* the file |
| Delete the original | Link becomes broken/dangling | Data still fully accessible |
| Cross filesystem / partition | Yes | No (`Invalid cross-device link`) |
| Link to a directory | Yes | No (`hard link not allowed for directory`) |
| `ls -l` display | `lrwxrwxrwx ... name -> target` | Looks like a normal file, link count > 1 |
| Size shown | Length of the target path | Same as the file |
| Permissions | Always `777` on the link itself; target's perms apply | Shared with the file (same inode) |
| Typical use | `/usr/bin/python3 -> python3.10`, config switching, shortcuts | Backup snapshots, de-duplication, keeping a file alive |

### Commands to create both

```bash
# Soft (symbolic) link
ln -s <target> <link_name>

# Hard link
ln <target> <link_name>

# Inspect: -i shows inode number, -l shows link count in column 3
ls -li
stat <file>
readlink <soft_link>
```

### Practice: creating, using and deleting links

I ran the whole sequence inside `docker run --rm ubuntu:22.04 bash` with `set -x` so every command is echoed before its output.

```bash
mkdir -p /root/linkdemo && cd /root/linkdemo
echo "Hello from Rudray - link demo" > original.txt
ln -s original.txt soft_link.txt
ln original.txt hard_link.txt
ls -li
stat -c "%n inode=%i links=%h size=%s" original.txt hard_link.txt soft_link.txt
cat soft_link.txt
cat hard_link.txt
readlink soft_link.txt
```

```text
+ ls -li
total 8
70712 -rw-r--r-- 2 root root 30 Sep  3 14:22 hard_link.txt
70712 -rw-r--r-- 2 root root 30 Sep  3 14:22 original.txt
70713 lrwxrwxrwx 1 root root 12 Sep  3 14:22 soft_link.txt -> original.txt
+ stat -c '%n inode=%i links=%h size=%s' original.txt hard_link.txt soft_link.txt
original.txt inode=70712 links=2 size=30
hard_link.txt inode=70712 links=2 size=30
soft_link.txt inode=70713 links=1 size=12
+ cat soft_link.txt
Hello from Rudray - link demo
+ cat hard_link.txt
Hello from Rudray - link demo
+ readlink soft_link.txt
original.txt
```

`original.txt` and `hard_link.txt` share inode `70712` and both show link count `2`. `soft_link.txt` has its own inode `70713`, size `12` (the length of the string `original.txt`), and `ls` shows the arrow to its target.

**Writing through a hard link changes the same data:**

```bash
echo "appended via hard link" >> hard_link.txt
cat original.txt
```

```text
Hello from Rudray - link demo
appended via hard link
```

**Delete the original and observe both links:**

```bash
rm original.txt
ls -li
cat soft_link.txt
cat hard_link.txt
```

```text
+ ls -li
total 4
70712 -rw-r--r-- 1 root root 53 Sep  3 14:22 hard_link.txt
70713 lrwxrwxrwx 1 root root 12 Sep  3 14:22 soft_link.txt -> original.txt
+ cat soft_link.txt
cat: soft_link.txt: No such file or directory
+ cat hard_link.txt
Hello from Rudray - link demo
appended via hard link
```

The hard link's count dropped from 2 to 1 and the data is still there. The soft link still exists in the listing but is now dangling, because the path it points to is gone.

**Limits of hard links (directories and other filesystems):**

```bash
mkdir mydir
ln -s mydir dir_soft_link          # works
ln mydir dir_hard_link             # fails
ln hard_link.txt /dev/shm/cross_fs_hard_link        # /dev/shm is tmpfs, a different filesystem
ln -s /root/linkdemo/hard_link.txt /dev/shm/cross_fs_soft_link
ls -l /dev/shm
```

```text
+ ln mydir dir_hard_link
ln: mydir: hard link not allowed for directory
+ ln hard_link.txt /dev/shm/cross_fs_hard_link
ln: failed to create hard link '/dev/shm/cross_fs_hard_link' => 'hard_link.txt': Invalid cross-device link
+ ls -l /dev/shm
total 0
lrwxrwxrwx 1 root root 28 Sep  3 14:22 cross_fs_soft_link -> /root/linkdemo/hard_link.txt
```

**Deleting links:** a link is removed with plain `rm` (or `unlink`). Removing a link never touches the target's data.

```bash
rm soft_link.txt dir_soft_link
ls -li
```

```text
total 8
70712 -rw-r--r-- 1 root root   53 Sep  3 14:22 hard_link.txt
70714 drwxr-xr-x 2 root root 4096 Sep  3 14:22 mydir
```

Note: when deleting a soft link to a directory, do **not** add a trailing slash (`rm dir_soft_link`, not `rm -r dir_soft_link/`), otherwise the shell resolves the link and you end up deleting the contents of the real directory.

### Interview preparation

**Q: What is the difference between a hard link and a soft link?**
A hard link is another directory entry for the same inode, so it is indistinguishable from the original and survives its deletion. A soft link is a separate file that stores a path; it can cross filesystems and point to directories, but breaks if the target is moved or removed.

**Q: Why can't a hard link cross filesystems?**
Inode numbers are only unique inside one filesystem. A hard link references an inode number directly, so it has no meaning on another filesystem. That is exactly the `Invalid cross-device link` error I got when linking into `/dev/shm`.

**Q: Why are hard links to directories not allowed?**
They could create cycles in the directory tree, which would break tools like `find`, `du`, `rm -r` and `fsck`. Only the kernel-managed `.` and `..` entries are hard links to directories.

**Q: How do you find out whether two files are hard links of each other?**
`ls -li` or `stat` - same inode number on the same filesystem means the same file. `find . -samefile hard_link.txt` lists all names for that inode. `find . -inum 70712` does the same by inode number.

**Q: What happens to a hard link when the original file is deleted?**
Nothing visible; the link count just decrements. The data is freed only when the last name is removed and no process has the file open.

**Q: How do you find broken symlinks?**
`find /path -xtype l` (or `find /path -type l ! -exec test -e {} \; -print`).

### What I understood

The word "original" is misleading for hard links: every name is equally the file. Soft links are pointers by path, which makes them flexible (directories, other disks) but fragile. In practice I would use soft links for things like switching a `current` release directory or pointing a binary at a versioned file, and hard links when I need a file to stay alive even if someone deletes one of its names.

---

## Task 2: `adduser` vs `useradd`

### Key differences

| Property | `useradd` | `adduser` |
| :--- | :--- | :--- |
| Type | Low-level compiled binary from the `passwd`/`shadow-utils` package; available on every Linux distribution | Debian/Ubuntu Perl script (`#!/usr/bin/perl`) that wraps `useradd` and friends |
| Behaviour | Non-interactive; does exactly what the flags say and nothing more | Interactive by default; asks for password and GECOS info (full name, room, phone) |
| Home directory | **Not** created unless `-m` is passed | Always created, with skeleton files copied from `/etc/skel` |
| Default shell | `/bin/sh` (from `useradd -D`) | `/bin/bash` (from `DSHELL` in `/etc/adduser.conf`) |
| Password | Not set; account is locked until `passwd <user>` is run | Prompts for a password immediately (skippable with `--disabled-password`) |
| Private group | Depends on distro defaults / `-U` | Always creates a same-named private group (`USERGROUPS=yes`) |
| Config file | `/etc/default/useradd`, `/etc/login.defs` | `/etc/adduser.conf` |
| Best for | Scripts, Dockerfiles, Ansible, CI, system accounts (`useradd -r`) | A human creating a normal login user on Ubuntu/Debian |
| Removal counterpart | `userdel [-r]` | `deluser [--remove-home]` |

### Which one is preferred on Ubuntu and why?

On Ubuntu and Debian the recommended command for a person at the terminal is **`adduser`**. The Ubuntu documentation itself points to it because it applies the sane defaults you almost always want: a home directory populated from `/etc/skel`, `/bin/bash` as the shell, a private group, and a password prompt. With `useradd` it is very easy to forget `-m` or `-s /bin/bash` and end up with a user that has no home and logs into a bare `sh` prompt (I reproduce exactly that mistake below).

`useradd` is still the right tool when the user is created by a script or a Dockerfile, because it is fully non-interactive, identical across distributions, and every option is explicit.

### Demonstration (real run inside `ubuntu:22.04`)

First, confirming what the two commands actually are:

```bash
which useradd adduser
head -1 $(which adduser)
```

```text
/usr/sbin/useradd
/usr/sbin/adduser
#!/usr/bin/perl
```

#### `useradd` with the correct flags

```bash
useradd -m -s /bin/bash testuser
id testuser
grep testuser /etc/passwd
```

```text
uid=1000(testuser) gid=1000(testuser) groups=1000(testuser)
testuser:x:1000:1000::/home/testuser:/bin/bash
```

#### `useradd` without `-m` (the common mistake)

```bash
useradd plainuser
grep plainuser /etc/passwd
ls -ld /home/plainuser
```

```text
plainuser:x:1001:1001::/home/plainuser:/bin/sh
ls: cannot access '/home/plainuser': No such file or directory
```

The passwd entry *claims* a home of `/home/plainuser` and the shell defaulted to `/bin/sh`, but the directory was never created.

#### `adduser` - the recommended command on Ubuntu

Because I ran the container with `bash -c` and no `-it`, there is no TTY for `adduser` to prompt on, so I used `--disabled-password --gecos ""` to skip the interactive questions. The output shows every step `adduser` performs on my behalf:

```bash
adduser --disabled-password --gecos "" devopsuser
id devopsuser
grep devopsuser /etc/passwd
```

```text
Adding user `devopsuser' ...
Adding new group `devopsuser' (1002) ...
Adding new user `devopsuser' (1002) with group `devopsuser' ...
Creating home directory `/home/devopsuser' ...
Copying files from `/etc/skel' ...
uid=1002(devopsuser) gid=1002(devopsuser) groups=1002(devopsuser)
devopsuser:x:1002:1002:,,,:/home/devopsuser:/bin/bash
```

On a real Ubuntu server with a terminal, plain `sudo adduser devopsuser` additionally prompts like this (expected output on a Linux server, not captured from the container):

```text
New password:
Retype new password:
passwd: password updated successfully
Changing the user information for devopsuser
Enter the new value, or press ENTER for the default
        Full Name []: Rudray Mehra
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y
```

#### Verifying the home directories and skeleton files

```bash
ls -la /home
ls -la /home/devopsuser
```

```text
total 16
drwxr-xr-x 1 root       root       4096 Sep  3 14:22 .
drwxr-xr-x 1 root       root       4096 Sep  3 14:22 ..
drwxr-x--- 2 devopsuser devopsuser 4096 Sep  3 14:22 devopsuser
drwxr-x--- 2 testuser   testuser   4096 Sep  3 14:22 testuser

total 20
drwxr-x--- 2 devopsuser devopsuser 4096 Sep  3 14:22 .
drwxr-xr-x 1 root       root       4096 Sep  3 14:22 ..
-rw-r--r-- 1 devopsuser devopsuser  220 Sep  3 14:22 .bash_logout
-rw-r--r-- 1 devopsuser devopsuser 3771 Sep  3 14:22 .bashrc
-rw-r--r-- 1 devopsuser devopsuser  807 Sep  3 14:22 .profile
```

Notice `plainuser` has no directory in `/home` at all.

#### Where the different defaults come from

```bash
grep -E "^(DSHELL|DHOME|SKEL|FIRST_UID|LAST_UID|USERGROUPS)" /etc/adduser.conf
useradd -D
```

```text
DSHELL=/bin/bash
DHOME=/home
SKEL=/etc/skel
FIRST_UID=1000
LAST_UID=59999
USERGROUPS=yes

GROUP=100
HOME=/home
INACTIVE=-1
EXPIRE=
SHELL=/bin/sh
SKEL=/etc/skel
CREATE_MAIL_SPOOL=no
```

This explains the shell difference: `adduser` reads `DSHELL=/bin/bash`, `useradd` uses `SHELL=/bin/sh`.

#### Follow-up user management (password status, sudo, deletion)

```bash
passwd -S devopsuser
usermod -aG sudo devopsuser && id devopsuser
userdel -r testuser
ls -la /home
id testuser
```

```text
devopsuser L 09/03/2026 0 99999 7 -1
uid=1001(devopsuser) gid=1001(devopsuser) groups=1001(devopsuser),27(sudo)
userdel: testuser mail spool (/var/mail/testuser) not found
total 12
drwxr-xr-x 1 root       root       4096 Sep  3 14:23 .
drwxr-xr-x 1 root       root       4096 Sep  3 14:23 ..
drwxr-x--- 2 devopsuser devopsuser 4096 Sep  3 14:23 devopsuser
id: 'testuser': no such user
```

(`passwd -S` shows `L` = locked, because I used `--disabled-password`; on a real server I would run `sudo passwd devopsuser` to set one. The UIDs differ from the earlier block because this was a fresh container.)

### What I understood

`adduser` is a friendlier layer on top of `useradd`, and on Ubuntu it is the command I should reach for when creating a normal user by hand. `useradd` is the portable, scriptable primitive - whenever I use it I must remember `-m` and `-s /bin/bash`, otherwise I get a half-configured account like `plainuser` above.

---

## Task 3: `journalctl`

### What is `journalctl` used for?

`journalctl` is the query tool for the **systemd journal**, the binary, indexed log store maintained by `systemd-journald`. On a systemd-based distro (Ubuntu, Debian, RHEL, Fedora, etc.) every service's stdout/stderr, kernel messages (`dmesg`), syslog messages and boot events all land in the journal. Instead of grepping through many files under `/var/log`, `journalctl` lets me filter one stream by unit, time, priority, boot, PID, or free-text pattern.

### Viewing system and service logs - the commands I practised

```bash
journalctl                          # everything, oldest first, paged with less
journalctl -e                       # jump straight to the end
journalctl -r                       # newest first
journalctl -n 50                    # last 50 lines
journalctl -f                       # follow live, like tail -f
journalctl -b                       # only the current boot
journalctl -b -1                    # the previous boot (useful after a crash)
journalctl --list-boots             # all recorded boots
journalctl -k                       # kernel messages only (same as dmesg)
journalctl -p err                   # priority err and worse (emerg..err)
journalctl -p warning -b            # warnings and worse for this boot
journalctl --since "1 hour ago"
journalctl --since "2026-09-03 09:00" --until "2026-09-03 10:00"
journalctl -u ssh                   # one service (unit)
journalctl -u nginx -u docker       # more than one unit
journalctl -u docker -f             # follow one service live
journalctl -u ssh -n 20 --no-pager  # last 20 lines, no pager (good for scripts)
journalctl _PID=1234                # by process id
journalctl -t sudo                  # by syslog identifier
journalctl -g "Failed password"     # grep-style pattern match
journalctl -u nginx -o json-pretty  # structured output for parsing
journalctl -x -u nginx              # add catalog explanations to messages
journalctl --disk-usage             # how much space the journal takes
sudo journalctl --vacuum-time=7d    # drop entries older than 7 days
```

Priority levels: `0 emerg`, `1 alert`, `2 crit`, `3 err`, `4 warning`, `5 notice`, `6 info`, `7 debug`. `-p err` means "level 3 and more severe".

### Running it for real - step 1: a plain container has no journal

My Mac has no systemd (`which journalctl` -> not found). My first attempt was to install the `systemd` package in a normal `ubuntu:22.04` container so I could at least run the binary and check the options:

```bash
apt-get update && apt-get install -y systemd
journalctl --version
journalctl --help | head -40
```

```text
systemd 249 (249.11-0ubuntu3.22)
+PAM +AUDIT +SELINUX +APPARMOR +IMA +SMACK +SECCOMP +GCRYPT +GNUTLS +OPENSSL +ACL +BLKID +CURL +ELFUTILS +FIDO2 +IDN2 -IDN +IPTC +KMOD +LIBCRYPTSETUP +LIBFDISK +PCRE2 -PWQUALITY -P11KIT -QRENCODE +BZIP2 +LZ4 +XZ +ZLIB +ZSTD -XKBCOMMON +UTMP +SYSVINIT default-hierarchy=unified
journalctl [OPTIONS...] [MATCHES...]

Query the journal.

Options:
     --system                Show the system journal
     --user                  Show the user journal for the current user
  -M --machine=CONTAINER     Operate on local container
  -S --since=DATE            Show entries not older than the specified date
  -U --until=DATE            Show entries not newer than the specified date
  -c --cursor=CURSOR         Show entries starting at the specified cursor
     --after-cursor=CURSOR   Show entries after the specified cursor
     --show-cursor           Print the cursor after all the entries
     --cursor-file=FILE      Show entries after cursor in FILE and update FILE
  -b --boot[=ID]             Show current boot or the specified boot
     --list-boots            Show terse information about recorded boots
  -k --dmesg                 Show kernel message log from the current boot
  -u --unit=UNIT             Show logs from the specified unit
     --user-unit=UNIT        Show logs from the specified user unit
  -t --identifier=STRING     Show entries with the specified syslog identifier
  -p --priority=RANGE        Show entries with the specified priority
     --facility=FACILITY...  Show entries with the specified facilities
  -g --grep=PATTERN          Show entries with MESSAGE matching PATTERN
     --case-sensitive[=BOOL] Force case sensitive or insensitive matching
  -e --pager-end             Immediately jump to the end in the pager
  -f --follow                Follow the journal
  -n --lines[=INTEGER]       Number of journal entries to show
     --no-tail               Show all lines, even in follow mode
  -r --reverse               Show the newest entries first
  -o --output=STRING         Change journal output mode (short, short-precise,
                               short-iso, short-iso-precise, short-full,
                               short-monotonic, short-unix, verbose, export,
                               json, json-pretty, json-sse, json-seq, cat,
                               with-unit)
     --output-fields=LIST    Select fields to print in verbose/export/json modes
     --utc                   Express time in Coordinated Universal Time (UTC)
  -x --catalog               Add message explanations where available
     --no-full               Ellipsize fields
  -a --all                   Show all fields, including long and unprintable
  -q --quiet                 Do not show info messages and privilege warning
```

Querying the journal in that container gives an honest "nothing here", because `systemd-journald` is not PID 1 there and never wrote any journal files:

```bash
journalctl --no-pager
journalctl -u ssh --no-pager
```

```text
No journal files were found.
-- No entries --
No journal files were found.
-- No entries --
```

### Running it for real - step 2: a container where systemd is PID 1

To get real journal entries I built a tiny image on top of `ubuntu:22.04` that installs `systemd`, `cron` and `openssh-server`, enables the two services and uses `/sbin/init` as its command, then started it with the privileges systemd needs inside Docker:

```bash
# Dockerfile (summary): FROM ubuntu:22.04; apt-get install -y systemd systemd-sysv cron openssh-server;
#                       systemctl enable cron ssh; CMD ["/sbin/init"]
docker build -t hwlinux-systemd:22.04 .
docker run -d --name hwlinux-systemd --privileged --cgroupns=host \
  --tmpfs /run --tmpfs /run/lock -v /sys/fs/cgroup:/sys/fs/cgroup:rw hwlinux-systemd:22.04
docker exec hwlinux-systemd systemctl is-system-running
docker exec hwlinux-systemd journalctl --no-pager -n 5
```

```text
running
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on :: port 22.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Started OpenBSD Secure Shell server.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Reached target Multi-User System.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Reached target Graphical Interface.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Startup finished in 187ms.
```

Now `systemd-journald` is actually running and the journal has real entries. Everything below was run with `docker exec hwlinux-systemd bash -c '...'`; I removed the container afterwards.

### Practice: checking logs for a specific service (real output)

**The SSH service - status plus its last 10 journal lines:**

```bash
systemctl status ssh --no-pager
journalctl -u ssh -n 10 --no-pager
```

```text
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Thu 2026-09-03 14:37:47 UTC; 22s ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 25 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 26 (sshd)
      Tasks: 1 (limit: 5895)
     Memory: 1.7M
        CPU: 22ms
     CGroup: /docker/a68e12e5bab993568c94fd79a146482549fd14995cd4776ddfaeef4b32999a0c/system.slice/ssh.service
             └─26 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"

Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Starting OpenBSD Secure Shell server...
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on 0.0.0.0 port 22.
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on :: port 22.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Started OpenBSD Secure Shell server.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Starting OpenBSD Secure Shell server...
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on 0.0.0.0 port 22.
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on :: port 22.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Started OpenBSD Secure Shell server.
```

`systemctl status` already shows the tail of the unit's journal; `journalctl -u ssh` gives me the same lines but with the full history and all the filtering options.

**Restart a service and watch the events land in its log (`cron`):**

```bash
systemctl restart cron
journalctl -u cron --no-pager
```

```text
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Started Regular background program processing daemon.
Sep 03 14:37:47 a68e12e5bab9 cron[24]: (CRON) INFO (pidfile fd = 3)
Sep 03 14:37:47 a68e12e5bab9 cron[24]: (CRON) INFO (Running @reboot jobs)
Sep 03 14:38:10 a68e12e5bab9 systemd[1]: Stopping Regular background program processing daemon...
Sep 03 14:38:10 a68e12e5bab9 systemd[1]: cron.service: Deactivated successfully.
Sep 03 14:38:10 a68e12e5bab9 systemd[1]: Stopped Regular background program processing daemon.
Sep 03 14:38:10 a68e12e5bab9 systemd[1]: Started Regular background program processing daemon.
Sep 03 14:38:10 a68e12e5bab9 cron[47]: (CRON) INFO (pidfile fd = 3)
Sep 03 14:38:10 a68e12e5bab9 cron[47]: (CRON) INFO (Skipping @reboot jobs -- not system startup)
```

The unit filter catches both the messages systemd itself writes about the unit (Stopping / Stopped / Started) and the daemon's own output (`cron[47]`), and I can see the PID change from 24 to 47 across the restart.

**Generate a failed login and find it with the pattern filter:**

```bash
ssh -o BatchMode=yes -o StrictHostKeyChecking=no nobody@localhost true   # deliberately fails
journalctl -u ssh -g "Connection closed|Invalid|Failed" --no-pager
journalctl -u ssh -n 3 --no-pager
```

```text
nobody@localhost: Permission denied (publickey,password).
Sep 03 14:40:28 a68e12e5bab9 sshd[377]: Connection closed by authenticating user nobody ::1 port 57606 [preauth]
Sep 03 14:37:47 a68e12e5bab9 sshd[26]: Server listening on :: port 22.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Started OpenBSD Secure Shell server.
Sep 03 14:40:28 a68e12e5bab9 sshd[377]: Connection closed by authenticating user nobody ::1 port 57606 [preauth]
```

**Boot, priority, disk usage and structured output:**

```bash
journalctl --list-boots --no-pager
journalctl -b -p warning --no-pager | tail -3
journalctl --disk-usage
journalctl -u ssh -o json-pretty -n 1 --no-pager | grep -E "MESSAGE|PRIORITY|SYSLOG_IDENTIFIER|_SYSTEMD_UNIT"
journalctl -xe --no-pager | tail -4
```

```text
 0 88dab7259a99416e826474c7343c87ed Thu 2026-09-03 14:37:47 UTC—Thu 2026-09-03 14:38:10 UTC
Sep 03 14:37:47 a68e12e5bab9 kernel: netlink: 'init': attribute type 4 has an invalid length.
Sep 03 14:37:47 a68e12e5bab9 kernel: fakeowner: loading out-of-tree module taints kernel.
Sep 03 14:37:47 a68e12e5bab9 systemd[1]: Dependency failed for Record Runlevel Change in UTMP.
Archived and active journals take up 8.0M in the file system.
	"MESSAGE" : "Started OpenBSD Secure Shell server.",
	"PRIORITY" : "6",
	"SYSLOG_IDENTIFIER" : "systemd",
	"_SYSTEMD_UNIT" : "init.scope",
░░ A start job for unit systemd-logind.service has finished successfully.
░░ 
░░ The job identifier is 64.
Sep 03 14:40:28 a68e12e5bab9 sshd[377]: Connection closed by authenticating user nobody ::1 port 57606 [preauth]
```

Each journal line has the same layout: timestamp, hostname, `unit/process[PID]`, message. Filtering with `-u` selects lines belonging to that unit's cgroup, which is far more reliable than grepping `/var/log/syslog` for the word "sshd". `-p warning` reduced a full boot to three lines, `-o json-pretty` shows the structured fields behind every line (`PRIORITY` 6 = info), and `-x` appends the catalog explanation for messages that have one.

On a production Ubuntu server the exact same commands apply, just prefixed with `sudo` (a normal user needs to be in the `systemd-journal` or `adm` group to read the system journal), and a follow view is `sudo journalctl -u ssh -f`.

### What I understood

`journalctl` replaces "which log file do I open?" with "which filter do I apply?". The three filters I will use most as a DevOps engineer are `-u <service>` (what did this service say), `-b` / `--since` (when), and `-p err` (how bad). Combining them with `-f` gives a live view while I restart or deploy a service, and `-o json` makes the output easy to ship to a log pipeline.

---

## Task 4: Linux Command Cheat Sheet

There are three cheat sheets in this folder and I went through all of them:

1. **`basic-linux.pdf`** - the everyday commands: files and directories, viewing/searching text, processes and services, basic networking, permissions, packages, disk, cron/background jobs, users, system information.
2. **`ad-linux.pdf`** ("Advance Linux Commands", 5 pages) - a level up from the basic sheet, organised as: *System Monitoring & Performance* (`top`/`htop`, `vmstat 1`, `iostat -xz 1`, `sar -u 1 3`, `uptime`, `free -h`), *Process & Job Control* (`ps aux | grep`, `kill -9`, `pkill`, `nice -n 10`, `renice -n -5 -p PID`, `nohup ... &`, `bg`/`fg`), *Networking* (`ip a`, `netstat -tulnp`, `ss -tulwn`, `nmap IP`, `curl -I URL`, `ping`, `traceroute`), *Security & Permissions* (`chmod`, `chown`, `umask`, `sudo visudo`, `passwd`, `ssh user@host`, `scp`), *Disk & File Management* (`df -h`, `du -sh * | sort -h`, `mount`/`umount`, `lsblk`, `rsync -avz`, `find`, `locate`), *Logs & Debugging* (`journalctl -xe`, `tail -f /var/log/syslog`, `dmesg | less`, `strace -p PID`, `lsof -i :80`, `file`) and a *Pro Tips* page (`watch -n 1 df -h`, `ss -plnt`, `history | grep ssh`, `uptime && who`, `tldr`, `ls -ltr`, `netstat -plant | grep :22`, `grep -ir "error" /var/log/`, `xargs`, `alias ll='ls -alF'`).
3. **`Linux Networking Cheat Sheet.pdf`** - the `ip` command family (`ip addr`, `ip link`, `ip route`, `ip neigh`) plus `ss`, `ethtool`, `arping`, and the net-tools to iproute2 mapping: `ifconfig -> ip addr`, `netstat -> ss`, `route -> ip route`, `arp -> ip neigh`.

### Essential commands - purpose and basic usage

| # | Command | Purpose | Example |
| :--- | :--- | :--- | :--- |
| 1 | `pwd` | Print the current working directory | `pwd` |
| 2 | `ls` | List directory contents (`-l` long, `-a` hidden, `-i` inode, `-h` human sizes) | `ls -la /var/log` |
| 3 | `cd` | Change directory (`cd -` previous, `cd ~` home) | `cd /etc/nginx` |
| 4 | `mkdir` | Create directories (`-p` creates parents) | `mkdir -p /tmp/devops_logs` |
| 5 | `touch` | Create an empty file or update its timestamp | `touch index.html` |
| 6 | `cp` | Copy files/dirs (`-r` recursive, `-p` keep perms) | `cp -r app/ app_backup/` |
| 7 | `mv` | Move or rename | `mv app.log backup_app.log` |
| 8 | `rm` | Remove files (`-r` dirs, `-f` no prompt) - dangerous with `-rf` | `rm -rf /tmp/devops_logs` |
| 9 | `ln` | Create hard (`ln`) or soft (`ln -s`) links | `ln -s /opt/app-1.2 /opt/current` |
| 10 | `cat` / `less` / `head` / `tail` | View a file / page through / first N / last N lines (`tail -f` follows) | `tail -n 100 -f /var/log/syslog` |
| 11 | `grep` | Search text with patterns (`-r` recursive, `-n` line no., `-i` ignore case) | `grep -rn "ERROR" /var/log/` |
| 12 | `find` | Locate files by name, type, size, mtime | `find / -name "*.conf" -mtime -1` |
| 13 | `chmod` | Change permissions (octal or symbolic) | `chmod 755 script.sh` |
| 14 | `chown` | Change owner and group (`-R` recursive) | `chown -R www-data:www-data /var/www` |
| 15 | `df` | Disk space per filesystem | `df -h` |
| 16 | `du` | Size of files/directories | `du -sh /var/log` |
| 17 | `free` | RAM and swap usage | `free -h` |
| 18 | `ps` | Snapshot of processes (`aux` all, `-ef` full format) | `ps aux \| grep nginx` |
| 19 | `top` / `htop` | Live process and resource view | `top -bn1 \| head` |
| 20 | `kill` / `pkill` | Send a signal to a process (`-15` TERM default, `-9` KILL) | `kill -9 1234`, `pkill -f node` |
| 21 | `systemctl` | Manage systemd services | `systemctl status nginx`, `systemctl restart nginx` |
| 22 | `journalctl` | Read systemd logs | `journalctl -u nginx -f` |
| 23 | `uname` / `hostname` / `uptime` / `whoami` / `date` | Kernel and host info, load, current user, time | `uname -a` |
| 24 | `cat /etc/os-release` | Which distro and version | `cat /etc/os-release` |
| 25 | `ip a` / `ip route` / `ip neigh` | Interfaces and addresses / routing table / ARP table (replaces `ifconfig`, `route`, `arp`) | `ip a`, `ip route` |
| 26 | `ss` | Socket statistics; listening ports (replaces `netstat`) | `ss -tulnp` |
| 27 | `ping` | Check reachability and latency | `ping -c 3 8.8.8.8` |
| 28 | `curl` / `wget` | Talk to HTTP endpoints / download files | `curl -I https://github.com`, `wget <url>` |
| 29 | `apt` / `yum` / `dnf` | Package management (Debian/Ubuntu vs RHEL family) | `apt update && apt install nginx -y` |
| 30 | `adduser` / `useradd` / `usermod` / `passwd` / `id` / `userdel` | User management | `usermod -aG sudo devops` |
| 31 | `crontab` | Schedule jobs (`-e` edit, `-l` list); `min hour dom mon dow cmd` | `0 2 * * * /home/rudray/backup.sh` |
| 32 | `nohup ... &` | Run a command in the background, immune to logout | `nohup python3 app.py &` |
| 33 | `history`, `!!`, `!n`, `Ctrl+C`, `Ctrl+L` | Command history / repeat last / repeat nth / cancel / clear screen | `history \| tail` |

**From the advanced sheet (`ad-linux.pdf`):**

| # | Command | Purpose | Example |
| :--- | :--- | :--- | :--- |
| 34 | `vmstat` | Memory, swap, I/O, interrupts and CPU every N seconds (`r` = runnable procs, `wa` = I/O wait) | `vmstat 1 3` |
| 35 | `iostat` | Per-device disk I/O stats (`-x` extended, `-z` hide idle devices); from `sysstat` | `iostat -xz 1` |
| 36 | `sar` | Historical / live CPU, memory, network stats; from `sysstat` | `sar -u 1 3` |
| 37 | `nice` / `renice` | Start a command with a lower priority / change the priority of a running PID (range -20 high .. 19 low) | `nice -n 10 backup.sh`, `renice -n 15 -p 1234` |
| 38 | `jobs`, `bg`, `fg`, `Ctrl+Z` | Shell job control: list, resume in background, bring to foreground, suspend | `Ctrl+Z` then `bg %1` |
| 39 | `traceroute` | Show every hop a packet takes to a host (`-m` max hops) | `traceroute -m 5 8.8.8.8` |
| 40 | `nmap` | Scan a host for open ports (needs `nmap`) | `nmap -p 22,80,443 10.0.0.5` |
| 41 | `umask` | Default permission mask for new files (`022` -> files 644, dirs 755) | `umask`, `umask -S` |
| 42 | `sudo visudo` | Edit `/etc/sudoers` with syntax checking so a typo cannot lock everyone out of sudo | `sudo visudo` |
| 43 | `ssh` / `scp` | Secure remote login / copy over SSH | `ssh rudray@server`, `scp app.tar rudray@server:/tmp/` |
| 44 | `mount` / `umount` | Show or attach/detach filesystems | `mount \| head`, `mount /dev/sdb1 /mnt/data` |
| 45 | `lsblk` | Tree of block devices, partitions, sizes and mount points | `lsblk` |
| 46 | `rsync` | Efficient sync/copy (`-a` archive, `-v` verbose, `-z` compress); only transfers changes | `rsync -avz src/ dest/` |
| 47 | `locate` / `updatedb` | Very fast filename search from a prebuilt index | `updatedb && locate a.txt` |
| 48 | `file` | Identify the type of a file by content, not extension | `file /bin/bash` |
| 49 | `lsof -i :PORT` | Which process has a port (or file) open | `lsof -i :22` |
| 50 | `strace -p PID` | Trace system calls of a running process for debugging | `strace -p 1234` |
| 51 | `journalctl -xe` / `dmesg` | Jump to the end of the journal with explanations / kernel ring buffer | `journalctl -xe`, `dmesg \| less` |
| 52 | `watch` | Re-run a command every N seconds | `watch -n 1 df -h` |
| 53 | `ls -ltr` | List by modification time, newest last | `ls -ltr /var/log` |
| 54 | `xargs` | Build commands from stdin | `find . -name "*.tmp" \| xargs rm` |
| 55 | `alias` | Shell shortcuts | `alias ll='ls -alF'` |

### Practice - real outputs from my machine

The first group was run on my Mac in zsh (macOS is a Unix and these commands behave the same as on Linux, apart from small formatting differences). The second group needed Linux-only tools so I ran it in `ubuntu:22.04`. The third group covers the advanced sheet and was also run in `ubuntu:22.04` (plus the systemd container from Task 3 for the port-related commands).

#### On my Mac

```bash
pwd
whoami
hostname
uname -a
uptime
date
```

```text
/Users/rudraym/Devops assignment/devops-heros
rudraym
MacBook-Air-9.local
Darwin MacBook-Air-9.local 24.5.0 Darwin Kernel Version 24.5.0: Tue Apr 22 19:54:26 PDT 2025; root:xnu-11417.121.6~2/RELEASE_ARM64_T8112 arm64
19:53  up 8 days,  7:19, 1 user, load averages: 4.82 3.66 3.02
Thu Sep  3 19:53:53 IST 2026
```

```bash
ls -la session2-linux
```

```text
total 8088
drwxr-xr-x@  6 rudraym  staff      192 Sep  3 19:48 .
drwxr-xr-x@ 13 rudraym  staff      416 Sep  3 19:48 ..
-rw-r--r--@  1 rudraym  staff    68994 Sep  3 19:48 Linux Networking Cheat Sheet.pdf
-rw-r--r--@  1 rudraym  staff  1924235 Sep  3 19:48 ad-linux.pdf
-rw-r--r--@  1 rudraym  staff  2140415 Sep  3 19:48 basic-linux.pdf
-rw-r--r--@  1 rudraym  staff        1 Sep  3 19:48 session2.md
```

```bash
df -h /
du -sh session2-linux
```

```text
Filesystem        Size    Used   Avail Capacity iused ifree %iused  Mounted on
/dev/disk3s1s1   228Gi    17Gi    30Gi    37%    426k  311M    0%   /
3.9M	session2-linux
```

```bash
ps aux | head -4
```

```text
USER               PID  %CPU %MEM      VSZ    RSS   TT  STAT STARTED      TIME COMMAND
rudraym          41599 140.2  5.1 415926208 424144   ??  Rs    7:48PM   0:58.24 /System/Library/Frameworks/Virtualization.framework/Versions/A/XPCServices/com.apple.Virtualization.VirtualMachine.xpc/Contents/MacOS/com.apple.Virtualization.VirtualMachine
rudraym          41547  16.9  1.4 412585312 117296   ??  R     7:48PM   0:12.38 /Applications/Docker.app/Contents/MacOS/com.docker.backend services
_windowserver      206   8.5  0.6 413319504  47200   ??  Ss   26Aug26 981:01.45 /System/Library/PrivateFrameworks/SkyLight.framework/Resources/WindowServer -daemon
```

(The top process is the Linux VM that Docker Desktop uses to run my containers.)

```bash
grep -n "journalctl" ../homework_doc.txt
find session2-linux -name "*.pdf"
head -n 3 ../homework_doc.txt
tail -n 3 ../homework_doc.txt
```

```text
16:journalctl
17:* Learn what journalctl is used for.
18:* Learn how to view system and service logs using journalctl.
session2-linux/Linux Networking Cheat Sheet.pdf
session2-linux/ad-linux.pdf
session2-linux/basic-linux.pdf
Linux Fundamental
Linux Homework Tasks
Task 1: Soft Link & Hard Link
   * Take screenshots of the completed exercises.
   * Add the screenshots to the README.md file in your GitHub repository.
   * Complete any remaining exercises from the session.
```

```bash
ping -c 3 8.8.8.8
curl -sI https://github.com | head -5
```

```text
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=24.556 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=55.957 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=31.348 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 24.556/37.287/55.957/13.490 ms
HTTP/2 200 
date: Thu, 03 Sep 2026 14:23:50 GMT
content-type: text/html; charset=utf-8
content-language: en-US
vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, X-Requested-With, X-GitHub-Client-Version, Accept-Language, Sec-Fetch-Site,Accept-Encoding, Accept, X-Requested-With
```

#### Inside `ubuntu:22.04` (after `apt-get install -y iproute2 procps curl`)

```bash
cat /etc/os-release | head -4
```

```text
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.5 LTS (Jammy Jellyfish)"
```

```bash
ip a
ip route
```

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
11: eth0@if39: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 65535 qdisc noqueue state UP group default 
    link/ether d2:16:3b:0b:04:2e brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
default via 172.17.0.1 dev eth0 
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.2 
```

(I trimmed the unused `tunl0`, `gre0`, `sit0`, etc. tunnel interfaces from the `ip a` listing for readability. The container got `172.17.0.2` on Docker's default bridge and its default gateway is the bridge, `172.17.0.1`.)

```bash
ss -tulnp
free -h
top -bn1 | head -8
```

```text
Netid State Recv-Q Send-Q Local Address:Port Peer Address:PortProcess

               total        used        free      shared  buff/cache   available
Mem:           4.8Gi       455Mi       228Mi       0.0Ki       4.1Gi       4.2Gi
Swap:          1.0Gi          0B       1.0Gi

top - 14:26:08 up 7 min,  0 users,  load average: 2.22, 1.35, 0.59
Tasks:   3 total,   1 running,   2 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.0 sy,  0.0 ni,100.0 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   4919.4 total,    229.3 free,    454.2 used,   4236.0 buff/cache
MiB Swap:   1024.0 total,   1024.0 free,      0.0 used.   4277.6 avail Mem 

  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
    1 root      20   0    3876   2632   2504 S   0.0   0.1   0:00.04 bash
```

`ss -tulnp` printed only the header because nothing is listening inside a bare container - on a web server this is where I would see `:80` and `:22`.

```bash
mkdir -p /tmp/devops_logs && touch /tmp/devops_logs/app.log && ls -l /tmp/devops_logs
chmod 755 /tmp/devops_logs/app.log && chown nobody:nogroup /tmp/devops_logs/app.log && ls -l /tmp/devops_logs/app.log
cp /tmp/devops_logs/app.log /tmp/devops_logs/app.bak && mv /tmp/devops_logs/app.bak /tmp/devops_logs/backup_app.log && ls /tmp/devops_logs
rm -rf /tmp/devops_logs && ls /tmp/devops_logs
```

```text
total 0
-rw-r--r-- 1 root root 0 Sep  3 14:26 app.log
-rwxr-xr-x 1 nobody nogroup 0 Sep  3 14:26 /tmp/devops_logs/app.log
app.log
backup_app.log
ls: cannot access '/tmp/devops_logs': No such file or directory
```

`chmod 755` turned `rw-r--r--` (644) into `rwxr-xr-x`, and `chown nobody:nogroup` changed both owner and group in one step.


#### Advanced sheet inside `ubuntu:22.04` (after `apt-get install -y procps sysstat traceroute nmap rsync mlocate file lsof iproute2`)

**System monitoring and performance:**

```bash
vmstat 1 3
iostat -xz 1 2 | head -20
sar -u 1 3
uptime
```

```text
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0     12 278560 334636 3863544    0    0    45   746  462  687  2  2 95  1  0
 0  0     12 278560 334636 3863544    0    0     0     0 1305 1778  0  0 99  0  0
 0  0     12 278560 334636 3863544    0    0     0  3840  301  161  0  0 100  0  0

Linux 6.10.14-linuxkit (e43bd31d273d) 	09/03/26 	_aarch64_	(8 CPU)

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.86    0.00    2.34    0.59    0.00   95.21

Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
vda             19.28    185.53     9.53  33.07    0.44     9.62   83.44   5879.09   242.89  74.43    9.35    70.46   10.41 189632.85     0.00   0.00    0.28 18218.52   35.75    0.40    0.81   3.39
vdb              2.48    171.86     0.00   0.00    1.45    69.43    0.00      0.00     0.00   0.00    0.00     0.00    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.00   0.20

Linux 6.10.14-linuxkit (e43bd31d273d) 	09/03/26 	_aarch64_	(8 CPU)

14:39:07        CPU     %user     %nice   %system   %iowait    %steal     %idle
14:39:08        all      0.75      0.00      0.13      0.00      0.00     99.12
14:39:09        all      0.50      0.00      1.13      0.00      0.00     98.36
14:39:10        all      0.12      0.00      0.87      0.25      0.00     98.75
Average:        all      0.46      0.00      0.71      0.08      0.00     98.75
 14:39:10 up 20 min,  0 users,  load average: 1.33, 1.31, 1.13
```

`vmstat` gives one line per second: the `r`/`b` columns (runnable / blocked processes), swap-in/out, block I/O and the CPU split (`us`/`sy`/`id`/`wa`). `iostat -xz` shows the two virtual disks of Docker's Linux VM (`vda`, `vdb`) with their `r/s`, `w/s`, await times and `%util`, and `sar -u` gives a per-second CPU breakdown ending in an average. The machine was almost idle (`~99% idle`).

**Process and job control (run with `docker run --rm -t` so the shell had a TTY and `set -m` job control):**

```bash
nice -n 10 sleep 300 &
sleep 60 &
jobs
ps -o pid,ni,stat,cmd -C sleep
renice -n 15 -p $(pgrep -x sleep | head -1)
ps -o pid,ni,stat,cmd -C sleep
kill -STOP %2        # same effect as pressing Ctrl+Z on a foreground job
jobs
bg %2
jobs
kill %1 %2
```

```text
[1]-  Running                 nice -n 10 sleep 300 &
[2]+  Running                 sleep 60 &
  PID  NI STAT CMD
  212  10 SN   sleep 300
  213   0 S    sleep 60
212 (process ID) old priority 10, new priority 15
  PID  NI STAT CMD
  212  15 SN   sleep 300
  213   0 S    sleep 60
[1]-  Running                 nice -n 10 sleep 300 &
[2]+  Stopped                 sleep 60
[2]+ sleep 60 &
[1]-  Running                 nice -n 10 sleep 300 &
[2]+  Running                 sleep 60 &
[1]-  Terminated              nice -n 10 sleep 300
[2]+  Terminated              sleep 60
```

The `NI` column shows the niceness: `nice -n 10` started the first `sleep` at 10 (the `N` in `SN` also marks it as low priority), `renice -n 15` moved it to 15 while it was running, and the normal `sleep` stayed at 0. `kill -STOP` put job 2 into `Stopped`, `bg %2` resumed it in the background, and `fg %2` would have brought it back to the terminal.

**Networking:**

```bash
ss -tulwn
traceroute -m 5 -w 1 8.8.8.8
nmap -p 22,80,443 127.0.0.1
```

```text
Netid State Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
traceroute to 8.8.8.8 (8.8.8.8), 5 hops max, 60 byte packets
 1  172.17.0.1 (172.17.0.1)  8.338 ms  0.053 ms  0.025 ms
 2  * * *
 3  * * *
 4  * * *
 5  * * *
Starting Nmap 7.80 ( https://nmap.org ) at 2026-09-03 14:39 UTC
Nmap scan report for localhost (127.0.0.1)
Host is up (0.000046s latency).

PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  closed http
443/tcp closed https

Nmap done: 1 IP address (1 host up) scanned in 0.10 seconds
```

The first hop is Docker's bridge gateway `172.17.0.1`; after that Docker Desktop's VM does not pass the ICMP time-exceeded replies back, so the remaining hops show `* * *` (on a normal Linux host I would see my router, the ISP and finally `8.8.8.8`). `nmap` confirms nothing is listening in the bare container - all three ports are `closed`.

In the systemd container from Task 3, where `sshd` is actually running, the same port-inspection commands show a real listener:

```bash
lsof -i :22
ss -plnt
```

```text
COMMAND PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
sshd     26 root    3u  IPv4  96214      0t0  TCP *:22 (LISTEN)
sshd     26 root    4u  IPv6  96216      0t0  TCP *:22 (LISTEN)
State  Recv-Q Send-Q Local Address:Port Peer Address:PortProcess
LISTEN 0      128          0.0.0.0:22        0.0.0.0:*    users:(("sshd",pid=26,fd=3))
LISTEN 0      128             [::]:22           [::]:*    users:(("sshd",pid=26,fd=4))
```

**Security and permissions:**

```bash
umask
umask -S
touch umask_test && ls -l umask_test
```

```text
0022
u=rwx,g=rx,o=rx
-rw-r--r-- 1 root root 0 Sep  3 14:39 umask_test
```

`umask 022` removes write permission for group and others: a new file starts from `666` and becomes `644` (`rw-r--r--`), a new directory starts from `777` and becomes `755`. I did not run `visudo`, `passwd` or `scp` here because they need an interactive terminal or a second host; their purpose is in the table above.

**Disk and file management:**

```bash
lsblk
mount | head -5
df -h / /dev/shm
mkdir -p src && echo one > src/a.txt && echo two > src/b.txt
rsync -avz src/ dest/
rsync -avz src/ dest/       # second run - nothing changed
updatedb && locate a.txt
file /bin/bash /etc/passwd src/a.txt
```

```text
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
vda    254:0    0 228.3G  0 disk 
`-vda1 254:1    0 228.3G  0 part /etc/hosts
                                 /etc/hostname
                                 /etc/resolv.conf
vdb    254:16   0 557.1M  1 disk 
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/4LYJIB5QGJ7WOXO6OVBUTUTXQI:/var/lib/docker/overlay2/l/QFIRTEPR5SNKFAQZJNF56TDBFH,upperdir=/var/lib/docker/overlay2/30ae75356b110a283efbcf5cdc5b7051e7c515e1b2660557da3617237b8317fe/diff,workdir=/var/lib/docker/overlay2/30ae75356b110a283efbcf5cdc5b7051e7c515e1b2660557da3617237b8317fe/work)
proc on /proc type proc (rw,nosuid,nodev,noexec,relatime)
tmpfs on /dev type tmpfs (rw,nosuid,size=65536k,mode=755)
devpts on /dev/pts type devpts (rw,nosuid,noexec,relatime,gid=5,mode=620,ptmxmode=666)
sysfs on /sys type sysfs (ro,nosuid,nodev,noexec,relatime)
Filesystem      Size  Used Avail Use% Mounted on
overlay         224G   28G  186G  13% /
shm              64M     0   64M   0% /dev/shm
sending incremental file list
created directory dest
./
a.txt
b.txt

sent 190 bytes  received 84 bytes  548.00 bytes/sec
total size is 8  speedup is 0.03
sending incremental file list

sent 87 bytes  received 12 bytes  198.00 bytes/sec
total size is 8  speedup is 0.08
/dest/a.txt
/src/a.txt
/bin/bash:   ELF 64-bit LSB pie executable, ARM aarch64, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux-aarch64.so.1, BuildID[sha1]=be49fa95e8d5f9adc2d850e7967b3c3082466448, for GNU/Linux 3.7.0, stripped
/etc/passwd: ASCII text
src/a.txt:   ASCII text
```

(I trimmed sixteen empty `nbd*` network-block devices from the `lsblk` output.) `lsblk` shows the VM's 228 GB virtual disk `vda` and its partition; the container root is an `overlay` filesystem, which is what `mount` and `df` report. The second `rsync` run transferred no files - that incremental behaviour is why it is the standard tool for backups and deployments. `locate` needed `updatedb` first because it searches an index, not the disk, and `file` identified the bash binary as an ARM64 ELF executable, which matches my Apple Silicon Mac.

**Logs, debugging and pro tips:**

```bash
ls -ltr /etc | tail -3
echo "a b c" | xargs -n1 echo item
alias ll="ls -alF"; alias ll
```

```text
-rw-r--r-- 1 root root    1229 Sep  3 14:39 passwd
drwxr-xr-x 1 root root    4096 Sep  3 14:39 default
-rw-r--r-- 1 root root    8604 Sep  3 14:39 ld.so.cache
item a
item b
item c
alias ll='ls -alF'
```

`ls -ltr` puts the most recently changed files last, so the ones `apt-get install` just touched appear at the bottom. `xargs -n1` turned one line of stdin into three separate commands. The `journalctl -xe` and `lsof -i :22` items from this page were covered above in the systemd container.

### What I understood

Most day-to-day DevOps work on a server is a small loop of these commands: find out where I am and what is running (`pwd`, `ls`, `ps`, `top`, `ss`), look at what went wrong (`tail -f`, `grep`, `journalctl -u`), fix permissions or files (`chmod`, `chown`, `cp`, `mv`), and check resources and the network (`df`, `free`, `ip a`, `ping`, `curl`). The networking cheat sheet made it clear that `ifconfig`, `netstat`, `route` and `arp` are legacy and I should default to `ip` and `ss`. The advanced sheet added the second layer I need when a box is slow or misbehaving: `vmstat`/`iostat`/`sar` to tell CPU, memory and disk problems apart, `nice`/`renice` and job control to keep a heavy job from hurting a service, `lsof -i`/`ss -plnt` to find who owns a port, and `rsync` as the default way to move files around.

---

## Summary

| Task | Status | Where executed |
| :--- | :--- | :--- |
| 1. Soft vs hard links | Done - created, inspected, deleted, tested cross-filesystem and directory cases | `ubuntu:22.04` container |
| 2. `adduser` vs `useradd` | Done - created `testuser` (useradd) and `devopsuser` (adduser), compared defaults, removed a user | `ubuntu:22.04` container |
| 3. `journalctl` | Done - options studied; real service logs (`ssh`, `cron`) captured with `-u`, `-n`, `-g`, `-p`, `-b`, `-o json-pretty`, `-x` in a systemd-as-PID-1 container | `ubuntu:22.04` container + custom `systemd` container |
| 4. Cheat sheet | Done - all three PDFs reviewed, 55-row table, 45+ commands executed for real | macOS terminal + `ubuntu:22.04` container |
