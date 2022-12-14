
import getopt
import sys
import commands
import os
from multiprocessing import Pool

servers = [
"172.16.34.119",
"172.16.34.146",
"172.16.34.129",
"172.16.34.145",
"172.16.34.134",
"172.16.34.107",
"172.16.34.130",
"172.16.34.109",
"172.16.34.132",
"172.16.34.112",
"172.16.34.125",
"172.16.34.144",
"172.16.34.104",
"172.16.34.137",
"172.16.34.148",
"172.16.34.108",
"172.16.34.123",
"172.16.34.113",
"172.16.34.118",
"172.16.34.105",
"172.16.34.124",
"172.16.34.120",
"172.16.34.140",
"172.16.34.136",
"172.16.34.106",
"172.16.34.143",
"172.16.34.138",
"172.16.34.131",
"172.16.34.114",
"172.16.34.110",
"172.16.34.117",
"172.16.34.133",
"172.16.34.121",
"172.16.34.142",
"172.16.34.116",
"172.16.34.139",
"172.16.34.115",
"172.16.34.126",
"172.16.34.127",
"172.16.34.128",
"172.16.34.141",
"172.16.34.135",
"172.16.34.122",
"172.16.34.111",
"172.16.34.147",
"172.16.34.68",
"172.16.34.102",
"172.16.34.73",
"172.16.34.96",
"172.16.34.101",
"172.16.34.97",
"172.16.34.83",
"172.16.34.63",
"172.16.34.94",
"172.16.34.64",
"172.16.34.54",
"172.16.34.84",
"172.16.34.60",
"172.16.34.55",
"172.16.34.95",
"172.16.34.98",
"172.16.34.51",
"172.16.34.82",
"172.16.34.80",
"172.16.34.74",
"172.16.34.75",
"172.16.34.91",
"172.16.34.85",
"172.16.34.100",
"172.16.34.65",
"172.16.34.70",
"172.16.34.77",
"172.16.34.89",
"172.16.34.53",
"172.16.34.78",
"172.16.34.86",
"172.16.34.72",
"172.16.34.81",
"172.16.34.62",
"172.16.34.103",
"172.16.34.92",
"172.16.34.58",
"172.16.34.49",
"172.16.34.69",
"172.16.34.93",
"172.16.34.79",
"172.16.34.59",
"172.16.34.99",
"172.16.34.66",
"172.16.34.50",
"172.16.34.61",
"172.16.34.71",
"172.16.34.90",
"172.16.34.52",
"172.16.34.88",
"172.16.34.67",
"172.16.34.57",
"172.16.34.87",
"172.16.34.76",
"172.16.34.56",
"172.16.34.40",
"172.16.34.21",
"172.16.34.15",
"172.16.34.8",
"172.16.34.19",
"172.16.34.14",
"172.16.34.33",
"172.16.34.31",
"172.16.34.25",
"172.16.34.20",
"172.16.34.43",
"172.16.34.39",
"172.16.34.30",
"172.16.34.29",
"172.16.34.37",
"172.16.34.32",
"172.16.34.45",
"172.16.34.35",
"172.16.34.10",
"172.16.34.42",
"172.16.34.41",
"172.16.34.13",
"172.16.34.46",
"172.16.34.26",
"172.16.34.47",
"172.16.34.44",
"172.16.34.36",
"172.16.34.5",
"172.16.34.24",
"172.16.34.48",
"172.16.34.22",
"172.16.34.38",
"172.16.34.6",
"172.16.34.34",
"172.16.34.11",
"172.16.34.16",
"172.16.34.18",
"172.16.34.9",
"172.16.34.12",
"172.16.34.23",
"172.16.34.27",
"172.16.34.28",
"172.16.33.246",
"172.16.34.7",
"172.16.34.17",
"172.16.34.1",
"172.16.33.227",
"172.16.34.2",
"172.16.33.213",
"172.16.33.221",
"172.16.33.247",
"172.16.33.243",
"172.16.33.250",
"172.16.34.4",
"172.16.33.220",
"172.16.33.212",
"172.16.33.245",
"172.16.33.237",
"172.16.33.210",
"172.16.33.219",
"172.16.33.224",
"172.16.33.242",
"172.16.33.205",
"172.16.33.239",
"172.16.33.249",
"172.16.33.251",
"172.16.33.238",
"172.16.33.218",
"172.16.33.252",
"172.16.33.232",
"172.16.33.244",
"172.16.33.233",
"172.16.33.216",
"172.16.33.217",
"172.16.33.253",
"172.16.33.241",
"172.16.33.254",
"172.16.33.226",
"172.16.33.248",
"172.16.33.222",
"172.16.34.0",
"172.16.33.211",
"172.16.34.3",
"172.16.33.215",
"172.16.33.255",
"172.16.33.209",
"172.16.33.223",
"172.16.33.206",
"172.16.33.240",
"172.16.33.207",
"172.16.33.235",
"172.16.33.225",
"172.16.33.234",
"172.16.33.214",
"172.16.33.230",
"172.16.33.228",
"172.16.33.208",
"172.16.33.231",
"172.16.33.229",
"172.16.33.236",
"172.16.33.200",
"172.16.33.169",
"172.16.33.186",
"172.16.33.197",
"172.16.33.173",
"172.16.33.203",
"172.16.33.190",
"172.16.33.185",
"172.16.33.181",
"172.16.33.202",
"172.16.33.191",
"172.16.33.204",
"172.16.33.175",
"172.16.33.172",
"172.16.33.176",
"172.16.33.182",
"172.16.33.194",
"172.16.33.171",
"172.16.33.184",
"172.16.33.193",
"172.16.33.198",
"172.16.33.166",
"172.16.33.177",
"172.16.33.187",
"172.16.33.195",
"172.16.33.170",
"172.16.33.188",
"172.16.33.167",
"172.16.33.180",
"172.16.33.201",
"172.16.33.179",
"172.16.33.192",
"172.16.33.165",
"172.16.33.196",
"172.16.33.183",
"172.16.33.133",
"172.16.33.174",
"172.16.33.189",
"172.16.33.199",
"172.16.33.178",
"172.16.33.123",
"172.16.33.122",
"172.16.33.124",
"172.16.33.154",
"172.16.33.149",
"172.16.33.146",
"172.16.33.151",
"172.16.33.162",
"172.16.33.153",
"172.16.33.168",
"172.16.33.164",
"172.16.33.120",
"172.16.33.159",
"172.16.33.152",
"172.16.33.125",
"172.16.33.140",
"172.16.33.161",
"172.16.33.155",
"172.16.33.118",
"172.16.33.134",
"172.16.33.143",
"172.16.33.141",
"172.16.33.130",
"172.16.33.156",
"172.16.33.131",
"172.16.33.148",
"172.16.33.147",
"172.16.33.157",
"172.16.33.132",
"172.16.33.113",
"172.16.33.158",
"172.16.33.119",
"172.16.33.136",
"172.16.33.139",
"172.16.33.150",
"172.16.33.121",
"172.16.33.137",
"172.16.33.142",
"172.16.33.135",
"172.16.33.145",
"172.16.33.163",
"172.16.33.114",
"172.16.33.112",
"172.16.33.115",
"172.16.33.144",
"172.16.33.160",
"172.16.33.109",
"172.16.33.111",
"172.16.33.108",
"172.16.33.127",
"172.16.33.117",
"172.16.33.107",
"172.16.33.110",
"172.16.33.106",
"172.16.33.105",
"172.16.33.129",
"172.16.33.128",
"172.16.33.116",
"172.16.33.126",
"172.16.33.138",
"172.16.33.91",
"172.16.33.96",
"172.16.33.95",
"172.16.33.87",
"172.16.33.100",
"172.16.33.94",
"172.16.33.72",
"172.16.33.84",
"172.16.33.103",
"172.16.33.68",
"172.16.33.67",
"172.16.33.90",
"172.16.33.81",
"172.16.33.98",
"172.16.33.102",
"172.16.33.76",
"172.16.33.93",
"172.16.33.85",
"172.16.33.83",
"172.16.33.88",
"172.16.33.75",
"172.16.33.97",
"172.16.33.80",
"172.16.33.104",
"172.16.33.77",
"172.16.33.73",
"172.16.33.101",
"172.16.33.70",
"172.16.33.92",
"172.16.33.86",
"172.16.33.89",
"172.16.33.74",
"172.16.33.71",
"172.16.33.79",
"172.16.33.78",
"172.16.33.52",
"172.16.33.69",
"172.16.33.82",
"172.16.33.50",
"172.16.33.36",
"172.16.33.99",
"172.16.33.66",
"172.16.33.16",
"172.16.33.63",
"172.16.33.60",
"172.16.33.25",
"172.16.33.13",
"172.16.33.15",
"172.16.33.12",
"172.16.33.10",
"172.16.33.28",
"172.16.33.53",
"172.16.33.20",
"172.16.33.7",
"172.16.33.11",
"172.16.33.22",
"172.16.33.31",
"172.16.33.65",
"172.16.33.55",
"172.16.33.27",
"172.16.33.23",
"172.16.33.37",
"172.16.33.54",
"172.16.33.40",
"172.16.33.64",
"172.16.33.62",
"172.16.33.59",
"172.16.33.26",
"172.16.33.30",
"172.16.33.33",
"172.16.33.61",
"172.16.33.32",
"172.16.33.51",
"172.16.33.29",
"172.16.33.49",
"172.16.33.43",
"172.16.33.14",
"172.16.33.19",
"172.16.33.56",
"172.16.33.57",
"172.16.33.58",
"172.16.33.17",
"172.16.33.45",
"172.16.33.41",
"172.16.33.24",
"172.16.33.8",
"172.16.33.48",
"172.16.33.35",
"172.16.33.9",
"172.16.33.47",
"172.16.33.21",
"172.16.33.42",
"172.16.33.18",
"172.16.33.5",
"172.16.33.39",
"172.16.33.46",
"172.16.33.44",
"172.16.33.6",
"172.16.33.34",
"172.16.33.38",
"172.17.133.189",
"172.17.133.177",
"172.17.133.187",
"172.17.133.180",
"172.17.133.184",
"172.17.133.190",
"172.17.133.185",
"172.17.133.186",
"172.17.133.188",
"172.17.133.178",
"172.17.133.183",
"172.17.133.181",
"172.17.133.179",
"172.17.133.182",
"172.17.133.148",
"172.17.133.147",
"172.17.133.166",
"172.17.133.175",
"172.17.133.176",
"172.17.133.172",
"172.17.133.155",
"172.17.133.153",
"172.17.133.156",
"172.17.133.161",
"172.17.133.149",
"172.17.133.165",
"172.17.133.164",
"172.17.133.157",
"172.17.133.160",
"172.17.133.168",
"172.17.133.173",
"172.17.133.162",
"172.17.133.170",
"172.17.133.171",
"172.17.133.152",
"172.17.133.150",
"172.17.133.163",
"172.17.133.159",
"172.17.133.158",
"172.17.133.169",
"172.17.133.174",
"172.17.133.167",
"172.17.133.108",
"172.17.133.103",
"172.17.133.114",
"172.17.133.138",
"172.17.133.151",
"172.17.133.135",
"172.17.133.139",
"172.17.133.154",
"172.17.133.124",
"172.17.133.112",
"172.17.133.100",
"172.17.133.131",
"172.17.133.140",
"172.17.133.136",
"172.17.133.134",
"172.17.133.123",
"172.17.133.146",
"172.17.133.142",
"172.17.133.137",
"172.17.133.115",
"172.17.133.145",
"172.17.133.141",
"172.17.133.132",
"172.17.133.105",
"172.17.133.110",
"172.17.133.101",
"172.17.133.125",
"172.17.133.102",
"172.17.133.130",
"172.17.133.126",
"172.17.133.127",
"172.17.133.104",
"172.17.133.109",
"172.17.133.144",
"172.17.133.111",
"172.17.133.99",
"172.17.133.107",
"172.17.133.129",
"172.17.133.98",
"172.17.133.97",
"172.17.133.118",
"172.17.133.117",
"172.17.133.116",
"172.17.133.119",
"172.17.133.120",
"172.17.133.122",
"172.17.133.121",
"172.17.133.128",
"172.17.133.106",
"172.17.133.113",
"172.17.133.133",
"172.17.133.81",
"172.17.133.79",
"172.17.133.75",
"172.17.133.96",
"172.17.133.95",
"172.17.133.89",
"172.17.133.74",
"172.17.133.88",
"172.17.133.92",
"172.17.133.83",
"172.17.133.94",
"172.17.133.72",
"172.17.133.71",
"172.17.133.45",
"172.17.133.86",
"172.17.133.93",
"172.17.133.82",
"172.17.133.87",
"172.17.133.69",
"172.17.133.55",
"172.17.133.53",
"172.17.133.73",
"172.17.133.67",
"172.17.133.64",
"172.17.133.143",
"172.17.133.63",
"172.17.133.80",
"172.17.133.90",
"172.17.133.91",
"172.17.133.50",
"172.17.133.57",
"172.17.133.85",
"172.17.133.78",
"172.17.133.84",
"172.17.133.9",
"172.17.133.66",
"172.17.133.56",
"172.17.133.65",
"172.17.133.20",
"172.17.133.70",
"172.17.133.28",
"172.17.133.15",
"172.17.133.43",
"172.17.133.16",
"172.17.133.36",
"172.17.133.11",
"172.17.133.35",
"172.17.133.68",
"172.17.133.51",
"172.17.133.3",
"172.17.133.38",
"172.17.133.17",
"172.17.133.7",
"172.17.133.76",
"172.17.133.44",
"172.17.133.77",
"172.17.133.33",
"172.17.133.32",
"172.17.133.62",
"172.17.133.21",
"172.17.133.61",
"172.17.133.27",
"172.17.133.46",
"172.17.133.4",
"172.17.133.13",
"172.17.133.5",
"172.17.133.60",
"172.17.133.54",
"172.17.133.39",
"172.17.133.40",
"172.17.133.18",
"172.17.133.26",
"172.17.132.255",
"172.17.133.58",
"172.17.133.1",
"172.17.133.24",
"172.17.133.25",
"172.17.133.41",
"172.17.133.10",
"172.17.133.48",
"172.17.133.52",
"172.17.133.47",
"172.17.133.31",
"172.17.133.59",
"172.17.133.2",
"172.17.133.30",
"172.17.133.49",
"172.17.133.19",
"172.17.133.6",
"172.17.133.34",
"172.17.133.37",
"172.17.133.12",
"172.17.133.8",
"172.17.133.0",
"172.17.132.254",
"172.17.133.23",
"172.17.133.29",
"172.17.133.14",
"172.17.133.22",
"172.17.133.42",
"172.17.132.235",
"172.17.132.238",
"172.17.132.239",
"172.17.132.231",
"172.17.132.224",
"172.17.132.242",
"172.17.132.234",
"172.17.132.226",
"172.17.132.252",
"172.17.132.250",
"172.17.132.221",
"172.17.132.215",
"172.17.132.225",
"172.17.132.245",
"172.17.132.248",
"172.17.132.220",
"172.17.132.236",
"172.17.132.219",
"172.17.132.213",
"172.17.132.243",
"172.17.132.244",
"172.17.132.237",
"172.17.132.217",
"172.17.132.227",
"172.17.132.216",
"172.17.132.247",
"172.17.132.233",
"172.17.132.218",
"172.17.132.229",
"172.17.132.223",
"172.17.132.222",
"172.17.132.240",
"172.17.132.246",
"172.17.132.232",
"172.17.132.230",
"172.17.132.241",
"172.17.132.253",
"172.17.132.228",
"172.17.132.212",
"172.17.132.251",
"172.17.132.214",
"172.17.132.204",
"172.17.132.249",
"172.17.132.186",
"172.17.132.157",
"172.17.132.174",
"172.17.132.158",
"172.17.132.202",
"172.17.132.189",
"172.17.132.173",
"172.17.132.175",
"172.17.132.209",
"172.17.132.169",
"172.17.132.200",
"172.17.132.203",
"172.17.132.156",
"172.17.132.211",
"172.17.132.172",
"172.17.132.185",
"172.17.132.160",
"172.17.132.191",
"172.17.132.197",
"172.17.132.184",
"172.17.132.206",
"172.17.132.155",
"172.17.132.179",
"172.17.132.187",
"172.17.132.196",
"172.17.132.208",
"172.17.132.195",
"172.17.132.181",
"172.17.132.192",
"172.17.132.164",
"172.17.132.167",
"172.17.132.201",
"172.17.132.207",
"172.17.132.210",
"172.17.132.165",
"172.17.132.198",
"172.17.132.205",
"172.17.132.171",
"172.17.132.194",
"172.17.132.190",
"172.17.132.188",
"172.17.132.154",
"172.17.132.166",
"172.17.132.183",
"172.17.132.168",
"172.17.132.161",
"172.17.132.193",
"172.17.132.182",
"172.17.132.199",
"172.17.132.178",
"172.17.132.163",
"172.17.132.159",
"172.17.132.176",
"172.17.132.170",
"172.17.132.180",
"172.17.132.162",
"172.17.132.177",
"172.17.132.143",
"172.17.132.142",
"172.17.132.145",
"172.17.132.153",
"172.17.132.149",
"172.17.132.118",
"172.17.132.150",
"172.17.132.117",
"172.17.132.120",
"172.17.132.123",
"172.17.132.119",
"172.17.132.144",
"172.17.132.132",
"172.17.132.116",
"172.17.132.148",
"172.17.132.131",
"172.17.132.135",
"172.17.132.133",
"172.17.132.141",
"172.17.132.139",
"172.17.132.127",
"172.17.132.129",
"172.17.132.152",
"172.17.132.126",
"172.17.132.151",
"172.17.132.115",
"172.17.132.134",
"172.17.132.140",
"172.17.132.122",
"172.17.132.146",
"172.17.132.114",
"172.17.132.138",
"172.17.132.130",
"172.17.132.137",
"172.17.132.128",
"172.17.132.125",
"172.17.132.121",
"172.17.132.124",
"172.17.132.70",
"172.17.132.147",
"172.17.132.136",
"172.17.132.56",
"172.17.132.104",
"172.17.132.71",
"172.17.132.69",
"172.17.132.72",
"172.17.132.90",
"172.17.132.109",
"172.17.132.111",
"172.17.132.91",
"172.17.132.96",
"172.17.132.62",
"172.17.132.97",
"172.17.132.103",
"172.17.132.100",
"172.17.132.89",
"172.17.132.112",
"172.17.132.101",
"172.17.132.107",
"172.17.132.55",
"172.17.132.99",
"172.17.132.86",
"172.17.132.65",
"172.17.132.93",
"172.17.132.95",
"172.17.132.88",
"172.17.132.102",
"172.17.132.64",
"172.17.132.94",
"172.17.132.92",
"172.17.132.66",
"172.17.132.105",
"172.17.132.108",
"172.17.132.110",
"172.17.132.87",
"172.17.132.68",
"172.17.132.77",
"172.17.132.98",
"172.17.132.76",
"172.17.132.82",
"172.17.132.78",
"172.17.132.80",
"172.17.132.63",
"172.17.132.59",
"172.17.132.57",
"172.17.132.84",
"172.17.132.106",
"172.17.132.113",
"172.17.132.58",
"172.17.132.54",
"172.17.132.67",
"172.17.132.74",
"172.17.132.79",
"172.17.132.85",
"172.17.132.75",
"172.17.132.61",
"172.17.132.83",
"172.17.132.81",
"172.17.132.60",
"172.17.132.73",
"172.17.132.11",
"172.17.132.21",
"172.17.132.28",
"172.17.132.18",
"172.17.132.9",
"172.17.132.53",
"172.17.132.38",
"172.17.132.52",
"172.17.132.49",
"172.17.132.48",
"172.17.132.34",
"172.17.132.26",
"172.17.132.33",
"172.17.132.17",
"172.17.132.13",
"172.17.132.25",
"172.17.132.19",
"172.17.132.20",
"172.17.132.32",
"172.17.132.16",
"172.17.132.12",
"172.17.132.14",
"172.17.132.10",
"172.17.132.30",
"172.17.132.47",
"172.17.132.44",
"172.17.132.23",
"172.17.132.31",
"172.17.132.22",
"172.17.132.42",
"172.17.132.39",
"172.17.132.37",
"172.17.132.51",
"172.17.132.40",
"172.17.132.15",
"172.17.132.41",
"172.17.132.27",
"172.17.132.45",
"172.17.132.43",
"172.17.132.46",
"172.17.132.24",
"172.17.132.36",
"172.17.132.29",
"172.17.131.237",
"172.17.132.50",
"172.17.132.7",
"172.17.131.240",
"172.17.131.243",
"172.17.131.221",
"172.17.132.35",
"172.17.131.236",
"172.17.131.247",
"172.17.131.245",
"172.17.131.239",
"172.17.131.238",
"172.17.131.241",
"172.17.132.0",
"172.17.131.223",
"172.17.131.234",
"172.17.131.255",
"172.17.132.8",
"172.17.132.3",
"172.17.131.231",
"172.17.131.253",
"172.17.131.250",
"172.17.132.6",
"172.17.131.230",
"172.17.131.229",
"172.17.131.248",
"172.17.131.232",
"172.17.131.227",
"172.17.131.225",
"172.17.132.1",
"172.17.131.219",
"172.17.131.215",
"172.17.131.252",
"172.17.131.220",
"172.17.131.251",
"172.17.131.246",
"172.17.131.218",
"172.17.131.222",
"172.17.132.4",
"172.17.131.235",
"172.17.131.244",
"172.17.131.228",
"172.17.131.217",
"172.17.131.216",
"172.17.131.233",
"172.17.131.224",
"172.17.131.249",
"172.17.131.242",
"172.17.132.2",
"172.17.131.214",
"172.17.131.211",
"172.17.131.226",
"172.17.131.212",
"172.17.131.254",
"172.17.132.5",
"172.17.131.213",
"172.17.131.210",
"172.17.131.202",
"172.17.131.174",
"172.17.131.207",
"172.17.131.196",
"172.17.131.171",
"172.17.131.194",
"172.17.131.169",
"172.17.131.193",
"172.17.131.205",
"172.17.131.192",
"172.17.131.180",
"172.17.131.208",
"172.17.131.204",
"172.17.131.184",
"172.17.131.183",
"172.17.131.199",
"172.17.131.176",
"172.17.131.182",
"172.17.131.172",
"172.17.131.191",
"172.17.131.179",
"172.17.131.209",
"172.17.131.181",
"172.17.131.187",
"172.17.131.206",
"172.17.131.200",
"172.17.131.198",
"172.17.131.177",
"172.17.131.178",
"172.17.131.201",
"172.17.131.186",
"172.17.131.175",
"172.17.131.185",
"172.17.131.188",
"172.17.131.197",
"172.17.131.189",
"172.17.131.132",
"172.17.131.160",
"172.17.131.127",
"172.17.131.195",
"172.17.131.203",
"172.17.131.139",
"172.17.131.150",
"172.17.131.148",
"172.17.131.159",
"172.17.131.190",
"172.17.131.143",
"172.17.131.122",
"172.17.131.173",
"172.17.131.131",
"172.17.131.130",
"172.17.131.165",
"172.17.131.163",
"172.17.131.151",
"172.17.131.145",
"172.17.131.158",
"172.17.131.134",
"172.17.131.125",
"172.17.131.152",
"172.17.131.128",
"172.17.131.116",
"172.17.131.140",
"172.17.131.123",
"172.17.131.124",
"172.17.131.146",
"172.17.131.157",
"172.17.131.164",
"172.17.131.142",
"172.17.131.136",
"172.17.131.162",
"172.17.131.118",
"172.17.131.133",
"172.17.131.137",
"172.17.131.120",
"172.17.131.166",
"172.17.131.168",
"172.17.131.156",
"172.17.131.149",
"172.17.131.119",
"172.17.131.144",
"172.17.131.115",
"172.17.131.126",
"172.17.131.154",
"172.17.131.114",
"172.17.131.167",
"172.17.131.147",
"172.17.131.170",
"172.17.131.161",
"172.17.131.153",
"172.17.131.129",
"172.17.131.138",
"172.17.131.117",
"172.17.131.135",
"172.17.131.155",
"172.17.131.113",
"172.17.131.141",
"172.17.131.111",
"172.17.131.112",
"172.17.131.121",
"172.17.131.110",
"172.17.131.85",
"172.17.131.102",
"172.17.131.104",
"172.17.131.99",
"172.17.131.75",
"172.17.131.107",
"172.17.131.72",
"172.17.131.80",
"172.17.131.81",
"172.17.131.93",
"172.17.131.84",
"172.17.131.91",
"172.17.131.86",
"172.17.131.88",
"172.17.131.67",
"172.17.131.103",
"172.17.131.76",
"172.17.131.89",
"172.17.131.90",
"172.17.131.87",
"172.17.131.77",
"172.17.131.97",
"172.17.131.96",
"172.17.131.82",
"172.17.131.78",
"172.17.131.70",
"172.17.131.94",
"172.17.131.95",
"172.17.131.109",
"172.17.131.68",
"172.17.131.74",
"172.17.131.92",
"172.17.131.108",
"172.17.131.71",
"172.17.131.79",
"172.17.131.106",
"172.17.131.69",
"172.17.131.83",
"172.17.131.73",
"172.17.131.19",
"172.17.131.105",
"172.17.131.35",
"172.17.131.53",
"172.17.131.18",
"172.17.131.32",
"172.17.131.31",
"172.17.131.43",
"172.17.131.20",
"172.17.131.66",
"172.17.131.63",
"172.17.131.98",
"172.17.131.50",
"172.17.131.15",
"172.17.131.58",
"172.17.131.101",
"172.17.131.59",
"172.17.131.17",
"172.17.131.51",
"172.17.131.65",
"172.17.131.57",
"172.17.131.61",
"172.17.131.100",
"172.17.131.42",
"172.17.131.16",
"172.17.131.14",
"172.17.131.39",
"172.17.131.38",
"172.17.131.41",
"172.17.131.22",
"172.17.131.27",
"172.17.131.46",
"172.17.131.54",
"172.17.131.37",
"172.17.131.60",
"172.17.131.56",
"172.17.131.49",
"172.17.131.45",
"172.17.131.64",
"172.17.131.12",
"172.17.131.36",
"172.17.131.24",
"172.17.131.28",
"172.17.131.21",
"172.17.131.55",
"172.17.131.26",
"172.17.131.13",
"172.17.131.23",
"172.17.131.33",
"172.17.131.52",
"172.17.131.40",
"172.17.131.62",
"172.17.131.30",
"172.17.131.44",
"172.17.131.10",
"172.17.131.48",
"172.17.131.25",
"172.17.131.34",
"172.17.131.11",
"172.17.130.230",
"172.17.130.241",
"172.17.130.246",
"172.17.130.242",
"172.17.130.196",
"172.17.130.193",
"172.17.130.202",
"172.17.130.228",
"172.17.131.2",
"172.17.130.250",
"172.17.130.213",
"172.17.130.248",
"172.17.130.247",
"172.17.130.218",
"172.17.130.200",
"172.17.130.189",
"172.17.130.238",
"172.17.130.215",
"172.17.130.179",
"172.17.130.185",
"172.17.130.221",
"172.17.130.191",
"172.17.130.182",
"172.17.130.216",
"172.17.130.233",
"172.17.130.192",
"172.17.130.195",
"172.17.130.194",
"172.17.130.190",
"172.17.130.178",
"172.17.130.197",
"172.17.130.224",
"172.17.130.187",
"172.17.130.203",
"172.17.130.222",
"172.17.130.223",
"172.17.130.199",
"172.17.130.225",
"172.17.130.220",
"172.17.130.186",
"172.17.130.219",
"172.17.130.183",
"172.17.130.201",
"172.17.130.180",
"172.17.130.206",
"172.17.130.176",
"172.17.130.172",
"172.17.130.217",
"172.17.130.177",
"172.17.130.184",
"172.17.130.175",
"172.17.130.205",
"172.17.130.188",
"172.17.130.227",
"172.17.130.208",
"172.17.130.210",
"172.17.130.214",
"172.17.130.226",
"172.17.130.212",
"172.17.130.174",
"172.17.130.198",
"172.17.130.173",
"172.17.130.166",
"172.17.130.170",
"172.17.130.169",
"172.17.130.181",
"172.17.130.167",
"172.17.130.209",
"172.17.130.211",
"172.17.130.204",
"172.17.130.171"
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
    cmd = "echo %d > /root/run/NodeId" % nserver
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

