index = [
    20, 0, 24, 19, 5, 11, 9, 8, 16, 4, 13, 21, 2, 3, 23, 15, 10, 17, 6, 1, 14, 7, 18, 22, 12
]
pieces = [
    100, 67, 125, 51, 97, 117, 121, 123, 116, 101, 99, 95, 70, 108, 51, 112, 48, 117, 114, 84, 52, 110, 114, 109, 95
]


r = []
for x in range(len(pieces)):
    r.append("")

for x in range(len(pieces)):
    r[index[x]] = chr(int(pieces[x]))

print ''.join(r)
