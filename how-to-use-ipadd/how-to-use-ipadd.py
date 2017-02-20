#! python
# This script provides a complex example of IPv4Network functions

# To use, just type in cmd: C:\Users\achuvakov\Desktop\My\Work\CLC\Python>cd Examples

# C:\Users\achuvakov\Desktop\My\Work\CLC\Python\Examples>python how-to-use-ipadd.py

# It is possible to redirect output to a file: C:\Users\achuvakov\Desktop\My\Work\CLC\Python\Examples>python how-to-use-ipadd.py > results.txt

from ipaddress import *

ipsec_peer_IPV4 = IPv4Network('192.168.0.0/24').subnets(new_prefix=30)



START_COUNT = 0
END_COUNT = 63

#COUNT starts from START_COUNT and increases by 1, untill reaches END_COUNT
for COUNT in range(START_COUNT, END_COUNT + 1):
    current_ipv4_net = next(ipsec_peer_IPV4)
    ipv4_host_1 = list(current_ipv4_net.hosts())[0]
    ipv4_host_2 = list(current_ipv4_net.hosts())[1]
	
    print('%s NET is' % (COUNT))
    print('%s' % (current_ipv4_net))
    print('MASK is %s' % (current_ipv4_net.prefixlen)) 	
    print('1-st host is %s' % (ipv4_host_1))
    print('2-st host is %s' % (ipv4_host_2))	
    
    print()
    print()
    print()
    
