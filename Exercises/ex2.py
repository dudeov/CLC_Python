string = '''
AU1
Primary: 10.164.15.22, 10.226.33.49
Secondary: 10.164.15.24, 10.226.33.50
Tertiary: 10.134.15.25, 10.225.129.49 (SG1 Primary)

CA1
Primary: 10.54.15.13, 10.226.65.49
Secondary: 10.54.15.14, 10.226.65.50
Tertiary: 10.88.15.33, 10.226.129.49 (WA1 Primary)

CA2
Primary: 10.59.15.12, 10.224.33.49
Secondary: 10.59.15.13, 10.224.33.50
Tertiary: 10.104.15.34, 10.224.65.49 (CA3 Primary)

CA3
Primary: 10.104.15.34, 10.224.65.49
Secondary: 10.104.15.35, 10.224.65.50
Tertiary: 10.59.15.12, 10.224.33.49 (CA2 Primary)

DE1
Primary: 10.114.15.15, 10.224.97.49
Secondary: 10.114.15.16, 10.224.97.50
Tertiary: 10.109.15.30, 10.224.161.49 (GB3 Primary)

DE3
Primary: 10.186.15.13, 10.226.1.49
Secondary: 10.186.15.14, 10.226.1.50
Tertiary: 10.114.15.15, 10.224.97.49 (DE1 Primary)

GB1
Primary: 10.64.15.47, 10.224.129.49
Secondary: 10.64.15.48, 10.224.129.50
Tertiary: 10.109.15.30, 10.224.161.49 (GB3 Primary)

GB3
Primary: 10.109.15.30, 10.224.161.49
Secondary: 10.109.15.37, 10.224.161.50
Tertiary: 10.64.15.47, 10.224.129.49 (GB1 Primary)

IL1
Primary: 10.98.115.35, 10.224.193.49
Secondary: 10.98.115.36, 10.224.193.50
Tertiary: 10.78.15.20, 10.225.97.49 (NY1 Primary)

NE1
Primary: 10.239.15.25, 10.225.65.49
Secondary: 10.239.15.26, 10.225.65.50
Tertiary: 10.98.115.35, 10.224.193.49 (IL1 Primary)

NY1
Primary: 10.78.15.20, 10.225.97.49
Secondary: 10.78.15.21, 10.225.97.50
Tertiary: 10.129.15.79, 10.226.97.49 (VA1 Primary)

SG1
Primary: 10.134.15.25, 10.225.129.49
Secondary: 10.134.15.27, 10.225.129.50
Tertiary: 10.164.15.22, 10.226.33.49 (AU1 Primary)

UC1
Primary: 10.124.15.77, 10.225.161.49
Secondary: 10.124.15.78, 10.225.161.50
Tertiary: 10.88.15.33, 10.226.129.49 (WA1 Primary)
TACACS+ Control: 10.124.15.79

UT1
Primary: 10.98.15.15, 10.225.193.49
Secondary: 10.98.15.16, 10.225.193.50
Tertiary: 10.124.15.77, 10.225.161.49 (UC1 Primary)

VA1
Primary: 10.129.15.79, 10.225.225.49
Secondary: 10.129.15.94, 10.225.225.50
Tertiary: 10.170.15.18, 10.226.97.49 (VA2 Primary)

VA2
Primary: 10.170.15.18, 10.226.97.49
Secondary: 10.170.15.21, 10.226.97.50
Tertiary: 10.129.15.79, 10.225.225.49 (VA1 Primary)

WA1
Primary: 10.88.15.33, 10.226.129.49
Secondary: 10.88.15.34, 10.226.129.50
Tertiary: 10.54.15.13, 10.226.65.49 (CA1 Primary)

'''
import re

l = string.split('\n')
new_l = []
'''
#print l
for line in l:
    if re.search(r'^\D\D\d', line): new_l.append(re.search(r'^\D\D\d', line).group())
    if re.search(r'(Primary: )(\d+.\d+.\d+.\d+)', line): new_l.append(re.search(r'(Primary: )(\d+.\d+.\d+.\d+)', line).group(2))
    else: continue

print new_l
'''
l = re.findall(r'(\D\D\d)\nPrimary:\s(\d+.\d+.\d+.\d+),\s(\d+.\d+.\d+.\d+).*?Primary\)', string, re.DOTALL)

print 'mgmt:'
for line in l:
    print '    ' + line[0] + ':' + line[2]
print 'adm:'
for line in l:
    print '    ' + line[0] + ':' + line[1]
print '\n\n\n\n'
for line in l:
    tmp = re.sub(r'(\d+.\d+.\d+)(.\d+)', r'\1.1', line[1])
    print line[0] + '_CFW ansible_host=' + tmp

print '\n\n\n\n'
for line in l:
    tmp1 = re.sub(r'(\d+.\d+.\d+)(.\d+)', r'\1.1', line[2])
    tmp2 = re.sub(r'(\d+.\d+.\d+)(.\d+)', r'\1.2', line[2])

    ntmp1 = tmp1.split('.')
    ntmp1[2] = str(int(ntmp1[2]) - 1)

    nntmp1 = '.'.join(ntmp1)


    ntmp2 = tmp2.split('.')
    ntmp2[2] = str(int(ntmp2[2]) - 1)

    nntmp2 = '.'.join(ntmp2)

    
    print line[0] + '_MX1 ansible_host=' + nntmp1
    print line[0] + '_MX2 ansible_host=' + nntmp2






