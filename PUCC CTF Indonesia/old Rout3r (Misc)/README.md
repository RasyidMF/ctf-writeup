# old Rout3r (250 Points)
Router usang milik seorang pakar IT menyimpan sebuah rahasia, bisakah kamu mencari rahasia didalam router tersebut ?
# Solved
Ini adalah challenge sederhana akan tetapi membuat kepala punyeng jika tidak tahu fungsi command dari linux :(
```
File Type :
0ld Rout3r-disk1.vmdk : VMWare4 Disk
```
Disini saya menggunakan <b>PowerISO</b> untuk mengekstrak file .vmdk nya, kemudian disitu ada 2 file yang bernama
```
0.iso
1.iso
```
0.iso berisi sebuah file yang tidak penting untuk challenge ini, sedangkan file 1.iso berisi Linux Directory, nah extract lah 1.iso.<br>
Setelah itu saya hanya sekedar menggunakan command
```
grep -rni "PUCC{"
```
Untuk mendapatkan flag, dan inilah hasilnya
```
rw/pckg/rahasia.txt:1:PUCC{there_is_no_place_like_1.3.3.7}
```
Flag : <b>PUCC{there_is_no_place_like_1.3.3.7}</b>
