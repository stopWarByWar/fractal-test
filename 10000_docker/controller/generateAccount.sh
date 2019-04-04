#!/bin/sh

echo -n "123" > pwd.txt
mkdir -p data
./gftl --password pwd.txt --datadir data/ account new > ./account.log 2>&1
ls data/keystore | awk -F"--" '{print $3}' | head -n 1 > ./addr

