#!bin/sh

for((i=0;i<=25;i++));
do
rm -rf docker_run/${i}/*
done

rm -rf run/*