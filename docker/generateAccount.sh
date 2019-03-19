#!/bin/sh

echo -n "123" > /root/run/pwd.txt
mkdir -p /root/run/data
./gftl --password /root/run/pwd.txt --datadir /root/run/data/ account new > /root/run/account.log 2>&1
ls /root/run/data/keystore | awk -F"--" '{print $3}' | head -n 1 > /root/run/addr

