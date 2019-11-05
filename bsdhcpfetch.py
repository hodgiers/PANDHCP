#!/usr/bin/python

import config
import requests
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup
import pprint
import json
import xmltodict


apikey = config.api_key
device = config.firewall
opcommand = "/api/?type=op&cmd=<show><dhcp><server><lease><interface>all</interface></lease></server></dhcp></show>&key="
response = requests.get(device + opcommand + apikey, verify=False)
response_mod = '<root>' + response.text + '</root>'
seed = ET.fromstring(response_mod)
soup = BeautifulSoup(response_mod, "xml")
tree = ET.ElementTree(soup)
root = tree.getroot()

new_file = open("info_xml.xml", 'w+')
new_file.write(str(soup))

new_file.close()


#tree._setroot(result)

print(soup.prettify())
###!!!!!Try printing this to a file and then calling that in convert_to_json!!!!!!!!!








#print (root.tag)

# #parsed_xml = object()
# def parse_xml():
# 	new_file = open("info_xml.txt", 'w+')
# 	for interfaces in root.iter('interface'):
# 		print (interfaces.attrib, file = new_file)
# 		for entries in interfaces.findall('./entry'):
# 			print (entries.attrib, entries.text, file = new_file)
# 			for details in entries.iter('*'):
# 				print ( details.tag, details.text, file = new_file)
# 				parsed_xml = ( details.tag, details.text)
# 				#print(parsed_xml, file = new_file)
# 	new_file.close()
# 				#print (parsed_xml)
# 	#print ("Parse_XML HAS BEEN RUN")	

# 	return parsed_xml

#def write_to_file(write_data):
	
	
	#new_file.close()

def convert_to_json(xml_data):
	#xmlstring = ET.tostring(xml_data)
	#jsonString = json.dumps(xmltodict.parse(xml_data), indent=4)
	#jsonString = json.dumps(xml_data)
	jsonString = xmltodict.parse(xml_data)
	print("Running Function", jsonString)
	#print("Second Function Running", xml_data)

def main():
	#parse_xml()
	convert_to_json("info_xml.xml")
	#print(tree)







main()


#What to do next: