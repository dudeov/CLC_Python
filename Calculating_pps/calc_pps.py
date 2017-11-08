from __future__ import division
from datetime import datetime, date, time
import re
import sys

time = []
counter_161 = []
counter_91 = []
counter_92 = []
counter_93 = []
counter_94 = []

fhand = open(sys.argv[1])

#Extracting all times and counters values from the file and writing them in lists defined above

for line in fhand:
    if line.startswith('2017'):
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

#Printing top 5 PPSs observed with the time it happened.
print('--- \n')
for key, val in c_92[:5]:
    print("UDP PPS to 206.152.35.92  at %s: %.1f" % (val, key))
print('--- \n')
c_91 = zip(c_91_value,time) 
#print(c_91)   
c_91.sort(reverse=True)
for key, val in c_91[:5]:
    print("UDP PPS to 206.152.35.91  at %s: %.1f" % (val, key))
print('--- \n')
c_93 = zip(c_93_value,time) 
#print(c_93)   
c_93.sort(reverse=True)
for key, val in c_93[:5]:
    print("UDP PPS to 206.152.35.93  at %s: %.1f" % (val, key))
print('--- \n')
c_94 = zip(c_94_value,time) 
#print(c_94)   
c_94.sort(reverse=True)
for key, val in c_94[:5]:
    print("UDP PPS to 206.152.35.94  at %s: %.1f" % (val, key))
print('--- \n')
c_161 = zip(c_161_value,time) 
#print(c_161)   
c_161.sort(reverse=True)
for key, val in c_161[:5]:
    print("UDP PPS to 206.152.35.161 at %s: %.1f" % (val, key))


#How to use the script and what it is for:

#Using
#
    
#Getting file in format of:

#alex.chuvakov@WA1T3NNETHOP01:~$ cat CA3-efw-pps.txt 
#root@CA3-SRX-EDGE-N0> file show /var/tmp/test.txt | no-more 
#2017-05-16 23:14:30
# 
#Filter: DOS-BLOCK
#Counters:
#Name                                                Bytes              Packets
#206.152.35.161_counter                          113896056               569488
#206.152.35.91_counter                           113114872               565600
#206.152.35.92_counter                           128569308               642876
#206.152.35.93_counter                            93636648               468199
#206.152.35.94_counter                           111186628               555947
#2017-05-16 23:14:33
# 
#Filter: DOS-BLOCK
#Counters:
#Name                                                Bytes              Packets
#206.152.35.161_counter                          114739056               573703
#206.152.35.91_counter                           113994072               569996
#206.152.35.92_counter                           129525508               647657
#206.152.35.93_counter                            94471448               472373
#206.152.35.94_counter                           112093828               560483
#2017-05-16 23:14:36


#and calculates PPS for every period

#Usage:
#alex.chuvakov@WA1T3NNETHOP01:~$ python calc_pps.py CA3-efw-pps.txt
#--- 
#
#UDP PPS to 206.152.35.92  at 2017-05-16 23:25:23: 2773.3
#UDP PPS to 206.152.35.92  at 2017-05-16 23:19:50: 2765.3
#UDP PPS to 206.152.35.92  at 2017-05-16 23:25:12: 2435.0
#UDP PPS to 206.152.35.92  at 2017-05-16 23:24:49: 2428.0
#UDP PPS to 206.152.35.92  at 2017-05-16 23:20:05: 2393.3
#--- 
#
#UDP PPS to 206.152.35.91  at 2017-05-16 23:20:05: 2210.0
#UDP PPS to 206.152.35.91  at 2017-05-16 23:20:42: 2064.0
#UDP PPS to 206.152.35.91  at 2017-05-16 23:21:15: 2058.7
#UDP PPS to 206.152.35.91  at 2017-05-16 23:21:12: 2008.7
#UDP PPS to 206.152.35.91  at 2017-05-16 23:20:08: 2007.7

#Where counter.txt is a name of the file. Appears here: fhand = open(sys.argv[1])




#Linux script that collects the data in the background:
#root@CA3-SRX-EDGE-N0% #!/bin/sh
#while :
#do
#date +%Y-%m-%d' '%H:%M:%S >> /var/tmp/test.txt 2>&1; cli show firewall filter DOS-BLOCK >> /var/tmp/test.txt 2>&1; sleep 2;
#done

#Running script in the background
#root@CA3-SRX-EDGE-N0% cat /var/tmp/run-sh.sh &
#parameter "&" tells to run that in the background, it continus working even after logout
#need to kill process manually then
#root@CA3-SRX-EDGE-N0% ps aux | grep run
#root         98644  0.0  0.1  2396  1048  p0  S+   11:46PM   0:00.01 grep run
#root         95534  0.0  0.0  1252   388  p2- S    11:13PM   0:00.63 sh /var/tmp/run-sh.sh
#root@CA3-SRX-EDGE-N0% kill -9 95534


#It show top 10 PPS that was observed for every counter