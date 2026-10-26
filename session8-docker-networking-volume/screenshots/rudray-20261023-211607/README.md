# Session 08 — bind-mount live update

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshot supplied by the user.

Nginx served the original host-mounted page, then served the edited page containing `Live bind-mount update` while the same container remained running. No image rebuild or container restart occurred. The helper restored the original tracked file and removed its temporary container.

- [Before/after bind-mount output](01-bind-mount-live-update.png)
