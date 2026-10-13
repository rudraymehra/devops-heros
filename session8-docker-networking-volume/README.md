# Docker Networking and Volumes Homework

## Task 1: three-container networking

The `demo/` Compose application contains an Nginx frontend, Flask backend, and MySQL
database. It defines three named networks. The backend joins `frontend_net` and
`backend_net`, allowing it to connect the two application tiers without exposing the
database directly to the frontend. `database_net` is an additional internal network.

```bash
docker compose -f demo/docker-compose.yml up --build -d
docker compose -f demo/docker-compose.yml ps
docker compose -f demo/docker-compose.yml exec frontend getent hosts backend
docker compose -f demo/docker-compose.yml exec backend getent hosts database
curl --fail http://localhost:8080/api
docker compose -f demo/docker-compose.yml down -v
```

Compose provides service-name DNS only between containers sharing a network.

## Task 2: host network

The `host-network/` example runs Apache with `network_mode: host`. On native Linux,
Apache listens directly on host port 80 and no `ports` mapping is used.

```bash
docker compose -f host-network/docker-compose.yml up -d
curl --fail http://localhost/
docker compose -f host-network/docker-compose.yml down
```

Docker Desktop requires host networking to be enabled in Settings and its behavior
differs from native Linux.

## Task 3: bind mount

```bash
docker compose -f bind-mount/docker-compose.yml up -d
curl --fail http://localhost:8088
```

Edit `bind-mount/site/index.html`, save it, and repeat the curl command. The result
changes immediately because the host directory is mounted into Nginx; no image
rebuild or container restart is required.

## Task 4: overlay network research

An overlay network creates a virtual Layer-2 network across multiple Docker hosts.
Docker Swarm uses VXLAN encapsulation and a distributed control plane so services
can communicate using service names even when tasks run on different nodes. Overlay
networks are useful for multi-host services, encrypted east-west traffic, and
service discovery. They require Swarm mode and open inter-node control/data-plane
ports; a normal single-host bridge network does not cross machines.

Example on a disposable multi-node Swarm:

```bash
docker swarm init
docker network create --driver overlay --attachable app-overlay
docker network inspect app-overlay
```

Do not initialize Swarm on a shared or production host solely for this exercise.

## Evidence checklist

- [ ] `docker compose ps` and successful `/api` response
- [ ] DNS/connectivity checks between allowed tiers
- [ ] Apache response through host networking
- [ ] Bind-mount page before and after editing
- [ ] `docker network inspect` output for the lab networks

Resource: <https://docs.docker.com/engine/network/drivers/>
