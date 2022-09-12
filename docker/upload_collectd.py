
import commands
from multiprocessing import Pool

servers = [
    "117.50.66.134",
    "106.75.9.243",
    "117.50.9.140",
    "106.75.107.121",
    "106.75.10.197",
    "106.75.91.102",
    "120.132.21.127",
    "120.132.103.111",
    "120.132.30.48",
    "120.132.101.195",
    "129.204.211.174",
    "129.204.215.61",
    "129.211.133.127",
    "129.211.133.204",
    "129.211.133.193",
    "129.211.99.139",
    "129.211.96.213",
    "129.211.99.171",
    "154.8.211.72",
    "154.8.227.24",
    "39.98.224.94",
    "39.98.217.136",
    "39.98.37.34",
    "39.98.171.238",
    "47.100.204.80",
    "47.100.245.35",
    "47.102.200.2",
    "47.105.56.7",
    "47.104.88.155",
    "47.104.78.207"
]

def remote_scp(nserver, local_file, remote_dir):
    print "run scp:%s: %s -> %s" % (servers[nserver], local_file, remote_dir)
    (status, output) = commands.getstatusoutput("scp %s root@%s:%s" % (local_file, servers[nserver], remote_dir))
    print "scp output:%s: %d, %s" % (servers[nserver], status, output)


def upload_collectd_config1():
    p = Pool(len(servers))
    for nserver in range(0, len(servers)):
        cmd = "sed -i 's/hostnumber/%s/' /etc/collectd.conf" % nserver
        (status, output) = commands.getstatusoutput(cmd)
        p.apply_async(remote_scp, args = (nserver, "/etc/collectd.conf", "/etc",))
        cmd = "sed -i 's/%s/hostnumber/' /etc/collectd.conf" % nserver
        (status, output) = commands.getstatusoutput(cmd)

    p.close()
    p.join()


def upload_collectd_config():

    for nserver in range(0, len(servers)):
        cmd = "sed -i 's/hostnumber/%s/' /etc/collectd.conf" % servers[nserver]
        (status, output) = commands.getstatusoutput(cmd)

        remote_scp(nserver, "/etc/collectd.conf", "/etc",)
        cmd = "sed -i 's/%s/hostnumber/' /etc/collectd.conf" % servers[nserver]
        (status, output) = commands.getstatusoutput(cmd)


if __name__ == "__main__":
    upload_collectd_config()


