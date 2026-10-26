# Session 06 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 17. Fresh native captures: 6 accepted for the six-app Docker build and HTTP run.

## Fresh execution records

### [rudray-20261023-092927](rudray-20261023-092927/README.md)

- Six application images built successfully. All six localhost HTTP checks returned content, and `docker ps` showed all six containers before the cleanup trap removed them.
- [Build commands and Node build](rudray-20261023-092927/01-commands-and-node-build.png)
- [Java, Apache, and React build output](rudray-20261023-092927/02-java-apache-react-builds.png)
- [Apache and React build output](rudray-20261023-092927/03-apache-and-react-builds.png)
- [React and Nginx build output](rudray-20261023-092927/04-react-and-nginx-builds.png)
- [Six HTTP responses](rudray-20261023-092927/05-http-checks.png)
- [Running containers and cleanup confirmation](rudray-20261023-092927/06-all-containers-and-cleanup.png)

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Docker must be running. Capture six real image builds, HTTP responses, container state and corresponding browser pages..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Docker must be running. Capture six real image builds, HTTP responses, container state and corresponding browser pages..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [Earlier GitHub Actions run](https://github.com/rudraymehra/devops-heros/actions/runs/38372002674)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Historical capture context

The pending notes below predate the successful 2026-10-23 Docker build and HTTP run. The new captures show terminal HTTP responses; separate browser screenshots were not part of this run.

Use the [coursework capture guide](../../COURSEWORK-EVIDENCE.md). The helper displays Rudray Mehra around freshly executed commands.

## Reference image inventory (not copied)

- `screenshots/all-apps-running.png`
- `screenshots/apache-app-01.png`
- `screenshots/browser-apache-app.png`
- `screenshots/browser-java-app.png`
- `screenshots/browser-nginx-app.png`
- `screenshots/browser-nodejs-app.png`
- `screenshots/browser-python-app.png`
- `screenshots/browser-react-app.png`
- `screenshots/java-app-01.png`
- `screenshots/java-app-02.png`
- `screenshots/nginx-app-01.png`
- `screenshots/nodejs-app-01.png`
- `screenshots/nodejs-app-02.png`
- `screenshots/python-app-01.png`
- `screenshots/python-app-02.png`
- `screenshots/react-app-01.png`
- `screenshots/react-app-02.png`

## Checked source files

- [Dockerfile](../nodejs-app/Dockerfile)
- [Dockerfile](../python-app/Dockerfile)
- [Dockerfile](../java-app/Dockerfile)
- [Dockerfile](../Apache-app/Dockerfile)
- [Dockerfile](../React-app/Dockerfile)
- [Dockerfile](../nginx-app/Dockerfile)
