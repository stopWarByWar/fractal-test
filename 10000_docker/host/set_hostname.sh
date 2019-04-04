#!/bin/sh

HOSTNAME=$(hostname)


for((i=1;i<=25;i++));
do
echo ${HOSTNAME}-${i} > /root/docker_run/${i}/No
done