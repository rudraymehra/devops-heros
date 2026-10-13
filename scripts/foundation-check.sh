#!/usr/bin/env bash
set -euo pipefail
set -x
lab_dir=$(mktemp -d)
test ! -e "$lab_dir/original"
printf 'Sudhir Mehra · 24 BCS 10425 · Batch B\n' > "$lab_dir/original"
ln "$lab_dir/original" "$lab_dir/hard"
ln -s "$lab_dir/original" "$lab_dir/soft"
ls -li "$lab_dir"
test "$(stat -c %i "$lab_dir/original")" = "$(stat -c %i "$lab_dir/hard")"
rm "$lab_dir/original"
test -f "$lab_dir/hard"
test ! -e "$lab_dir/soft"
getent passwd campusfix-lab && exit 1
sudo adduser --disabled-password --gecos 'Sudhir Mehra lab' campusfix-lab
id campusfix-lab
sudo deluser --remove-home campusfix-lab
sudo journalctl -u ssh --no-pager -n 15
date
hostname
whoami
df -h
ip -brief address
ip route
ss -tuln
getent hosts github.com
curl -I --fail https://example.com
printf 'Sudhir Mehra\n24 BCS 10425\n' | bash session3-shell-scripting/system-info.sh
bash session5-git-github/run-cherry-pick-lab.sh
docker compose -p campusfix-homework -f session8-docker-networking-volume/demo/docker-compose.yml up -d --build
docker compose -p campusfix-homework -f session8-docker-networking-volume/demo/docker-compose.yml ps
docker network inspect campusfix-homework_frontend_net campusfix-homework_backend_net campusfix-homework_database_net
curl --retry 20 --retry-delay 2 --retry-all-errors --fail http://127.0.0.1:8080
docker compose -p campusfix-homework -f session8-docker-networking-volume/demo/docker-compose.yml exec -T backend python -c 'import socket,time; time.sleep(20); print(socket.gethostbyname("database")); s=socket.create_connection(("database",3306),timeout=10); print("MySQL reachable from backend"); s.close()'
printf 'Hello students\n' > "$lab_dir/index.html"
docker run -d --name bind-demo -p 8081:80 -v "$lab_dir:/usr/share/nginx/html:ro" nginx:alpine
curl --retry 20 --retry-delay 2 --retry-all-errors --fail http://127.0.0.1:8081
printf 'Hello students — updated without restart\n' > "$lab_dir/index.html"
curl --fail http://127.0.0.1:8081 | grep 'updated without restart'
docker run -d --name host-demo --network host httpd:2.4-alpine
curl --retry 20 --retry-delay 2 --retry-all-errors --fail http://127.0.0.1:80
docker rm -f bind-demo host-demo
docker compose -p campusfix-homework -f session8-docker-networking-volume/demo/docker-compose.yml down -v
echo 'PASS: Linux, shell, Git, networking, Compose networks, bind mount and host networking.'
