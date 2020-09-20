# Rockyou.txt
Seringkali dalam CTF kita diberikan sebuah zip berpassword, dan kita dituntut untuk menebak password dari file zip tersebut tanpa clue apa-apa.
<br>
Untuk kasus seperti ini, kita dapat menggunakan file rockyou.txt yang sudah tersebar luas di internet, dimana file tersebut berisi sekumpulan password paling common yang biasa dipakai.
<br>
Pada challenge kali ini, kalian bisa coba mengcrack password file zip yang diberikan untuk mendapatkan flag
# Solved
Saya menggunakan command ini untuk mencari tau password dari file zip tersebut
```
fcrackzip -u -D -p /usr/share/wordlist/rockyou/rockyou.txt flag.zip
```
```
PASSWORD FOUND!!!!: pw == loveyou
```
Password yang ditemukan ialah <b>loveyou</b>, mari kita ekstrak dan buka file yang telah di ekstrak!<br>
Flag : <b>PlaygroundCTF{w3_w3r3_r0cky0uu}</b>