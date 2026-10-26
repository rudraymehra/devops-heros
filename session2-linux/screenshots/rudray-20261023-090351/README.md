# Session 01–02 — Task 2 user management

Rudray Mehra | 24 BCS 10425 | Batch B

Capture date: 2026-10-23, approximately 09:03–09:04 local time. Environment:
Ubuntu 24.04 container.

`adduser` created a regular account with a home directory. `deluser --remove-home`
removed it. `useradd` created a system service account with `/usr/sbin/nologin`,
and `userdel` removed it. The final lookup confirmed that both accounts were gone.

![Account creation and package setup](02-user-management-setup.png)
![Account verification and cleanup](03-user-management-result.png)
