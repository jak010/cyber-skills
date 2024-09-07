from sets import Set
from pwn import *
import json

sh = remote('2018shell2.picoctf.com', 14079)

with open('./incidents.json') as f:
  data = json.loads(f.read())

# question 1
src = {}

for each in data[u'tickets']:
  src_ip = each[u'src_ip']
  if src_ip in src:
    src[src_ip] += 1
  else:
    src[src_ip] = 1

print sh.recvuntil('ones.\n')
sh.sendline(max(src, key=src.get))

# question 2
target = sh.recvuntil('?\n').split(' ')[-1][:-2]
target_ls = {}
count = 0
for each in data[u'tickets']:
  if each[u'src_ip'] == target and each[u'dst_ip'] not in target_ls:
    target_ls[each[u'dst_ip']] = True
    count += 1

sh.sendline(str(count))

# question 3
hashes = {}
for each in data[u'tickets']:
  hash = each[u'file_hash']
  if hash not in hashes:
    hashes[hash] = Set()
  hashes[hash].add(each[u'dst_ip'])

avg = 0
for each in hashes:
  e = hashes[each]
  avg += len(e)

print("current avg " ,avg)
print("len(hashes)",len(hashes))
avg = (avg * 1.0) / len(hashes)

print(avg)

print sh.recvuntil('.\n')
sh.sendline(str(avg))

sh.interactive()