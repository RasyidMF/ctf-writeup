# Bobby Toe's iPad (70 Points)
Here is a pic of my friend Bobby Toe. while he's happy to give you his iPad, he's not as willing to give you the flag. can you get it from him? here is an image of Bobby Toe: https://mega.nz/#!iWAm2KJL!2uRVDKrHOWryZkZNW6leV0sQMh-b0-AYQksa3i-A3Eg
# Solved
Saat saya menjalankan perintah <code>strings</code> saya menemukan
```
congrats you found me! you win an iPad!
```
Pada file gambar ini tidak memiliki file lainnya, akan tetapi jika kita analisis lebih dalam menggunakan xxd
```
$ xxd bobbytoesipad.png | grep "congrats"
000101a0: ffd8 ffe0 0063 6f6e 6772 6174 7320 796f  .....congrats yo
```
Saya menemukan signature jpg https://www.filesignatures.net/index.php?page=search&search=JPG&mode=EXT
```
FF D8 FF E0

JPG	    FF D8 FF E0	JPEG IMAGE
 	    ASCII
Sizet   : 4 Bytes
Offset  : 0 Bytes
```
Dan setelah teks dari <b>congrats...</b> terdapat teks <b>JFIF</b>.
```
000101a0: ffd8 ffe0 0063 6f6e 6772 6174 7320 796f  .....congrats yo
000101b0: 7520 666f 756e 6420 6d65 2120 796f 7520  u found me! you
000101c0: 7769 6e20 616e 2069 5061 6421 104a 4649  win an iPad!.JFI
000101d0: 4600 0101 0100 4100 4100 00ff db00 4300  F.....A.A.....C
```
Sedangkan pada baris tersebut ada penghalangan <b>congrats..</b> kemudian saya menghapus teks tersebut. Disitu bisa kita lihat bahwa ada signature <b>JFIF</b> https://www.filesignatures.net/index.php?search=JFIF&mode=EXT. Kemudian saya ambil raw-data nya ke python untuk melakukan pengekstrakan
```
$ python secimage.py
```
saya menemukan 1 gambar lagi yang berisi teks
```
bbbabydonthurtmewhatislove
```
Kemudian pada gambar pertama, saya menggunakan <b>stegsolve</b> untuk menyelesaikan nya! Pada <b>Red Plane 0</b> saya menemukan pesan
```
zpv_tigqylhbafmeoesllpms

BobbyToe
```
Challenge nya menunjukan petunjuk untuk mengdecode flag tersebut http://rumkin.com/tools/cipher/otp.php dan meminta <b>The pad</b>
```
Your Message :
zpv_tigqylhbafmeoesllpms
The pad :
bbbabydonthurtmewhatislove
```
```
you_thinkyougotskillshuh
```
Flag : <b>you_thinkyougotskillshuh</b>