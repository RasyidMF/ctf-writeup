from PIL import Image

img 	= Image.open("out copy.jpg")
pixel	= img.load()

flag	= Image.new("RGB", (304, 92), "white")
pixel_f = flag.load()

column = 0

for x in range(flag.size[0]):
	for i in range(flag.size[1]):
		pixel_f[x, i] = pixel[column, 0]
		column = column + 1

flag.save("flag.jpg")

