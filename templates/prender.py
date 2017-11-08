from jinja2 import Template
import yaml
import sys

datavars_fname = sys.argv[1]
template_fname = sys.argv[2]

datavars = yaml.load(open(datavars_fname).read())
template = Template(open(template_fname).read())

print template.render(datavars)

