#!/bin/sh

#time python test.py docker -c 'killall -9 gftl'
#time python test.py docker -c 'rm -rf /root/docker_run/data/chaindata'
time python test.py exec -c 'docker rm -f $(docker ps -aq)'
time python test.py exec -c 'killall -9 gftl'
time python test.py exec -c 'killall -9 txgen'
killall -9 gftl

