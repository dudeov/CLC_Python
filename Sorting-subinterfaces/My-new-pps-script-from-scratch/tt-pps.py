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
# Get filename from user input
filename = raw_input('\nType filename with "show interface" output:   ')

# trying to open the file
try:
    raw = open(filename)
except:
    print("Unable to open the file:")
    print(filename)
    exit()


reth = list()
inp = list()
out = list()

for line in raw:
    # Deleting all spaces at the begining of the line
    line = line.strip()
    
    # Finding all rethX.XX names and writing them in the list "reth"
    if re.search('reth[0-9]+[.][0-9]+',line):
        
        #---------find method------------
        #spos is a position where "reth" starts in the string "line"
        #spos = line.find('reth')
        #fpos is a position where "reth" ends - finds 1-st space after rethXXX
        #fpos = line.find(' ',spos )
        #getting reth name by cutting "line" from the position "spos" to the position "fpos"
        #reth1 = line[spos:fpos]
        #reth.append(reth1)
        
        #---------findall method---------
        #re.findall('reth[0-9]+[.][0-9]+',line) - returns a !!LIST!! of all rethX.XX in the string
        #''.join(re.findall('reth[0-9]+[.][0-9]+',line)) - join converts the list from above to a string
        reth.append(''.join(re.findall('reth[0-9]+[.][0-9]+',line)))        
    
    # Wring all input pps values in list "inp" 
    elif re.search('Input\s*:',line):
        # deleting all punctuation
        line = line.translate(None, string.punctuation) 
        temp = line.split()
        # pps is a 3-rd value in the list "temp" eg 2-nd position
        inp1 = int(temp[2])
        inp.append(inp1)
    
    # Wring all out pps values in list "out" 
    elif 'Output:' in line:
        line = line.translate(None, string.punctuation)
        temp = line.split()
        out1 = int(temp[2])
        out.append(out1)
    else: continue

tempres = list()

# Joining lists "reth", "inp", "out" to the one common list
# Creating a list of tuples of (input pps value, output pps value, reth name)
for i in range(len(reth)):
     tempres.append((inp[i],out[i],reth[i]))

# Sorting list by the first variables in tuples, by "inp"
tempres.sort(reverse=True)

res = list()


if len(tempres) < 10:
     l = len(tempres)
else:
     l = 10

# Creating a new list containing first 10 values of list "res"
for z in range(l):
     res.append(tempres[z])

print("\nTop %s pps talkers: \n" % (l))
for z, x, c in res:
     print("Interface:%s       (Input pps:%s)" % (c,z))
