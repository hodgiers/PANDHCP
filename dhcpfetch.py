#!/usr/bin/python

import config
import requests
from xml.etree import ElementTree as ET
import pprint
import json
import xmltodict
import pymongo
from pymongo import MongoClient


apikey = config.api_key
device = config.firewall
opcommand = "/api/?type=op&cmd=<show><dhcp><server><lease><interface>all</interface></lease></server></dhcp></show>&key="
response = requests.get(device + opcommand + apikey, verify=False)
seed = ET.fromstring(response.content)
#Mongo Connection
client = MongoClient(config.mongohost, 27017)


def convert_to_json():
	xml = seed
	to_dict = xmltodict.parse(ET.tostring(xml))
	to_json_string = json.dumps(to_dict, indent=3)
	to_json = json.loads(to_json_string)
	#print (to_json['response'])
	#for item in to_json.items():
		#print(item.get('interface', "no response"))
	#print(list(to_json.values()))
	print('Converted api results to JSON')
	return to_json

def create_db(document):
	db = client.networkdata
	dhcpcollection = db.dhcpdata
	result = dhcpcollection.insert_one(document)
	print('Saved data to DB. First article key is: {}'.format(result.inserted_id))
 



	

def main():
	create_db(convert_to_json())


main()

#Top portion to delete:[0:68]
#Bottom portion to delete:[18815:18830]
#length = 18830

#What to do next:
#Build MongoDB 
	#What parameters will be used for this DB?
	#How will I get that data to the DB?
