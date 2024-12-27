#!/bin/sh

#time python test.py upload -f ./gftl
#time python test.py exec -c 'bash copy.sh gftl'
time python test.py upload -f ./test.toml
time python test.py exec -c 'bash /data/copy.sh test.toml'


time python test.py exec -c 'cd /data && bash run_docker.sh 100'

#time python test.py docker -c 'cat /root/docker_run/No | xargs hostname'
#time python test.py tc -t 'qdisc add dev eth0 root handle 1:0 netem delay 50ms'
#time python test.py tc -t 'qdisc add dev eth0 parent 1:1 handle 10: tbf rate 20Mbit buffer 12800 limit 24000'
#time python test.py exec -c "bash /data/set_docker_hostname.sh"

killall -9 gftl
rm -rf data/chaindata
nohup ./gftl --unlock 123 --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir ./data --port 30503 --pprof --pprofport 6060 --verbosity 3 > ./node.log 2>&1 &

time python test.py exec -c 'cd /data/run && bash startPacker.sh 10'
sleep 3

#time python test.py docker -c 'cd /root/docker_run && bash startNode.sh'
time python test.py exec -c "cd /data && bash start_docker_node.sh"

time python test.py exec -c 'cd /data/run && bash startTx.sh'

#time python test.py docker -c 'killall -9 gftl'
#time python test.py docker -c 'rm -rf /root/docker_run/data/chaindata'
#time python test.py exec -c 'docker rm -f $(docker ps -aq)'
