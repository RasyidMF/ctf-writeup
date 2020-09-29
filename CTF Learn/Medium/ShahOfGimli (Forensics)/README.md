# ShahOfGimli (50 Points)
That still only counts as one!
# Solved
Disini ada beberapa fake flag / hint yang saya dapatkan
```
CTFlearn{Gimli_Was_Part_Of_The_Fellowship_Of_The_Ring}
CTFlearn{Gimli.Is.A.Dwarf}

Who is Gimli?  You can learn more about Gimli here:
https://lotr.fandom.com/wiki/Gimli
https://en.wikipedia.org/wiki/Gimli_(Middle-earth)

This challenge is based on hash algorithms and encryption.

I am using OPENSSL v1.1.1 to create this challenge.

Here is a reference for using hash calculations with OPENSSL:
https://www.openssl.org/docs/man1.1.1/man1/openssl-dgst.html

If you are a Python coder, Python provides a hashing library you might find useful:
https://docs.python.org/3/library/hashlib.html

If this challenge has you wondering what to do next, please try my other challenges
that are worth fewer points.  The more points, the more difficult the challenge.

If you are new to CTF and/or not quite sure how to solve this challenge,
you should probably try these other challenges first in this order:
RubberDuck
Snowboard
PikesPeak
GandalfTheWise

After solving this ShahOfGimli challenge, then try:
HailCaesar
MountainMan
KeyMaker
VargasIsland

My Twitter DM's are open @kcbowhunter.

----------------------------

The third comment block is encrypted with AES CBC encryption using the following key:
sha256 hash of the string "CTFlearn"

Note that the comment block is also base64 encoded
There is no iv but you need to determine how to express this mathematically

If you are new to encryption and hash algorithms here is a good place to start:
openssl enc -help
openssl dgst -help
sha256sum

Of course Google is your friend (if you don't mind them recording all your online activity)

https://wiki.openssl.org/index.php/Enc is a good reference for openssl encryption algorithms
https://docs.python.org/3/library/hashlib.html
```
Dan pada baris ke-3 adalah hint nya berada yang menggunakan enkripsi openssl menggunakan key <b>Sha256 (CTFlearn)</b>
```
TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8va
CK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4
A3aM2Mp0AGDPrK3X4eMu8Q==
```
Inilah code untuk mengekstrak hint tersebut
```python
import base64
import os

key  = "b18ef1351fc0df641abbe56dcd4928a8bb98452b1b43d8c1c13f1874c8b35056" # SHA256 of CTFlearn 
hint = "TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8vaCK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4A3aM2Mp0AGDPrK3X4eMu8Q=="

f = open("hint.enc", "wb")
f.write(base64.b64decode(hint))
f.close()

iv = 00000000000000000000000000000000 # Since there is none hint for IV, let it set as 0 * 32
os.system("openssl enc -d -aes-256-cbc -iv " + str(iv) + " -K " + str(key) + " -in hint.enc -out hint.txt -nopad")
```
```
CTFlearn{The_Shah_Of_Gimli_Is_The_Key}
CTFlearn{Gimli_Has_256_Gemstones}
CTFlearn{Breakfast_Hash_Is_The_Best}
```
Sebelum itu kita tau bahwa file ini memiliki file lainnya
```
$ binwalk -D=".*" ShahOfGimli.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
132375        0x20517         gzip compressed data, from Unix, last modified: 1970-01-01 00:00:00 (null date)

$ file *
0:       JPEG image data, JFIF standard 1.01, resolution (DPI), density 0x0, segment length 16, comment: "CTFlearn{Gimli_Was_Part_Of_The_Fellowship_Of_The_Ring}", comment: "Q1RGbGVhcm57R2ltbGkuSXMuQS5Ed2FyZn0KCldobyBpcyBHaW1saT8gIFlvdSBjYW4gbGVhcm4g", comment: "TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8va", comment: "uq3wDbqt8A26rfANuq3wDQ==", comment: "5VVoFK+6zDi3cJLX57zPLkf4WnbqsA6nywxZp9B+GGJP", comment: "H4sIAAAAAAAAA+1YWW/bOBDOq/UrWPnFQp1Ukp2jRtKizdED22ObFlggDQzKpm1tZMmQ6MbZIP99", baseline, precision 8, 720x540, components 3
20517:   POSIX tar archive (GNU)
20517-0: gzip compressed data, from Unix, original size modulo 2^32 3657367552 gzip compressed data, reserved method, ASCII, was "", has comment, from FAT filesystem (MS-DOS, OS/2, NT), original size modulo 2^32 3657367552

$ tar xvf 20517
Gimli04Base.jpg
flag.enc
```
Untuk mengdecode hal tersebut, kita diperlukan kunci lagi, dan kunci tersbut hasil sha256 dari <b>Gimli</b>
```
$ sha256sum Gimli04Base.jpg
e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87  Gimli04Base.jpg
```
Kemudian jalankan perintah
```
openssl enc -d -aes-256-cbc -iv 00000000000000000000000000000000 -K e26db845ae634c7d774f8924a565e34e215b659a97c7e1d01a401fea7c5f6d87 -in flag.enc -out flag.txt -nopad
```
```
$ cat flag.txt
CTFlearn{Gimli.Is.A.Warrior}
```
Flag : <b>CTFlearn{Gimli.Is.A.Warrior}</b>