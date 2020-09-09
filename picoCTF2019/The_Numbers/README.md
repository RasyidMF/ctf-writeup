# The Numbers - Points: 50
<b>Description : </b>The numbers... what do they mean?<br>
<b>Hints : </b>The flag is in the format PICOCTF{}
# Solved
Saat kita membuka gambar dari <b>the_numbers.png</b>, disitu ada angka-angka unik yang menunjukkan flag nya disana.
Kebetulan sekali di <b>Python</b> memiliki fungsi yang bernama <b>string.ascii_upper/lowercase</b>, saat di test beberapa index
sesuai dengan angka yang ada di gambar (Index - 1), menunjukkan kata-kata yang logikal. Contohnya <b>PICO</b>, setelah yakin
fungsi tersebut adalah jawaban dari challenge ini, kami buat script sederhana untuk meraih flag nya agar cepat dan mudah dipahami!<br>

Number : 
```
[16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]
```
Python Script :
```python
import string

flag = [16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]
a = string.ascii_uppercase
r = ""

for x in flag:
        if x == "{":
                r += "{"
        elif x == "}":
                r += "}"
        else:
                r += a[x - 1]
print r
```
Flag : <b>PICOCTF{THENUMBERSMASON}</b>
