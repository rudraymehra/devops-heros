# Python Hello World (Flask) in Docker

A small Flask application that returns an HTML page with the text **Hello World from Python!**
It listens on port `5000` inside the container and is built on `python:3.11-slim`.

## Files

| File | Purpose |
|------|---------|
| `app.py` | Flask app, routes `/` (HTML page) and `/health` (JSON) |
| `requirements.txt` | Pinned dependency: `flask==3.0.3` |
| `Dockerfile` | Installs requirements and starts the app |

## Build the image

```bash
cd python-app
docker build -t hwdf-python .
```

Real output (tail):

```text
#6 [1/5] FROM docker.io/library/python:3.11-slim@sha256:9534e5a8e315485d4061ed659af0fd78a284c015f9b73661b41d6bab25604534
#6 DONE 11.8s
#7 [2/5] WORKDIR /app
#7 DONE 0.3s
#8 [3/5] COPY requirements.txt .
#8 DONE 0.1s
#9 [4/5] RUN pip install --no-cache-dir -r requirements.txt
#9 DONE 16.2s
#10 [5/5] COPY app.py .
#10 DONE 0.1s
#11 exporting to image
#11 writing image sha256:dc00a09e15b075b97b80bd508550c588234e6772f05ffb7e6ac046daa20d795d done
#11 naming to docker.io/library/hwdf-python done
#11 DONE 0.1s
```

## Run the container

The usual command is `-p 5000:5000`. On my Mac, port 5000 is already taken by the macOS AirPlay
Receiver (`ControlCenter`), so the first attempt failed with a real error:

```bash
docker run -d --name hwdf-python -p 5000:5000 hwdf-python
```

```text
docker: Error response from daemon: ports are not available: exposing port TCP 0.0.0.0:5000 -> 127.0.0.1:0: listen tcp 0.0.0.0:5000: bind: address already in use
```

```bash
lsof -nP -iTCP:5000 -sTCP:LISTEN
```

```text
COMMAND   PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
ControlCe 536 rudraym  10u  IPv4  0x5d9f9fad343108e      0t0  TCP *:5000 (LISTEN)
```

The fix is simply to publish on a different host port. The container port stays `5000`.

```bash
docker rm -f hwdf-python
docker run -d --name hwdf-python -p 5001:5000 hwdf-python
```

```text
5010471a4eecb10d0529a1de3942b852de1aa68b974409dcd4077384e1c37325
```

On a Linux server where 5000 is free, `-p 5000:5000` works as-is.

## Verify

Open <http://localhost:5001> in the browser, or:

```bash
curl -s http://localhost:5001 | grep Hello
curl -s http://localhost:5001/health
docker logs hwdf-python | tail -2
```

```text
    <h1>Hello World from Python!</h1>
{"app":"python-app","status":"ok"}
192.168.65.1 - - [03/Sep/2026 14:27:20] "GET / HTTP/1.1" 200 -
192.168.65.1 - - [03/Sep/2026 14:27:20] "GET /health HTTP/1.1" 200 -
```

## Clean up

```bash
docker rm -f hwdf-python
```

## What I understood

`-p HOST:CONTAINER` are two independent numbers. The app always listens on 5000 inside its own
network namespace; only the host side had to change. `--no-cache-dir` keeps pip's download cache
out of the image layer, and `python:3.11-slim` is a good middle ground between the huge full image
and Alpine (which often needs compilers for Python wheels).
