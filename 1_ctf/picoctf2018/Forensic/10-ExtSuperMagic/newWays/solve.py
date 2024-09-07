

"""

ext2/ext3/ext4 filesystem always has the bytes 0x53 0xEF at positions 1080–1081.
"""

with open("ext-super-magic.img","r+b") as ext:
	ext.seek(0x438) # 0x438 -> 1080
	ext.write(b"\x53\xef")

print("Magic Number Fixed")