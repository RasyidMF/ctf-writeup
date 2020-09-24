# Tux! (20 Points)
The flag is hidden inside the Penguin! Solve this challenge before solving my 100 point Scope challenge which uses similar techniques as this one.
# Solved
Gunakan perintah
```
$ binwalk -D=".*" Tux.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
5488          0x1570          Zip archive data, encrypted at least v1.0 to extract, compressed size: 39, uncompressed size: 27, name: flag
5679          0x162F          End of Zip archive, footer length: 22
```
Kemudian pindah ke folder hasil ekstrak dari binwalk
```
$ file *
0:    JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, comment: "ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK", baseline, precision 8, 196x216, components 3
1570: Zip archive data, at least v1.0 to extract
162F: Zip archive data (empty)
```
Kita lihat disini, terdapat komentar yang terencoded dengan base64 mari kita decode
```
$ echo 'ICAgICAgUGFzc3dvcmQ6IExpbnV4MTIzNDUK' | base64 -d
Password: Linux12345
```
Mungkin sebuah password untuk mengunzip file <b>1570</b>
```
$ unzip 1570
Archive:  1570
[1570] flag password:
    extracting: flag
```
Yep, mari kita coba buka file flag nya
```
$ cat flag
CTFlearn{Linux_Is_Awesome}
```
Flag : <b>CTFlearn{Linux_Is_Awesome}</b>