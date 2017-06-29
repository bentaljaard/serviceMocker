import yaml
from pprint import pprint

file = "test.yaml"
with open(file) as data_file:    
	    orchdata = yaml.load(data_file)

pprint(orchdata)