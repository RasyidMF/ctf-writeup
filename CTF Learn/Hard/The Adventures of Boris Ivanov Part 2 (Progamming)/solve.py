from PIL import Image

flag = Image.new("RGB", (500, 500), "black")

no = 0
while no < 500:
    img = Image.open(str(no) + ".png")
    flag.paste(img, (0, no))
    no += 1

flag.save("flag.png")