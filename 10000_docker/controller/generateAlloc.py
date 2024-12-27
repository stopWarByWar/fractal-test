import commands
import json
from multiprocessing import Pool


servers = []

def get_addr(i):
    cmd = "ssh %s 'find /data/run/ -name addr | xargs cat'" % servers[i]
    (status, output) = commands.getstatusoutput(cmd)
    return output.split("\n")

def get_addr_list():
    p = Pool(500)
    addrs = []
    for nserver in range(0, len(servers)):
        add = p.apply_async(get_addr, args=(nserver,))
        addr=add.get()[0]
        print addr
        addrs.append(addr)
    p.close()
    p.join()
    return addrs

def generate_alloc_json(addrs):
    v = {}
    for addr in addrs:
        key = "0x" + addr
        v[key] = { "balance": 500000000000000 }

    str = json.dumps(v, indent=4)
    f = open("genesis_alloc.json", "w")
    f.write(str)
    f.close()

if __name__ == "__main__":
    file = "ip.txt"
    with open(file, "r") as f:
        contain = f.read()
        servers = contain.rstrip('\n').split('\n')
    addrs = get_addr_list()
    generate_alloc_json(addrs)

