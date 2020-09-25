# Up For A Little Challenge?
https://mega.nz/#!LoABFK5K!0sEKbsU3sBUG8zWxpBfD1bQx_JY_MuYEWQvLrFIqWZ0 You Know What To Do ...
# Solved
Pada file tersebut terdapat fake flag
```
flag{Not_So_Simple...}
```
Dan ada beberapa informasi yang mungkin berguna yaitu
```
https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg
real_unlock_key: Nothing Is As It SeemsU
password: Really? Again
```
Terlihat ada link yg harus didownload lagi
```
$ megadl 'https://mega.nz/#!z8hACJbb!vQB569ptyQjNEoxIwHrUhwWu5WCj1JWmU-OFjf90Prg'
Downloaded Up For A Little Challenge.zip
```
Saya diberikan 2 file lagi yaitu
```
.Processing.cerb4
'Loo Nothing Becomes Useless ack.jpg'
```
Saya tidak tau apa itu ektensi dari .cerb4 maka dari itu saya mencoba mendeteksi filenya
```
$ file .Processing.cerb4
.Processing.cerb4: Zip archive data, at least v2.0 to extract
```
Ternyata sebuah zip! Mari kita unzip
```
$ unzip .Processing.cerb4
Archive:  .Processing.cerb4
[.Processing.cerb4] skycoder.jpg password:
```
Ternyata membutuhkan password, Saya mencoba input <b>Nothing Is As It Seems</b>
```
inflating: skycoder.jpg
```
Diberikan lagi sebuah gambar hitam putih. Kemudian saya menggunakan <b>StegSolve</b> untuk mencari dimana flag tersebut!. Disaat saya berada di <b>Full red</b> pada stegsolve, saya menemukan sebuah teks kecil dibawah kanan yang bertulisan flagnya!
```
flag{hack_complete}
```
Flag : <b>flag{hack_complete}</b>