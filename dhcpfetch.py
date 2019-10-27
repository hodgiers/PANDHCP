#!/usr/bin/python

import config
import requests
from xml.etree import ElementTree as ET
import pprint


apikey = config.api_key
device = config.firewall
opcommand = "/api/?type=op&cmd=<show><dhcp><server><lease><interface>all</interface></lease></server></dhcp></show>&key="

response = requests.get(device + opcommand + apikey, verify=False)
seed = ET.fromstring(response.content)
tree = ET.ElementTree(seed)
root = tree.getroot()

#print (root.tag)

for interfaces in root.iter('interface'):
	print (interfaces.attrib)
	for entries in interfaces.findall('./entry'):
		print (entries.attrib)
		for details in entries.iter('*'):
			print (details.tag)

	#print (interface)
#	print (child.tag, child.attrib)


#for child in tree.iter('*'):
#	print (child.tag, child.attrib)

#####root = tree.getroot()
#####print(root.attrib)

######for child in tree.iter('*'):
#####	print (child.tag, child.attrib)