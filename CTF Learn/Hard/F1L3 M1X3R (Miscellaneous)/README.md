# F1L3 M1X3R (80 Points)
I think my amazing photo was hit by a mixer and now it is not working. Help me fix it? https://mega.nz/#!Ds0mWaCJ!4uKfJeJwhupG7Tvx8ReTBP1reFgdzRLE3YrN0l-5Jrg hint: visit: https://en.wikipedia.org/wiki/List_of_file_signatures Programming might be useful in this challenge
# Solved
Diberikan sebuah gambar korup yang tidak dapat dibuka, kemudian saya cek signature file tersebut
```console
00000000: e0ff d8ff 464a 1000 0100 4649 6000 0101  ....FJ....FI`...
```
Jika dilihat pada <b>WikiPedia</b>
```
FF D8 FF E0 00 10 4A 46 49 46 00 01
```
Disini saya melihat bahwa file tersebut telah di <b>Reverse</b> dari Header / Content / dll nya, jadi saya solving menggunakan python untuk memutarbalikkan lagi
```python
f = open("fl4g.jpeg", "rb")
byteimg = b""
fbyte = bytearray(f.read(4))

while fbyte:
    byteimg += fbyte[::-1]
    fbyte = f.read(4)

f = open("result.jpeg", "wb")
f.write(byteimg)
f.close()
```
Kemudian buka file <b>result.jpeg</b>
```
Flag{byt3_sw4p}
```
Flag : <b>Flag{byt3_sw4p}</b>