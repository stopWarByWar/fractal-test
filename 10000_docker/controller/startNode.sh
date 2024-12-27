#!/bin/sh

rm -rf data/chaindata
nohup ./gftl --nat extip:HOSTNAME --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port PORT --verbosity 3 --mine --bootnodes enode://fdc9b748ec1d742dc93f0db180e191f84c3bf5ff7f5503d5cadaf94dedca6a7415e1c46569bc3ebe7e5dc4658a7802dcebb60e84e7bcb4a29224c0c8d571b9a7@106.75.224.16:30503 --unlock 123 > /data/docker_run/node.log 2>&1 &