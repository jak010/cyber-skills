import pwn
import re

host,port = "2018shell2.picoctf.com", 15853

s = pwn.remote(host,port)

prompt = s.recv()

print prompt
binay = re.findall('the (.*) as a word' ,prompt)[0]
answer = hex(int(binay.replace(' ',''),2))[2:].decode("hex")
s.sendline(answer)

prompt = s.recv()
print prompt
hexadecimal = re.findall('the (.*) as a word' ,prompt)[0]
answer = hexadecimal.decode("hex")
s.sendline(answer)


prompt = s.recv()
print prompt
octal = re.findall('the (.*) as a word' ,prompt)[0]
# print  hex(int(octal.replace(' ',''),8))[2:].decode('hex')
answer = ''.join([ chr(int(x,8)) for x in octal.split()])
s.sendline(answer)


prompt = s.recv()
print prompt
print re.findall('picoCTF{.*}',prompt)[0]


s.close()