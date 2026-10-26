# Session 08 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 6. Five fresh native captures document the Compose network lab, the blocked host-network attempt, the bind-mount update, and the overlay network inspection.

## Fresh execution records

### [rudray-20261023-204911](rudray-20261023-204911/README.md)

- Task 1: PASS. Frontend, backend, and database became healthy; frontend resolved `backend`, backend resolved `database`; `database_net` was internal; `/api` returned backend and MySQL messages.
- [Compose build and service status](rudray-20261023-204911/01-compose-build-and-status.png)
- [DNS, network inspection, and API output](rudray-20261023-204911/02-dns-networks-and-api.png)

### [rudray-20261023-211109](rudray-20261023-211109/README.md)

- Task 2: BLOCKED on Docker Desktop. Apache started with `NetworkMode=host`, but `localhost:80` returned no HTTP response; the run output notes host networking may need to be enabled in Docker Desktop settings.
- [Host-network attempt and Apache logs](rudray-20261023-211109/01-host-network-blocked.png)

### [rudray-20261023-211607](rudray-20261023-211607/README.md)

- Task 3: PASS. Nginx first served the tracked page, then served the changed host-mounted page without rebuilding or restarting. The helper restored the tracked page and removed its container.
- [Before/after bind-mount output](rudray-20261023-211607/01-bind-mount-live-update.png)

### [rudray-20261023-212307](rudray-20261023-212307/README.md)

- Task 4: PASS. The helper confirmed Swarm was inactive, initialized a temporary manager, inspected the attachable `overlay` network, and cleaned up.
- [Swarm node and overlay network details](rudray-20261023-212307/01-overlay-network-inspection.png)

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Capture Compose networks/connectivity. Bind-mount edit/reload and host-network behaviour need their own live run; Docker Desktop host networking may need explicit support..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Capture Compose networks/connectivity. Bind-mount edit/reload and host-network behaviour need their own live run; Docker Desktop host networking may need explicit support..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [Earlier GitHub Actions run](https://github.com/rudraymehra/devops-heros/actions/runs/38372002674)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Still needs genuine capture

The four assignment tasks now have execution records. Task 2 is explicitly blocked because Docker Desktop did not serve the Apache host-network container on `localhost:80`; all other task checks passed.

The overlay capture was rerun with Swarm initialization output suppressed. The first successful run that displayed a worker join token is intentionally excluded from this repo.

## Reference image inventory (not copied)

- `screenshots/browser-apache-host-port80.png`
- `screenshots/browser-nginx-bind-mount.png`
- `screenshots/task1-connectivity-01.png`
- `screenshots/task1-networks-containers-01.png`
- `screenshots/task2-host-network.png`
- `screenshots/task3-bind-mount.png`

## Checked source files

- [docker-compose.yml](../demo/docker-compose.yml)
- [docker-compose.yml](../bind-mount/docker-compose.yml)
- [docker-compose.yml](../host-network/docker-compose.yml)
