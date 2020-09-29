# HailCaesar! (40 Points)
You might need to write some Python to solve this challenge. Some encryption may be involved. Good Luck!
# Solved
Disini terdapat fake flag yaitu
```
CTFlearn{Hail_Caesar!!!}
CTFlearn{Airplanes_Sometimes_Cause_Inflight_Incidents}
CTFlearn{Flight_32_Leaves_soon_from_gate_126}
```
Dan terdapat hint pada challenge ini
```
If you are having trouble solving this challenge, please solve my other
challenges first:
RubberDuck
Snowboard
PikesPeak
GandalfTheWise

The challenges are designed to be increasing in difficulty and this HailCaesar challenge is the next
challenge in the series.

My Twitter DM is open @kcbowhunter but please only ping me if you have solved the above challenges first.

If you are new to the jpeg file format please read this:
https://dev.exiv2.org/projects/exiv2/wiki/The_Metadata_in_JPEG_files

If you are new to hacking and are still learning about bits and bytes please watch this video:
https://www.youtube.com/watch?v=tLdvEOam3sk

xorpd has a lot of free videos that teach important computer science / hacking concepts.

Note that often my challenges combine forensics and some aspect of cryptography.

Have fun!
kcbowhunter
```
Kemudian saat saya mengecheck <b>file</b> tersebut saya menemukan
```
$ file HailCaesar.jpg
HailCaesar.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, comment: "CTFlearn{Hail_Caesar!!!}", comment: "/<V5;)j}j6\<Y)8><\9Fbu,Hy4ONC}pxP"4st12wn`?@O$6BgQo7i#gtD|s>3lf=", comment: "SWYgeW91IGFyZSBoYXZpbmcgdHJvdWJsZSBzb2x2aW5nIHRoaXMgY2hhbGxlbmdlLCBwbGVhc2Ug", comment: "2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0", progressive, precision 8, 700x372, components 3
```
<b>2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0</b>, saya mencoba mencari tau teks ini menggunakan <b>caesar cipher</b> http://java.cyberbass.com/crypto/crypto_shift_cipher.html
```
2m{y!"%w2'z{&o2UfX~ws%!._s+{ (&@Vwu{ (&@_w%{v{(&0
=> (-18) Encrypted Text --> Zignore this] CSFlearn{Laximus.Decimus.Meridius}
```
Kita dapat lihat bahwa flag nya tidak sempurna dan butuh perbaikan
```
Encrypted Text --> Zignore this] CSFlearn{Laximus.Decimus.Leridius}
```
Saat saya input tetap salah, saya belum pernah mendengar Laximus / Decimus / Leridius, <i>Disini ada kesalahan perhitungan ASCII yaitu pada huruf <b>S dan L</b>, Seharusnya mereka di beri 1 shift lagi, jadi <b>S => T dan L => M</b></i> kemudian saya searching https://www.google.com/search?q=Meridius dan mendapatkan
```
Maximus Decimus Meridius!
```
<b>Maximus Decimus Meridius</b>, Sesuai challenge pada gambar tersebut!. Dapat kita lihat disini bahwa google membantu kita untuk menyelesaikan challenge ini, kemudian saya ubah menjadi
```
CTFlearn{Maximus.Decimus.Meridius}
```
Flag : <b>CTFlearn{Maximus.Decimus.Meridius}</b>