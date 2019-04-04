#!/bin/sh

for id in $(docker ps -aq);
do
docker exec ${id} /bin/bash -c "cat /root/docker_run/No | xargs hostname"
pipework tc ${id} qdisc add dev eth0 root handle 1:0 netem delay 100ms
pipework tc ${id} qdisc add dev eth0 parent 1:1 handle 10: tbf rate 20Mbit buffer 12800 limit 24000
done

