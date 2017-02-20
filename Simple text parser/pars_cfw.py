#! /usr/bin/python

import sys
import string
import re

# There is a difference in syntax of function "input" in Python 2 and 3
# "raw_input" in P2 is "input" in P3
# Checking that Python2 in use
if sys.version_info[0] != 2:
    print ("Wrong python version is in use, please use python2")
    exit()
# Get filename and IP from user input
filename = raw_input('\nType filename with "show configuration security ike | match external-interface | display set | no-more" output:   ')
ip = raw_input('\nType the pld reth3.998 ip address:   ')


# trying to open the file
try:
    raw = open(filename)
except:
    print("Unable to open the file:")
    print(filename)
    exit()

#Creating new file, erasing if already exists	
f = open("result.txt", 'w')
f.close()		
	
for line in raw:
    # Deleting all spaces at the begining of the line
    line = line.strip()
    
    # Finding all ike gateway names
    if re.search('set security ike gateway\s*',line):
        
        temp = line.split()
        print('set security ike gateway %s local-address %s'% (temp[4],ip))
        f = open("result.txt", 'a')
        f.write('set security ike gateway %s local-address %s\n'% (temp[4],ip))
        f.close()		
    else: 
	   continue

