# giff me flag (100 Points)
admin sangat butuh sekali flag ini, bisakah kamu membantu admin untuk mendapatkan flag nya
# Solved
File dari <b>soal.go</b> adalah hasil konversi text to hex, maka dari itu saya menggunakan https://tomeko.net/online_tools/hex_to_file.php?lang=en untuk mengkonversi file tersebut, setelah itu saya coba cek ektensi file tersebut adalah
```
$ file myfile.dat
myfile.dat: GIF image data, version 89a, 800 x 534
```
Setelah mengetahui tipe file tersebut adalah <b>GIF</b>, saya ubah nama file .dat nya menjadi .gif
```
$ mv myfile.dat myfile.gif
```
Flag : <b>PUCC{Bl1nk_bl4nk}</b>
