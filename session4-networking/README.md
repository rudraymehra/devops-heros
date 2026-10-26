# Networking Homework

## Screenshot evidence audit — 2026-10-23

See [this session's screenshot inventory and actual capture results](screenshots/README.md).
The 2026-10-16 records below remain historical. Fresh native captures from 2026-10-23 are linked in the evidence page.

## Command observations

| Command | What it demonstrates |
|---|---|
| `ip addr` / `ifconfig` | Interface state, MAC addresses, and assigned IP addresses |
| `ip route` / `netstat -rn` | The route selected for local and internet traffic |
| `ss -tuln` / `netstat -an` | Listening TCP/UDP sockets without DNS lookup delays |
| `ping -c 4 1.1.1.1` | Basic IP reachability and round-trip latency |
| `dig example.com` / `nslookup example.com` | DNS name resolution |
| `curl -I https://example.com` | DNS, TCP, TLS, and HTTP connectivity |
| `traceroute example.com` | Layer-3 path and hop latency, when permitted by the network |

`collect-network-info.sh` runs the portable subset and writes the results to
`network-command-output.txt`. Review the output before committing because interface
details may contain private IP addresses.

```bash
chmod +x collect-network-info.sh
./collect-network-info.sh
```

## Understanding

An IP address identifies an interface on an IP network. A subnet mask or CIDR prefix
separates its network and host portions. The routing table chooses a next hop; DNS
maps names to addresses; transport ports identify services on a host. A successful
ping proves ICMP reachability but does not prove that an application port works, so
`curl` or `nc` should also be used when troubleshooting.

## Evidence checklist

- [x] Reviewed command attempts and their exit codes are linked in [the evidence page](screenshots/README.md).
- [x] Capture the live networking checks and native screenshots on the Mac; `wget` was unavailable and is recorded as skipped.
- [x] The earlier sandbox/network failures remain documented as historical attempts; the latest host run succeeded except for the unavailable optional `wget` command.
