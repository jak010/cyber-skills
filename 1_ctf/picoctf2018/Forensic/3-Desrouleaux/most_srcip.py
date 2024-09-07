import json
from collections import Counter

list_src = []
list_src2 = []
list_src3 = []
Q2cnt = 0


with open("./incidents.json") as json_file:
	json_data = json.load(json_file)
	max_len = len(json_data['tickets'])

	# Question 1 
	for x in range(0,max_len):
		list_src.append(json_data['tickets'][x]['src_ip'])

	Q1cnt = Counter(list_src)
	print(Q1cnt)

	print("===============================================")

	for x in range(0,max_len):
		if "93.124.108.240" in json_data['tickets'][x]['src_ip']:
			print(json_data['tickets'][x]['dst_ip'])
	print("Answer is 1")
	print("===============================================")



with open('./incidents.json') as f:
	data = json.loads(f.read())

# question 3
hashes = {}
for each in data[u'tickets']:
  hash = each[u'file_hash']
  
  if hash not in hashes:
    hashes[hash] = set()

  hashes[hash].add(each[u'dst_ip'])
 
from pprint import pprint
pprint(hashes)

avg = 0
for each in hashes:
  e = hashes[each]
  avg += len(e)
avg = (avg * 1.0) / len(hashes)

print(avg)