
import getopt
import sys
import commands
import os
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

def print_help():
    print "%s [upload|exec|download|change_hostname] -f file -c cmd -l local_dir" % sys.argv[0]

def remote_ssh(nserver, cmd):
    print "run cmd:%s: %s" % (servers[nserver], cmd)
    (status, output) = commands.getstatusoutput("ssh %s \"%s\"" % (servers[nserver], cmd))
    print "cmd output:%s: %d, %s" % (servers[nserver], status, output)

def remote_ssh_parallel(cmd):
    p = Pool(len(servers))
    for nserver in range(0, len(servers)):
        p.apply_async(remote_ssh, args = (nserver, cmd, ))
    p.close()
    p.join()

def remote_scp(nserver, local_file, remote_dir):
    print "run scp:%s: %s -> %s" % (servers[nserver], local_file, remote_dir)
    (status, output) = commands.getstatusoutput("scp %s root@%s:%s" % (local_file, servers[nserver], remote_dir))
    print "scp output:%s: %d, %s" % (servers[nserver], status, output)

def remote_scp_parallel(local_file, remote_dir):
    p = Pool(len(servers))
    for nserver in range(0, len(servers)):
        p.apply_async(remote_scp, args = (nserver, local_file, remote_dir, ))
    p.close()
    p.join()


def reverse_scp(nserver, remote_file,local_dir):
    print "run reverse scp:%s:%s -> %s/%s" % (servers[nserver], remote_file, local_dir,servers[nserver])
    (status, output) = commands.getstatusoutput("scp -r root@%s:%s %s/%s" % (servers[nserver],remote_file,local_dir,servers[nserver]))
    print "scp output:%s: %d, %s" % (servers[nserver], status, output)


def reverse_scp_parallel(remote_file,local_dir):
    commands.getstatusoutput("rm -rf %s" % local_dir)
    p = Pool(len(servers))
    for nserver in range(0, len(servers)):
        p.apply_async(reverse_scp, args = (nserver, remote_file,local_dir,))
        commands.getstatusoutput("mkdir -p %s/%s" % (local_dir,servers[nserver]))
    p.close()
    p.join()

def change_hostname():
    for i in range(0,len(servers)):
        cmd = "ssh %s hostnamectl set-hostname %s" % (servers[i],servers[i])
        print "run cmd:%s: %s" % (servers[i], cmd)
        (status, output) = commands.getstatusoutput(cmd)
        print "scp output:%s: %d, %s" % (servers[i], status, output)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    try:
        opts, args = getopt.getopt(sys.argv[2:], "hd:f:c:l:")
    except getopt.GetoptError:
        print_help()
        sys.exit(1)

    file = ""
    cmd = ""
    dir = ""
    daemon = False
    for cmd, arg in opts:
        if cmd in ("-h"):
            print_help()
            sys.exit(0)
        elif cmd in ("-d"):
            daemon = True
        elif cmd in ("-f"):
            file = arg
        elif cmd in ("-c"):
            cmd = arg
        elif cmd in ("-l"):
            dir = arg

    if command == "upload":
        if file == "":
            print_help()
        else:
            remote_scp_parallel(file, "/root/run")
    elif command == "exec":
        if cmd == "":
            print_help()
        else:
            remote_ssh_parallel(cmd)
    elif command == "download":
        if file =="" or dir == "":
            print_help()
        else:
            reverse_scp_parallel(file,dir)
    elif command == "change_hostname":
        change_hostname()
    else:
        print "unknown command %s" % command
        print_help()

