# We want Nudes instead of Nukes (90 Points)
Donald has gone completely crazy. To prevent world chaos, you kidnapped him. Right before the kidnapping he tried to send one encrypted message to his wife Melania. Luckily you intercepted the message. Donald admits that he used AES-CBC encryption - a block cipher operating with a block length of 16 bytes. (here represented by 32 characters)<br /> The message was: {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
<br>
The format contains first the Initialization vector(IV) and then the cipher text(c) separated by a colon all wrapped in curly braces. {IV,c} After torturing him by stealing his hairpiece, he tells you the plain text of the message is:
<br>
FIRE_NUKES_MELA!
<br>
As a passionate hacker you of course try to take advantage of this message. To get the flag alter the message that Melania will read: SEND_NUDES_MELA!
<br>
Submit the flag in the format: flag{IV,c}
<br>
The characters are hexlified, and one byte is represented by two characters; e.g. the string "84" represents the character "F" of the message and so on.
# Solved
Pada challenge ini kita disuruh input flag dengan <b>IV</b> dan <b>c</b>
```
The message was : {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
```
Pada note tersebut ada 2 pesan, yaitu <b>FIRE_NUKES_MELA!</b> dan <b>SEND_NUDES_MELA!</b>. Digunakan untuk key dari <b>XOR Encrypt</b> agar menghasilkan value untuk <b>IV</b>. Disini juga saya melihat enkripsi dari IV adalah
```
The characters are hexlified, and one byte is represented by two characters; e.g. the string "84" represents the character "F" of the message and so on.

IV ^ MESSAGE ^ MELANIA
```
Inilah code yang saya gunakan
```python
# {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
IV = bytearray.fromhex("391e95a15847cfd95ecee8f7fe7efd66")
C  = bytearray.fromhex("8473dcb86bc12c6b6087619c00b6657e")

# FIRE_NUKES_MELA!
MESSAGE = bytearray.fromhex("464952455f4e554b45535f4d454c4121")

# SEND_NUDES_MELA!
MELANIA = bytearray.fromhex("53454e445f4e554445535f4d454c4121")

RES = bytearray()

for x in range(16): # Length of Message
    RES.append(IV[x] ^ MESSAGE[x] ^ MELANIA[x])

print(RES.hex())
```
```console
$ python3 solve.py
2c1289a05847cfd65ecee8f7fe7efd66
```
Yang dihasilkan dari code nya adalah <b>IV</b>, kemudian saya masukkan dan parse menjadi
```
flag{2c1289a05847cfd65ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
```
Dan saya input, ternyata flag benar.<br>
Flag : <b>flag{2c1289a05847cfd65ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}</b>