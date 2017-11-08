efw={'NY1_EFW': '10.254.7.1',
    'CA3_EFW': '10.254.104.1',
    'SG1_EFW': '10.254.134.1',
    'UT1_EFW': '10.254.98.1',
    'GB3_EFW': '10.254.109.1',
    'GB1_EFW': '10.254.64.1',
    'VA1_EFW': '10.254.129.1',
    'IL1_EFW': '10.254.9.1',
    'WA1_EFW': '10.254.88.1',
    }    
cfw={
    'CA3_CFW': '10.104.15.1',
    'GB1_CFW': '10.64.15.1',
    'GB3_CFW': '10.109.15.1',
    'IL1_CFW': '10.98.100.1',
    'NY1_CFW': '10.78.15.1',
    'SG1_CFW': '10.134.8.4',
    'UT1_CFW': '10.98.15.1',
    'VA1_CFW': '10.129.15.1',
    'WA1_CFW': '10.88.15.1',
    }



for e,c in zip(sorted(efw.keys()), sorted(cfw.keys())):


  print('\n############## %s ##################\n'% e)
  
  print('set security nat destination pool uc1_syslog address 10.124.15.68/32')

  print('set security nat destination rule-set uc1_syslog from zone trust')
  print('set security nat destination rule-set uc1_syslog rule 1 match source-address %s/32'% cfw[c])
  print('set security nat destination rule-set uc1_syslog rule 1 match destination-address 198.51.100.1/32')
  print('set security nat destination rule-set uc1_syslog rule 1 match destination-port 514')
  print('set security nat destination rule-set uc1_syslog rule 1 match protocol udp')
  print('set security nat destination rule-set uc1_syslog rule 1 then destination-nat pool uc1_syslog')

  print('set security policies from-zone trust to-zone trust policy to_uc1_syslog match source-address %s/32'% cfw[c])
  print('set security policies from-zone trust to-zone trust policy to_uc1_syslog match destination-address 10.124.15.0/24')
  print('set security policies from-zone trust to-zone trust policy to_uc1_syslog match application junos-syslog')
  print('set security policies from-zone trust to-zone trust policy to_uc1_syslog then permit')

  print('set security zones security-zone trust address-book address %s/32 %s/32'% (cfw[c], cfw[c]))
  print('set security zones security-zone trust address-book address 10.124.15.0/24 10.124.15.0/24')


  print('\n%s\n'% c)

  print('set system syslog host 198.51.100.1 any any')
  print('set system syslog host 198.51.100.1 source-address %s'% cfw[c])
  print('set security address-book global address 10.124.15.0/24 10.124.15.0/24')
  print('set security policies from-zone untrust to-zone vpn-zone policy to_uc1_syslog match source-address %s/32'% efw[e])
  print('set security policies from-zone untrust to-zone vpn-zone policy to_uc1_syslog match destination-address 10.124.15.0/24')
  print('set security policies from-zone untrust to-zone vpn-zone policy to_uc1_syslog match application junos-syslog')
  print('set security policies from-zone untrust to-zone vpn-zone policy to_uc1_syslog then permit tunnel ipsec-vpn uc1-vpn')
  print ('set security address-book global address %s/32 %s/32'% (efw[e], efw[e]))



print('\n############## %s ##################\n')
for i in efw:
  string = i.split('_')[0].lower()
  print('set security policies from-zone vpn-zone to-zone trust policy %s_to_syslog match source-address %s/32'% (string, efw[i]))
  print('set security policies from-zone vpn-zone to-zone trust policy %s_to_syslog match destination-address 10.124.15.0/24'% string)
  print('set security policies from-zone vpn-zone to-zone trust policy %s_to_syslog match application junos-syslog'% string)
  print('set security policies from-zone vpn-zone to-zone trust policy %s_to_syslog then permit tunnel ipsec-vpn %s-vpn'% (string, string))
  print('set security address-book global address %s/32 %s/32'% (efw[i], efw[i]))
  print('\n\n')
