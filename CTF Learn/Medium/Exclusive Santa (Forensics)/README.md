# Exclusive Santa (60 Points)
Dear Santa, <br>
Hey! There are so many toys that I want, but I just don't have the money. I don't care which toy I get as long as it's one or the other, but not both!
# Solved
Diberikan 2 Gambar file
```
-rw-r--r-- 1 rasyidmf rasyidmf 2134264 Dec  4  2019 1.png
-rw-r--r-- 1 rasyidmf rasyidmf 1221575 Dec  3  2019 3.png
```
Untuk mengekstrak isi file pada gambar tersebut, saya menggunakan perintah <code>foremost</code>
```
$ foremost 1.png
Processing: 1.png
|*|
$ foremost 3.png
Processing: 3.png
|*|
```
Pada output <b>formost 3.png</b> terdapat 1 gambar yang berbeda pada gambar yang sebelumnya saya download. Apakah kemungkinan challenge ini, kita disuruh untuk menyamakan gambar tersebut <b>XOR</b> ? Saya menggunakan stegsolve untuk menyelesaikan ini.
```
Buka stegsolve kemudian pilihkan gambar 1.png, Kemudian klik Analyse -> Image Combiner -> **Hasil Output dari Gambar ke 3 tadi**
```
Setelah melakukan hal tersebut, terlihat lah flag dalam posisi terbalik
```
CTFlearn{Santa_1s_C0ming}
```
Flag : <b>CTFlearn{Santa_1s_C0ming}</b>