# Session 07 — evidence and screenshots

Rudray Mehra | 24 BCS 10425 | Batch B

Reference: Vivek's supplied ZIP. Filenames below are an audit inventory, not imported images.
No reference screenshot has been relabelled. A command log is not a native screenshot.

Required entry point/core-file checks: all listed files present (not a runtime pass).
Reference images: 4. Tasks 1 and 3 have fresh successful Docker build and runtime captures.

## Fresh execution records

### [rudray-20261023-203855](rudray-20261023-203855/README.md)

- Task 1: PASS. The multi-stage image built, returned the expected Hello World response, and appeared in `docker ps` on port 8080 before cleanup.
- Task 3's Node.js, Python, and Java deployment checks are still pending; use the helper described below.
- [Build, HTTP response, and running container](rudray-20261023-203855/01-multistage-build-and-http.png)

### [rudray-20261023-204406](rudray-20261023-204406/README.md)

- Task 3: PASS. Node.js, Python, and Java images built, each app returned its expected HTTP response on a temporary localhost port, and the image sizes and running containers were shown.
- [Three app builds and Node response](rudray-20261023-204406/01-builds-and-node-output.png)
- [All app responses, container list, and image sizes](rudray-20261023-204406/02-all-apps-and-image-sizes.png)

### [rudray-20261023-093325](../../screenshots/rudray-20261023-093325/README.md)

- The pasted command did not run: the terminal stayed at `dquote>` waiting for a closing quote. This is recorded as an incomplete attempt, not a Docker pass.
- A helper script now contains the same build/run/check steps. Cancel the pending quote with Ctrl+C, change to `session6-7-docker`, then run `bash ./run-multistage-lab.sh`.
- The helper built the image and started the container on 2026-10-23, but the first immediate HTTP request was reset. The helper now retries readiness for up to 20 seconds and prints container logs if it still fails. See the [captured attempt](../../screenshots/rudray-20261023-093738/README.md).

### [rudray-20261016-212856-656600](rudray-20261016-212856-656600/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Capture the actual multi-stage image build, image metadata, running application and browser. App-type discussion is documentation, not runtime proof..

### [rudray-20261016-215104-093414](rudray-20261016-215104-093414/README.md)

- Docker live labs: NOT RUN: Add --docker-labs; never inferred from file presence.
- Reference-specific pending items: NOT RUN: Capture the actual multi-stage image build, image metadata, running application and browser. App-type discussion is documentation, not runtime proof..


## Rendered record images (not native screenshots)

[View generated images of our actual logs/recorded CI metadata](rendered-log-views/README.md).
These are explicitly labelled renderings. They do not change native-capture counts or turn failures into passes.


## Existing historical evidence

- [Earlier GitHub Actions run](https://github.com/rudraymehra/devops-heros/actions/runs/38372002674)

Historical timestamps, identities and resource names remain unchanged. These links do not imply a current live deployment.

## Historical capture context

The pending items below predate the successful 2026-10-23 Task 1 and Task 3 captures above.

## Reference image inventory (not copied)

- `screenshots/browser-multistage-8080.png`
- `screenshots/task1-multistage-build-run-01.png`
- `screenshots/task1-multistage-build-run-02.png`
- `screenshots/task3-three-app-types.png`

## Checked source files

- [Dockerfile](../Dockerfile)
