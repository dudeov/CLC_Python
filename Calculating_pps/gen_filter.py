list = ['206.152.32.20', '206.152.32.21', '206.152.32.22', '206.152.32.23', '206.152.32.24', '206.152.32.25', '206.152.32.26', '206.152.32.27', '206.152.32.28', '206.152.32.29', '206.152.32.30', '206.152.32.31', '206.152.32.32', '206.152.32.39', '206.152.32.50', '206.152.32.54', '206.152.32.57', '206.152.32.62', '206.152.32.65', '206.152.32.114', '206.152.32.190', '206.152.32.201', '206.152.32.204', '206.152.32.211', '206.152.32.223', '206.152.32.231', '206.152.32.232', '206.152.32.247', '206.152.33.5', '206.152.33.46', '206.152.33.50', '206.152.33.55', '206.152.33.111', '206.152.33.126', '206.152.33.137', '206.152.33.150', '206.152.33.171', '206.152.33.217', '206.152.33.218', '206.152.33.219', '206.152.33.238', '206.152.33.239', '206.152.33.240', '206.152.33.241', '206.152.33.242', '206.152.34.2', '206.152.34.116', '206.152.34.117', '206.152.34.157', '206.152.34.218', '206.152.35.91', '206.152.35.92', '206.152.35.93', '206.152.35.94', '206.152.35.123', '206.152.35.129', '206.152.35.130', '206.152.35.146', '206.152.35.147', '206.152.35.150', '206.152.35.161', '206.152.35.222']

# for i in list:
    # print('set firewall family inet filter DOS-BLOCK term count_%s from destination-address %s/32' % (i,i))
    # print('set firewall family inet filter DOS-BLOCK term count_%s from protocol udp' % i)
    # print('set firewall family inet filter DOS-BLOCK term count_%s then count %s_counter' % (i,i))    
    # print('set firewall family inet filter DOS-BLOCK term count_%s then accept\n\n' % i)
    
    
    
for i in list:
    print('counter_%s = []' % i)    

    
print('for line in fhand:')

for i in list:
    print('    if \'%s_counter\' in line:' % i) 
    print('    temp = line.split()')
    print('    counter_%s.append(int(temp[2]))' % i) 

  
print('fhand.close()')

for i in list:
    print('c_%s_value = []' % i)   


#Creating lists of PPSs - differences between each two values devided by time

print('for i in (range(len(time) - 1)):')
print('    dt = datetime.strptime(time[i], "%Y-%m-%d %H:%M:%S")')
print('    dt1 = datetime.strptime(time[i+1], "%Y-%m-%d %H:%M:%S")')
print('    delta = dt1 - dt ')

for i in list:
    print('    c_%s_value.append((counter_%s[i+1] - counter_%s[i])/delta.seconds)' % (i,i,i))

for i in list:
    print('c_%s = []' % i)   

#Since the lists of PPS are one value shorter than the lists of counter ant time values
#We need adjust the length of the list containing the time values
print('time.pop(0)')


#c_92 is list of tuples where first value is PPS and the second - the time when it was observed
for i in list:
    print('c_%s = zip(c_%s_value,time) ' % (i,i)) 
#print(c_92)   
for i in list:
    print('c_%s.sort(reverse=True)' % i) 

#Printing top 5 PPSs observed with the time it happened.
for i in list:
    print('print(\'--- \\n\')')
    print('for key, val in c_%s[:5]:' % i) 
    print('    print(\'UDP PPS to %s  at %%s: %%.1f\' %% (val, key)' % i)

