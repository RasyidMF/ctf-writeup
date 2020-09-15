# c0rrupt - Points: 250
<b>Description : </b>We found this file. Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.<br>
<b>Hints : </b>Try fixing the file header
# Solved
I try to analyzing the file with this command <b>file</b>
```
mystery: data
```
Seems like we need to read signature file in first line
```
00000000: 8965 4e34 0d0a b0aa 0000 000d 4322 4452  .eN4........C"DR
00000010: 0000 066a 0000 0447 0802 0000 007c 8bab  ...j...G.....|..
00000020: 7800 0000 0173 5247 4200 aece 1ce9 0000  x....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 aa00 1625 0000 1625 0149  ..pHYs...%...%.I
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
00000060: 8e64 cd71 bd2d 8b20 2080 9041 8302 08d0  .d.q.-.  ..A....
00000070: f9ed 40a0 f36e 407b 9023 8f1e d720 8b3e  ..@..n@{.#... .>
00000080: b7c1 0d70 0374 b503 ae41 6bf8 bea8 fbdc  ...p.t...Ak.....
00000090: 3e7d 2a22 336f de5b 55dd 3d3d f920 9188  >}*"3o.[U.==. ..
000000a0: 3871 2232 eb4f 57cf 14e6 25ff e5ff 5b2c  8q"2.OW...%...[,
000000b0: 168b c562 b158 2c16 8bc5 62b1 582c 161d  ...b.X,...b.X,..
000000c0: d6d7 678b c562 b158 2c16 8bc5 62b1 582c  ..g..b.X,...b.X,
000000d0: 168b 4597 f5f5 d962 b158 2c16 8bc5 62b1  ..E....b.X,...b.
000000e0: 582c 168b c562 d165 7d7d b658 2c16 8bc5  X,...b.e}}.X,...
000000f0: 62b1 582c 168b c562 b158 7459 5f9f 2d16  b.X,...b.XtY_.-.
00000100: 8bc5 62b1 582c 168b c562 b158 2c16 5dd6  ..b.X,...b.X,.].
00000110: d767 8bc5 62b1 582c 168b c562 b158 2c16  .g..b.X,...b.X,.
00000120: 8b45 97f5 f5d9 62b1 582c 168b c562 b158  .E....b.X,...b.X
```
We can see, header file simmilar with <b>PNG header / signature / magic number</b>. <i>Well if you correct again, there is word <b>sRGB so we can sure this is a image file</b></i>
```
PNG : 89 50 4E 47 0D 0A 1A 0A
Current : 89 65 4E 34 0D 0A B0
```
Lets try to change the header byte, and try to check the image file using <b>pngcheck</b>
```
mystery  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERROR: mystery
```
<b>Note: A valid PNG image must contain an IHDR chunk, one or more IDAT chunks, and an IEND chunk.<br>
I think i missing smthing, well yeah we can see right here there is no <b>IHDR Image header</b>. As i know there is 4 Character called <b>C"DR</b> well we need to change it into <b>IHDR</b>
```
43 22 44 52 = C"DR
49 48 44 52 = IHDR
```
After i fixing the <b>IHDR</b>, now we must check <b>IDAT chunks</b>, im kinda confusing to find where i must to place <b>IDAT</b> header untill i found this
```
00000050: 5224 f0aa aaff a5ab 4445 5478 5eec bd3f  R$......DETx^..?
```
We see there is <b>.DET (ab 44 45 54)</b>, meanwhile the letter is <b>IDAT (49 44 41 54)</b>, 2 Character include <b>D</b> amd <b>T</b>. So that is a <b>IDAT Chunk</b>. Try to change that and check the file again
```
mystery  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERROR: mystery
```
To see the specific length and error CRC using this command <b>pngcheck -v mystery</b>
```
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERRORS DETECTED in mystery
```
We see this message <b>CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)</b>, our CRC <b>pHYs</b> was wrong calculated. So i change the <b>expected</b> into <b>computed</b> in
```
before:
00000040: 0009 7048 5973 aa00 1625 0000 1625 01<b>49</b>
00000050: <b>5224 f0</b>aa aaff a5ab 4445 5478 5eec bd3f

after:
00000040: 0009 7048 5973 aa00 1625 0000 1625 01<b>38</b>
00000050: <b>d82c 82</b>aa aaff a5ab 4445 5478 5eec bd3f
```
Try to check the image file again
```
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
:  invalid chunk length (too large)
ERRORS DETECTED in mystery
```
The last thing we need to do is calculating the <b>Chunk Size</b>, known size :
```
AA AA FF A5
```
Thats to large right, i try to change with my knowledge
```
before:
AA AA FF A5

after:
00 00 FF A5
```
And try to check image
```
File: mystery (202940 bytes)
  chunk IHDR at offset 0x0000c, length 13
    1642 x 1095 image, 24-bit RGB, non-interlaced
  chunk sRGB at offset 0x00025, length 1
    rendering intent = perceptual
  chunk gAMA at offset 0x00032, length 4: 0.45455
  chunk pHYs at offset 0x00042, length 9: 2852132389x5669 pixels/meter
  chunk IDAT at offset 0x00057, length 65445
    zlib: deflated, 32K window, fast compression
  chunk IDAT at offset 0x10008, length 65524
  chunk IDAT at offset 0x20008, length 65524
  chunk IDAT at offset 0x30008, length 6304
  chunk IEND at offset 0x318b4, length 0
No errors detected in mystery (9 chunks, 96.3% compression).
``
No errors ? Well that nice guess i think. <b>Well in my mind, i never see that big chunk size, well i just try it and boom</b>, Open the image and see the flag!<br>
Flag : <b>picoCTF{c0rrupt10n_1847995}</b>