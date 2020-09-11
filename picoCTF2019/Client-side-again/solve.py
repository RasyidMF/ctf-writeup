
flag = []
for _ in range(33):
	flag.append(" ") # We knew that flag size is 32

def setSubString(_start, _end, value):
	i = 0
	# Create safe string array
	d = []
	for a in range(0, (_end - _start)):
		if a > len(value) - 1:
			d.append(" ")
		else:
			d.append(value[a])
	for x in range(_start, _end):
		flag[x] = d[i]
		i = i + 1


setSubString(0, 8, "picoCTF")
setSubString(0x7, 0x9, "{n")
setSubString(8, 16, "not_this")
setSubString(24, 32, "25df2}")
setSubString(16, 24, "_again_b")
print ''.join(flag)
