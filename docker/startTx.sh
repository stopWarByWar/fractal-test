#!/bin/sh

nohup ./txgen --tps 6000 --nprocess 10 --batch 10 --rpc http://127.0.0.1:8545 --from $(cat addr) --to $(cat addr) --verbosity 3 > /home/tx.log 2>&1 &

