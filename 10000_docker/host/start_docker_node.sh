#!/bin/sh

for id in $(docker ps -aq);
do
docker exec ${id} /bin/bash -c "cd /root/docker_run && bash startNode.sh"
done
