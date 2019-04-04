#!/bin/sh
File=${1}

for((i=1;i<=25;i++));
do
cp /root/run/${File} /root/docker_run/${i}
done