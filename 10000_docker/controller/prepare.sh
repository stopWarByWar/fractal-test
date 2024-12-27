#!/bin/sh
time python3 test.py exec -c 'rm -rf /data/run'
time python3 test.py exec -c 'mkdir -p /data/run'

time python3 test.py upload1 -f ./host/clean.sh
time python3 test.py upload1 -f ./host/copy_all.sh
time python3 test.py upload1 -f ./host/copy.sh
time python3 test.py upload1 -f ./host/daemon.json
time python3 test.py upload1 -f ./host/generate_accout.sh
time python3 test.py upload1 -f ./host/prepare_host.sh
time python3 test.py upload1 -f ./host/restart_docker_gftl.sh
time python3 test.py upload1 -f ./host/run_docker.sh
time python3 test.py upload1 -f ./host/set_docker_hostname.sh
time python3 test.py upload1 -f ./host/set_hostname.sh
time python3 test.py upload1 -f ./host/set_sshd.sh
time python3 test.py upload1 -f ./host/start_docker_node.sh

time python3 test.py exec -c 'bash /data/clean.sh'
time python3 test.py exec -c 'systemctl restart docker'
time python3 test.py change_hostname
time python3 test.py set_NodeId
time python3 test.py upload -f ./gftl
time python3 test.py upload -f ./txgen
time python3 test.py upload -f ./test.toml
time python3 test.py upload -f ./startNode.sh
time python3 test.py upload -f ./generateAccount.sh
time python3 test.py upload -f ./startPacker.sh
time python3 test.py upload -f ./startTx.sh

time python3 test.py exec -c 'bash /data/set_hostname.sh'
time python3 test.py exec -c 'bash /data/copy_all.sh'
time python3 test.py exec -c 'bash /data/generate_accout.sh'

time python3 generateAlloc.py

time python3 test.py upload -f ./genesis_alloc.json
time python3 test.py exec -c 'bash /data/copy.sh genesis_alloc.json'





