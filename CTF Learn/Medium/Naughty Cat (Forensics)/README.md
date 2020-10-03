# Naughty Cat (50 Points)
I think my cat is hiding something...
# Solved
Saya menggunakan binwalk untuk mengektrak file dari gambar tersebut, diketahui bahwa file .rar nya Rusak. setelah saya cek HexDump nya ternyata <b>Header</b> file tersebut di ubah menjadi Cat
```console
00000000: 4361 7421 1a07 0100 3392 b5e5 0a01 0506  Cat!....3.......
00000010: 0005 0101 8080 007c bc22 8d58 0203 3c90  .......|.".X..<.
00000020: 0104 c102 2067 b83d 0880 0300 0b66 316e  .... g.=.....f1n
00000030: 346c 6c79 2e74 7874 3001 0003 0f67 c16b  4lly.txt0....g.k
00000040: 5eea ad33 4801 8fe1 06a1 a1b4 9cd8 7130  ^..3H.........q0
00000050: d73e 873b f253 bf05 2444 2af9 7806 4f48  .>.;.S..$D*.x.OH
00000060: 7a08 9021 dcde 2e38 b30a 0302 7d84 a466  z..!...8....}..f
00000070: 0f01 d601 1485 be3b 2d96 5f8c 4f57 4711  .......;-._.OWG.
00000080: b087 2992 f043 d1ee ab9a 4f1a 3408 dc6a  ..)..C....O.4..j
00000090: fd43 2438 9f7c c279 9461 8767 409d 196d  .C$8.|.y.a.g@..m
000000a0: f2b3 4377 9aa9 f326 ba94 fa90 88e7 e1f3  ..Cw...&........
000000b0: 3f4f ca1b 9ccb 4b5f 566b 915a 0f03 7572  ?O....K_Vk.Z..ur
000000c0: 9c39 4967 f1c7 1499 10b4 78cf 6cbb eae9  .9Ig......x.l...
000000d0: 9035 eb88 bcff 9ae3 2d2e eab2 2cdc c281  .5......-...,...
000000e0: 8fde 1db7 a8ab ea0d 8863 8e80 0ee3 1c37  .........c.....7
000000f0: 9205 0565 28b2 cb2b d9fb 67d0 6263 bbe7  ...e(..+..g.bc..
00000100: be57 694a 1d77 5651 0305 0400            .WiJ.wVQ....
```
Kemudian saya perbaiki https://en.wikipedia.org/wiki/List_of_file_signatures
```console
52 61 72 21 1A 07 00
```
Kemudian pas saya ingin mengekstraknya, ternyata butuh Password!
```console
$ unrar e y0u_4r3_cl0s3.rar

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal


Extracting from y0u_4r3_cl0s3.rar

Enter password (will not be echoed) for f1n4lly.txt:
```
Kemudian setelah saya menjalankan perintah strings pada file purrr
```console
$ strings purrr_2.mp3
 -TPE1
is a password here?
```
Kemudian setelah saya menjalankan <b>Sonic Visualiser</b> saya menemukan teks pada file tersebut
```
sp3ctrum_1s_y0ur_fr13nd
```
Ekstrak file tersebut dengan menggunakan password tadi
```console
$ cat f1n4lly.txt
            __/|
            \o.O|
       _____(___)______
      |       U        |________    __
      |ZjByM241MWNzX21h|        |__|  |_________
      |________________|NXQzcg==|::|  |        /
      |                \._______|::|__|       <
      |                         \::/  \._______\
      |
      |

$ echo 'ZjByM241MWNzX21hNXQzcg==' | base64 -d
f0r3n51cs_ma5t3r
```
Flag : <b>f0r3n51cs_ma5t3r</b>