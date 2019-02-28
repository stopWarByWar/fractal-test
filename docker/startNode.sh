#!/bin/sh

nohup ./gftl --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port 30303 --pprof --pprofaddr 0.0.0.0 --pprofport 6060 --verbosity 3 --metrics --influxdburl http://172.16.100.100:8086 --influxdbdatabase metrics --influxdbusername admin --influxdbpassword 123456 --mine --bootnodes enode://5447f2d9e134ff8c2db3dcce772878181b584715a66ba022edcd246e9749d374c46529453908d4ec8ae82bb3b0d70dda5b6d99b4f3dd2ef46f4e5f1c6d75e598@172.16.100.100:30303 > /root/run/test.log 2>&1 

