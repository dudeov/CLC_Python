try:
    from lxml import etree
except ImportError:
    print('Failed to import ElementTree from any known place')
    exit()


import sys
# There is a difference in syntax of function "input" in Python 2 and 3
# "raw_input" in P2 is "input" in P3
# Checking that Python2 in use
if sys.version_info[0] != 2:
    print ("Wrong python version is in use, please use python2")
    exit()
    
    
 
def parse_file(file_to_parse):
    """
    Parse a file with multiple junos outputs in xml format
    Args: file_to_parse (file): an open file to parse
    Returns: A list of lxml trees with <rpc-reply> root elements
    """
    f = open("tmp.xml", 'w')
    f.close()     
    #getting rid of everything not related to xml (\n, promts and other crap)	
    for line in file_to_parse:
        line1 = line.strip()
        if line1.startswith('</rpc-reply>'):
           f = open("tmp.xml", 'a')
           f.write(line)
           f.write('\n')
           f.close()           
        elif line1.startswith('<'):
           f = open("tmp.xml", 'a')
           f.write(line)
           f.close()              
        else: 
            continue
	
    #File tmp.xml is a clear XML file with set of "rpc-reply" elements	
    f = open("tmp.xml")
    list_of_xml_trees = []
    parser = etree.XMLPullParser(events=['end'], recover=True)
    for line in f:
        parser.feed(line)
        for action, element in parser.read_events():
            if (action == 'end') and (element.tag == 'rpc-reply'):
                list_of_xml_trees.append(parser.close())
                parser = etree.XMLPullParser(events=('start', 'end'), recover=True)
    return list_of_xml_trees

    
    
#For test try this: D:\GitHub\Gathering-info\CLC_output.txt

fn = raw_input("XML filename for parsing : ")
try:
    raw = open(fn)
except:
    print("Unable to open the file:")
    print(fn)
    exit()
	
rpc_reply_list = parse_file(raw)
raw.close()

#We want to see serial numbers of all chassis, but not linecards
for xml_tree in rpc_reply_list:
    for element in xml_tree.xpath("//*[local-name() = 'chassis']/*[local-name() = 'serial-number']"):
       print element.text