import yaml

yml_string = '''
---
interface1_name: xe-0/0/1
interface2_name: xe-0/0/2

    
'''

s = yaml.load(yml_string)
print s
