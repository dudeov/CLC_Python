#! /usr/bin/python


import os
import re
import sys
from pprint import pprint

if sys.version_info[0] != 2:
    print ("Wrong python version is in use, please use python2")
    exit()
 
filename = raw_input('\nType filename with "show interface" output:   ')

try:
    raw = open(filename)
except:
    print("Unable to open the file:")
    print(filename)
    exit()
	
interface_data = raw.read()

STRING_MAX_RESULTS=input('Type how many sub-interfaces youd like to see:    ')

MAX_RESULTS = int(STRING_MAX_RESULTS)

if MAX_RESULTS<1:
    print ("Type positive integer higher than 0")
    exit()

logical_interfaces = re.findall(
        r'Logical interface (\S+) .*?'
        r'(Input.*?)\n.*?'
        r'(Output.*?)\n',
        interface_data, re.DOTALL
)

input_stats = {}
output_stats = {}


for i in logical_interfaces:
    interface, input_raw, output_raw = i
    output_pps = int(output_raw.split()[-3])
    input_pps = int(input_raw.split()[-3])
    input_stats[interface] = (input_pps, output_pps)
    output_stats[interface] = (output_pps, input_pps)

   

input_total, output_total = (0,0)

def getKey(item):
    return item[1]


print ("\nTop talkers: \n")
count = 0

for interface in sorted(input_stats, key=input_stats.get, reverse=True):
    if count >= MAX_RESULTS:
        break
    input_pre, output_pre = input_stats[interface]
 
    
    print('{0} - input {1} - output {2}'.format(interface, input_pre, output_pre))
    input_total += input_pre
    output_total += output_pre
    count += 1

print("\n\n")
count = 0
for interface in sorted(output_stats, key=output_stats.get, reverse=True):
    if count >= MAX_RESULTS:
        break
    input_pre, output_pre = output_stats[interface]

    
    print('{0} - output {1} - input {2}'.format(interface, input_pre, output_pre))
    count += 1
print("\n\n")




print('Total Input {0} pps\tOutput {1} pps'.format(input_total, output_total))

