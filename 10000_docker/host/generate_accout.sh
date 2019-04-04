#!bin/sh

rm /root/account

cd /root/run
rm -rf /root/run/data/

bash generateAccount.sh
echo $(cat /root/run/addr) >> /root/account

for((i=1;i<=25;i++));
do
cd /root/docker_run/${i}
rm -rf ./data
bash generateAccount.sh
echo $(cat /root/docker_run/${i}/addr) >> /root/account
done