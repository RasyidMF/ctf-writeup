# Taking LS (30 Points)
Just take the Ls. Check out this zip file and I be the flag will remain hidden. https://mega.nz/#!mCgBjZgB!_FtmAm8s_mpsHr7KWv8GYUzhbThNn0I8cHMBi4fJQp8
# Solved
Jadi disini kita di berikan sebuah file zip, maka dari itu mari kita ekstrak dan kita akan menemukan file <b>The Flag.pdf</b>. Saat kita membuka file tersebut membutuhkan password untuk masuknya! Jika kalian menyelesaikan challenge ini di windows dapat secara mudah ke folder <b>.ThePassword</b> sedangkan pada Linux, ketik perintah ini
```
$ ls -al
total 28
drwxr-xr-x 1 rasyidmf rasyidmf  4096 Oct 30  2016  .
drwxr-xr-x 1 rasyidmf rasyidmf  4096 Sep 23 18:46  ..
-rw-r--r-- 1 rasyidmf rasyidmf  6148 Oct 30  2016  .DS_Store
drwxr-xr-x 1 rasyidmf rasyidmf  4096 Oct 30  2016  .ThePassword
-rw-r--r-- 1 rasyidmf rasyidmf 16647 Oct 30  2016 'The Flag.pdf'
```
Kemudian pindah ke folder <b>.ThePassword</b>
```
$ cd .ThePassword/
$ cat ThePassword.txt
Nice Job!  The Password is "Im The Flag".
```
Password dari PDF tersebut ialah <b>Im The Flag</b>, Masukan password dan password akan muncul dalam gambar! <br>.
Flag : <b>ABCTF{T3Rm1n4l_is_C00l}</b>
