
import getopt
import sys
import commands
import os
from multiprocessing import Pool

servers = [
    "10.1.1.50",
    "10.1.1.51",
    "10.1.1.52",
    "10.1.1.53",
    "10.1.1.54"
]

def print_help():
    print "%s [upload|exec] -f file -c cmd" % sys.argv[0]

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


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    try:
        opts, args = getopt.getopt(sys.argv[2:], "hd:f:c:")
    except getopt.GetoptError:
        print_help()
        sys.exit(1)

    file = ""
    cmd = ""
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
    else:
        print "unknown command %s" % command
        print_help()

