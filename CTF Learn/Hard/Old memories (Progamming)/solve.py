from PIL import Image

img1 = Image.open("1.png", "r")
img2 = Image.open("2.png", "r")

p1 = img1.load()
p2 = img2.load()

size = 512

for x in range(size):
    for i in range(size):
        if not p1[x, i] == p2[x, i]:
            p1[x, i] = 255
        else:
            p1[x, i] = 0

img1.save("solve.png")