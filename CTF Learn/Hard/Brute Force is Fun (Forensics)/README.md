# Brute Force is Fun! (140 Points)
You'll need Brute Force to solve this. Knowing Python should help too. Oh! And Base64 encryption of course! Find the flag!
<br>
https://mega.nz/#!vf43RCyC!NNpuYjB3d-gevhsHXefwAAAmzk4tJHxUZr0GnrSDI_c Hash: e82a4b4a0386d5232d52337f36d2ab73
# Solved
Diberikan sebuah gambar yang memiliki file .zip, saya menggukan perintah <b>foremost</b> untuk mengekstrak file tersebut. Kemudian di temui banyak folder yang harus di ekstrak. kemudian saya menggunakan perintah <b>grep</b>
```console
$ grep -rni "ctf"
folders/73/47/p:The password is: "ctflag*****" where * is a number.
folders/73/43/p:The password is: "ctflag*****" where * is a number.
```
Ditemukan 2 kata yang mengatakan bahwa Password nya adalah <b>ctflag*****</b> dan 5 angka yang harus dipecahkan. Disini saya membrute menggunakan python
```python
from zipfile import ZipFile
import itertools
import string

digit = itertools.product(string.digits, repeat=5)

f = ZipFile("./output/zip/00000012.zip")

for x in digit:
    x = ''.join(x)
    res = "ctflag" + x
    # print(res)
    try:
        f.extractall(pwd=bytes(res, 'utf-8'))
        print ("Flag Founded: " + res)
        exit(0)
    except:
        pass
```
Menunggu sekitar <b>2 menit</b>
```console
$ python3 solve.py
Flag Founded: ctflag48625
```
Kemudian ekstrak flag.zip tersebut menggunakan pass yg tadi.
```console
$ cat flag.txt
RkxBR3ttYXlfdGhlX2JydXRlX2ZvcmNlX2JlX3dpdGhfeW91fQ==

$ echo 'RkxBR3ttYXlfdGhlX2JydXRlX2ZvcmNlX2JlX3dpdGhfeW91fQ==
> ' | base64 -d
FLAG{may_the_brute_force_be_with_you}
```
Flag : <b>FLAG{may_the_brute_force_be_with_you}</b>