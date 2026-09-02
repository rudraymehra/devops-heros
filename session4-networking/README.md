# Session 4 - Networking Fundamentals Homework

**Student:** Rudray Mehra (GitHub: [rudraymehra](https://github.com/rudraymehra))

This document covers both homework tasks for the networking session:

- **Task 1** - practiced the commands and concepts from `resources.md` and `ip.md` in this folder (IP addressing, subnetting, and the everyday troubleshooting commands from the shared networking repos).
- **Task 2** - executed the networking commands on my own machine and recorded the real output of each command together with a short explanation of what I understood.

All commands below were run on my MacBook Air (macOS 15.5, Apple Silicon, zsh). Where the Linux-only equivalents (`ip`, `ss`) are shown, I ran them inside an `alpine:3.20` Docker container on the same machine. Long outputs have been trimmed to the relevant lines; nothing was invented.

---

## Part A - IP Addressing Basics (from `ip.md`)

Before running commands I revised the theory from `ip.md` in my own words.

### What is an IP address?

An IP address is a unique 32-bit number (IPv4) that identifies a device on a network. It is written as four decimal octets, e.g. `197.23.45.10`, so the full range is `0.0.0.0` to `255.255.255.255`. Every address has two parts: a **network part** (which network the device belongs to) and a **host part** (which device inside that network). The **subnet mask** tells us where that split happens.

### IP classes

| Class | First octet range | Default subnet mask | CIDR | Network bits | Host bits | Usable hosts per network |
|-------|-------------------|---------------------|------|--------------|-----------|--------------------------|
| A | 1 - 127 | 255.0.0.0 | /8 | 8 | 24 | 2^24 - 2 = 16,777,214 |
| B | 128 - 191 | 255.255.0.0 | /16 | 16 | 16 | 2^16 - 2 = 65,534 |
| C | 192 - 223 | 255.255.255.0 | /24 | 24 | 8 | 2^8 - 2 = 254 |
| D | 224 - 239 | n/a (multicast) | - | - | - | - |

We subtract 2 from the total host count because the first address in a block is the **network address** and the last one is the **broadcast address**; neither can be assigned to a host.

### Subnet mask and CIDR notation

`255.0.0.0` and `/8` mean the same thing: the first 8 bits are network bits and the remaining 24 are host bits. Working through the examples from the class notes:

| IP address | Mask / CIDR | Class | Network address | Broadcast address | Usable host range |
|------------|-------------|-------|-----------------|-------------------|-------------------|
| 120.27.1.0 | 255.0.0.0 (/8) | A | 120.0.0.0 | 120.255.255.255 | 120.0.0.1 - 120.255.255.254 |
| 120.27.1.0 | 255.255.0.0 (/16) | A address, subnetted like B | 120.27.0.0 | 120.27.255.255 | 120.27.0.1 - 120.27.255.254 |
| 197.23.45.10 | 255.255.255.0 (/24) | C | 197.23.45.0 | 197.23.45.255 | 197.23.45.1 - 197.23.45.254 |
| 194.23.56.10 | 255.255.255.0 (/24) | C | 194.23.56.0 | 194.23.56.255 | 194.23.56.1 - 194.23.56.254 |

The same IP with a different mask gives a different network: `120.27.1.0/8` belongs to the huge `120.0.0.0` network, but `120.27.1.0/16` belongs to the smaller `120.27.0.0` network. That is the whole point of subnetting - splitting a big block into smaller, more manageable networks.

### Private IP ranges

These ranges are never routed on the public internet and are what we see on home Wi-Fi, office LANs, cloud VPCs and Docker networks:

| Class | Private range | CIDR |
|-------|---------------|------|
| A | 10.0.0.0 - 10.255.255.255 | 10.0.0.0/8 |
| B | 172.16.0.0 - 172.31.255.255 | 172.16.0.0/12 |
| C | 192.168.0.0 - 192.168.255.255 | 192.168.0.0/16 |

**What I understood:** the subnet mask is what actually decides "who is on my network". Two hosts whose addresses match on all the network bits can talk directly (Layer 2, via ARP); anything else has to go through the default gateway. This is exactly what I later saw in the `netstat -rn` routing table and `arp -a` output on my own laptop.

---

## Part B - Networking Commands Executed (Task 2)

### 1. `hostname` and `whoami`

Identify the machine and the user I am running commands as. Useful first step on any server before touching its network config.

```bash
hostname
whoami
```

```text
MacBook-Air-9.local
rudraym
```

**What I understood:** `hostname` prints the device name that shows up in DNS/mDNS (`.local` means it is advertised via Bonjour on the LAN), and `whoami` confirms which account's permissions I have (some network commands like `tcpdump` need root).

---

### 2. `ipconfig getifaddr en0` - my IP address

Quick way on macOS to get only the IPv4 address of an interface (`en0` is the Wi-Fi adapter on a MacBook).

```bash
ipconfig getifaddr en0
```

```text
100.129.161.230
```

**What I understood:** my laptop received `100.129.161.230` from DHCP. This is in the `100.64.0.0/10` block (carrier-grade NAT range), which tells me the campus Wi-Fi is doing NAT between me and the internet.

---

### 3. `ifconfig` - interface configuration

Shows every network interface with its MAC address, IP address, netmask, broadcast address and status. On Linux the modern equivalent is `ip addr show` (shown in section 15).

```bash
ifconfig en0
ifconfig lo0
```

```text
en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether 12:8f:6e:e1:56:65
	inet 100.129.161.230 netmask 0xfffff000 broadcast 100.129.175.255
	media: autoselect
	status: active

lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
	inet 127.0.0.1 netmask 0xff000000
	inet6 ::1 prefixlen 128
	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
	nd6 options=201<PERFORMNUD,DAD>
```

Applying the subnetting theory from Part A to the real values:

| Field | Value | Meaning |
|-------|-------|---------|
| `ether` | `12:8f:6e:e1:56:65` | MAC address (Layer 2 identity of the Wi-Fi card) |
| `inet` | `100.129.161.230` | My IPv4 address |
| `netmask` | `0xfffff000` = `255.255.240.0` | `/20` -> 20 network bits, 12 host bits |
| network address | `100.129.160.0` | first address of the block |
| `broadcast` | `100.129.175.255` | last address of the block |
| usable hosts | 2^12 - 2 = 4094 | enough for a whole campus |
| `lo0 inet` | `127.0.0.1` with `/8` | loopback - traffic never leaves the machine |

**What I understood:** the netmask is shown in hex on macOS, so I converted `0xfffff000` to `255.255.240.0` (/20). The broadcast address `100.129.175.255` matches what the CIDR maths predicts, which confirmed my understanding of network vs host bits. `lo0` is the loopback interface that services such as PostgreSQL bind to when they should only be reachable locally.

---

### 4. `ping` - reachability and latency

`ping` sends ICMP Echo Request packets and waits for Echo Replies. `-c 4` limits it to four packets (otherwise it runs forever on macOS/Linux).

```bash
ping -c 4 google.com
```

```text
PING google.com (142.250.207.174): 56 data bytes
64 bytes from 142.250.207.174: icmp_seq=0 ttl=117 time=22.133 ms
64 bytes from 142.250.207.174: icmp_seq=1 ttl=117 time=23.328 ms
64 bytes from 142.250.207.174: icmp_seq=2 ttl=117 time=21.970 ms
64 bytes from 142.250.207.174: icmp_seq=3 ttl=117 time=45.424 ms

--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 21.970/28.214/45.424/9.950 ms
```

**What I understood:** `ping` proves three things at once - DNS resolved `google.com` to an IP, there is a route to that IP, and the host answers. `0.0% packet loss` and ~22 ms RTT means the link is healthy; the one 45 ms spike is normal Wi-Fi jitter. `ttl=117` means the reply passed through roughly 11 routers (Google starts at 128). A failing ping does not always mean a host is down because many servers block ICMP, so I would follow up with `nc`/`curl` on the actual port.

---

### 5. `curl -I` - HTTP headers

`curl` transfers data over HTTP/HTTPS and many other protocols. `-I` sends a HEAD request so only the response headers come back, which is perfect for health checks.

```bash
curl -I https://github.com
```

```text
HTTP/2 200
date: Thu, 03 Sep 2026 14:22:27 GMT
content-type: text/html; charset=utf-8
content-language: en-US
cache-control: max-age=0, private, must-revalidate
strict-transport-security: max-age=31536000; includeSubdomains; preload
x-frame-options: deny
x-content-type-options: nosniff
referrer-policy: origin-when-cross-origin, strict-origin-when-cross-origin
server: github.com
accept-ranges: bytes
x-github-request-id: D5E0:3EFCB5:2E2456:31655F:6A9982AC
x-github-edge-region: centralindia
```

(The very long `content-security-policy` and `set-cookie` headers were removed from the output above for readability.)

**What I understood:** `HTTP/2 200` confirms the TLS handshake succeeded and the server returned OK. The headers are useful for debugging in DevOps: `strict-transport-security` shows HSTS is enabled, `x-frame-options: deny` is a security header, and `x-github-edge-region: centralindia` tells me which CDN edge served my request. In pipelines I would use `curl -sf -o /dev/null -w "%{http_code}" URL` as a smoke test after a deployment.

---

### 6. `netstat -an | grep LISTEN` - listening ports

`netstat` shows active sockets. `-a` includes listening sockets, `-n` keeps addresses numeric. Filtering for `LISTEN` shows which ports have a server process waiting for connections.

```bash
netstat -an | grep LISTEN | head -n 10
```

```text
tcp4       0      0  127.0.0.1.48643        *.*                    LISTEN
tcp6       0      0  *.53493                *.*                    LISTEN
tcp4       0      0  *.53493                *.*                    LISTEN
tcp4       0      0  127.0.0.1.17430        *.*                    LISTEN
tcp6       0      0  ::1.27017              *.*                    LISTEN
tcp4       0      0  127.0.0.1.27017        *.*                    LISTEN
tcp4       0      0  127.0.0.1.11434        *.*                    LISTEN
tcp4       0      0  127.0.0.1.5432         *.*                    LISTEN
tcp6       0      0  ::1.5432               *.*                    LISTEN
tcp4       0      0  127.0.0.1.7265         *.*                    LISTEN
```

To see *which process* owns a port I used `lsof` (on Linux this is `ss -tulnp`):

```bash
lsof -iTCP -sTCP:LISTEN -P -n | head -n 8
```

```text
COMMAND     PID    USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
rapportd    461 rudraym    8u  IPv4 0xf6aeda387b0208ec      0t0  TCP *:53493 (LISTEN)
rapportd    461 rudraym   11u  IPv6 0x9092d160a39fe671      0t0  TCP *:53493 (LISTEN)
ControlCe   536 rudraym    8u  IPv4 0xc3d725b8239da524      0t0  TCP *:7000 (LISTEN)
ControlCe   536 rudraym    9u  IPv6 0x936ab42229a2ac27      0t0  TCP *:7000 (LISTEN)
ControlCe   536 rudraym   10u  IPv4  0x5d9f9fad343108e      0t0  TCP *:5000 (LISTEN)
ControlCe   536 rudraym   11u  IPv6 0xe9059e4da224a0ed      0t0  TCP *:5000 (LISTEN)
ollama      772 rudraym    3u  IPv4 0xeeaa63ef0d90c281      0t0  TCP 127.0.0.1:11434 (LISTEN)
```

**What I understood:** I could immediately recognise `5432` (PostgreSQL) and `27017` (MongoDB) bound to `127.0.0.1`/`::1` only, which means they are reachable from my laptop but not from the network - a good default. `*.53493` and `*.7000` are bound to all interfaces, so they are exposed on the LAN. This is the first command I would run for an `Address already in use` error or to check that a container's published port is actually open.

---

### 7. `netstat -rn` and `route get default` - routing table

The routing table decides where each outgoing packet is sent. `-r` shows routes, `-n` keeps it numeric.

```bash
netstat -rn | head -n 15
```

```text
Routing tables

Internet:
Destination        Gateway            Flags               Netif Expire
default            100.129.160.1      UGScg                 en0
100.129.160/20     link#11            UCS                   en0      !
100.129.160.1/32   link#11            UCS                   en0      !
100.129.160.1      f4:1e:57:xx:xx:xx  UHLWIir               en0   1155
100.129.160.53     8e:37:ba:xx:xx:xx   UHLWI                 en0    549
100.129.160.54     c6:b2:8b:xx:xx:xx  UHLWI                 en0   1049
100.129.160.65     8a:9b:54:xx:xx:xx  UHLWI                 en0    642
```

```bash
route -n get default
```

```text
   route to: default
destination: default
       mask: default
    gateway: 100.129.160.1
  interface: en0
      flags: <UP,GATEWAY,DONE,STATIC,PRCLONING,GLOBAL>
```

**What I understood:** two rules matter most. `100.129.160/20 -> link#11` says anything in my own subnet is delivered directly over Wi-Fi (the `/20` matches the netmask from `ifconfig`). `default -> 100.129.160.1` says everything else goes to the gateway/router. If the default route is missing, local hosts still work but the internet does not - a classic troubleshooting scenario. On Linux the same is `ip route`.

---

### 8. `traceroute` - path to a destination

`traceroute` sends packets with increasing TTL values so each router on the way reveals itself. `-m 8` caps it at 8 hops, `-w 2` waits 2 s per probe, `-q 2` sends 2 probes per hop.

```bash
traceroute -m 8 -w 2 -q 2 8.8.8.8
```

```text
traceroute to 8.8.8.8 (8.8.8.8), 8 hops max, 40 byte packets
 1  wifi.height8tech.com (100.129.160.1)  17.868 ms  15.409 ms
 2  202.131.133.5.convergentindia.com (202.131.133.5)  15.388 ms  14.975 ms
 3  115.117.125.189.static-mumbai.vsnl.net.in (115.117.125.189)  17.381 ms *
 4  * *
 5  115.112.15.114.static-chennai.vsnl.net.in (115.112.15.114)  18.614 ms  20.719 ms
 6  * *
 7  dns.google (8.8.8.8)  17.145 ms  26.382 ms
```

**What I understood:** hop 1 is my Wi-Fi gateway (same IP as the default route), hop 2 is the ISP, hops 3 and 5 are Tata (VSNL) backbone routers in Mumbai and Chennai, and hop 7 is Google's DNS. The `*` lines are routers that do not send ICMP "time exceeded" replies (often rate-limited or firewalled) - they are not necessarily a problem since the final hop was reached. This is how I would find *where* latency or packet loss starts when a remote service is slow.

---

### 9. `nslookup` - DNS lookup

Queries the configured DNS server for a record.

```bash
nslookup github.com
```

```text
Server:		100.129.160.1
Address:	100.129.160.1#53

Non-authoritative answer:
Name:	github.com
Address: 20.207.73.82
```

**What I understood:** the query went to my gateway (`100.129.160.1`) on UDP port `53`, which forwarded it upstream. "Non-authoritative" means the answer came from a cache/resolver, not from GitHub's own nameservers. I also noticed GitHub resolved to `20.207.73.82` (an Azure India address) while a friend elsewhere would get a different IP - DNS answers can be geo-based.

---

### 10. `dig` - detailed DNS lookup

`dig` is the more detailed DNS tool. `+short` gives only the answer; without it you see the full response including authority and timing.

```bash
dig github.com +short
dig google.com MX +short
```

```text
20.207.73.82
10 smtp.google.com.
```

```bash
dig github.com
```

```text
; <<>> DiG 9.10.6 <<>> github.com
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 49366
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 8, ADDITIONAL: 7

;; QUESTION SECTION:
;github.com.			IN	A

;; ANSWER SECTION:
github.com.		7	IN	A	20.207.73.82

;; AUTHORITY SECTION:
github.com.		166189	IN	NS	ns-520.awsdns-01.net.
github.com.		166189	IN	NS	dns1.p08.nsone.net.
github.com.		166189	IN	NS	ns-1283.awsdns-32.org.
github.com.		166189	IN	NS	ns-1707.awsdns-21.co.uk.

;; Query time: 38 msec
;; SERVER: 100.129.160.1#53(100.129.160.1)
;; WHEN: Thu Sep 03 19:52:43 IST 2026
;; MSG SIZE  rcvd: 379
```

Common record types I practised:

| Record | Purpose | Example |
|--------|---------|---------|
| A | hostname -> IPv4 | `github.com -> 20.207.73.82` |
| AAAA | hostname -> IPv6 | `dig github.com AAAA` |
| MX | mail server for a domain | `google.com -> 10 smtp.google.com.` |
| NS | authoritative nameservers | `ns-520.awsdns-01.net.` |
| CNAME | alias to another name | `dig www.github.com CNAME` |
| TXT | free text (SPF, domain verification) | `dig google.com TXT` |

**What I understood:** `status: NOERROR` and `ANSWER: 1` mean the lookup worked. The TTL of `7` seconds on the A record shows GitHub keeps it very short so they can move traffic quickly; the NS records have a TTL of ~46 hours. The `10` in the MX answer is a priority (lower is preferred). `dig` is what I would use to verify a new A/CNAME record has propagated after changing DNS for a deployment.

---

### 11. DNS configuration - `scutil --dns` and `/etc/resolv.conf`

On Linux the resolver is configured in `/etc/resolv.conf`. macOS keeps that file for compatibility but the real source of truth is `scutil --dns`.

```bash
scutil --dns | head -n 20
```

```text
DNS configuration

resolver #1
  nameserver[0] : 100.129.160.1
  nameserver[1] : 8.8.8.8
  if_index : 11 (en0)
  flags    : Request A records
  reach    : 0x00020002 (Reachable,Directly Reachable Address)

resolver #2
  domain   : local
  options  : mdns
  timeout  : 5
```

```bash
cat /etc/resolv.conf
```

```text
# macOS Notice
# This file is not consulted for DNS hostname resolution ...
# To view the DNS configuration used by this system, use:
#   scutil --dns
nameserver 100.129.160.1
nameserver 8.8.8.8
```

**What I understood:** DHCP handed my laptop two DNS servers - the local gateway first and Google's `8.8.8.8` as a fallback. Resolver #2 handles `.local` names via mDNS/Bonjour, which is why `MacBook-Air-9.local` works on the LAN without any DNS server. If `ping 8.8.8.8` works but `ping google.com` fails, this is the file/command I would check first.

---

### 12. `arp -a` - ARP cache

ARP (Address Resolution Protocol) maps IP addresses to MAC addresses inside the local subnet. `arp -a` shows what the OS has learned so far.

```bash
arp -a | head -n 8
```

```text
wifi.height8tech.com (100.129.160.1) at f4:1e:57:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.53) at 8e:37:ba:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.54) at c6:b2:8b:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.65) at 8a:9b:54:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.70) at e6:6e:9:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.82) at aa:d:70:xx:xx:xx on en0 ifscope [ethernet]
? (100.129.160.102) at (incomplete) on en0 ifscope [ethernet]
? (100.129.160.122) at aa:13:25:xx:xx:xx on en0 ifscope [ethernet]
```

**What I understood:** every entry is a device in my `/20` subnet that my laptop has exchanged packets with - all of them are Layer 2 neighbours, which ties back to the "same network bits = talk directly" rule from Part A. The gateway's MAC `f4:1e:57:xx:xx:xx` is the same one in the routing table. `(incomplete)` means an ARP request was sent but no reply came, so that host is probably offline. Duplicate IPs or a wrong gateway MAC in this table are signs of misconfiguration or ARP spoofing.

---

### 13. `nc -zv` - port connectivity check (telnet replacement)

`nc` (netcat) with `-z` (scan, do not send data) and `-v` (verbose) tests whether a specific TCP port is open. It replaces the old `telnet host port` habit.

```bash
nc -zv github.com 443
nc -zv github.com 80
```

```text
Connection to github.com port 443 [tcp/https] succeeded!
Connection to github.com port 80 [tcp/http] succeeded!
```

**What I understood:** unlike `ping` (ICMP), this proves the actual TCP handshake to the service port works, which is what matters for an application. It is my go-to check for "can this server reach the database on 3306 / 5432?" and for verifying security-group or firewall rules from inside a VM or container.

---

### 14. `nmap` - port scanner (not installed on my machine)

`nmap` scans hosts for open ports and running services. It is not part of macOS, so I did not run it; the command below and its output are shown as an **example of expected output only**, not a real run.

```bash
brew install nmap          # how I would install it
nmap -p 80,443 scanme.nmap.org
```

```text
# expected output on a machine with nmap installed (sample, not executed here)
Nmap scan report for scanme.nmap.org
Host is up.

PORT    STATE SERVICE
80/tcp  open  http
443/tcp open  https
```

**What I understood:** `nmap` does at scale what `nc -zv` does for one port. In DevOps it is used to audit that only the intended ports (e.g. 22, 80, 443) are exposed on a server or cloud security group. It should only be run against hosts you own or have permission to scan.

---

### 15. Linux equivalents - `ip addr`, `ip route`, `ss` (inside Docker)

The course material uses the modern Linux `iproute2` tools. macOS does not ship them, so I ran them inside a throwaway Alpine container on my Mac to compare with the `ifconfig`/`netstat` output above.

```bash
docker run --rm --name netfund-linux alpine:3.20 sh -c '
  apk add -q iproute2 bind-tools
  ip addr show eth0
  ip route
  ss -tuln
  cat /etc/resolv.conf
  hostname -i'
```

```text
11: eth0@if49: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 65535 qdisc noqueue state UP group default
    link/ether 2e:69:c1:xx:xx:xx brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.4/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever

default via 172.17.0.1 dev eth0
172.17.0.0/16 dev eth0 proto kernel scope link src 172.17.0.4

Netid State Recv-Q Send-Q Local Address:Port Peer Address:Port

nameserver 192.168.65.7

172.17.0.4
```

| Task | Old tool (macOS / net-tools) | Modern Linux tool |
|------|------------------------------|-------------------|
| Show interfaces and IPs | `ifconfig` | `ip addr show` (`ip a`) |
| Show routing table | `netstat -rn` | `ip route` (`ip r`) |
| Listening sockets | `netstat -an \| grep LISTEN` | `ss -tuln` (`-p` adds process) |
| ARP / neighbours | `arp -a` | `ip neigh` |
| Test a TCP port | `telnet host port` | `nc -zv host port` |

**What I understood:** the container got `172.17.0.4/16` on Docker's default bridge - a Class B private address with a `/16` mask, so the network is `172.17.0.0`, broadcast `172.17.255.255`, and the gateway `172.17.0.1` is the bridge on my host. `ss -tuln` printed only the header because a fresh Alpine container has no services listening, which is exactly what I would expect. Seeing the same concepts (interface, mask, default route, DNS server) appear identically on macOS and inside a Linux container made the theory in Part A feel concrete.

---

## Summary

| Command | Layer | What it answers |
|---------|-------|-----------------|
| `hostname` / `whoami` | - | Which machine and which user am I? |
| `ifconfig` / `ip addr` | 2-3 | What is my IP, mask, MAC, and is the link up? |
| `arp -a` / `ip neigh` | 2 | Which neighbours are in my subnet and what are their MACs? |
| `netstat -rn` / `ip route` | 3 | Where do packets go - directly, or via the gateway? |
| `ping` | 3 | Is the host reachable and what is the latency? |
| `traceroute` | 3 | Which routers are on the path and where does it break? |
| `nslookup` / `dig` / `scutil --dns` | 7 (DNS) | Does the name resolve, to what, via which server? |
| `nc -zv` / `nmap` | 4 | Is the TCP port open? |
| `netstat -an` / `ss -tuln` / `lsof -i` | 4 | What is listening on my machine, and which process owns it? |
| `curl -I` | 7 (HTTP) | Does the web service respond and with what status/headers? |

My biggest takeaway from this session is that troubleshooting follows the layers: first check my own address and mask (`ifconfig`), then the route (`netstat -rn`), then reachability (`ping`/`traceroute`), then name resolution (`dig`), then the port (`nc`), and finally the application itself (`curl`). Each command answers one question, and running them in that order finds the problem quickly.
