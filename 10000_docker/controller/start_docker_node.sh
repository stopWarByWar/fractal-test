#!/bin/sh

for id in $(docker ps -aq);
do
#docker exec ${id} /bin/bash -c "rm -rf /data/docker_run/data/chaindata"
docker exec ${id} /bin/bash -c "cd /data/docker_run && bash startNode.sh"
done
