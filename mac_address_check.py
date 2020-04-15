#!/usr/bin/python

import json
import sys
import os
if (len(sys.argv[1:]) != 1):
	print("Please pass mac address check below for reference\n********Example*********\ndocker run mycustomimage:v1 python /opt/mac_address_check.py 44:38:39:ff:ef:57")
	exit(0)
else:
	mac_address=sys.argv[1]
	result = os.popen("curl --silent --location --request GET 'https://api.macaddress.io/v1?apiKey=at_ID5RGEuFVTM1pbsNcD0Oz3G3YvI5X&output=json&search='"+mac_address).read()

#Converting output to dictionary

	dict_data=json.loads(str(result))
	print("Vendor name is "+"\""+dict_data["vendorDetails"]["companyName"]+"\"")
