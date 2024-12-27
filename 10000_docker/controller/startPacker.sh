#!/bin/sh

NodeId=$(cat /root/run/NodeId)

if [ ${IP:0:6} == "172.16" ];then
exit 0
fi

delay=$(($RANDOM%2000))
Delay=$(echo "scale=3; $delay / 1000  "|bc -l)
sleep ${Delay}

killall -9 gftl
rm -rf /data/run/packer_data/chaindata

flag=$[(${NodeId}%${1})]
if [ ${flag} -eq 0 ];then
nohup ./gftl --identity $(hostname) --unlock 123 --pack --metrics --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir ./packer_data --port 30403 --verbosity 3 --metrics --bootnodes enode://81612a70a65cc7eaba00382fab55693e0d0988765b3e0757e6239fd9bdf8798bdd34bf565c703d4cc57aae0d331f9ed96db89809d3e7ae70e3071bc3ecdddf2a@172.17.129.221:30503 > ./test.log 2>&1 &
fi

