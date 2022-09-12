# -*- coding: utf-8 -*-

from datetime import datetime

def transform_string_to_time(time):
    date = time.replace('T',' ').replace('+0800','')
    print "the string is %s" % date
    Datetime = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    return Datetime

def clean_time(stime,etime,time):
    if stime < time and etime > time:
        return True
    else:
        return False

def clean_the_line(line,stime,etime):
    time = line.split(' ')[0].split('=')[1]
    Datetime = transform_string_to_time(time)
    if clean_time(stime,etime,Datetime):
        print str
    else:
        print "no in interupt"

if __name__ == '__main__':

    for i in range(0, int(maximum)):
        if count.has_key(i):
            current = current + count[i]
        percentage[i] = (current / total) * 100
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