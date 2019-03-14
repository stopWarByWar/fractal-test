import commands
import json

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
    "47.104.78.207",
    "10.1.1.50"
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

