# MountainMan (50 Points)
Don't be fooled by two 0xffd9 markers. xor is your friend.
# Solved
Disini kita diberikan sebuah gambar yang pada gambar tersebut tidak memiliki file lainnya, akan tetapi disini ada hint yang cukup mencurigakan
```
$ xxd MountainMan.jpg | grep "ff d9"
0001edd0: ab43 5d03 c115 1c29 19ff d988 9f8d a7ae  .C]....)........
0001edf0: b6ff d9
```
Setelah saya analisi, terdapat <b>Hex</b> pada akhir file, kemudian dikatakan lagi <b>XOR is your friend</b>, nah maka dari itu saya copy
```
88 9F 8D A7 AE AA B9 A5 B0 9E A9 BE A5 BF BE 94 B9 FB A8 A0 FE B6
```
Menggunakan https://www.dcode.fr/xor-cipher
```
[11001011]: 0100001101010100...	CTFlearn{Ubuntu_r0ck5}
```
Flag : <b>CTFlearn{Ubuntu_r0ck5}</b>