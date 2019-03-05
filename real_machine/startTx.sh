#!/bin/sh

nohup ./txgen --tps 100 --nprocess 10 --batch 10 --rpc http://127.0.0.1:8545 --from $(cat addr) --to $(cat addr) --verbosity 3 > /root/run/tx.log 2>&1 &

