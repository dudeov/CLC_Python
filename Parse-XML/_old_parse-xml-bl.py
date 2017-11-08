from lxml import etree

def parse_file(file_to_parse):
#"""Parse a file with multiple junos outputs in xml format
#Args:
#file_to_parse (file): an open file to parse
#Returns:
#A list of lxml trees with <rpc-reply> root elements
#"""
    list_of_xml_trees = []
    parser = etree.XMLPullParser(events=['end'], recover=True)
    for line in file_to_parse:
        parser.feed(line)
        for action, element in parser.read_events():
            if (action == 'end') and (element.tag == 'rpc-reply'):
                    list_of_xml_trees.append(parser.close())
        parser = etree.XMLPullParser(events=('start', 'end'), recover=True)
    return list_of_xml_trees

#f = open('tmp.xml', 'r')
#xmldata = etree.fromstring(f.read())

f = open('CLC_output.txt', 'r')
xmldata =  etree.fromstring(parse_file(f))

testsearch = xmldata.find('.//serial-number')

print etree.tostring(testsearch, pretty_print="True")