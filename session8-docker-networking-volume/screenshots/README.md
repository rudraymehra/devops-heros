# Session 08 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 6. Native captures: 0 accepted; 0 awaiting review; 0 rejected.

## Fresh execution records

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

Capture Compose networks/connectivity. Bind-mount edit/reload and host-network behaviour need their own live run; Docker Desktop host networking may need explicit support.

Use the [coursework capture guide](../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

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
