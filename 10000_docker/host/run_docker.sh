#!/bin/bash

#!bin/sh
docker rm -f $(docker ps -aq)
Hostname=$(/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:" | grep 172 | grep -v 172.17.0.1)

sed -i "s/HOSTNAME/${Hostname}/g" /root/run/startNode.sh
bash copy.sh startNode.sh

Count=${1}
NodeId=$(cat /root/run/NodeId)
low=$[${NodeId}/100+1]
high=$[${NodeId}%100+1]

for((i=1;i<10;i++));
do
cd /root/docker_run/${i}
sed -i "s/PORT/3030${i}/g" startNode.sh
docker run -itd --privileged --net=test --ip=10.${high}.${low}.${i} --name=$(hostname)_0${i} -p 3030${i}:3030${i}/tcp -p 3030${i}:3030${i}/udp -v /root/docker_run/${i}:/root/docker_run 138b1e2a24ac
done

for((i=10;i<=25&&i<=${Count};i++));
do
cd /root/docker_run/${i}
sed -i "s/PORT/303${i}/g" startNode.sh
docker run -itd --privileged --net=test --ip=10.${high}.${low}.${i} --name=$(hostname)_${i} -p 303${i}:303${i}/tcp -p 303${i}:303${i}/udp -v /root/docker_run/${i}:/root/docker_run 138b1e2a24ac
done