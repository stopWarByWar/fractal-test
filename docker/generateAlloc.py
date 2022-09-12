import commands
import json
import random

servers = [
    "47.100.204.80",
    "47.100.245.35",
    "47.102.200.2"
]

def get_addr_list():
    addrs = []
    for s in servers:
        (status, output) = commands.getstatusoutput("ssh %s 'find /root/run/ -name addr | xargs cat'" % s)
        addrs.extend(output.split("\n"))
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

def generate_count(count):
    v = {}

    for i in range(0,count):
        addr = ''
        for i in range (0,40):
            addr = addr + random.sample('123456789abcdef', 1)[0]
        key = "0x" + addr
        v[key] = {"balance": 500000000000000}

    str = json.dumps(v, indent=4)
    f = open("genesis_alloc.json", "w")
    f.write(str)
    f.close()


if __name__ == "__main__":
#    addrs = get_addr_list()
#    generate_alloc_json(addrs)
    generate_count(500)
