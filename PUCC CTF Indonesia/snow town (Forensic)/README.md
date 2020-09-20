# snow town (150 Points)
salju hujan tuh habis
# Solved
Saya menyelesaikan ini sekitar 2 hari :'D, dikarenakan saya terlalu fokus memerhatikan 2 byte yg harus saya decode
```
\x09 \x20
```
Saya mengira bahwa, saya perlu mengkonversi <b>\x09</b> menjadi <b>1</b> dan <b>\x20</b> menjadi <b>0</b>, akan tetapi tidak dapat sama sekali jawabannya. Sampai dimana saya memperhatikan <b>PUCC{nopassword}</b>, yang bisa di anggap Steganography yang dipakai adalah <b>stegsnow</b>, sesuai dengan judulnya tapi saya tidak memerhatikannya. <br>
Setelah saya menjalankan perintah ini, saya mendapatkan flag nya!
```
$ stegsnow -C -p "" snowman.txt
Warning: an empty password is being used
PUCC{PUCC_4ND_BLUG_B3ST_fr1nds_f0r3vah}
```
Flag : <b>PUCC{PUCC_4ND_BLUG_B3ST_fr1nds_f0r3vah}</b>
