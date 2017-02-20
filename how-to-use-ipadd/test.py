#! python

from ipaddress import *

ipsec_peer_IPV4 = IPv4Network('192.168.0.0/24').subnets(new_prefix=30)
#ipsec_peer_IPV4_peer = IPv4Network('10.128.0.0/22').subnets(new_prefix=30)


START_COUNT = 0
END_COUNT = 10

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
    
