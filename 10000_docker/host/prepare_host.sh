#!/bin/sh

bash clean.sh
systemctl restart docker
ifconfig down docker0

cd /root/run && tar -zxvf prepare.tar.gz
cd /root

bash set_hostname.sh
bash copy_all.sh
bash generate_accout.sh

