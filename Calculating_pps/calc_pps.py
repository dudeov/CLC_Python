from __future__ import division
from datetime import datetime, date, time
import re
import sys

#Getting file in format of:

#alex.chuvakov@WA1T3NNETHOP01:~$ cat counter.txt 
#---(refreshed at 2017-05-15 23:14:45 UTC)---
#206.152.35.161_counter                                  0                    1
#206.152.35.91_counter                                   0                    1
#206.152.35.92_counter                                   0                    1
#206.152.35.93_counter                                   0                    1
#206.152.35.94_counter                                   0                    1
#---(refreshed at 2017-05-15 23:14:49 UTC)---
#206.152.35.161_counter                                  0                    12
#206.152.35.91_counter                                   0                    12
#206.152.35.92_counter                                   0                    12
#206.152.35.93_counter                                   0                    12
#206.152.35.94_counter                                   0                    12
#---(refreshed at 2017-05-15 23:14:56 UTC)---
#206.152.35.161_counter                                  0                    25
#206.152.35.91_counter                                   0                    25
#206.152.35.92_counter                                   0                    25
#206.152.35.93_counter                                   0                    25
#206.152.35.94_counter                                   0                    25

#and calculates PPS for every period

#Usage:
#alex.chuvakov@WA1T3NNETHOP01:~$ python calc_pps.py counter.txt 

#Where counter.txt is a name of the file. Appears here: fhand = open(sys.argv[1])


#UDP PPS to 206.152.35.92  at 2017-05-15 23:14:49: 2.75
#UDP PPS to 206.152.35.92  at 2017-05-15 23:15:18: 2.27272727273
#UDP PPS to 206.152.35.92  at 2017-05-15 23:14:56: 1.85714285714
#UDP PPS to 206.152.35.92  at 2017-05-15 23:15:07: 1.54545454545

#UDP PPS to 206.152.35.91  at 2017-05-15 23:14:49: 2.75
#UDP PPS to 206.152.35.91  at 2017-05-15 23:15:18: 2.27272727273
#UDP PPS to 206.152.35.91  at 2017-05-15 23:14:56: 1.85714285714
#UDP PPS to 206.152.35.91  at 2017-05-15 23:15:07: 1.54545454545

#...


#It show top 10 PPS that was observed for every counter

time = []
counter_161 = []
counter_91 = []
counter_92 = []
counter_93 = []
counter_94 = []

fhand = open(sys.argv[1])

#Extracting all times and counters values from the file and writing them in lists defined above

for line in fhand:
    if line.startswith('---'):
        time_temp = re.findall('20.*:[0-5][0-9]', line)
        time.extend(time_temp)
#        print(time)
    if '206.152.35.161_counter' in line:
        temp = line.split()
        counter_161.append(int(temp[2]))
#        print(counter_161)
    if '206.152.35.91_counter' in line:
        temp = line.split()
        counter_91.append(int(temp[2]))
#        print(counter_91)
    if '206.152.35.92_counter' in line:
        temp = line.split()
        counter_92.append(int(temp[2]))
#        print(counter_92)
    if '206.152.35.93_counter' in line:
        temp = line.split()
        counter_93.append(int(temp[2]))
#        print(counter_93)
    if '206.152.35.94_counter' in line:
        temp = line.split()
        counter_94.append(int(temp[2]))
#        print(counter_94)
        
fhand.close()


c_91_value = []
c_92_value = []
c_93_value = []
c_94_value = []
c_161_value = []

#Creating lists of PPSs - differences between each two values devided by time

for i in (range(len(time) - 1)):
    dt = datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S")
    dt1 = datetime.strptime(time[i+1], "%Y-%m-%d %H:%M:%S")
    delta = dt1 - dt 
    c_161_value.append((counter_161[i+1] - counter_161[i])/delta.seconds)
#    print("UDP PPS to 206.152.35.161 at %s: %s" % (time[i+1],c_161_value[i]))
    c_91_value.append((counter_91[i+1] - counter_91[i])/delta.seconds)
#    print("UDP PPS to 206.152.35.91  at %s: %s" % (time[i+1],c_91_value[i]))
    c_92_value.append((counter_92[i+1] - counter_92[i])/delta.seconds)
#    print("UDP PPS to 206.152.35.92  at %s: %s" % (time[i+1],c_92_value[i]))
    c_93_value.append((counter_93[i+1] - counter_93[i])/delta.seconds)
#    print("UDP PPS to 206.152.35.93  at %s: %s" % (time[i+1],c_93_value[i]))
    c_94_value.append((counter_94[i+1] - counter_94[i])/delta.seconds)
#    print("UDP PPS to 206.152.35.94  at %s: %s" % (time[i+1],c_94_value[i]))

c_91 = []
c_92 = []
c_93 = []
c_94 = []
c_161 = []

#Since the lists of PPS are one value shorter than the lists of counter ant time values
#We need adjust the length of the list containing the time values
time.pop(0)


#c_92 is list of tuples where first value is PPS and the second - the time when it was observed
c_92 = zip(c_92_value,time) 
#print(c_92)   
c_92.sort(reverse=True)

#Printing top 10 PPSs observed with the time it happened.
for key, val in c_92[:10]:
    print("UDP PPS to 206.152.35.92  at %s: %s" % (val, key))

c_91 = zip(c_91_value,time) 
#print(c_91)   
c_91.sort(reverse=True)
for key, val in c_91[:10]:
    print("UDP PPS to 206.152.35.91  at %s: %s" % (val, key))

c_93 = zip(c_93_value,time) 
#print(c_93)   
c_93.sort(reverse=True)
for key, val in c_93[:10]:
    print("UDP PPS to 206.152.35.93  at %s: %s" % (val, key))

c_94 = zip(c_94_value,time) 
#print(c_94)   
c_94.sort(reverse=True)
for key, val in c_94[:10]:
    print("UDP PPS to 206.152.35.94  at %s: %s" % (val, key))

c_161 = zip(c_161_value,time) 
#print(c_161)   
c_161.sort(reverse=True)
for key, val in c_161[:10]:
    print("UDP PPS to 206.152.35.161  at %s: %s" % (val, key))
