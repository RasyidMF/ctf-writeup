flag = []

for x in range(28):
	flag.append(".")

first = "CTFlearn{"
for x in range(len(first)):
	flag[x] = first[x]

flag[len(flag) - 1] = chr(125)
flag[17] = chr(95)


print ''.join(flag)
