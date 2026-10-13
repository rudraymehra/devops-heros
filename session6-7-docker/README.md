# Docker Homework Submission

**Student:** Sudhir Mehra | **Roll number:** 24 BCS 10425 | **Batch:** B

This directory contains six independent Hello World applications and a separate
multi-stage-build exercise.

| Application | Build context | Container port | Example host port |
|---|---|---:|---:|
| Node.js | `node-app` | 3000 | 3000 |
| Python | `python-app` | 8000 | 8000 |
| Java | `java-app` | 8080 | 8081 |
| Apache | `Apache-app` | 80 | 8082 |
| React | `React-app` | 80 | 8083 |
| Nginx | `nginx-web` | 80 | 8084 |

## Build and verify

```bash
docker build -t homework-node ./node-app
docker build -t homework-python ./python-app
docker build -t homework-java ./java-app
docker build -t homework-apache ./Apache-app
docker build -t homework-react ./React-app
docker build -t homework-nginx ./nginx-web

docker run -d --name homework-node -p 3000:3000 homework-node
docker run -d --name homework-python -p 8000:8000 homework-python
docker run -d --name homework-java -p 8081:8080 homework-java
docker run -d --name homework-apache -p 8082:80 homework-apache
docker run -d --name homework-react -p 8083:80 homework-react
docker run -d --name homework-nginx -p 8084:80 homework-nginx

for port in 3000 8000 8081 8082 8083 8084; do curl --fail "http://localhost:${port}"; done
docker ps
```

Clean up only these homework containers:

```bash
docker rm -f homework-node homework-python homework-java homework-apache homework-react homework-nginx
```

## Multi-stage build

```bash
docker build -t homework-multistage ./multi-stage-dockerfile
docker run -d --name homework-multistage -p 8080:8080 homework-multistage
curl --fail http://localhost:8080
docker ps --filter name=homework-multistage
docker rm -f homework-multistage
```

Expected page text: `Hello World from Docker Multi-Stage Build!`

## Evidence checklist

- [x] Add your name and enrollment number.
- [ ] Add screenshots or captured output for all six application pages.
- [ ] Add `docker ps` output showing the multi-stage container on port 8080.
- [ ] Never commit registry passwords or environment secrets.
