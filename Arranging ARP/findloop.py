import re

inp_file = raw_input('Input file name:  ')
out_file = raw_input('Output file name:  ')
try:
   file = open(inp_file)
except:
   print('No file, sorry. Closing the programm')
   exit()


IN = dict()
OUT = dict()
count = 0


for line in file:
    line = line.rstrip()
    if re.search('Out arp who-has', line):
       x = ''.join(re.findall('[0-9]+.[0-9]+.[0-9]+.[0-9]+ tell [0-9]+.[0-9]+.[0-9]+.[0-9]+', line))
       if len(x) > 0:
          OUT[x] = line 
    if re.search('In arp who-has', line):
       x = ''.join(re.findall('[0-9]+.[0-9]+.[0-9]+.[0-9]+ tell [0-9]+.[0-9]+.[0-9]+.[0-9]+', line))
       if len(x) > 0:
          if IN.get(x, 0) != 0: count = count + 1 
          IN[x] = line
          if OUT.get(x, 0) != 0:
             print IN[x]
             print OUT[x]  
print count
