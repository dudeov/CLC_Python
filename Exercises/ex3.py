str = '''
AU1_CFW_get-interfaces_output.log:        Destination: 10.254.164/24, Local: 10.254.164.5,
CA1_CFW_get-interfaces_output.log:        Destination: 10.254.54/24, Local: 10.254.54.5, Broadcast: 10.254.54.255
CA2_CFW_get-interfaces_output.log:        Destination: 10.254.59/24, Local: 10.254.59.5, Broadcast: 10.254.59.255
CA3_CFW_get-interfaces_output.log:        Destination: 10.254.104/24, Local: 10.254.104.5,
DE1_CFW_get-interfaces_output.log:        Destination: 10.254.114/24, Local: 10.254.114.5,
DE3_CFW_get-interfaces_output.log:        Destination: 10.254.186/24, Local: 10.254.186.5,
GB1_CFW_get-interfaces_output.log:        Destination: 10.254.64/24, Local: 10.254.64.5, Broadcast: 10.254.64.255
GB3_CFW_get-interfaces_output.log:        Destination: 10.254.109/24, Local: 10.254.109.5,
IL1_CFW_get-interfaces_output.log:        Destination: 10.254.9/24, Local: 10.254.9.5, Broadcast: 10.254.9.255
NY1_CFW_get-interfaces_output.log:        Destination: 10.254.7/24, Local: 10.254.7.5, Broadcast: 10.254.7.255
SG1_CFW_get-interfaces_output.log:        Destination: 10.254.134/24, Local: 10.254.134.5,
UC1_CFW_get-interfaces_output.log:        Destination: 10.254.124/24, Local: 10.254.124.5,
UT1_CFW_get-interfaces_output.log:        Destination: 10.254.98/24, Local: 10.254.98.5, Broadcast: 10.254.98.255
VA1_CFW_get-interfaces_output.log:        Destination: 10.254.129/24, Local: 10.254.129.5,
VA2_CFW_get-interfaces_output.log:        Destination: 10.254.170/24, Local: 10.254.170.5,
WA1_CFW_get-interfaces_output.log:        Destination: 10.254.88/24, Local: 10.254.88.5, Broadcast: 10.254.88.255
'''

import re
d={}
for i in re.findall(r'(\D\D\d_CFW).*(10.254.\d+\.5),', str):
    d[re.search(r'[A-Z]+[1-3]', i[0]).group().lower()] = re.search(r'10.254.\d+', i[1]).group() + '.1'

for n in d:
    print n.upper() + '_EFW ansible_host=' + d[n]


print '\n\n\n\n\n'

for t in d:
    print ('set security address-book global address %s/24 %s/24'%(d[t],d[t]))
    print ('set security policies from-zone trust to-zone vpn-zone policy efw_mgmt_%s match source-address 10.124.0.0/16'%t)
    print ('set security policies from-zone trust to-zone vpn-zone policy efw_mgmt_%s match destination-address %s/24'%(t,d[t]))
    print ('set security policies from-zone trust to-zone vpn-zone policy efw_mgmt_%s match application any'%t)
    print ('set security policies from-zone trust to-zone vpn-zone policy efw_mgmt_%s then permit tunnel ipsec-vpn %s-vpn'%(t,t))


print '\n\n\n\n\n'

for t in d:
    if t == 'uc1': continue
    print ('\n\n=======  %s ==========\n\n'%t)
    print ('set security address-book global address %s/24 %s/24'%(d[t],d[t]))
    print ('set security address-book global address 10.124.0.0/16 10.124.0.0/16')
    print ('set security policies from-zone vpn-zone to-zone untrust policy efw_mgmt_from_uc1 match source-address 10.124.0.0/16')
    print ('set security policies from-zone vpn-zone to-zone untrust policy efw_mgmt_from_uc1 match destination-address %s/24'%(d[t]))
    print ('set security policies from-zone vpn-zone to-zone untrust policy efw_mgmt_from_uc1 match application any')
    print ('set security policies from-zone vpn-zone to-zone untrust policy efw_mgmt_from_uc1 then permit tunnel ipsec-vpn uc1-vpn')

print '\n\n\n\n\n'

for t in d:
    tmp = t.upper()
    print ('%s_EFW ansible_host=%s'%(tmp,d[t]))

