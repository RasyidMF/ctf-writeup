from PIL import Image

im = Image.open("color_img.png", "r")

data = list(im.getdata())

unique = []

for x in data:
    if not x in unique:
        unique.append(x)

res = ""

for x in unique:
    res += chr(x[0])
    res += chr(x[1])
    res += chr(x[2])

print res