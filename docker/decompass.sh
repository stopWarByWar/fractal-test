#!/bin/sh

for dir in $(ls ./log/)
do
  echo log/${dir}/node.log.gz
  gzip -d log/${dir}/node.log.gz
done
