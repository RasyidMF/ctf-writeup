# 07601 (60 Points)
https://mega.nz/#!CXYXBQAK!6eLJSXvAfGnemqWpNbLQtOHBvtkCzA7-zycVjhHPYQQ I think I lost my flag in there. Hopefully, it won't get attacked...
# Solved
Disini ada beberapa fake flag yaitu <i>setelah saya menggunakan perintah <b>strings</b></i>
```
ABCTF{fooled_ya_dustin}
```
Saya mengetahui bahwa didalam gambar ini terdapat file lainnya, jadi saya menggunakan perintah
```
$ binwalk -M -D=".*" AGT.png

Scan Time:     2020-09-25 11:44:43
Target File:   /home/rasyidmf/ctf-writeup/CTF Learn/Medium/07601 (Forensics)/AGT.png
MD5 Checksum:  78fa8c6e483d2fdf9f109d10fec336eb
Signatures:    391

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
9584          0x2570          Zip archive data, at least v1.0 to extract, name: Secret Stuff.../
9646          0x25AE          Zip archive data, at least v2.0 to extract, name: Secret Stuff.../.DS_Store
10270         0x281E          Zip archive data, at least v1.0 to extract, name: __MACOSX/
10325         0x2855          Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../
10396         0x289C          Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../._.DS_Store
10546         0x2932          Zip archive data, at least v1.0 to extract, name: Secret Stuff.../Don't Open This.../
10627         0x2983          Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../.DS_Store
10988         0x2AEC          Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../
11078         0x2B46          Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../._.DS_Store
11247         0x2BEF          Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../I Warned You.jpeg
150550        0x24C16         Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../._I Warned You.jpeg
151810        0x25102         End of Zip archive, footer length: 22
151832        0x25118         Zip archive data, at least v1.0 to extract, name: Secret Stuff.../
151894        0x25156         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../.DS_Store
152518        0x253C6         Zip archive data, at least v1.0 to extract, name: __MACOSX/
152573        0x253FD         Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../
152644        0x25444         Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../._.DS_Store
152794        0x254DA         Zip archive data, at least v1.0 to extract, name: Secret Stuff.../Don't Open This.../
152875        0x2552B         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../.DS_Store
153236        0x25694         Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../
153326        0x256EE         Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../._.DS_Store
153495        0x25797         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../I Warned You.jpeg
292768        0x477A0         Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../._I Warned You.jpeg
294028        0x47C8C         End of Zip archive, footer length: 22
294050        0x47CA2         Zip archive data, at least v1.0 to extract, name: Secret Stuff.../
294112        0x47CE0         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../.DS_Store
294736        0x47F50         Zip archive data, at least v1.0 to extract, name: Secret Stuff.../Don't Open This.../
294817        0x47FA1         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../.DS_Store
295162        0x480FA         Zip archive data, at least v2.0 to extract, name: Secret Stuff.../Don't Open This.../I Warned You.jpeg
434433        0x6A101         Zip archive data, at least v1.0 to extract, name: __MACOSX/
434488        0x6A138         Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../
434559        0x6A17F         Zip archive data, at least v1.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../
434649        0x6A1D9         Zip archive data, at least v2.0 to extract, name: __MACOSX/Secret Stuff.../Don't Open This.../._I Warned You.jpeg
435702        0x6A5F6         End of Zip archive, footer length: 22
```
```
$ file *
0: JPEG image data, JFIF standard 1.01, aspect ratio, density 1x1, segment length 16, baseline, precision 8, 300x168, components 3
25102: Zip archive data (empty)
25118: Zip archive data, at least v1.0 to extract
2570:  Zip archive data, at least v1.0 to extract
47C8C: Zip archive data (empty)
47CA2: Zip archive data, at least v1.0 to extract
6A5F6: Zip archive data (empty)
```
Disana banyak terdapat File zip yang harus kita unzip filenya dan saya coba 1 1, file tersebut mengekstrak gambar yang bernama
```
I Warned You.jpeg
```
Kemudian saya menjalankan perintah <b>strings</b>
```
ABCTF{Du$t1nS_D0jo}
```
Lokasi flag tidak ada berada pada awal utama strings ataupun akhiran, akan tetapi di pertengahan ! <br>
Flag : <b>ABCTF{Du$t1nS_D0jo}</b>