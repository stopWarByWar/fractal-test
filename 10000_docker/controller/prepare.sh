#!/bin/sh
time python test.py exec -c 'rm -rf /root/run'
time python test.py exec -c 'mkdir /root/run'

time python test.py exec -c 'bash clean.sh'
time python test.py exec -c 'systemctl restart docker'
time python test.py change_hostname
time python test.py set_NodeId
time python test.py upload -f ./gftl
time python test.py upload -f ./txgen
time python test.py upload -f ./test.toml
time python test.py upload -f ./startNode.sh
time python test.py upload -f ./generateAccount.sh
time python test.py upload -f ./startPacker.sh
time python test.py upload -f ./startTx.sh

time python test.py exec -c 'bash set_hostname.sh'
time python test.py exec -c 'bash copy_all.sh'
time python test.py exec -c 'bash generate_accout.sh'

time python generateAlloc.py

time python test.py upload -f ./genesis_alloc.json
time python test.py exec -c 'bash copy.sh genesis_alloc.json'





