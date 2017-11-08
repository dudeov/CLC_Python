#!/usr/bin/env python
from jinja2 import Template
import yaml
import sys
import re

'''
Usage: python prender.py YAML-DATA.yml JINJA-TEMPLATE.j2
Order of .yml and .j2 files doesn't matter.
The text will be printed out to your terminal
'''
def print_the_config(files):

  for file in files:
    if re.search(r'.*.yml', file):
      yaml_fname = file
    elif re.search(r'.*.j2', file):
      j2_fname = file
    else:
      print('Unrecognized extension. Supports either .yml or .j2')
      exit()
  datavars = yaml.load(open(yaml_fname).read())
  template = Template(open(j2_fname).read())

  print(template.render(datavars))

if __name__ == '__main__':
  if len(sys.argv) >= 3:
    print_the_config(sys.argv[1:])
  else:
    print('Argument error! Usage: python prender.py YAML-DATA.yml JINJA-TEMPLATE.j2')
    exit()
