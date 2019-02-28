time python docker.py stop
time python docker.py delete
time python docker.py start -n 60 -m 5
time python docker.py upload -n 60 -m 5 -f ./gftl
time python docker.py upload -n 60 -m 5 -f ./txgen
time python docker.py upload -n 60 -m 5 -f ./test.toml
time python docker.py upload -n 60 -m 5 -f ./startNode.sh
time python docker.py upload -n 60 -m 5 -f ./startPacker.sh
time python docker.py upload -n 60 -m 5 -f ./startTx.sh
time python docker.py upload -n 60 -m 5 -f ./generateAccount.sh

time python docker.py exec -c "cd /root/run && bash generateAccount.sh"
time python generateAlloc.py
time python docker.py upload -n 60 -m 5 -f ./genesis_alloc.json

killall -9 gftl
rm -rf boot/data
mkdir -p boot/data
cp boot/nodekey boot/data/nodekey
cd boot
nohup ./gftl --config ../test.toml --genesisAlloc ../genesis_alloc.json --rpc --rpcport 8545 --datadir data --port 30303 --pprof --pprofport 6060 --verbosity 3 --metrics > test.log 2>&1 &
cd ..
sleep 1

time python docker.py exec -l 10 -s 0 -d -c "cd /root/run && bash startNode.sh"
sleep 3
time python docker.py exec -l 12 -s 10 -d -c "cd /root/run && bash startPacker.sh"
sleep 3
time python docker.py exec -l 12 -s 10 -d -c "cd /root/run && bash startTx.sh"

