# Docker Fundamentals Homework - Hello World Applications

**Author:** Rudray Mehra
**Environment:** macOS 15.5 (Apple Silicon), Docker Desktop 28.3.2

This session's task was to containerise six "Hello World" web applications, one per technology,
each in its own folder with the application code and a `Dockerfile`, then build the image, run a
container and confirm that the Hello World page is served. Everything below was actually built and
run on my machine; the outputs are copied from my terminal.

## Overview

| Folder | Technology | Base image(s) | Container port | Host port | URL |
|--------|------------|---------------|----------------|-----------|-----|
| [`nodejs-app/`](nodejs-app/) | Node.js 18 + Express | `node:18-alpine` | 3000 | 3000 | <http://localhost:3000> |
| [`python-app/`](python-app/) | Python 3.11 + Flask | `python:3.11-slim` | 5000 | 5001 (see note) | <http://localhost:5001> |
| [`java-app/`](java-app/) | Java 17 `HttpServer` | `eclipse-temurin:17-jdk` -> `eclipse-temurin:17-jre` (multi-stage) | 8080 | 8084 | <http://localhost:8084> |
| [`Apache-app/`](Apache-app/) | Apache httpd 2.4 | `httpd:2.4-alpine` | 80 | 8081 | <http://localhost:8081> |
| [`React-app/`](React-app/) | React 18 + Vite 5 | `node:18-alpine` -> `nginx:alpine` (multi-stage) | 80 | 8082 | <http://localhost:8082> |
| [`nginx-app/`](nginx-app/) | Nginx | `nginx:alpine` | 80 | 8083 | <http://localhost:8083> |

Every image and container is prefixed `hwdf-` (hello world docker fundamentals) so they are easy to
find and remove together. Each folder has its own `README.md` with more detail.

Final image sizes:

```text
REPOSITORY    TAG       SIZE
hwdf-java     latest    318MB
hwdf-nginx    latest    68.3MB
hwdf-react    latest    68.4MB
hwdf-apache   latest    75.9MB
hwdf-python   latest    174MB
hwdf-nodejs   latest    134MB
```

---

## 1. Node.js application (`nodejs-app/`)

An Express server that returns an HTML page. `package.json` is copied and `npm install` is run
before the source is copied so the dependency layer stays cached.

```bash
cd nodejs-app
docker build -t hwdf-nodejs .
```

```text
#5 [1/5] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc4b8ca09d9e
#5 DONE 7.3s
#6 [2/5] WORKDIR /app
#7 [3/5] COPY package*.json ./
#8 [4/5] RUN npm install --omit=dev
#8 DONE 2.0s
#9 [5/5] COPY server.js .
#10 exporting to image
#10 writing image sha256:f7187c1c9ae828098198e7fe5de20d5d2215ba44f357e4aedcd594f69baac528 done
#10 naming to docker.io/library/hwdf-nodejs done
```

```bash
docker run -d --name hwdf-nodejs -p 3000:3000 hwdf-nodejs
curl -s http://localhost:3000 | grep Hello
```

```text
223eaeeb37a2914d02ff0d6c0d0fb5713410044fa03fb330f3397da46d85d709
    <h1>Hello World from Node.js!</h1>
```

## 2. Python application (`python-app/`)

A Flask app listening on `0.0.0.0:5000`. `requirements.txt` is installed in its own layer.

```bash
cd python-app
docker build -t hwdf-python .
```

```text
#6 [1/5] FROM docker.io/library/python:3.11-slim@sha256:9534e5a8e315485d4061ed659af0fd78a284c015f9b73661b41d6bab25604534
#6 DONE 11.8s
#7 [2/5] WORKDIR /app
#8 [3/5] COPY requirements.txt .
#9 [4/5] RUN pip install --no-cache-dir -r requirements.txt
#9 DONE 16.2s
#10 [5/5] COPY app.py .
#11 exporting to image
#11 writing image sha256:dc00a09e15b075b97b80bd508550c588234e6772f05ffb7e6ac046daa20d795d done
#11 naming to docker.io/library/hwdf-python done
```

**Port note.** `-p 5000:5000` failed on my Mac because macOS AirPlay Receiver (`ControlCenter`)
already listens on 5000:

```bash
docker run -d --name hwdf-python -p 5000:5000 hwdf-python
```

```text
docker: Error response from daemon: ports are not available: exposing port TCP 0.0.0.0:5000 -> 127.0.0.1:0: listen tcp 0.0.0.0:5000: bind: address already in use
```

So I published the same container port on host port 5001 instead. On a Linux server `5000:5000`
works directly.

```bash
docker rm -f hwdf-python
docker run -d --name hwdf-python -p 5001:5000 hwdf-python
curl -s http://localhost:5001 | grep Hello
```

