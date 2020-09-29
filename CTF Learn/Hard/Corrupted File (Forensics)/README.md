# Corrupted File (70 Points)
Help! I can't open this file. Something to do with the file header… Whatever that is. https://mega.nz/#!aKwGFARR!rS60DdUh8-jHMac572TSsdsANClqEsl9PD2sGl-SyDk
# Solved
Diberikan sebuah file yang <b>Header</b> nya di ubah, mari kita fix menggunakan HxD. <i>Perlu diketahui, file tersebut adalah <b>GIF</b></i>
```
?? MISSING SIGNATURE ?? 39 61 F4 01 F4 01 F4
```
Yang saya lakukan adalah menambahkan <b>4 Byte</b> lagi yaitu
```
GIF8
```
Hasil
```
GIF89a
```
Kemudian buka file tersebut
```
ZmxhZ3tnMWZfb3JfajFmfQ==
```
```
$ echo 'ZmxhZ3tnMWZfb3JfajFmfQ==' | base64 -d
flag{g1f_or_j1f}
```
Flag : <b>flag{g1f_or_j1f}</b>