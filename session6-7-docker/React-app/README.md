# React Hello World in Docker (Vite + multi-stage build)

A React 18 single page app created with Vite that renders **Hello World from React!**
The image is built in two stages: `node:18-alpine` installs dependencies and runs `vite build`,
then the static `dist/` output is copied into `nginx:alpine`. The final image contains no Node.js.

## Files

| File | Purpose |
|------|---------|
| `package.json` | React 18, Vite 5 and the React plugin; `build` script |
| `vite.config.js` | Enables the React plugin |
| `index.html` | Vite entry HTML with the `#root` div |
| `src/main.jsx` | Mounts `<App />` into `#root` |
| `src/App.jsx` | The Hello World component |
| `Dockerfile` | Two-stage build (Node build, Nginx serve) |
| `.dockerignore` | Excludes `node_modules` and `dist` from the build context |

## Build the image

```bash
cd React-app
docker build -t hwdf-react .
```

Real output (tail):

```text
#6 [build 1/6] FROM docker.io/library/node:18-alpine@sha256:8d6421d663b4c28fd3ebc498332f249011d118945588d0a35cb9bc4b8ca09d9e
#8 [build 2/6] WORKDIR /app
#8 CACHED
#9 [stage-1 1/2] FROM docker.io/library/nginx:alpine@sha256:a9ae6f6d078d477e21323310498e5196cb2b7c0aedd9e07b7306612077227d7c
#10 [build 3/6] COPY package*.json ./
#10 DONE 0.2s
#9 DONE 9.6s
#11 [build 4/6] RUN npm install
#11 DONE 19.3s
#12 [build 5/6] COPY . .
#12 DONE 1.7s
#13 [build 6/6] RUN npm run build
#13 DONE 3.1s
#14 [stage-1 2/2] COPY --from=build /app/dist /usr/share/nginx/html
#14 DONE 0.1s
#15 exporting to image
#15 writing image sha256:cd87374ba90f1ce9bd4efe2927920bf73db0296d40f77f2b1f842683157b22bd done
#15 naming to docker.io/library/hwdf-react done
#15 DONE 0.1s
```

Note that `node:18-alpine` shows `DONE 0.0s` because it was already pulled for the Node.js app;
Docker reuses base image layers across projects.

## Run the container

```bash
docker run -d --name hwdf-react -p 8082:80 hwdf-react
```

```text
2e80afe1f4488c79e2c3af475e12ad42f85bcac789ca73757b3abaa82e42bc20
```

## Verify

Open <http://localhost:8082> in the browser. The heading "Hello World from React!" is rendered by
React at runtime, so with `curl` the raw `index.html` only contains the empty `#root` div and the
script tag. The text lives inside the built JavaScript bundle:

```bash
curl -s http://localhost:8082
curl -s http://localhost:8082/assets/index-DNIeimAC.js | grep -o 'Hello World from React!'
```

```text
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

(The hashed bundle file name changes on every build; read it from the `<script>` tag.)

```bash
docker logs hwdf-react | tail -2
```

```text
192.168.65.1 - - [03/Sep/2026:14:26:47 +0000] "GET / HTTP/1.1" 200 328 "-" "curl/8.7.1" "-"
192.168.65.1 - - [03/Sep/2026:14:26:47 +0000] "GET /assets/index-DNIeimAC.js HTTP/1.1" 200 143219 "-" "curl/8.7.1" "-"
```

## Clean up

```bash
docker rm -f hwdf-react
```

## What I understood

The build stage needs Node, npm and hundreds of MB of `node_modules`, but the runtime only needs a
few static files. Multi-stage builds let me use both without shipping the toolchain: the final
image is 68.4 MB, essentially the same size as the plain Nginx image. The `.dockerignore` matters
because `COPY . .` would otherwise upload a local `node_modules` folder into the build context.
