rm -rf data2/chaindata
rm -rf data2/nodes

nohup ./gftl --identity node  --bootnodes enode://ac5675c3ffd17ecfed81895d3daabba10438fa2b67fad3bb1134d7d505a469d3b20fc14b3e67edc4f0cb67a07f89bbf16960ebc6d6999c889ee0061a05fb8bd7@127.0.0.1:40505 --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8645 --datadir data2 --port 40314 --pprof --pprofport 7066 --verbosity 3 > node2.log 2>&1 &
 

