# Apache HTTP Server Hello World in Docker

A static HTML page with the text **Hello World from Apache!** served by Apache httpd 2.4.
The Dockerfile only copies `index.html` over the default page in the official `httpd:2.4-alpine`
image; the base image already starts httpd in the foreground.

## Files

| File | Purpose |
|------|---------|
| `index.html` | The Hello World page |
| `Dockerfile` | Copies the page to `/usr/local/apache2/htdocs/` |

## Build the image

```bash
cd Apache-app
docker build -t hwdf-apache .
```

Real output (tail):

```text
#6 [1/2] FROM docker.io/library/httpd:2.4-alpine@sha256:1b766f17b84026429b7cb243317b142921b24432336e798bc881c43f45ed9567
#6 DONE 8.9s
#7 [2/2] COPY index.html /usr/local/apache2/htdocs/index.html
#7 DONE 1.3s
#8 exporting to image
#8 writing image sha256:acfcd7f72638a18a744de95287efe82e776846ba3691fd774ab83b45ebd7c262 done
#8 naming to docker.io/library/hwdf-apache done
#8 DONE 0.0s
```

## Run the container

Apache listens on port `80` inside the container; I publish it on host port `8081`.

```bash
docker run -d --name hwdf-apache -p 8081:80 hwdf-apache
```

```text
cb7d4697c1d93fc698b63eb53bc0ca165f3e42fbf77908e9b604d2a1e8ba5c97
```

## Verify

Open <http://localhost:8081> in the browser, or:

```bash
curl -s http://localhost:8081 | grep Hello
docker logs hwdf-apache | tail -2
```

```text
    <h1>Hello World from Apache!</h1>
[Thu Sep 03 14:26:40.932856 2026] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
192.168.65.1 - - [03/Sep/2026:14:26:47 +0000] "GET / HTTP/1.1" 200 718
```

## Clean up

```bash
docker rm -f hwdf-apache
```

## What I understood

The official image runs `httpd -D FOREGROUND` as PID 1, which is what keeps the container alive.
The document root in this image is `/usr/local/apache2/htdocs` (different from `/var/www/html` on a
Debian package install), so that is where the page has to be copied.
