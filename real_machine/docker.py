
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
    print "%s [start|stop|delete|upload|exec|tc|collect] -n count -m multiple -f file -c cmd -s start -l limit" % sys.argv[0]

def get_ip(index, nserver):
    nserver_high = nserver / 10
    nserver_low = nserver % 10
    return "172.16.%d.%d%d" % (nserver_high, nserver_low, index)

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

def start_docker_on_server(index, nserver):
    ip = get_ip(index, nserver)
    print "start docker %s:%d: %s" % (servers[nserver], index, ip)
    (status, output) = commands.getstatusoutput("ssh %s docker run -itd --net=none -v /root/docker_run/%s:/root/run centos:7.5.1804.v5 bash" % (servers[nserver], ip))
    if status == 0:
        docker_id = output
        (status, output) = commands.getstatusoutput("ssh %s pipework br0 %s %s/16" % (servers[nserver], docker_id, ip))
        if status == 0:
            print "start docker %s:%d: %s ok: %s" % (servers[nserver], index, ip, docker_id)
        else:
            print "start docker %s:%d: %s failed: %d:%s" % (servers[nserver], index, ip, status, output)
            os.system("ssh %s docker kill %s" % (servers[nserver], docker_id))
    else:
        print "start docker %s:%d: %s failed: %d:%s" % (servers[nserver], index, ip, status, output)

def start_docker(count, nprocess):
    remote_ssh_parallel("rm -rf /root/docker_run")

    p = Pool(len(servers) * nprocess)
    count_per_server = count / len(servers)
    for i in range(0, count_per_server):
        for nserver in range(0, len(servers)):
            p.apply_async(start_docker_on_server, args = (i, nserver, ))
    p.close()
    p.join()

def upload_file_to_docker(file, nserver, ndocker):
    ip = get_ip(ndocker, nserver)
    command = "ssh %s cp /root/docker_run/%s /root/docker_run/%s/" % (servers[nserver], file, ip)
    print command
    commands.getstatusoutput(command)

def upload_file(file, count, nprocess):
    remote_scp_parallel(file, "/root/docker_run")

    p = Pool(len(servers) * nprocess)
    count_per_server = count / len(servers)
    for j in range(0, count_per_server):
        for i in range(0, len(servers)):
            p.apply_async(upload_file_to_docker, args = (file, i, j, ))
    p.close()
    p.join()

def collect():
    for i in range(1, len(servers)):
        os.system("scp -r %s:/root/docker_run/* /root/docker_run/" % servers[i])

def exec_cmd_on_docker(cmd, nserver, docker_id, daemon):
    if daemon:
        command = "ssh %s \"docker exec -itd %s /bin/bash -c '%s'\"" % (servers[nserver], docker_id, cmd)
    else:
        command = "ssh %s \"docker exec %s /bin/bash -c '%s'\"" % (servers[nserver], docker_id, cmd)
    print command
    (status, output) = commands.getstatusoutput(command)
    print output

def exec_cmd(cmd, nprocess, daemon, start, limit):
    docker_ids = []
    count_per_server = 0
    for i in range(0, len(servers)):
        docker_id_list = get_running_docker_id_list_on_server(i)
        if limit > 0:
            docker_id_list = docker_id_list[start:limit]
        docker_ids.append(docker_id_list)
        count_per_server = max(len(docker_id_list), 0)

    p = Pool(len(servers) * nprocess)
    for j in range(0, count_per_server):
        for i in range(0, len(servers)):
            p.apply_async(exec_cmd_on_docker, args = (cmd, i, docker_ids[i][j], daemon ))
    p.close()
    p.join()

def exec_tc_on_docker(tc, nserver, docker_id):
    command = "ssh %s \"pipework tc %s %s\"" % (servers[nserver], docker_id, tc)
    print command
    (status, output) = commands.getstatusoutput(command)
    print output

def exec_tc(tc, nprocess, start, limit):
    docker_ids = []
    count_per_server = 0
    for i in range(0, len(servers)):
        docker_id_list = get_running_docker_id_list_on_server(i)
        if limit > 0:
            docker_id_list = docker_id_list[start:limit]
        docker_ids.append(docker_id_list)
        count_per_server = max(len(docker_id_list), 0)

    p = Pool(len(servers) * nprocess)
    for j in range(0, count_per_server):
        for i in range(0, len(servers)):
            p.apply_async(exec_tc_on_docker, args = (tc, i, docker_ids[i][j], ))
    p.close()
    p.join()

def delete_docker_on_server(nserver):
    docker_id_list = get_all_docker_id_list_on_server(nserver)
    if len(docker_id_list) <= 0:
        return

    str = " ".join(docker_id_list)
    print "delete docker on server %d: %s" % (nserver, str)
    cmd = "ssh %s \"echo '%s' | xargs docker rm\"" % (servers[nserver], str)
    os.system(cmd)

def delete_docker():
    p = Pool(len(servers))
    for i in range(0, len(servers)):
        p.apply_async(delete_docker_on_server, args = (i, ))
    p.close()
    p.join()

def stop_docker_on_server(nserver):
    docker_id_list = get_running_docker_id_list_on_server(nserver)
    if len(docker_id_list) <= 0:
        return

    str = " ".join(docker_id_list)
    print "stoping docker on server %d: %s" % (nserver, str)
    cmd = "ssh %s \"echo '%s' | xargs docker kill\"" % (servers[nserver], str)
    os.system(cmd)

def stop_docker():
    p = Pool(len(servers))
    for i in range(0, len(servers)):
        p.apply_async(stop_docker_on_server, args = (i, ))
    p.close()
    p.join()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1]

    try:
        opts, args = getopt.getopt(sys.argv[2:], "hdn:m:f:c:s:l:t:")
    except getopt.GetoptError:
        print_help()
        sys.exit(1)

    count = 10
    start = -1
    limit = -1
    multi = 1
    file = ""
    cmd = ""
    tccmd = ""
    daemon = False
    for cmd, arg in opts:
        if cmd in ("-h"):
            print_help()
            sys.exit(0)
        elif cmd in ("-d"):
            daemon = True
        elif cmd in ("-n"):
            count = int(arg)
        elif cmd in ("-s"):
            start = int(arg)
        elif cmd in ("-l"):
            limit = int(arg)
        elif cmd in ("-m"):
            multi = int(arg)
        elif cmd in ("-f"):
            file = arg
        elif cmd in ("-c"):
            cmd = arg
        elif cmd in ("-t"):
            tccmd = arg

    if command == "start":
        start_docker(count, multi)    
    elif command == "stop":
        stop_docker()
    elif command == "delete":
        delete_docker()    
    elif command == "collect":
        collect()    
    elif command == "upload":
        if file == "":
            print_help()
        else:
            upload_file(file, count, multi)
    elif command == "exec":
        if cmd == "":
            print_help()
        else:
            exec_cmd(cmd, multi, daemon, start, limit)
    elif command == "tc":
        if cmd == "":
            print_help()
        else:
            exec_tc(tccmd, multi, start, limit)
    else:
        print "unknown command %s" % command
        print_help()

