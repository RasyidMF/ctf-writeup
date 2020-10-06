# The Adventures of Boris Ivanov Part 2 (80 Points)
The KGB agent Boris Ivanov found the place where one of the criminals was hiding for a long time. Unfortunately the criminal disappeared and more than that he shredded the piece of paper with important information. Help Boris to restore it. Here is a bin with the strips of paper: https://mega.nz/#!KLR3gaYD!6qvqvopHKjjzZZ0HC6pnWjXw0Pw5Z9kgKdGQCMXeUb0. Boris is an experienced agent and he instantly realized that the size of the sheet was 500x500
# Solved
Diberikan 500 File gambar yang harus kita gabungkan 1 per 1 dengan besar <b>500x500</b>
```python
from PIL import Image

flag = Image.new("RGB", (500, 500), "black")

no = 0
while no < 500:
    img = Image.open(str(no) + ".png")
    flag.paste(img, (0, no))
    no += 1

flag.save("flag.png")
```
Kemudian diberikan lagi Hexadecimal pada gambar tersebut
```
66 6c 61 67 7b 74 68 33 5f 4b 47 42 5f 6c 30 76 33 73 5f 43 54 46 7d
```
Konversi ke text
```
flag{th3_KGB_l0v3s_CTF}
```
Flag : <b>flag{th3_KGB_l0v3s_CTF}</b>
