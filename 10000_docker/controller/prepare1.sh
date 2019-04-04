#! /bin/sh

tar -czf  prepare.tar.gz ./gftl ./txgen ./test.toml ./startNode.sh ./generateAccount.sh ./startPacker.sh ./startTx.sh

time python test.py upload -f ./prepare.tar.gz
time python test.py change_hostname
time python test.py set_NodeId

time python test.py exec -c 'bash prepare_host.sh'

sleep 5

time python generateAlloc.py
time python test.py upload -f ./genesis_alloc.json