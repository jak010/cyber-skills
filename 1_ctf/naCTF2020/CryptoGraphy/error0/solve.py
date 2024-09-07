#!/usr/bin/python3


with open("enc.txt") as f:
	data = f.read()

enc = []

for i in range(0,101):
	enc.append(data[i*232 : (i+1)*232])

result = " "

for i in range(232):
	count = 0
	for j in range(101):
		if(enc[j][i] == '1'):
			count +=1
	if (count >51):
		result += "1"
	else:
		result += "0"

print(result)