# Segala Cara (75 Points)
aku akan menggunakan Segala Cara untuk mendapatkan mu mbak ukhty<br>
Format Flag : PUCC{1ni_fLa6}
# Solved
Disini bisa kita lihat bahwasannya ada file .zip yang sangat besar. Setelah di unzip, file tersebut mengekstrak file <b>rahasia_ukhty.zip</b> yang memiliki password. <br>
Tugas kita disini ialah <b>Membrute-force</b> password tersebut sesuai yang ada di list file <b>rockyou.txt</b>. Disini saya menggunakan command
```
fcrackzip -u -D -p rockyou.txt rahasia_ukhty.zip
```
Password yang berhasil setelah di bruteforce : <b>ukhty1337</b>. setelah dapat dicoba untuk unzip file tersebut.
```
unzip rahasia_ukhty.zip
```
Flag : <b>PUCC{0p3N_th3_z1p_us1ng_diCtionAry}</b>
