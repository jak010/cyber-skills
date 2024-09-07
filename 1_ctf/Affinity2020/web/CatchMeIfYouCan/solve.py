#!/usr/bin/env python3

import sys

import requests

# imagefile = sys.argv[1]
# h = Image.open(imagefile)
# unlock = pytesseract.image_to_string(h, lang="env", config="--psm 10 --osm 3 -c tessdir_char_whtielist=0123456789abcdef")
# unlock = ''.join(unlock.strip().split("\n"))

# print(unlock)

url = "http://web4.affinityctf.com/"
r = requests.Session()
html =  r.get(url).text

print(html)
