#!python3

import sys

if sys.version_info[0] != 3:
    print ("Wrong python version is in use, please use python3")
    exit()


from ipaddress import *

ipsec_peer_IPV4_our = IPv4Network('10.0.0.0/22').subnets(new_prefix=30)
ipsec_peer_IPV4_peer = IPv4Network('20.0.0.0/22').subnets(new_prefix=30)
ipsec_peer_IPV4_gw = IPv4Network('30.0.0.0/22').subnets(new_prefix=30) 

START_COUNT = 2
END_COUNT = 4

#COUNT starts from START_COUNT and increases by 1, untill reaches END_COUNT
for COUNT in range(START_COUNT, END_COUNT + 1):








    current_ipv4_net_our = next(ipsec_peer_IPV4_our)
    current_ipv4_net_peer = next(ipsec_peer_IPV4_peer)
    current_ipv4_net_gw = next(ipsec_peer_IPV4_gw)


    ipv4_host_1 = list(current_ipv4_net_our.hosts())[0]
    
    ipv4_host_2 = list(current_ipv4_net_gw.hosts())[0]

    
    print()
    print()
    print()
    
    print('set security ike policy client-%s mode main' % (COUNT))
    print('set security ike policy client-%s proposals c-p1-psk-aes256-g5-sha256-28800' % (COUNT))
    print('set security ike policy client-%s pre-shared-key ascii-text "$9$lUEMWXJZjHkPaZ/tu0hcxNdw4JGUHPfzkquOIRSylKv"' % (COUNT))

    print('set security ike gateway client-%s ike-policy client-%s' % (COUNT, COUNT))
    print('set security ike gateway client-%s address %s' % (COUNT, ipv4_host_2))
    print('set security ike gateway client-%s no-nat-traversal' % (COUNT))
    print('set security ike gateway client-%s external-interface reth3.998' % (COUNT))

    print('set security ipsec vpn client-%s ike gateway client-%s' % (COUNT, COUNT))
    print('set security ipsec vpn client-%s ike ipsec-policy c-p2-esp-aes256-sha-28800-g2' % (COUNT))
    print('set security ipsec vpn client-%s establish-tunnels immediately' % (COUNT))
    print()
    print('set security policies from-zone vpn-zone to-zone cust-%s-zone policy client-%s-inbound match source-address %s' % (COUNT, COUNT, current_ipv4_net_peer))
    print('set security policies from-zone vpn-zone to-zone cust-%s-zone policy client-%s-inbound match destination-address %s' % (COUNT, COUNT, current_ipv4_net_our))
    print('set security policies from-zone vpn-zone to-zone cust-%s-zone policy client-%s-inbound match application any' % (COUNT, COUNT))
    print('set security policies from-zone vpn-zone to-zone cust-%s-zone policy client-%s-inbound then permit tunnel ipsec-vpn client-%s' % (COUNT, COUNT, COUNT))
    print('set security policies from-zone vpn-zone to-zone cust-%s-zone policy client-%s-inbound then permit tunnel pair-policy client-%s-outbound' % (COUNT, COUNT, COUNT))

    print()
    print('set security policies from-zone cust-%s-zone to-zone vpn-zone policy client-%s-outbound match source-address %s' % (COUNT, COUNT, current_ipv4_net_our))
    print('set security policies from-zone cust-%s-zone to-zone vpn-zone policy client-%s-outbound match destination-address %s' % (COUNT, COUNT, current_ipv4_net_peer))
    print('set security policies from-zone cust-%s-zone to-zone vpn-zone policy client-%s-outbound match application any' % (COUNT, COUNT))
    print('set security policies from-zone cust-%s-zone to-zone vpn-zone policy client-%s-outbound then permit tunnel ipsec-vpn client-%s' % (COUNT, COUNT, COUNT))
    print('set security policies from-zone cust-%s-zone to-zone vpn-zone policy client-%s-outbound then permit tunnel pair-policy client-%s-inbound' % (COUNT, COUNT, COUNT))

    print()
    print('set interfaces reth1 unit %s vlan-id %s' % (COUNT, COUNT))
   
    print('set interfaces reth1 unit %s family inet address %s/30' % (COUNT, ipv4_host_1))