```text
5010471a4eecb10d0529a1de3942b852de1aa68b974409dcd4077384e1c37325
    <h1>Hello World from Python!</h1>
```

## 3. Java application (`java-app/`)

A plain JDK HTTP server (`com.sun.net.httpserver`) with no framework. Multi-stage Dockerfile:
compile with the JDK, run with only the JRE.

```bash
cd java-app
docker build -t hwdf-java .
```

My first attempt used `eclipse-temurin:17-jdk-alpine`, which only exists for `linux/amd64`:

```text
ERROR: failed to build: failed to solve: eclipse-temurin:17-jdk-alpine: failed to resolve source metadata for docker.io/library/eclipse-temurin:17-jdk-alpine: no match for platform in manifest: not found
```

After switching to the multi-arch `eclipse-temurin:17-jdk` / `17-jre` tags:

```text
#6 [build 1/4] FROM docker.io/library/eclipse-temurin:17-jdk@sha256:a27c79d44326d5f689668df5fedfee487652066d2a91e172747056cc7fbee6fc
#7 [stage-1 1/3] FROM docker.io/library/eclipse-temurin:17-jre@sha256:13cc28a6cc72a38ce1f00c906be3580c1a3e604b8984d694f369a96742abc93b
#7 DONE 31.6s
#6 DONE 51.3s
#10 [build 3/4] COPY Main.java .
#11 [build 4/4] RUN javac Main.java
#11 DONE 1.9s
#12 [stage-1 3/3] COPY --from=build /app/Main.class .
#13 exporting to image
#13 writing image sha256:d7b0ef21dc5cba46d5ab831f5992a538723637fb27eb4373f997cbb4dce1c929 done
#13 naming to docker.io/library/hwdf-java done
```

```bash
docker run -d --name hwdf-java -p 8084:8080 hwdf-java
curl -s http://localhost:8084 | grep Hello
```

```text
dd9127cf91ef44f070b578708bd8fd8514f4c6d33dc38c42e241a014d3c6ddd4
    <h1>Hello World from Java!</h1>
```

## 4. Apache web server (`Apache-app/`)

Static `index.html` copied into the `httpd:2.4-alpine` document root
(`/usr/local/apache2/htdocs`). The base image's `CMD` already runs `httpd-foreground`.

```bash
cd Apache-app
docker build -t hwdf-apache .
```

```text
#6 [1/2] FROM docker.io/library/httpd:2.4-alpine@sha256:1b766f17b84026429b7cb243317b142921b24432336e798bc881c43f45ed9567
#6 DONE 8.9s
#7 [2/2] COPY index.html /usr/local/apache2/htdocs/index.html
#8 exporting to image
#8 writing image sha256:acfcd7f72638a18a744de95287efe82e776846ba3691fd774ab83b45ebd7c262 done
#8 naming to docker.io/library/hwdf-apache done
```

```bash
docker run -d --name hwdf-apache -p 8081:80 hwdf-apache
curl -s http://localhost:8081 | grep Hello
```

```text
cb7d4697c1d93fc698b63eb53bc0ca165f3e42fbf77908e9b604d2a1e8ba5c97
    <h1>Hello World from Apache!</h1>
```

## 5. React application (`React-app/`)

Vite + React 18. Stage 1 (`node:18-alpine`) runs `npm install` and `npm run build`; stage 2
(`nginx:alpine`) serves the `dist/` folder. Node.js is not present in the final image.

```bash
cd React-app
docker build -t hwdf-react .
```

```text
#6 [build 1/6] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc4b8ca09d9e
#9 [stage-1 1/2] FROM docker.io/library/nginx:alpine@sha256:a9ae6f6d078d477e21323310498e5196cb2b7c0aedd9e07b7306612077227d7c
#9 DONE 9.6s
#11 [build 4/6] RUN npm install
#11 DONE 19.3s
#12 [build 5/6] COPY . .
#13 [build 6/6] RUN npm run build
#13 DONE 3.1s
#14 [stage-1 2/2] COPY --from=build /app/dist /usr/share/nginx/html
#15 exporting to image
#15 writing image sha256:cd87374ba90f1ce9bd4efe2927920bf73db0296d40f77f2b1f842683157b22bd done
#15 naming to docker.io/library/hwdf-react done
```

```bash
docker run -d --name hwdf-react -p 8082:80 hwdf-react
curl -s http://localhost:8082
curl -s http://localhost:8082/assets/index-DNIeimAC.js | grep -o 'Hello World from React!'
```

React renders the heading in the browser, so `curl` on `/` returns only the shell HTML; the text is
inside the built bundle referenced by the script tag:

```text
2e80afe1f4488c79e2c3af475e12ad42f85bcac789ca73757b3abaa82e42bc20
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>React Hello World</title>
    <script type="module" crossorigin src="/assets/index-DNIeimAC.js"></script>
  </head>
  <body>
    <div id="root"></div>
  </body>
</html>
Hello World from React!
```

