#!/usr/bin/env python3
"""
@ Description
  Seems like HTML ENTITIES and replace them all?

"""


import re
import requests

r = requests.Session()
url = "http://web2.affinityctf.com/"

req = r.get(url).text

HTML_ENTITIES = re.findall("&#[0-9]{2,3}",req)

print(HTML_ENTITIES)

for i in HTML_ENTITIES:
	sub = i.replace("&#","")
	print(chr(int(sub)),end="")