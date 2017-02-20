import xml.etree.ElementTree as ET
from lxml import etree

fn = raw_input("XML filename for parsing : ")

try:
    raw = open(fn)
except:
    print("Unable to open the file:")
    print(fn)
    exit()

f = open("tmp.xml", 'w')
temp = '<?xml version="1.0"?>\n'
f.write(temp)
f.close()		
	
for line in raw:
    line1 = line.strip()
    if line1.startswith('<'):
        f = open("tmp.xml", 'a')
        f.write(line)
        f.close()		
    else: 
	    continue

#tree = ET.parse("tmp.xml")
#root = tree.getroot()

tree = etree.parse('tmp.xml')

nodes = tree.xpath('rpc-reply xmlns/multi-routing-engine-results/multi-routing-engine-item/chassis-inventory')
               
for node in nodes: 
    print 'text =',[node.text] 

