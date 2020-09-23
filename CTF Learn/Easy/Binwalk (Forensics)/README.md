# Binwalk (30 Points)
Here is a file with another file hidden inside it. Can you extract it? https://mega.nz/#!qbpUTYiK!-deNdQJxsQS8bTSMxeUOtpEclCI-zpK7tbJiKV0tXYY
# Solved
Ketik perintah
```
$ binwalk -D=".*" PurpleThing.jpeg
```
Kemudian pindah ke directory hasil binwalk tadi, kemudian ada file yang bernama <b>25795</b>, Cek ektensi file tersebut menggunakan perintah <b>file</b>
```
$ file 25795
25795: PNG image data, 802 x 118, 8-bit/color RGBA, non-interlaced
```
File tersebut adalah sebuah gambar yang berektensi <b>PNG</b>. Maka dari itu mari kita ubah nama file tersebut menjadi <b>25795.png</b> dan buka gambar tersebut! <br>
Flag : <b>ABCTF{b1nw4lk_is_us3ful}</b>
