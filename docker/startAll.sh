#!/bin/sh
killall -9 txgen
killall -9 txgenkillall -9 gftl

time python test.py exec -c "killall -9 gftl"
time python test.py exec -c "rm -rf /root/run/*"
time python test.py upload -f ./gftl
time python test.py upload -f ./test.toml
time python test.py upload -f ./startNode.sh
time python test.py upload -f ./generateAccount.sh

#rm /home/data/keystore/*
#bash /root/run/generateAccount.sh

time python test.py exec -c "cd /root/run && bash generateAccount.sh"
time python generateAlloc.py
time python test.py upload -f ./genesis_alloc.json

rm -rf /home/data/chaindata

IP=$(hostname)

nohup ./gftl --identity ${IP} --unlock 123 --pack --metrics --influxdburl http://129.28.54.225:8086 --influxdbdatabase metrics --influxdbusername fractal --influxdbpassword fractal666 --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir /home/data --port 30303 --pprof --pprofport 6060 --verbosity 3 --metrics > /home/test.log 2>&1 &
sleep 3

bash startTx.sh
sleep 3

cd /root/boot
time python test.py exec -c "ntpdate cn.pool.ntp.org"
time python test.py exec -c "cd /root/run && bash startNode.sh"