Opening <http://localhost:8082> in the browser shows the "Hello World from React!" card.

## 6. Nginx application (`nginx-app/`)

Static `index.html` copied into `/usr/share/nginx/html` of `nginx:alpine`.

```bash
cd nginx-app
docker build -t hwdf-nginx .
```

```text
#4 [1/2] FROM docker.io/library/nginx:alpine
#4 CACHED
#6 [2/2] COPY index.html /usr/share/nginx/html/index.html
#7 exporting to image
#7 writing image sha256:e8657ffd8b0ce30307c3c65a6402421c40a50b068d911f0c6c5f35c9cf6ad907 done
#7 naming to docker.io/library/hwdf-nginx done
```

`nginx:alpine` shows `CACHED` because the React build had just pulled it.

```bash
docker run -d --name hwdf-nginx -p 8083:80 hwdf-nginx
curl -s http://localhost:8083 | grep Hello
```

```text
c7d0135bbcc3a8b4755f36043e023abbfc431d56ecb278ea9603809c7d29b041
    <h1>Hello World from Nginx!</h1>
```

---

## All six containers running at once

```bash
docker ps --filter name=hwdf- --format "table {{.ID}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}\t{{.Names}}"
```

```text
CONTAINER ID   IMAGE         STATUS          PORTS                                         NAMES
5010471a4eec   hwdf-python   Up 3 seconds    0.0.0.0:5001->5000/tcp, [::]:5001->5000/tcp   hwdf-python
c7d0135bbcc3   hwdf-nginx    Up 38 seconds   0.0.0.0:8083->80/tcp, [::]:8083->80/tcp       hwdf-nginx
2e80afe1f448   hwdf-react    Up 39 seconds   0.0.0.0:8082->80/tcp, [::]:8082->80/tcp       hwdf-react
cb7d4697c1d9   hwdf-apache   Up 40 seconds   0.0.0.0:8081->80/tcp, [::]:8081->80/tcp       hwdf-apache
dd9127cf91ef   hwdf-java     Up 40 seconds   0.0.0.0:8084->8080/tcp, [::]:8084->8080/tcp   hwdf-java
223eaeeb37a2   hwdf-nodejs   Up 41 seconds   0.0.0.0:3000->3000/tcp, [::]:3000->3000/tcp   hwdf-nodejs
```

Quick check of every endpoint in one go:

```bash
for p in 3000 5001 8084 8081 8082 8083; do
  echo "== $p"; curl -s -o /dev/null -w "HTTP %{http_code}\n" http://localhost:$p
done
```

```text
== 3000
HTTP 200
== 5001
HTTP 200
== 8084
HTTP 200
== 8081
HTTP 200
== 8082
HTTP 200
== 8083
HTTP 200
```

## Cleanup

```bash
docker rm -f hwdf-nodejs hwdf-python hwdf-java hwdf-apache hwdf-react hwdf-nginx
docker ps -a --filter name=hwdf-
```

```text
hwdf-nodejs
hwdf-python
hwdf-java
hwdf-apache
hwdf-react
hwdf-nginx
CONTAINER ID   NAMES     STATUS
```

To also delete the images:

```bash
docker rmi hwdf-nodejs hwdf-python hwdf-java hwdf-apache hwdf-react hwdf-nginx
```

---

## What I understood

**Images vs containers.** An image is the read-only, layered template produced by `docker build`;
a container is a running (or stopped) instance of it with its own writable layer, process tree and
network namespace. I built six images and could have started many containers from each; deleting
the containers with `docker rm -f` left the images untouched.

**EXPOSE vs `-p`.** `EXPOSE` in a Dockerfile is documentation for whoever runs the image; it does
not open anything. Only `-p HOST:CONTAINER` at run time publishes the port on the host. The Python
app made this very concrete: the container always listened on 5000, and when host port 5000 was
busy I just changed the host side to 5001.

**Layers and caching.** Each Dockerfile instruction creates a layer, and Docker reuses layers whose
inputs have not changed. That is why `package.json` / `requirements.txt` are copied and installed
before the application code, and why `nginx:alpine` and `node:18-alpine` showed as `CACHED` or
`DONE 0.0s` for the second project that used them.

**Multi-stage builds.** The Java and React Dockerfiles use a heavy build stage (JDK, Node + npm)
and a light runtime stage (JRE, Nginx), copying only the artefacts across with `COPY --from`. The
React image ended up at 68.4 MB, practically identical to plain Nginx, even though building it
needed a full Node toolchain.

**Platforms.** A tag on Docker Hub is a manifest list; if it has no entry for the current CPU
architecture the build fails with `no match for platform in manifest`. I hit this with the Temurin
Alpine tags on Apple Silicon and fixed it by picking multi-arch tags.
