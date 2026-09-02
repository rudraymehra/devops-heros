# Nginx Hello World in Docker

A static HTML page with the text **Hello World from Nginx!** served by Nginx.
The Dockerfile copies `index.html` over the default welcome page in the official `nginx:alpine`
image. The base image already starts Nginx in the foreground (`nginx -g "daemon off;"`).

## Files

| File | Purpose |
|------|---------|
| `index.html` | The Hello World page |
| `Dockerfile` | Copies the page to `/usr/share/nginx/html/` |

## Build the image

```bash
cd nginx-app
docker build -t hwdf-nginx .
```

Real output (tail):

```text
#4 [1/2] FROM docker.io/library/nginx:alpine
#4 CACHED
#6 [2/2] COPY index.html /usr/share/nginx/html/index.html
#6 DONE 0.0s
#7 exporting to image
#7 writing image sha256:e8657ffd8b0ce30307c3c65a6402421c40a50b068d911f0c6c5f35c9cf6ad907 done
#7 naming to docker.io/library/hwdf-nginx done
#7 DONE 0.0s
```

The base layer shows `CACHED` because `nginx:alpine` had just been pulled for the React app.

## Run the container

Nginx listens on port `80` inside the container; I publish it on host port `8083`.

```bash
docker run -d --name hwdf-nginx -p 8083:80 hwdf-nginx
```

```text
c7d0135bbcc3a8b4755f36043e023abbfc431d56ecb278ea9603809c7d29b041
```

## Verify

Open <http://localhost:8083> in the browser, or:

```bash
curl -s http://localhost:8083 | grep Hello
docker logs hwdf-nginx | tail -2
```

```text
    <h1>Hello World from Nginx!</h1>
2026/09/03 14:26:43 [notice] 1#1: start worker process 37
192.168.65.1 - - [03/Sep/2026:14:26:47 +0000] "GET / HTTP/1.1" 200 705 "-" "curl/8.7.1" "-"
```

## Clean up

```bash
docker rm -f hwdf-nginx
```

## What I understood

Because the base image already has a sensible `CMD`, the whole Dockerfile is `FROM` + `COPY` +
`EXPOSE`. `EXPOSE 80` is documentation only; the port only becomes reachable from the host because
of `-p 8083:80` at run time. The request in the log comes from `192.168.65.1`, which is the Docker
Desktop gateway, not my real host IP, showing that the container sits on its own bridge network.
