#!/bin/sh

mkdir -p /root/run/packer/data

./gftl --password pwd.txt --datadir packer/data/ account new
 
nohup ./gftl --config test.toml --unlock 123 --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir packer/data --port 30305 --pprof --pprofport 6060 --verbosity 3 --pack --bootnodes enode://81612a70a65cc7eaba00382fab55693e0d0988765b3e0757e6239fd9bdf8798bdd34bf565c703d4cc57aae0d331f9ed96db89809d3e7ae70e3071bc3ecdddf2a@172.16.100.100:30303 > /root/run/packer.log 2>&1 &

