import commands
import json

servers = [
    "10.1.1.50",
    "10.1.1.51",
    "10.1.1.52",
    "10.1.1.53",
    "10.1.1.54"
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

if __name__ == "__main__":
    addrs = get_addr_list()
    generate_alloc_json(addrs)

