# Odading Mang Oleh (300 Points)
Odading mang oleh emm rasanya seperti anda menjadi ironman, belilah odading mang oleh di dieu karna lamun teu ngadahar odading mang oleh maneh teu gaul jeung aing, lain balad aing goblog, ikan hiu makan eu tomat, goblog mun teu kadieu, odading mang oleh rasanya anjing banget.
# Solved
File <b>odading.png</b> tidak hanya memiliki 1 file, akan tetapi didalam nya memiliki file lainnya. Maka dari itu saya menggunakan command
```
binwalk -e odading.png
```
Jika sudah terekstrak semua, sebelum itu saya mencari string yang ada pada gambar <b>odading.png</b>, ini yang saya dapatkan
```
key:ikanhiumakantomat
clue.txt
rasanyamenjadironman.jpg
```
Saya simpan sebagai note, kemudian setelah saya pindah di folder hasil ekstrak binwalk, disana terdapat file .zip.
```
70AE.zip  clue.txt  rasanyamenjadironman.jpg
```
Saya coba ekstrak, membutuhkan password. Untung saja saya note bahwa password nya adalah <b>key</b> yang tadi <b>ikanhiumakantomat</b>. Setelah itu saya mencoba membuka file <b>clue.txt</b>
```
jsteg mungkin membantu anda.
```
Clue nya sangat dibutuhkan untuk mensolve challenge ini, karena sebelumnya saya mencoba mencari tau file dari <b>rasanyamenjadironman.jpg</b> dari <b>StegSolve</b>, <b>XOR</b> dll. Saya solve menggunakan website ini https://lukeslytalker.pythonanywhere.com/jsteg/scan
```
Image Scanned:
PUCC{0D4!i9_m4n9_0l3h_r4saNy4_AJG_bgt}
```
Flag : <b>PUCC{0D4!i9_m4n9_0l3h_r4saNy4_AJG_bgt}</b>
