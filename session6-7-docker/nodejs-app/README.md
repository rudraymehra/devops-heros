# Node.js Hello World (Express) in Docker

A minimal Express server that returns an HTML page with the text **Hello World from Node.js!**
It runs on port `3000` inside the container and is packaged with a `node:18-alpine` image.

## Files

| File | Purpose |
|------|---------|
| `package.json` | Declares the `express` dependency and the `start` script |
| `server.js` | Express server, listens on `0.0.0.0:3000`, serves `/` and `/health` |
| `Dockerfile` | Installs dependencies and runs the server |
| `.dockerignore` | Keeps a local `node_modules` folder out of the build context |

## Build the image

```bash
cd nodejs-app
docker build -t hwdf-nodejs .
```

Real output (tail):

```text
#5 [1/5] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc4b8ca09d9e
#5 DONE 7.3s
#6 [2/5] WORKDIR /app
#6 DONE 0.3s
#7 [3/5] COPY package*.json ./
#7 DONE 0.0s
#8 [4/5] RUN npm install --omit=dev
#8 DONE 2.0s
#9 [5/5] COPY server.js .
#9 DONE 0.0s
#10 exporting to image
#10 writing image sha256:f7187c1c9ae828098198e7fe5de20d5d2215ba44f357e4aedcd594f69baac528 done
#10 naming to docker.io/library/hwdf-nodejs done
#10 DONE 0.1s
```

## Run the container

```bash
docker run -d --name hwdf-nodejs -p 3000:3000 hwdf-nodejs
```

```text
223eaeeb37a2914d02ff0d6c0d0fb5713410044fa03fb330f3397da46d85d709
```

## Verify

Open <http://localhost:3000> in the browser, or:

```bash
curl -s http://localhost:3000 | grep Hello
curl -s http://localhost:3000/health
docker logs hwdf-nodejs
```

```text
    <h1>Hello World from Node.js!</h1>
{"status":"ok","app":"nodejs-app"}
Node.js Hello World app listening on port 3000
```

## Clean up

```bash
docker rm -f hwdf-nodejs
```

## What I understood

Copying `package.json` and running `npm install` before copying `server.js` means the dependency
layer is cached: editing the server code only rebuilds the last, tiny layer. Binding to `0.0.0.0`
instead of `localhost` is required, otherwise the process inside the container is not reachable
through the published port.
