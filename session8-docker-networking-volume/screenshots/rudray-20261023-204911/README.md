# Session 08 — Compose networking

Capture date: 2026-10-23 (Asia/Kolkata). Untouched native terminal screenshots supplied by the user.

The frontend, backend, and MySQL database became healthy. Frontend DNS resolved `backend`, backend DNS resolved `database`, and `database_net` was reported as internal. The frontend `/api` response contained both the backend and MySQL messages. The isolated Compose project and volume were removed by the helper after the checks.

- [Compose build and service status](01-compose-build-and-status.png)
- [DNS, networks, and API response](02-dns-networks-and-api.png)
