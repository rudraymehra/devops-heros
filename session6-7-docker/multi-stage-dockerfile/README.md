# Docker Multi-Stage Build Homework

## Screenshot evidence audit — 2026-10-23

See [this session's screenshot inventory and actual capture results](screenshots/README.md).
Fresh Task 1 build/run evidence was captured on 2026-10-23. Fresh Task 3 app-type verification is still pending.

## Student Details

| Field | Value |
|---|---|
| **Name** | Rudray Mehra |
| **Enrollment Number** | 24 BCS 10425 |
| **Batch** | B |
| **GitHub** | [rudraymehra](https://github.com/rudraymehra) |
| **Environment** | macOS 15.5 (Apple Silicon), Docker Desktop 28.3.2 |

---

## What is in this folder

| File | Purpose |
|---|---|
| `Dockerfile` | Two-stage build: `builder` installs dependencies, `production` copies only what is needed to run |
| `server.js` | Small Express server that prints **Hello World from Docker multi-stage build** on port 8080 (`PORT` env, default 8080) |
| `package.json` | App metadata and the single runtime dependency (`express`) |
| `.dockerignore` | Keeps `node_modules`, git metadata and markdown files out of the build context |
| `README.md` | This documentation (Task 2) |

### The multi-stage Dockerfile

```dockerfile
# Stage 1: Build
FROM node:24-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

# Stage 2: Production
FROM node:24-alpine AS production
ENV NODE_ENV=production \
    PORT=8080
WORKDIR /app
COPY --from=builder /app/package*.json ./
RUN npm install --omit=dev && npm cache clean --force
COPY --from=builder /app/server.js ./
RUN chown -R node:node /app
USER node
EXPOSE 8080
CMD ["node", "server.js"]
```

Key points I made sure of:

- Two named stages (`builder` and `production`). Only files explicitly copied with `COPY --from=builder` reach the final image.
- The final stage installs **production dependencies only** (`--omit=dev`) and clears the npm cache.
- The container runs as the unprivileged `node` user, not root.
- `EXPOSE 8080` documents the port and `PORT=8080` is the default inside `server.js`.

---

## Task 1: Run the Multi-Stage Dockerfile

### Step 1 - Clone the repository and move into the folder

```bash
git clone https://github.com/rudraymehra/devops-heros.git
cd devops-heros/session6-7-docker/multi-stage-dockerfile
```

### Step 2 - Build the image

```bash
docker build -t hwms-multistage-hello:1.0 .
```

Tail of the build output (both stages ran, dependencies installed twice - once in `builder`, once with `--omit=dev` in `production`):

```text
#10 [builder 5/5] COPY . .
#10 DONE 0.0s

#11 [production 3/6] COPY --from=builder /app/package*.json ./
#11 DONE 0.0s

#12 [production 4/6] RUN npm install --omit=dev && npm cache clean --force
#12 1.225 added 68 packages, and audited 69 packages in 1s
#12 1.226 found 0 vulnerabilities
#12 DONE 1.4s

#13 [production 5/6] COPY --from=builder /app/server.js ./
#13 DONE 0.0s

#14 [production 6/6] RUN chown -R node:node /app
#14 DONE 0.8s

#15 exporting to image
#15 exporting layers 0.1s done
#15 writing image sha256:fe3316d415398a3bb336d177e87a37b6c254cc2e7274b5273e0b0e7661ebd386 done
#15 naming to docker.io/library/hwms-multistage-hello:1.0 done
#15 DONE 0.1s
```

### Step 3 - Run a container on port 8080

```bash
docker run -d -p 8080:8080 --name hwms-hello-app hwms-multistage-hello:1.0
```

```text
dc8a187549490269058a50a23b9b14dbaf7a9cec594a0a760b51342272365ebe
```

### Step 4 - Access the application and verify the message

```bash
curl http://localhost:8080
```

```text
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Docker Multi-Stage Build</title>
  </head>
  <body>
    <h1>Hello World from Docker multi-stage build</h1>
    <p>Served by Express inside a container, listening on port 8080</p>
  </body>
</html>
```

The response headers confirm a `200 OK` from Express:

```bash
curl -i http://localhost:8080 | head -4
```

```text
HTTP/1.1 200 OK
X-Powered-By: Express
Content-Type: text/html; charset=utf-8
Content-Length: 279
```

I also added a small `/health` endpoint that reports the port the app is bound to:

```bash
curl http://localhost:8080/health
```

```text
{"status":"ok","port":8080}
```

Opening `http://localhost:8080` in the browser shows the same heading, **Hello World from Docker multi-stage build**.

### Step 5 - Verify the running container with `docker ps`

```bash
docker ps
```

```text
CONTAINER ID   IMAGE                       COMMAND                  CREATED         STATUS         PORTS                                         NAMES
dc8a18754949   hwms-multistage-hello:1.0   "docker-entrypoint.s…"   2 seconds ago   Up 2 seconds   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp   hwms-hello-app
```

`0.0.0.0:8080->8080/tcp` confirms host port 8080 is mapped to container port 8080, and the container status is `Up`.

### Step 6 - Extra checks (logs and non-root user)

```bash
docker logs hwms-hello-app
docker exec hwms-hello-app whoami
docker exec hwms-hello-app id
docker exec hwms-hello-app ls -la /app
```

```text
Server running on port 8080
node
uid=1000(node) gid=1000(node) groups=1000(node)
total 60
drwxr-xr-x    1 node     node          4096 Sep  3 14:23 .
drwxr-xr-x    1 root     root          4096 Sep  3 14:23 ..
drwxr-xr-x    1 node     node          4096 Sep  3 14:23 node_modules
-rw-r--r--    1 node     node         30932 Sep  3 14:23 package-lock.json
-rw-r--r--    1 node     node           178 Sep  3 14:18 package.json
-rw-r--r--    1 node     node           613 Sep  3 14:22 server.js
```

The final image contains only `server.js`, the package files and the production `node_modules` - nothing else from the build stage - and the process runs as `node` (uid 1000) instead of root.

**What I understood:** the build stage is a throwaway workspace. Whatever I do not `COPY --from` it is simply dropped, so the runtime image stays small and does not carry build-time tooling or dev dependencies.

---

## Task 2: Documentation

This `README.md` is the Task 2 deliverable. It contains:

- My name and enrollment number (Student Details section above).
- The output showing the application running successfully (`curl http://localhost:8080` in Task 1, Step 4).
- The `docker ps` output showing the container running on port 8080 (Task 1, Step 5).

---

## Task 3: Docker Application Deployment (3+ application types)

I containerised several different kinds of applications in this repository. Each folder has its own `Dockerfile` and source code. I built and ran the three core ones (Node.js, Python, Java) and checked their HTTP responses.

| # | Application type | Folder | Base image | Container port | Verification (real run) |
|---|---|---|---|---|---|
| 1 | Node.js (Express) | [`../nodejs-app`](../nodejs-app) | `node:18-alpine` | 3000 | `curl` returned `<h1>Hello World from Node.js!</h1>` |
| 2 | Python (Flask) | [`../python-app`](../python-app) | `python:3.11-slim` | 5000 | `curl` returned `<h1>Hello World from Python!</h1>` |
| 3 | Java (built-in HttpServer, multi-stage JDK -> JRE) | [`../java-app`](../java-app) | `eclipse-temurin:17-jdk` -> `eclipse-temurin:17-jre` | 8080 | `curl` returned `<h1>Hello World from Java!</h1>` |
| 4 | Apache HTTP Server (static site) | [`../Apache-app`](../Apache-app) | `httpd:2.4-alpine` | 80 | Custom `index.html` replaces the default page |
| 5 | React (Vite build, multi-stage Node -> Nginx) | [`../React-app`](../React-app) | `node:18-alpine` -> `nginx:alpine` | 80 | Built bundle served by Nginx |
| 6 | Nginx (static site) | [`../nginx-app`](../nginx-app) | `nginx:alpine` | 80 | Custom `index.html` served by Nginx |
| 7 | Node.js multi-stage (this folder) | [`.`](.) | `node:24-alpine` (2 stages) | 8080 | Task 1 above |

### Commands I used to verify Node.js, Python and Java

I published each app on a random localhost port so nothing collided with the multi-stage app on 8080.

```bash
cd devops-heros/session6-7-docker

docker build -t hwms-verify-node   ./nodejs-app
docker build -t hwms-verify-python ./python-app
docker build -t hwms-verify-java   ./java-app

docker run -d --name hwms-verify-node   -p 127.0.0.1::3000 hwms-verify-node
docker run -d --name hwms-verify-python -p 127.0.0.1::5000 hwms-verify-python
docker run -d --name hwms-verify-java   -p 127.0.0.1::8080 hwms-verify-java

docker ps --filter name=hwms- --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

```text
NAMES                IMAGE                       STATUS         PORTS
hwms-verify-java     hwms-verify-java            Up 7 seconds   127.0.0.1:55184->8080/tcp
hwms-verify-python   hwms-verify-python          Up 7 seconds   127.0.0.1:55182->5000/tcp
hwms-verify-node     hwms-verify-node            Up 9 seconds   127.0.0.1:55180->3000/tcp
hwms-hello-app       hwms-multistage-hello:1.0   Up 3 minutes   0.0.0.0:8080->8080/tcp, [::]:8080->8080/tcp
```

```bash
curl -s http://127.0.0.1:55180 | grep -E '<h1>|<p>'
curl -s http://127.0.0.1:55182 | grep -E '<h1>|<p>'
curl -s http://127.0.0.1:55184 | grep -E '<h1>|<p>'
```

```text
    <h1>Hello World from Node.js!</h1>
    <p>Served by Express inside a Docker container on port 3000</p>
    <h1>Hello World from Python!</h1>
    <p>Served by Flask inside a Docker container on port 5000</p>
    <h1>Hello World from Java!</h1>
    <p>Served by com.sun.net.httpserver inside a Docker container on port 8080</p>
```

Image sizes of the three apps:

```bash
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.Size}}' | grep hwms-verify
```

```text
REPOSITORY                 TAG            SIZE
hwms-verify-java           latest         318MB
hwms-verify-python         latest         174MB
hwms-verify-node           latest         134MB
```

**What I understood:** the Docker workflow is identical regardless of language - pick a base image, copy the code, install dependencies, `EXPOSE` the port, set a `CMD`. The only thing that changes is the runtime inside the image. Java and React are natural fits for multi-stage builds because the compiler/bundler is not needed at runtime.

---

## Multi-Stage Builds Explained

### What is a multi-stage build?

A multi-stage build is a single `Dockerfile` with more than one `FROM` instruction. Each `FROM` starts a new stage with its own filesystem. Later stages can pull files from earlier stages with `COPY --from=<stage>`. Only the **last** stage becomes the final image; everything else is discarded once the build finishes.

In this homework:

1. **`builder` stage** - installs all npm dependencies and copies the whole source tree. This is where compilation, testing or bundling would happen in a bigger project.
2. **`production` stage** - starts from a clean `node:24-alpine`, copies only `package*.json` and `server.js`, installs production dependencies, drops to a non-root user and runs `node server.js`.

### Why use it?

| Benefit | How it shows up here |
|---|---|
| **Smaller images** | No devDependencies, no build caches, no source files other than `server.js` in the final image. Compared with a single-stage build on the full `node:24` image the difference is ~1 GB (see below). |
| **Security / smaller attack surface** | Build tooling (compilers, dev packages, extra shells) never reaches production. Fewer packages means fewer CVEs to patch. The final stage also runs as `node`, not root. |
| **Better layer caching** | `package*.json` is copied before the source, so the `npm install` layer is reused as long as dependencies do not change. Editing `server.js` only re-runs the cheap `COPY` layers. |
| **One Dockerfile, no host tooling** | Build and runtime are both described in the same file; a CI runner only needs Docker, not Node or npm installed. |

### Real image size comparison

To make the point measurable I built three images from the same `server.js`:

- `hwms-multistage-hello:1.0` - the real two-stage image submitted here.
- `hwms-multistage-hello:builder-only` - the `builder` stage on its own (`docker build --target builder`).
- `hwms-single-stage-debian:1.0` - the same app in a single stage on the full `node:24` (Debian) image, which is what a naive Dockerfile often looks like.

```bash
docker pull node:24-alpine
docker build --target builder -t hwms-multistage-hello:builder-only .
docker build -f /tmp/hwms-single.Dockerfile -t hwms-single-stage-debian:1.0 .   # FROM node:24 (Debian), single stage
docker images --format 'table {{.Repository}}\t{{.Tag}}\t{{.ID}}\t{{.Size}}' | grep -E 'REPOSITORY|hwms-|^node '
```

```text
REPOSITORY                 TAG            IMAGE ID       SIZE
hwms-single-stage-debian   1.0            51287a2393e0   1.14GB
hwms-multistage-hello      1.0            fe3316d41539   169MB
hwms-multistage-hello      builder-only   e9f2dcb22d3f   172MB
node                       24-alpine      722cc1507731   163MB
```

| Image | Size | Notes |
|---|---|---|
| `node:24-alpine` (base) | 163 MB | Starting point for both stages |
| `hwms-multistage-hello:1.0` (final) | **169 MB** | Only ~6 MB on top of the base: production `node_modules` + `server.js` |
| `hwms-multistage-hello:builder-only` | 172 MB | Full install + entire build context |
| `hwms-single-stage-debian:1.0` | 1.14 GB | Same app, single stage, on full `node:24` - almost 7x larger |

The layer history of the final image confirms that the application itself adds very little:

```bash
docker history hwms-multistage-hello:1.0 --format 'table {{.CreatedBy}}\t{{.Size}}' | head -9
```

```text
CREATED BY                                      SIZE
CMD ["node" "server.js"]                        0B
EXPOSE map[8080/tcp:{}]                         0B
USER node                                       0B
RUN /bin/sh -c chown -R node:node /app # bui…   2.28MB
COPY /app/server.js ./ # buildkit               613B
RUN /bin/sh -c npm install --omit=dev && npm…   3.7MB
COPY /app/package*.json ./ # buildkit           31.1kB
WORKDIR /app                                    0B
```

**What I understood:** with a tiny Express app most of the size is the Node runtime itself, so the builder-vs-final difference is small (172 MB vs 169 MB). The savings become large when the build stage needs heavy tooling (Debian toolchains, a JDK, a frontend bundler) - which is exactly the case for the Java and React apps in Task 3, and why picking a slim base image for the final stage matters as much as splitting the stages.

---

## Cleanup

```bash
docker rm -f hwms-hello-app hwms-verify-node hwms-verify-python hwms-verify-java
docker ps -a --filter name=hwms-
```

```text
hwms-hello-app
hwms-verify-node
hwms-verify-python
hwms-verify-java
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

All containers created for this homework were removed; only the images remain locally.
