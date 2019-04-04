#!/bin/sh

rm -rf data/chaindata
nohup ./gftl --nat extip:HOSTNAME --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port PORT --pprof --pprofaddr 0.0.0.0 --pprofport 6060 --verbosity 3 --mine --bootnodes enode://81612a70a65cc7eaba00382fab55693e0d0988765b3e0757e6239fd9bdf8798bdd34bf565c703d4cc57aae0d331f9ed96db89809d3e7ae70e3071bc3ecdddf2a@172.17.129.221:30503 --unlock 123 > /root/docker_run/node.log 2>&1 &

