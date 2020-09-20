# File Formats (50 Points)
Tentunya kita tahu bahwa ada berbagai macam jenis file, yang pada umumnya dibedakan dari extensionnya (.jpg, .png, .exe, .zip, dll). Tapi, pada kenyataannya, file extension tidak menjadi satu - satunya cara untuk membedakan jenis file.
<br>
Jika kita mencoba dump content suatu file kedalam bentuk hexadecimal, kita dapat melihat beberapa byte awal pada file tersebut, dimana byte - byte awal tersebut disebut File Signature.
<br>
Pada challenge kali ini, akan diberikan sebuah file jpeg yang rusak, dan kalian diminta untuk melihat apakah File Signature nya sudah benar atau belum. Jika belum benar, coba kalian perbaiki file signaturenya agar kalian bisa membuka file tersebut.
<br>
Flag pada challenge ini tersembunyi pada foto yang rusak tersebut.
# Solved
Deskripsi nya menunjukan bahwa kita harus memperbaiki <b>Magic Number</b> untuk menyelesaikan challenge ini. Mari kita cek hex pada file tersebut
```
00 00 00
```
Jika kita melihat nama file tersebut adalah <b>.jpg</b>, sedangkan signature dari <b>jpg</b> adalah
```
ff d8 ff
```
Mari kita coba ubah, dan kemudian buka file tersebut akan menunjukan gambar yang berisi flag! <br>
Flag : <b>PlaygroundCTF{ez_f1l3_5ignatuR3}</b>