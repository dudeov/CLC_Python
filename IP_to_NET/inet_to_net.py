#  How to use:
#  python d:\GitHub\CLC_Python\IP_to_NET\inet_to_net.py 192.168.1.2
#  49.0001.1921.6800.1002.00

import sys

arg1 = sys.argv[1]

t = arg1.split('.')
p = []

for i in t:
   if len(i) == 2: i = '0' + i
   if len(i) == 1: i = '00' + i
   p.append(i)
d = "".join(p)

print "49.0001." + d[0:4] + '.' + d[4:8] + '.' + d[8:12] + '.' + '00'



