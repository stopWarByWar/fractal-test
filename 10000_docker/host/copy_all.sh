#!/bin/sh

for((i=1;i<=25;i++));
do
cp /root/run/* /root/docker_run/${i}
done