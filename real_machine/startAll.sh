#!/usr/bin/env bash

time python test.py exec -c "killall -9 gftl"
time python test.py exec -c "rm -rf /root/run"
time python test.py exec -c "mkdir /root/run"
time python test.py upload -f ./gftl
time python test.py upload -f ./txgen
time python test.py upload -f ./test.toml
time python test.py upload -f ./startNode.sh
time python test.py upload -f ./startPacker.sh
time python test.py upload -f ./startTx.sh
time python test.py upload -f ./generateAccount.sh

time python test.py exec -c "cd /root/run && bash generateAccount.sh"
time python generateAlloc.py
time python test.py upload -f ./genesis_alloc.json

#killall -9 gftl
rm -rf /root/boot/data
mkdir -p /root/boot/data
cp /root/boot/nodekey /root/boot/data/nodekey
cd /root/boot

nohup ./gftl --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port 30304 --pprof --pprofport 6060 --verbosity 3 --metrics > test.log 2>&1 &
cd /root/run

sleep 4
bash startPacker.sh
sleep 3
bash startTx.sh
sleep 3

cd /root/boot
time python test.py exec -c "cd /root/run && bash startNode.sh"

