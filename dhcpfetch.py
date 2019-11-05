#!/usr/bin/python

import config
import requests
from xml.etree import ElementTree as ET
import pprint
import json
import xmltodict


apikey = config.api_key
device = config.firewall
opcommand = "/api/?type=op&cmd=<show><dhcp><server><lease><interface>all</interface></lease></server></dhcp></show>&key="
response = requests.get(device + opcommand + apikey, verify=False)
seed = ET.fromstring(response.content)

def convert_to_json():
	xml = seed
	to_dict = xmltodict.parse(ET.tostring(xml))
	to_json = json.dumps(to_dict, indent=3)
	print (to_json)

def main():
	convert_to_json()


main()


#What to do next:
#Build MongoDB 
	#What parameters will be used for this DB?
	#How will I get that data to the DB?
	