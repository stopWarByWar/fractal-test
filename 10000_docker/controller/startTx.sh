#!/bin/sh

IP=$(hostname)

if [ ${IP:0:6} == "172.16" ];then
exit 0
fi

delay=$(($RANDOM%10000))
Delay=$(echo "scale=3; $delay / 1000  "|bc -l)
sleep ${Delay}

killall -9 txgen
nohup ./txgen --tps 1000 --nprocess 10 --batch 10 --rpc http://127.0.0.1:8545 --from $(cat addr) --to $(cat addr) --verbosity 3 > /data/run/tx.log 2>&1 &

