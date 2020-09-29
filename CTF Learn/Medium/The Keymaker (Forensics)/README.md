# The Keymaker (50 Points)
Jpeg comments can be very interesting.
# Solved
Disini ada beberapa fake flag yaitu
```
CTFlearn{TheKeymakerIsK00l}
```
Dan ada beberapa hint pada komentar dalam file tersebut
```
$ file The-Keymaker.jpg
The-Keymaker.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 100x100, segment length 16, comment: "CTFlearn{TheKeymakerIsK00l}", comment: "b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg", comment: "mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY", baseline, precision 8, 200x190, components 3

$ echo 'b3BlbnNzbCBlbmMgLWQgLWFlcy0yNTYtY2JjIC1pdiBTT0YwIC1LIFNPUyAtaW4gZmxhZy5lbmMg' | base64 -d
openssl enc -d -aes-256-cbc -iv SOF0 -K SOS -in flag.enc

$ echo 'mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY' | base64 -d
# Unicode data
```
Bisa saya simpulkan, pada base64 encoded pertama adalah hint cara kita untuk mengdecode hasil enkripsi ssl pada base64 encoded ke 2
```
$ echo 'mmtaSHhAsK9pLMepyFDl37UTXQT0CMltZk7+4Kaa1svo5vqb6JuczUqQGFJYiycY' | base64 -d > flag.enc
```
Nah mari kita cari tau bagaimana mendapatkan kunci untuk mengdecrypt flag tersebut, dikatakan pada hint tersebut <b>SOF0</b> https://www.ccoderun.ca/programming/2017-01-31_jpeg/
```
SOF0:
    start of frame (baseline DCT)

    Hex:
    0xFF 0xC0

    Size:
    Variable size. Typically 0x00 0x11 (17 bytes) for images with 3 components (e.g., YCrCb)
```
<b>SOF0</b> adalah <b>start of frame</b> dari sebuah gambar yang berektensi <b>jpeg</b> dan memiliki besar <b>0x11 / 17 bytes</b>. Mari kita ambil dimanakah hex ini berada
```
Dari 000001F0 FF C0 00 11

08 00 BE 00 C8 03 01 11 00 02 11 01 03 11 01 FF
# 0800BE00C803011100021101031101FF
```
Sedangkan <b>SOS</b>
```
SOS:
    start of scan

    Hex:
    0xFF 0xDA

    Size:
    Complicated. See below for details.
```
Jika mencari di google bahwa, size dari <b>SOS</b> adalah 32 byte. disini kita hanya mengambil 32 byte setelah signature dari <b>SOS</b>
```
00 0C 03 01 00 02 11 03 11 00 3F 00 F9 76 6B FC 44 BE DA 8F 3F 5C 03 1B 92 CB 0E 92 D6 BD C9 52

# 000C03010002110311003F00F9766BFC44BEDA8F3F5C031B92CB0E92D6BDC952
```
Kemudian jadikan 1 untuk mengeksekusi perintah decrypt
```
openssl enc -d -aes-256-cbc -iv 0800BE00C803011100021101031101FF -K 000C03010002110311003F00F9766BFC44BEDA8F3F5C031B92CB0E92D6BDC952 -in flag.enc -out flag.txt -nopad
```
```
$ cat flag.txt
CTFlearn{Ne0.TheMatrix}
```
Flag : <b>CTFlearn{Ne0.TheMatrix}</b>