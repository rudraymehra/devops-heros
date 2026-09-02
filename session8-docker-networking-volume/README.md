# Docker Networking & Volumes Homework

**Author:** Rudray Mehra
**Environment:** macOS 15.5 (Apple Silicon), Docker Desktop 28.3.2 (engine runs inside a `linuxkit` VM, kernel 6.10.14, aarch64)

This README covers the four tasks from the Docker Networking & Volume session. Every command below was run on my machine and the outputs are pasted from my terminal. I prefixed all my containers and networks with `hwdn-` so they are easy to find and clean up afterwards.

**Contents**

1. [Task 1: Docker Container Networking](#task-1-docker-container-networking)
2. [Task 2: Host Network](#task-2-host-network)
3. [Task 3: Bind Mount](#task-3-bind-mount)
4. [Task 4: Overlay Network](#task-4-overlay-network)
5. [Cleanup](#cleanup)
6. [Resources](#resources)

---

## Task 1: Docker Container Networking

**Goal:** run a `frontend`, a `backend` and a `database` container, create three separate networks, attach the backend to two of them, and check which containers can talk to each other.

My plan for the three tiers:

| Container       | Image          | Networks it is attached to             | Role                          |
|-----------------|----------------|----------------------------------------|-------------------------------|
| `hwdn-frontend` | `nginx:alpine` | `hwdn-frontend-net`                    | web tier                      |
| `hwdn-backend`  | `alpine`       | `hwdn-backend-net` + `hwdn-db-net`     | app tier (on **two** networks) |
| `hwdn-db`       | `mysql:8.0`    | `hwdn-db-net`                          | database tier                 |

### Step 1: Create the three networks

```bash
docker network create hwdn-frontend-net
docker network create hwdn-backend-net
docker network create hwdn-db-net
docker network ls --filter name=hwdn-
```

```text
c0ee9c39f423037793218fbf8267114562046982be7448cb41cbea081956cb28
5b139ea3f7437f3fbff9b69c6a51e9a12f7f364c8230a1c641e343a6fadc02b6
9a20fba5317ee87d24cd141e489bd78bbf71919624ba789755e51ae1a888483f

NETWORK ID     NAME                DRIVER    SCOPE
5b139ea3f743   hwdn-backend-net    bridge    local
9a20fba5317e   hwdn-db-net         bridge    local
c0ee9c39f423   hwdn-frontend-net   bridge    local
```

Without `-d` Docker uses the default `bridge` driver, so each of these is a separate user-defined bridge with its own subnet and its own embedded DNS.

### Step 2: Start the three containers, each on its own network

```bash
docker run -d --name hwdn-frontend --network hwdn-frontend-net nginx:alpine
docker run -d --name hwdn-backend  --network hwdn-backend-net  alpine sleep infinity
docker run -d --name hwdn-db       --network hwdn-db-net -e MYSQL_ROOT_PASSWORD=Secret123 mysql:8.0
docker ps --filter name=hwdn- --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
```

```text
7b130bf3bca288db3e7e4e5b956fddd108938e48bb62e1dbefc9569240c6fde2
aabd3ad6e910f29d5e104904f91ccb86e8a149f47d2cf50b74e747fdc3ab012a
1eed4681cd83c245ba16a6de2bb68ce30c7bcadc57d0d43724c0f3f1efd010de

NAMES           IMAGE          STATUS                  PORTS
hwdn-db         mysql:8.0      Up Less than a second   3306/tcp, 33060/tcp
hwdn-backend    alpine         Up Less than a second
hwdn-frontend   nginx:alpine   Up 1 second             80/tcp
```

The backend is plain Alpine running `sleep infinity` so it stays alive and I can `docker exec` into it for `ping` / `nc`. MySQL needs `MYSQL_ROOT_PASSWORD` or the container exits immediately.

### Step 3: Before connecting - backend cannot see the database

```bash
docker exec hwdn-backend ping -c 2 hwdn-db
```

```text
ping: bad address 'hwdn-db'
```

At this point the backend is only on `hwdn-backend-net` and the database only on `hwdn-db-net`, so Docker's DNS does not even resolve the name.

### Step 4: Attach the backend to the database network (backend is now on 2 networks)

```bash
docker network connect hwdn-db-net hwdn-backend

docker inspect hwdn-backend  --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} -> {{$v.IPAddress}}{{println}}{{end}}'
docker inspect hwdn-frontend --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} -> {{$v.IPAddress}}{{println}}{{end}}'
docker inspect hwdn-db       --format '{{range $k,$v := .NetworkSettings.Networks}}{{$k}} -> {{$v.IPAddress}}{{println}}{{end}}'
```

```text
# hwdn-backend
hwdn-backend-net -> 172.21.0.2
hwdn-db-net -> 172.22.0.3

# hwdn-frontend
hwdn-frontend-net -> 172.20.0.2

# hwdn-db
hwdn-db-net -> 172.22.0.2
```

The backend now has **two interfaces and two IPs**, one in each subnet. `docker network connect` works on a running container; no restart was needed.

### Step 5: `docker network inspect` (trimmed with `jq`)

```bash
docker network inspect hwdn-db-net --format '{{json .}}' \
  | jq '{Name, Driver, Subnet: .IPAM.Config[0].Subnet, Containers: [.Containers[] | {Name, IPv4Address}]}'
```

```text
{
  "Name": "hwdn-db-net",
  "Driver": "bridge",
  "Subnet": "172.22.0.0/16",
  "Containers": [
    { "Name": "hwdn-db",      "IPv4Address": "172.22.0.2/16" },
    { "Name": "hwdn-backend", "IPv4Address": "172.22.0.3/16" }
  ]
}
```

Same command for the other two networks:

```text
{
  "Name": "hwdn-backend-net",
  "Driver": "bridge",
  "Subnet": "172.21.0.0/16",
  "Containers": [
    { "Name": "hwdn-backend", "IPv4Address": "172.21.0.2/16" }
  ]
}
{
  "Name": "hwdn-frontend-net",
  "Driver": "bridge",
  "Subnet": "172.20.0.0/16",
  "Containers": [
    { "Name": "hwdn-frontend", "IPv4Address": "172.20.0.2/16" }
  ]
}
```

### Step 6: Connectivity checks

**backend -> db (same network `hwdn-db-net`) - works**

```bash
docker exec hwdn-backend ping -c 2 hwdn-db
docker exec hwdn-backend nc -zv hwdn-db 3306
```

```text
PING hwdn-db (172.22.0.2): 56 data bytes
64 bytes from 172.22.0.2: seq=0 ttl=64 time=0.905 ms
64 bytes from 172.22.0.2: seq=1 ttl=64 time=0.151 ms

--- hwdn-db ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.151/0.528/0.905 ms

hwdn-db (172.22.0.2:3306) open
```

**frontend -> db (no shared network) - blocked**

```bash
docker exec hwdn-frontend ping -c 2 hwdn-db
docker exec hwdn-frontend ping -c 2 -W 2 172.22.0.2   # try the db IP directly
```

```text
ping: bad address 'hwdn-db'

PING 172.22.0.2 (172.22.0.2): 56 data bytes

--- 172.22.0.2 ping statistics ---
2 packets transmitted, 0 packets received, 100% packet loss
```

Two different layers block this: the name does not resolve (DNS is per-network), and even the raw IP is unreachable because the two bridges are isolated at Layer 2/3.

**frontend -> backend (no shared network yet) - blocked**

```bash
docker exec hwdn-frontend ping -c 2 hwdn-backend
```

```text
ping: bad address 'hwdn-backend'
```

### Step 7: Let the frontend reach the backend, but still not the database

A realistic 3-tier layout is: frontend talks to backend, backend talks to db, frontend never talks to db. I connected the frontend to `hwdn-backend-net` to complete that picture.

```bash
docker network connect hwdn-backend-net hwdn-frontend
docker exec hwdn-frontend ping -c 2 hwdn-backend
docker exec hwdn-backend wget -qO- http://hwdn-frontend | head -n 5
docker exec hwdn-frontend ping -c 2 hwdn-db
```

```text
PING hwdn-backend (172.21.0.2): 56 data bytes
64 bytes from 172.21.0.2: seq=0 ttl=64 time=0.408 ms
64 bytes from 172.21.0.2: seq=1 ttl=64 time=0.402 ms

--- hwdn-backend ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.402/0.405/0.408 ms

<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>

ping: bad address 'hwdn-db'
```

### Connectivity summary

| From            | To              | Shared network?      | Result                           |
|-----------------|-----------------|----------------------|----------------------------------|
| `hwdn-backend`  | `hwdn-db`       | `hwdn-db-net`        | ping OK, TCP 3306 open           |
| `hwdn-frontend` | `hwdn-backend`  | `hwdn-backend-net`   | ping OK, HTTP from backend works |
| `hwdn-frontend` | `hwdn-db`       | none                 | `bad address`, 100% packet loss  |

**What I understood:** a user-defined bridge network is both a broadcast domain and a DNS zone. Containers only resolve and reach each other if they share at least one network, and a container attached to two networks (like my backend) acts as the only bridge between the tiers. That is how network segmentation is done in Docker without writing any firewall rules.

---

## Task 2: Host Network

**Goal:** pull the Apache2 image, run it with the host network driver, and access it on port 80 without any `-p` mapping.

### Step 1: Pull and run Apache on the host network

```bash
docker pull httpd:2.4
docker run -d --name hwdn-apache --network host httpd:2.4
docker ps --filter name=hwdn-apache --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'
docker inspect hwdn-apache --format 'NetworkMode={{.HostConfig.NetworkMode}} Ports={{.NetworkSettings.Ports}} IP="{{.NetworkSettings.IPAddress}}"'
```

```text
bc23b1e50410fca84f9874c4ca003fe39359a6097eb527e3b2f7502b34f1e912

NAMES         IMAGE       STATUS         PORTS
hwdn-apache   httpd:2.4   Up 3 seconds

NetworkMode=host Ports=map[] IP=""
```

The `PORTS` column is empty and the container has **no IP of its own**. In host mode Docker does not create a network namespace for the container - Apache binds straight to port 80 of the host's network stack, so there is nothing to publish.

### Step 2: Access the site on port 80

On a **Linux server** this is simply:

```bash
curl http://localhost:80
```

On my Mac, "the host" for the Docker engine is the Docker Desktop Linux VM, not macOS itself. So I checked from two places:

**a) From macOS directly**

```bash
curl -s -i --max-time 5 http://localhost:80
```

```text
(no response) curl exit code: 7  -> Connection refused
```

**b) From inside the Docker host's network namespace** (another `--network host` container shares the same stack as Apache):

```bash
docker run --rm --network host alpine wget -qO- http://localhost:80
docker run --rm --network host alpine netstat -tln | grep ':80 '
```

```text
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<title>It works! Apache httpd</title>
</head>
<body>
<p>It works!</p>
</body>
</html>

tcp        0      0 :::80                   :::*                    LISTEN
```

`netstat` on the host network shows Apache listening on `:::80` and the page is served, which confirms host networking works exactly as expected - port 80 on the Docker host, no `-p` required.

### macOS caveat

| Where I ran `curl localhost:80` | Result | Why |
|---|---|---|
| Linux server (expected)        | `It works!` | container shares the real host's network stack |
| Docker host namespace on my Mac (`--network host alpine`) | `It works!` | same Linux network stack as Apache |
| macOS terminal                  | connection refused | the Docker "host" is a VM; macOS is outside it |

Docker Desktop for Mac has an opt-in setting (*Settings -> Resources -> Network -> Enable host networking*) that forwards host-mode ports to macOS. It was not enabled on my machine, so the macOS `curl` failed. This is a Docker Desktop limitation, not a problem with the container. The `docker inspect` output (`NetworkMode=host`) and the in-namespace test above are the proof that the task is done correctly.

**What I understood:** `--network host` removes network isolation completely - the container sees the host's interfaces and ports. It is fast (no NAT) and handy for tools that need to see the real host network, but two host-mode containers cannot both listen on port 80, and it is Linux-only in the true sense of the word.

---

## Task 3: Bind Mount

**Goal:** create a folder with an `index.html` that says *Hello students*, bind-mount it into Nginx, verify it, edit the file, and confirm the change shows up without restarting the container.

### Step 1: Create the folder and file

The folder is committed in this repo as [`bind_mount_demo/`](./bind_mount_demo/).

```bash
mkdir -p bind_mount_demo
cat bind_mount_demo/index.html
```

```text
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Bind Mount Demo</title>
</head>
<body>
  <h1>Hello students</h1>
  <p>This page is served by Nginx from a bind-mounted folder on my laptop.</p>
</body>
</html>
```

### Step 2: Run Nginx with the folder bind-mounted

```bash
docker run -d --name hwdn-nginx-bind \
  -v "$(pwd)/bind_mount_demo:/usr/share/nginx/html" \
  -p 8085:80 nginx:alpine

docker inspect hwdn-nginx-bind --format '{{json .Mounts}}' | jq '.[] | {Type, Source, Destination, RW}'
```

```text
ec251c8b594934d7751d0cbdf6a9edce745732a1dc0ca1d2985fce86c0e50033

{
  "Type": "bind",
  "Source": "/Users/rudraym/Devops assignment/devops-heros/session8-docker-networking-volume/bind_mount_demo",
  "Destination": "/usr/share/nginx/html",
  "RW": true
}
```

`Type: bind` confirms this is a bind mount (a host path), not a Docker-managed volume.

### Step 3: Verify the initial content

```bash
curl -s http://localhost:8085
```

```text
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Bind Mount Demo</title>
</head>
<body>
  <h1>Hello students</h1>
  <p>This page is served by Nginx from a bind-mounted folder on my laptop.</p>
</body>
</html>
```

### Step 4: Edit the file on my laptop (container is NOT restarted)

```bash
sed -i '' 's|<h1>Hello students</h1>|<h1>Hello students - updated live</h1>|' bind_mount_demo/index.html
curl -s http://localhost:8085 | grep h1
docker ps --filter name=hwdn-nginx-bind --format '{{.Names}} {{.Status}}'
docker exec hwdn-nginx-bind cat /usr/share/nginx/html/index.html | grep h1
```

```text
  <h1>Hello students - updated live</h1>
hwdn-nginx-bind Up 24 seconds
  <h1>Hello students - updated live</h1>
```

The container's uptime kept counting (`Up 24 seconds`), so no restart happened, yet both `curl` and the file inside the container show the new heading.

### Step 5: Restore the original text

```bash
sed -i '' 's|<h1>Hello students - updated live</h1>|<h1>Hello students</h1>|' bind_mount_demo/index.html
curl -s http://localhost:8085 | grep h1
```

```text
  <h1>Hello students</h1>
```

### Bind mount vs named volume

| | Bind mount (`-v /host/path:/ctr/path`) | Named volume (`-v name:/ctr/path`) |
|---|---|---|
| Who manages the data | me, on the host filesystem | Docker (`/var/lib/docker/volumes`) |
| Good for | local development, live-editing config/HTML | databases, persistent app data |
| Portable across hosts | no (depends on host path) | yes (Docker handles it) |
| Shows in `docker volume ls` | no | yes |

**What I understood:** a bind mount is not a copy - the same directory inode is visible from both the host and the container, so any write on one side is instantly visible on the other. That is why Nginx served the edited page without a restart, and why bind mounts are so useful in development.

---

## Task 4: Overlay Network

**Goal:** research Docker overlay networks - what they are, how they work across multiple hosts, and when to use them. I also created one locally to see the real objects Docker produces.

### What an overlay network is

The bridge networks from Task 1 only exist on one machine: `hwdn-db-net` is a Linux bridge inside my Docker host and a container on another server has no way to join it. An **overlay network** solves this. It is a virtual Layer 2 network that spans several Docker hosts, so containers on different physical machines get IPs from one shared subnet and talk to each other by name as if they were plugged into the same switch. The physical network between the hosts (the "underlay") only needs to route normal IP traffic between them.

Overlay networks require **Swarm mode** (or another key-value store) because some component has to know which container IP lives on which host.

### How it works across hosts

1. **VXLAN encapsulation (data plane).** Each overlay network gets a VXLAN Network Identifier (VNI). When container A on host 1 sends an Ethernet frame to container B on host 2, the kernel on host 1 wraps that whole frame inside a UDP packet (destination port **4789**) addressed to host 2's IP. Host 2 receives the UDP packet, strips the outer headers and delivers the original frame to container B. Neither container knows the packet crossed a physical network. The VNI is what keeps different overlay networks separate even though they all travel over the same UDP port.

2. **Control plane (Swarm managers + gossip).** Managers store the network definition (subnet, VNI, which services are attached) in the Raft-replicated Swarm state. Nodes that have a container on the overlay exchange the "which MAC/IP is on which host" information using a **gossip protocol** (SWIM-style, on TCP/UDP **7946**). This populates the VXLAN forwarding database on every host, so there is no flooding and no need to broadcast ARP across the physical network.

3. **Service discovery and load balancing.** Docker's embedded DNS on each node resolves container/service names to overlay IPs. In Swarm, a service also gets a virtual IP (VIP), and IPVS on each host load-balances connections to the VIP across all replicas wherever they run.

4. **Optional encryption.** `docker network create -d overlay --opt encrypted` makes Docker set up IPsec tunnels between the nodes, so the VXLAN traffic is encrypted on the wire.

Ports that must be open between hosts:

| Port        | Protocol  | Purpose                              |
|-------------|-----------|--------------------------------------|
| 2377/tcp    | TCP       | Swarm cluster management (Raft)      |
| 7946        | TCP + UDP | Gossip between nodes                 |
| 4789/udp    | UDP       | VXLAN data traffic                   |
| ESP (50)    | IP        | Only if `--opt encrypted` is used    |

### Bridge vs overlay

| | `bridge`                              | `overlay`                                   |
|---|---|---|
| Scope        | `local` (one host)               | `swarm` (all nodes in the cluster)         |
| Needs Swarm  | no                               | yes                                         |
| How frames move | Linux bridge on the host      | VXLAN tunnels over UDP 4789 between hosts  |
| DNS          | embedded DNS per network          | embedded DNS + service VIPs                |
| Typical use  | single-host apps, local dev      | multi-host microservices, Swarm services   |

### Use cases

- **Multi-host microservices** - a web service on node 1 talks to an API on node 2 and a cache on node 3 by name, without publishing ports on every host.
- **Swarm services and rolling updates** - replicas move between nodes and keep working because they stay on the same overlay subnet.
- **Isolating tiers across a cluster** - exactly what I did in Task 1, but cluster-wide: a `frontend` overlay and a `backend` overlay with only the API attached to both.
- **Encrypted east-west traffic** - `--opt encrypted` when nodes sit in different data centres or clouds.
- **Attaching standalone containers** - with `--attachable`, plain `docker run` containers (not only services) can join the overlay, useful for debugging.

### Hands-on: creating an overlay network locally

Swarm can run with a single node, so I initialised it, created an attachable overlay, and put two containers on it.

```bash
docker network ls
```

```text
NETWORK ID     NAME                DRIVER    SCOPE
bdea4a3d5380   bridge              bridge    local
cd32e3e8a932   host                host      local
5b139ea3f743   hwdn-backend-net    bridge    local
9a20fba5317e   hwdn-db-net         bridge    local
c0ee9c39f423   hwdn-frontend-net   bridge    local
d6d519a401fe   none                null      local
(unrelated project networks omitted)
```

```bash
docker swarm init
docker network create -d overlay --attachable hwdn-overlay-net
docker network ls --filter driver=overlay
docker node ls
```

```text
Swarm initialized: current node (au8qlpqvuh51gzvapvd7tdrgd) is now a manager.

hr1jtrqncu11j0ygxmy7khc96

NETWORK ID     NAME               DRIVER    SCOPE
hr1jtrqncu11   hwdn-overlay-net   overlay   swarm
v1sgpsuk8ylx   ingress            overlay   swarm

ID                            HOSTNAME         STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
au8qlpqvuh51gzvapvd7tdrgd *   docker-desktop   Ready     Active         Leader           28.3.2
```

Note the scope changed from `local` to `swarm`, and Docker also created the `ingress` overlay automatically - that is the network used for the routing mesh when services publish ports.

```bash
docker network inspect hwdn-overlay-net --format '{{json .}}' \
  | jq '{Name, Driver, Scope, Attachable, Subnet: .IPAM.Config[0].Subnet, Options}'
```

```text
{
  "Name": "hwdn-overlay-net",
  "Driver": "overlay",
  "Scope": "swarm",
  "Attachable": true,
  "Subnet": "10.0.1.0/24",
  "Options": {
    "com.docker.network.driver.overlay.vxlanid_list": "4097"
  }
}
```

The `vxlanid_list: 4097` is the VNI that would tag this network's VXLAN packets on the wire - real evidence of the encapsulation described above.

```bash
docker run -d --name hwdn-ov-a --network hwdn-overlay-net alpine sleep infinity
docker run -d --name hwdn-ov-b --network hwdn-overlay-net alpine sleep infinity
docker exec hwdn-ov-a ping -c 2 hwdn-ov-b
docker exec hwdn-ov-a ip -o addr show | grep -v ' lo ' | awk '{print $2, $4}'
```

```text
PING hwdn-ov-b (10.0.1.4): 56 data bytes
64 bytes from 10.0.1.4: seq=0 ttl=64 time=0.441 ms
64 bytes from 10.0.1.4: seq=1 ttl=64 time=0.304 ms

--- hwdn-ov-b ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.304/0.372/0.441 ms

eth0 10.0.1.2/24
eth1 172.23.0.3/16
```

The containers got `10.0.1.x` addresses from the overlay subnet (`eth0`), plus a second interface on the `docker_gwbridge` (`eth1`) which is what gives overlay containers outbound internet access. With a second node joined via `docker swarm join`, the same `ping` would work across machines with no extra configuration.

**What I understood:** an overlay network is Docker's way of making a cluster look like a single host from the container's point of view. VXLAN carries the frames, Swarm's gossip tells each node where every container lives, and embedded DNS plus VIPs make services discoverable by name. It is the networking foundation that Swarm services (and, conceptually, Kubernetes CNI plugins) are built on.

---

## Cleanup

I removed everything I created (containers with their anonymous volumes, all four networks) and left Swarm mode.

```bash
docker rm -f -v hwdn-frontend hwdn-backend hwdn-db hwdn-apache hwdn-nginx-bind hwdn-ov-a hwdn-ov-b
docker network rm hwdn-frontend-net hwdn-backend-net hwdn-db-net hwdn-overlay-net
docker swarm leave --force
docker ps -a --filter name=hwdn- ; docker network ls --filter name=hwdn-
docker info --format 'Swarm: {{.Swarm.LocalNodeState}}'
```

```text
hwdn-frontend
hwdn-backend
hwdn-db
hwdn-apache
hwdn-nginx-bind
hwdn-ov-a
hwdn-ov-b

hwdn-frontend-net
hwdn-backend-net
hwdn-db-net
hwdn-overlay-net

Node left the swarm.

NETWORK ID   NAME      DRIVER    SCOPE
Swarm: inactive
```

---

## Resources

- https://docs.docker.com/engine/network/drivers/
- https://docs.docker.com/engine/network/drivers/overlay/
- https://docs.docker.com/engine/network/drivers/host/
- https://docs.docker.com/engine/storage/bind-mounts/
- https://docs.docker.com/engine/swarm/networking/
