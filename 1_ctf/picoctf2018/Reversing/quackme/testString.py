# !/usr/bin/python3

from io import StringIO

import sys
import pwn


sekruBufferr = pwn.p32(0x8048858)

greetingMessage = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"


xorString = '2906164f2b35301e511b5b144b085d2b56475750164d51515d00'

var = "\\x"

# Copy MSG Gen
for x in range(len(xorString)):
	if x %2 !=0 :
		var += "".join(xorString[x-1]+xorString[x]+"\\x")


print("[+]Copy, Msg ---> " , var[0:-2])

print("\n\n")

byteString = '\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x56\x47\x57\x50\x16\x4d\x51\x51\x5d\x00'

print(byteString)

# Usage :  pwn.xor(pasteMsg, greetingMessage)

print(pwn.xor(byteString,greetingMessage))
