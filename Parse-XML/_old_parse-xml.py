import xml.etree.ElementTree as ET
#from lxml import etree
from xml.etree.ElementTree import parse
try:
    from lxml import etree
except ImportError:
    print('Failed to import ElementTree from any known place')
    exit()

from lxml import etree

import string
import re

fn = raw_input("XML filename for parsing : ")

try:
    raw = open(fn)
except:
    print("Unable to open the file:")
    print(fn)
    exit()

f = open("tmp.xml", 'w')
temp = '<?xml version="1.0"?>\n<data>\n'
f.write(temp)
f.close()		
	
for line in raw:
    line1 = line.strip()
    if line1.startswith('<'):

			
       f = open("tmp.xml", 'a')
       line = "    "+line
       f.write(line)
       f.close()		
    else: 
	    continue

f = open("tmp.xml", 'a')
temp = '</data>'
f.write(temp)
f.close()	
		
#tree = ET.parse("tmp.xml")
#root = tree.getroot()

f = open("tmp.xml", 'r')

xmldata = etree.fromstring(f.read())

testsearch = xmldata.xpath('.//serial-number')

print testsearch
for i in testsearch:
    print etree.tostring(i, pretty_print="True")

#namespaces = {'xmlns:junos=': 'xmlns=': 'junos:style='}
#lst = root.findall('rpc-reply/multi-routing-engine-results/multi-routing-engine-item/chassis-inventory/chassis')
#lst1 = root.findall('.//serial-number[7]')
#print('Node count:', len(lst))

#print lst

#print('Node count:', len(lst1))

#for item in lst:
#    print('Name', item.find('version').text)
