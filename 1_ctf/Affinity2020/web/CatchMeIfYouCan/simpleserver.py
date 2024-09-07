import re
import http.server

import requests
from PIL import Image
from io import BytesIO
import pytesseract

import base64
PNG_OUT="out.png"

# DATA Length?
def parse_req(reqbody):
	req = reqbody.decode("utf-8").split(",")[1]
	return req


def save_png(path,bytestream):
	# h = open(path,"wb")
	# img = Image.open(BytesIO(b64encode(bytestream.encode("utf-8"))))
	# h.write(img)
	# h.close()

	with open(PNG_OUT,"wb") as file:
		file.write(base64.decodebytes(bytestream.encode("utf-8")))



def get_text(imagefile):

	fill_color = (255,255,255)
    
	with Image.open(imagefile) as im:
		with Image.new('RGBA', im.size, fill_color) as canvas:

			canvas_im = Image.alpha_composite(canvas,im)
			canvas_im = canvas_im.convert("RGB")

			canvas_im.save(PNG_OUT,"PNG")


	h = Image.open(imagefile)
	unlock  = pytesseract.image_to_string(h)


	isCheckitString = unlock.replace(" ","").replace("\n","")
	print(isCheckitString)


class MyHandler(http.server.BaseHTTPRequestHandler):
	def do_POST(self):
		
		content_len = int(self.headers.get('Content-Length'))
		post_body = self.rfile.read(content_len)[4:]
		b64 = parse_req(post_body)
		save_png(PNG_OUT,b64)
		pwn = get_text(PNG_OUT)
		# print(pwn)

		self.send_header('Access-Control-Allow-Origin', '*')
		self.end_headers()
	

		return None


while True:

	s = http.server.HTTPServer(('localhost',80),MyHandler)
	s.serve_forever()