f = open("fl4g.jpeg", "rb")
byteimg = b""
fbyte = bytearray(f.read(4))

while fbyte:
    byteimg += fbyte[::-1]
    fbyte = f.read(4)

f = open("result.jpeg", "wb")
f.write(byteimg)
f.close()