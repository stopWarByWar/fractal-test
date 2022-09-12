killall -9 gftl
rm -rf ./data/chaindata
rm -rf ./data/nodes

sleep 2
nohup ./gftl --identity packer --pack --mine --unlock 123  --config test.toml --genesisAlloc genesis_alloc.json --rpc --rpcport 8545 --datadir data --port 40505 --pprof --pprofport 6060 --verbosity 3 --nat none > packer.log 2>&1 &

sleep 2
killall -9 txgen
bash startTx.sh
 
sleep 2
bash start2.sh
