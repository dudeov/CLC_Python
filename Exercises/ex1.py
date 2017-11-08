str = '''
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-1 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-1 match destination-address 192.168.64.0/23
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-1 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-1 then permit tunnel ipsec-vpn wa1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-1 then permit tunnel pair-policy t3n-ib-1
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-2 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-2 match destination-address 10.88.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-2 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-2 then permit tunnel ipsec-vpn wa1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-2 then permit tunnel pair-policy t3n-ib-2
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-4 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-4 match destination-address 10.160.1.0/24
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-4 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-4 then permit tunnel ipsec-vpn ut1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-4 then permit tunnel pair-policy t3n-ib-4
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-5 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-5 match destination-address 10.98.96.0/19
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-5 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-5 then permit tunnel ipsec-vpn il1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-5 then permit tunnel pair-policy t3n-ib-5
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-6 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-6 match destination-address 10.78.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-6 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-6 then permit tunnel ipsec-vpn ny1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-6 then permit tunnel pair-policy t3n-ib-6
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-7 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-7 match destination-address 10.54.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-7 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-7 then permit tunnel ipsec-vpn ca1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-7 then permit tunnel pair-policy t3n-ib-7
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-8 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-8 match destination-address 10.59.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-8 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-8 then permit tunnel ipsec-vpn ca2-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-8 then permit tunnel pair-policy t3n-ib-8
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-9 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-9 match destination-address 10.64.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-9 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-9 then permit tunnel ipsec-vpn gb1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-9 then permit tunnel pair-policy t3n-ib-9
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-11 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-11 match destination-address 10.114.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-11 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-11 then permit tunnel ipsec-vpn de1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-11 then permit tunnel pair-policy t3n-ib-11
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-12 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-12 match destination-address 10.129.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-12 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-12 then permit tunnel ipsec-vpn va1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-12 then permit tunnel pair-policy t3n-ib-12
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-13 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-13 match destination-address 10.104.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-13 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-13 then permit tunnel ipsec-vpn ca3-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-13 then permit tunnel pair-policy t3n-ib-13
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-14 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-14 match destination-address 10.109.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-14 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-14 then permit tunnel ipsec-vpn gb3-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-14 then permit tunnel pair-policy t3n-ib-14
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-3 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-3 match destination-address 10.98.0.0/19
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-3 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-3 then permit tunnel ipsec-vpn ut1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-3 then permit tunnel pair-policy t3n-ib-3
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-33 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-33 match destination-address 10.239.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-33 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-33 then permit tunnel ipsec-vpn ne1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-33 then permit tunnel pair-policy t3n-ib-33
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-35 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-35 match destination-address 10.134.0.0/16
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-35 match application any
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-35 then permit tunnel ipsec-vpn sg1-vpn
set security policies from-zone trust to-zone vpn-zone policy t3n-ob-35 then permit tunnel pair-policy t3n-ib-35
set security policies from-zone trust to-zone vpn-zone policy uc1-au1-1 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-au1-1 match destination-address 10.164.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-au1-1 match application any
set security policies from-zone trust to-zone vpn-zone policy uc1-au1-1 then permit tunnel ipsec-vpn au1-vpn
set security policies from-zone trust to-zone vpn-zone policy uc1-au1-1 then permit tunnel pair-policy au1-uc1-1
set security policies from-zone trust to-zone vpn-zone policy uc1-va2-1 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-va2-1 match destination-address 10.170.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-va2-1 match application any
set security policies from-zone trust to-zone vpn-zone policy uc1-va2-1 then permit tunnel ipsec-vpn va2-vpn
set security policies from-zone trust to-zone vpn-zone policy uc1-va2-1 then permit tunnel pair-policy va2-uc1-1
set security policies from-zone trust to-zone vpn-zone policy vpn_va1_outbound_t3a_trust match source-address 10.124.15.14/32
set security policies from-zone trust to-zone vpn-zone policy vpn_va1_outbound_t3a_trust match destination-address 10.125.194.0/24
set security policies from-zone trust to-zone vpn-zone policy vpn_va1_outbound_t3a_trust match application any
set security policies from-zone trust to-zone vpn-zone policy vpn_va1_outbound_t3a_trust then permit tunnel ipsec-vpn va1-vpn
set security policies from-zone trust to-zone vpn-zone policy vpn_va1_outbound_t3a_trust then permit tunnel pair-policy vpn_va1_inbound_t3a_trust
set security policies from-zone trust to-zone vpn-zone policy uc1-de3-1 match source-address 10.124.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-de3-1 match destination-address 10.186.0.0/16
set security policies from-zone trust to-zone vpn-zone policy uc1-de3-1 match application any
set security policies from-zone trust to-zone vpn-zone policy uc1-de3-1 then permit tunnel ipsec-vpn de3-vpn
set security policies from-zone trust to-zone vpn-zone policy uc1-de3-1 then permit tunnel pair-policy de3-uc1-1
'''

import re
d={}
for i in re.findall(r'(ipsec-vpn\s)(\D\D\d-vpn)', str):
    d[i[1]]=0

print d

