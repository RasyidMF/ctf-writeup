f = open("dotted", "r")
r = f.read()

flag = []
c = 0
for x in r:
	if x == ".":
		c = c + 1
	elif x == " ":
		flag.append(c)
		c = 0
print ''.join([chr(x) for x in flag])

