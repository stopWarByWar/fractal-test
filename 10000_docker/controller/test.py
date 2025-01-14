
import getopt
import sys
import commands
import os
from multiprocessing import Pool

servers = [
    "106.75.236.201",
    "113.31.111.250",
    "106.75.252.79",
    "106.75.227.197",
    "106.75.250.95",
    "106.75.247.225",
    "113.31.112.15",
    "106.75.246.201",
    "113.31.113.19",
    "106.75.213.34",
]

def print_help():
    print "%s [upload|exec|download|change_hostname] -f file -c cmd -l local_dir" % sys.argv[0]

def remote_ssh(nserver, cmd):
    print "run cmd:%s: %s" % (servers[nserver], cmd)
    (status, output) = commands.getstatusoutput("ssh %s \"%s\"" % (servers[nserver], cmd))
    print "cmd output:%s: %d, %s" % (servers[nserver], status, output)

def remote_ssh_parallel(cmd):
    p = Pool(500)
    for nserver in range(0, len(servers)):
        p.apply_async(remote_ssh, args = (nserver, cmd, ))
    p.close()
    p.join()

def remote_scp(nserver, local_file, remote_dir):
    print "run scp:%s: %s -> %s" % (servers[nserver], local_file, remote_dir)
    (status, output) = commands.getstatusoutput("scp %s root@%s:%s" % (local_file, servers[nserver], remote_dir))
    print "scp output:%s: %d, %s" % (servers[nserver], status, output)

def remote_scp_parallel(local_file, remote_dir):
    p = Pool(500)
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
    p = Pool(500)
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

def get_running_docker_id_list_on_server(nserver):
    ret = []
    print "get running docker list on server %s" % (servers[nserver])
    (status, output) = commands.getstatusoutput("ssh %s docker ps -q" % servers[nserver])
    docker_id_list = output.split("\n")
    for docker_id in docker_id_list:
        docker_id = docker_id.strip()
        if docker_id == "":
            continue
        ret.append(docker_id)
    return ret

def get_all_docker_id_list_on_server(nserver):
    ret = []
    print "get all docker list on server %s" % (servers[nserver])
    (status, output) = commands.getstatusoutput("ssh %s docker ps -a -q" % servers[nserver])
    docker_id_list = output.split("\n")
    for docker_id in docker_id_list:
        docker_id = docker_id.strip()
        if docker_id == "":
            continue
        ret.append(docker_id)
    return ret

def exec_cmd_on_docker(cmd, nserver, docker_id, daemon):
    if daemon:
        command = "ssh %s \"docker exec -itd %s /bin/bash -c '%s'\"" % (servers[nserver], docker_id, cmd)
    else:
        command = "ssh %s \"docker exec %s /bin/bash -c '%s'\"" % (servers[nserver], docker_id, cmd)
    print command
    commands.getstatusoutput(command)

def exec_cmd(cmd):
    docker_ids = []
    count_per_server = 0
    for i in range(0, len(servers)):
        docker_id_list = get_running_docker_id_list_on_server(i)
        docker_ids.append(docker_id_list)
        count_per_server = max(len(docker_id_list), 0)
    print "count_per_server: ", count_per_server

    #p = Pool(len(servers) * count_per_server)
    p = Pool(500)
    for j in range(0, count_per_server):
        for i in range(0, len(servers)):
            p.apply_async(exec_cmd_on_docker, args = (cmd, i, docker_ids[i][j], False ))
    p.close()
    p.join()

def exec_tc_on_docker(tc, nserver, docker_id):
    command = "ssh %s \"pipework tc %s %s\"" % (servers[nserver], docker_id, tc)
    print command
    (status, output) = commands.getstatusoutput(command)
    print output

def exec_tc(tc):
    docker_ids = []
    count_per_server = 0
    for i in range(0, len(servers)):
        docker_id_list = get_running_docker_id_list_on_server(i)
        docker_ids.append(docker_id_list)
        count_per_server = max(len(docker_id_list), 0)

    p = Pool(500)
    for j in range(0, count_per_server):
        for i in range(0, len(servers)):
            p.apply_async(exec_tc_on_docker, args = (tc, i, docker_ids[i][j], ))
    p.close()
    p.join()

def set_NodeId(nserver):
    print "run set %s NodeId" % (servers[nserver])
    cmd = "echo %d > /data/run/NodeId" % nserver
    (status, output) = commands.getstatusoutput("ssh %s \"%s\"" % (servers[nserver], cmd))
    print "cmd output:%s: %d, %s" % (servers[nserver], status, output)

def set_NodeId_parallel():
    p = Pool(500)
    for nserver in range(0, len(servers)):
        p.apply_async(set_NodeId, args = (nserver, ))
    p.close()
    p.join()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    try:
        opts, args = getopt.getopt(sys.argv[2:], "hd:f:c:l:t:m:")
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
        elif cmd in ("-t"):
            tccmd = arg
        elif cmd in ("-m"):
            multi = int(arg)

    if command == "upload":
        if file == "":
            print_help()
        else:
            remote_scp_parallel(file, "/data/run")
    elif command == "upload1":
        if file == "":
            print_help()
        else:
            remote_scp_parallel(file, "/data")
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
    elif command == "tc":
        if cmd == "":
            print_help()
        else:
            exec_tc(tccmd)
    elif command == "docker":
        if cmd == "":
            print_help()
        else:
            exec_cmd(cmd)
    elif command == "set_NodeId":
        set_NodeId_parallel()
    else:
        print "unknown command %s" % command
        print_help()

