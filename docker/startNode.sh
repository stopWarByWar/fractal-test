#!/bin/sh

IP=$(hostname)

nohup ./gftl --identity ${IP} --unlock 123 --config test.toml --metrics --influxdburl http://129.28.54.225:8086 --influxdbdatabase metrics --influxdbusername fractal --influxdbpassword fractal666 --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port 30303 --pprof --pprofaddr 0.0.0.0 --pprofport 6060 --verbosity 3 --mine --bootnodes enode://5447f2d9e134ff8c2db3dcce772878181b584715a66ba022edcd246e9749d374c46529453908d4ec8ae82bb3b0d70dda5b6d99b4f3dd2ef46f4e5f1c6d75e598@210.22.171.162:30303  > /root/run/node.log 2>&1 &

