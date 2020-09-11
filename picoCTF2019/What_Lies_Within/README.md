# What Lies Within - Points: 150
<b>Description : </b>Theres something in the building. Can you retrieve the flag?<br>
<b>Hints : </b>There is data encoded somewhere, there might be an online decoder
# Solved
Im trying to check file with binwalk this what i got
```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 657 x 438, 8-bit/color RGBA, non-interlaced
41            0x29            Zlib compressed data, compressed
```
Well i believe this file has some Crypto called <b>Steganography</b>, im try to decode online (https://stylesuxx.github.io/steganography/) this is what i got
```
picoCTF{h1d1ng_1n_th3_b1t5} ... (Some Byte)
```
Flag : <b>picoCTF{h1d1ng_1n_th3_b1t5}</b>
