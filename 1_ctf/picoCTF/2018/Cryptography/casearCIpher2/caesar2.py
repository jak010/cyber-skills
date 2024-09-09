f = open("./ciphertext","r")

fileContent = f.read()

for i in range(255):
	new_String = []
	for c in fileContent:
		new_String.append( chr( (ord(c) + i  ) % 255  ))

	print ("".join(new_String))

