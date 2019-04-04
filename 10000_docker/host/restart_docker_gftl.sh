#!/bin.sh


for id in $(docker ps -aq);
do
docker exec ${id} /bin/bash -c "killall -9 gftl"
docker exec ${id} /bin/bash -c "rm /root/docker_run/data/chaindata"
done
