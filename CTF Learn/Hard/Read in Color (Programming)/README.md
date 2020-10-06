# Read in Color (70 Points)
I was sent this picture by an unknown individual, and after putting it through a hex editor, I found nothing out of the ordinary hidden inside. A message came with the image saying, "Can You Read Me?" Could you help me figure out what the hidden message says?? I can't figure out another way to read the image! Maybe Python's Pillow library can help you out? https://mega.nz/#!XewWgaaR!oXBHx7ZrmiKeRZy2OEfxTrrWcw511KCokzjNlBWV0Ao
# Solved
```python
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
```
```console
$ python solve.py
flag{c0l0r_c0d3d}
```
Flag : <b>flag{c0l0r_c0d3d}</b>

