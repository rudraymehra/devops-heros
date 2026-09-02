# Java Hello World in Docker (multi-stage build)

A dependency-free Java HTTP server built with the JDK's own `com.sun.net.httpserver.HttpServer`.
It serves an HTML page with the text **Hello World from Java!** on port `8080`.

The Dockerfile is multi-stage: the first stage compiles `Main.java` with a full JDK, the second
stage copies only the compiled `Main.class` into a JRE image, so the compiler is never shipped.

## Files

| File | Purpose |
|------|---------|
| `Main.java` | HTTP server with `/` (HTML) and `/health` (JSON) handlers |
| `Dockerfile` | Stage 1 `eclipse-temurin:17-jdk` (compile), Stage 2 `eclipse-temurin:17-jre` (run) |

## Build the image

```bash
cd java-app
docker build -t hwdf-java .
```

### First attempt with the Alpine tags (failed)

I first tried `eclipse-temurin:17-jdk-alpine` / `17-jre-alpine`. Those tags are published for
`linux/amd64` only, so on an Apple Silicon Mac the build failed before pulling anything:

```text
ERROR: failed to build: failed to solve: eclipse-temurin:17-jdk-alpine: failed to resolve source metadata for docker.io/library/eclipse-temurin:17-jdk-alpine: no match for platform in manifest: not found
```

Switching to the multi-arch Ubuntu based tags `eclipse-temurin:17-jdk` and `eclipse-temurin:17-jre`
fixed it and also works on x86 Linux servers.

### Successful build (tail)

```text
#6 [build 1/4] FROM docker.io/library/eclipse-temurin:17-jdk@sha256:a27c79d44326d5f689668df5fedfee487652066d2a91e172747056cc7fbee6fc
#7 [stage-1 1/3] FROM docker.io/library/eclipse-temurin:17-jre@sha256:13cc28a6cc72a38ce1f00c906be3580c1a3e604b8984d694f369a96742abc93b
#7 DONE 31.6s
#8 [stage-1 2/3] WORKDIR /app
#8 DONE 0.2s
#6 DONE 51.3s
#9 [build 2/4] WORKDIR /app
#9 DONE 0.2s
#10 [build 3/4] COPY Main.java .
#10 DONE 0.0s
#11 [build 4/4] RUN javac Main.java
#11 DONE 1.9s
#12 [stage-1 3/3] COPY --from=build /app/Main.class .
#12 DONE 0.0s
#13 exporting to image
#13 writing image sha256:d7b0ef21dc5cba46d5ab831f5992a538723637fb27eb4373f997cbb4dce1c929 done
#13 naming to docker.io/library/hwdf-java done
#13 DONE 0.1s
```

## Run the container

Container port is `8080`; I published it on host port `8084` so it does not clash with anything
else on my machine.

```bash
docker run -d --name hwdf-java -p 8084:8080 hwdf-java
```

```text
dd9127cf91ef44f070b578708bd8fd8514f4c6d33dc38c42e241a014d3c6ddd4
```

## Verify

Open <http://localhost:8084> in the browser, or:

```bash
curl -s http://localhost:8084 | grep Hello
curl -s http://localhost:8084/health
docker logs hwdf-java
```

```text
    <h1>Hello World from Java!</h1>
{"status":"ok","app":"java-app"}
Java Hello World server listening on port 8080
```

## Clean up

```bash
docker rm -f hwdf-java
```

## What I understood

The multi-stage build keeps the final image at 318 MB even though the JDK stage is much larger;
only `Main.class` crosses the stage boundary via `COPY --from=build`. I also learned that a tag
existing on Docker Hub does not mean it exists for every CPU architecture; `docker build` checks the
manifest for the current platform and refuses if there is no match.
