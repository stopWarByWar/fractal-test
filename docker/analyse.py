# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from datetime import datetime

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

count = {0:0}
global total
global maximum
global txpkg
txpkg = 0
total = 0
maximum = 0

def analyze(grading,stime,etime):
    for dir in servers:
        file = './log/%s/node.log' % dir
        print "open the log of %s" % file
        with open(file, 'r') as f:
            line = f.readline()
            while line:
                clean_the_line(line,grading,stime,etime)
                line = f.readline()
    print "total: %d" % total

def clean_the_line(line,grading,stime,etime):

    if "Insert" in line :
        time = line.split(' ')[0].split('=')[1]
        Datetime = transform_string_to_time(time)
        print line
        if clean_time(stime,etime,Datetime):
            counte_dely(line,grading)

def counte_dely(line,grading):
    global maximum
    data_array = line.split(' ')
    duration = data_array[8].split('=')[1]
    pkgCount = int(data_array[-1].split('=')[1])
    if "µ" in duration:
        dur = 0
    elif 'm' in duration:
        dur = int(float(duration[:-2])) * 1000
    else:
        dur = float(duration[:-1]) * 1000000

    elapse = float(data_array[9].split("=")[1])

    if elapse > 6000:
        return
    elapse = elapse * 1000000

    delay = int((elapse - dur)/grading)

    print delay
    if delay > maximum:
        maximum = delay

    if delay < 0:
        count[0] = count[0] + 1
    elif count.has_key(delay):
       count[delay] = count[delay] + 1
    else:
        count[delay]=1

    global total
    total = total + 1
    global txpkg
    txpkg = txpkg + pkgCount

def clean_time(stime,etime,time):
    if stime < time and etime > time:
        print "The time is %s" % time
        return True
    else:
        return False

def transform_string_to_time(time):
    date = time.replace('T',' ').replace('+0800','')
    Datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return Datetime

def count_percentage(i):
    current = 0.0
    for k in count:
        if k <= i :
            current = current + count[k]
    return (current / total) * 100

def count_accout():
    a = 0
    file = './tx.log'
    print "open the log of %s" % file
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            if "Addr" in line:
                a = a + 1
            line = f.readline()
    print "The num of accounts is %d" % a

if __name__ == "__main__":
    stime = datetime.strptime("2019-03-14 21:00:23", "%Y-%m-%d %H:%M:%S")
    etime = datetime.strptime("2019-03-16 21:00:25", "%Y-%m-%d %H:%M:%S")
    current = 0.0
    percentage = {0: 0.0}
    analyze(1000000, stime, etime)
    print count

    print "the average of pkgCount is %f" % float(txpkg / total)

    perx98 = 0
    perx95 = 0
    perx80 = 0
    pery98 = 0.0
    pery95 = 0.0
    pery80 = 0.0

    x = []
    y = []
    y1 = []

    for i in count:
        percentage[i] = count_percentage(i)

        if percentage[i] >= 80 and pery80 == 0:
            pery80 = percentage[i]
            perx80 = i

        elif percentage[i] >= 95 and pery95 == 0:
            pery95 = percentage[i]
            perx95 = i

        elif percentage[i] >= 98 and pery98 == 0:
            pery98 = percentage[i]
            perx98 = i

        x.append(i)
        y.append(percentage[i])
        y1.append(90)
        print "%d,%f" % (i, percentage[i])

    plt.title("network delay", fontproperties='SimHei')
    plt.ylim((0, 110))
    plt.xlim((0, 10))
    plt.xlabel(u'delay time/s', fontproperties='SimHei', fontsize=14)
    plt.ylabel(u'percentage  %', fontproperties='SimHei', fontsize=14)

    plt.scatter(perx80, pery80, color='blue')
    plt.scatter(perx95, pery95, color='blue')
    plt.scatter(perx98, pery98, color='blue')
    plt.plot([perx80, perx80], [pery80, 0], 'k--', color="blue", lw=1)
    plt.plot([perx95, perx95], [pery95, 0], 'k--', color="blue", lw=1)
    plt.plot([perx98, perx98], [pery98, 0], 'k--', color="blue", lw=1)

    plt.plot(x, y, color='red')
    #    plt.plot(x,y1,color='blue')
    plt.text(3, 30, r'98% : ' + str(perx98), fontdict={'size': 14, 'color': 'blue'})
    plt.text(3, 20, r'95% : ' + str(perx95), fontdict={'size': 14, 'color': 'blue'})
    plt.text(3, 10, r'80% : ' + str(perx80), fontdict={'size': 14, 'color': 'blue'})
    plt.show()