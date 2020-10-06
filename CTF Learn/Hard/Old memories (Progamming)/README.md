# Old memories (80 Points)
General RONX was cleaning up his cupboard last night, when he finds this archive out of the blue. He recalls that it was something about what he loves immensely. But the old General does not remember what it was. He sent this to me but I don't know what to do with it. Can you find it out? https://mega.nz/#!aHhhGAAB!QPWGYtUiW59R_DhE0-Dv7rAm8fqkW1YXmwLsAPZSOK8
# Solved
Diberikan sebuah 2 gambar yang memiliki pixel berbeda, saya menggunakan python untuk menyelesaikan ini
```python
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
```
Buka file <b>solve.png</b> and boom!<br>
Flag : <b>CTF{I_L0V3_PYTH0N}</b>
