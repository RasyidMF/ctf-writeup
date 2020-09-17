# Kue Kering Enak (25 Points)
Mbak ukhty membuat kue kuring untuk aku dong ^_^. http://soal.pucc.or.id/cok/
# Solved
Setelah kita membuka website tersebut, terdapat pesan
```
Selamat Datang Guest
Maaf, hadiah untuk anda tidak ada.
Karna hadiah hanya untuk root
```
Setelah saya lihat, disitu ada cookie yang menunjukan level, kemudian saya jalankan curl untuk mengubah cookie tersebut
```
curl 'https://soal.pucc.or.id/cok/' -H 'Cookie: level=root' --compressed -L
```
Flag : <b>PUCC{c00kies_1s_d4ngerous}</b>
