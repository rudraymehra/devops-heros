# Session 08 — host network attempt

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshot supplied by the user.

The Apache container started with `NetworkMode=host` and the image reports Apache 2.4.69. The check to `localhost:80` returned no HTTP response, so the task is recorded as blocked on Docker Desktop host-networking support/configuration. The helper removed its temporary Compose container. This is not a successful host-network HTTP check.

- [Host-network attempt and logs](01-host-network-blocked.png)
