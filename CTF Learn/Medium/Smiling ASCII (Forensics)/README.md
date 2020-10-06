# Smiling ASCII (40 Points)
Find the flag on the smiling face.
# Solved
Diberikan sebuah gambar yang memilik ASCII pada gambar tersebut. Saya menggunakan <b>zsteg</b> untuk menyelesaikan ini
```console
$ zsteg smiling.png -a
[?] 104 bytes of extra data after image end (IEND), offset = 0xe6cd
extradata:0         .. text: "RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg=="
b3,abgr,lsb,xy      .. file: very old 16-bit-int little-endian archive
b1,rgba,lsb,yx      .. file: AIX core file
b1,abgr,lsb,yx      .. file: AIX core file fulldump 32-bit
b8,g,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
b8,a,lsb,yx         .. text: "CTFlearn{ascii_pixel_flag}"
b4,r,lsb,yx,prime   .. file: AIX core file fulldump 32-bit
b4,g,lsb,yx,prime   .. file: AIX core file 32-bit
b8,g,lsb,yx,prime   .. text: "Flancixla"
b8,a,lsb,yx,prime   .. text: "Flancixla"
```
Disana terdapat Key juga
```
$ echo 'RGlkIHlvdSBrbm93IHRoYXQgcGl4ZWxzIGFyZSwgbGlrZSB0aGUgYXNjaWkgdGFibGUsIG51bWJlcmVkIGZyb20gMCB0byAyNTU/Cg==' | base64 -d
Did you know that pixels are, like the ascii table, numbered from 0 to 255?
```
Flag : <b>CTFlearn{ascii_pixel_flag}</b>