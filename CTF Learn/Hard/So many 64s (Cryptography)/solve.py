import base64

f = open("flag.txt", "r")
h = f.read()

while True:
	h = base64.b64decode(h).decode("utf-8")
	if '{' in h:
		print(h)
		break

