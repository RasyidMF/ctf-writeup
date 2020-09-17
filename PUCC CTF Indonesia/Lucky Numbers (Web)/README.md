# Lucky Number (100 Points)
apakah kamu punya angka keberuntungan ? http://soal.pucc.or.id/lucky/
# Solved
Lokasi source terdapat pada
```
https://soal.pucc.or.id/lucky/?debug
```
```php
require 'flag.php';

$angka = $_GET['number'];
if (isset($angka)) {
  if (is_numeric($angka)){
    if (!strpos($angka, ".")){
      if (strlen($angka) > 6){
        if ($angka < 99999 && $angka > 90000)

        echo('<h1><div class="alert alert-success centered" role="alert"> Flag: '.FLAG.' </div></h1>');
        else
        echo('<h1><div class="alert alert-danger centered" role="alert">too long!</div></h1>');
      } else
        echo('<h1><div class="alert alert-danger centered" role="alert">too short!</div></h1>');
    } else
    echo('<h1><div class="alert alert-danger centered" role="alert">dont use dots!</div></h1>');
  } else
    echo('<h1><div class="alert alert-danger centered" role="alert">must be numbers!</div></h1>');
die;
}
```
Bisa kita lihat variabel <b>$angka</b>, meminta inputan kita untuk mendapatkan flag. Ada beberapa yang harus dipahami disini
```php
isset($angka); // Mengecheck apakah variabel angka tidak kosong
is_numeric($angka); // Mengecheck apakah variabel angka adalah angka
strpos($angka, "."); // Mengecheck apakah variabel memiliki huruf "."
strlen($angka) > 6; // Mengecheck apakah size dari variabel angka melebihi 6
$angka < 99999 && $angka > 90000; // Mengecheck apakah angka tersebut dibawah 99999 dan diatas 90000
```
Ini adalah challenge yang bisa membuat bingung untuk pemula, mari kita coba dump. Jika kita menginput <b>0000000</b> inilah hasilnya
```
string(7) "0000000"
```
Bagaimana pun, hasil dari <b>$_GET</b> adalah bersifat <b>string</b>, Jadi kita sudah melewati 4 step, sekarang tinggal step terakhir, Inilah inputan yang melewati semua if condition
```
https://soal.pucc.or.id/lucky/?number=0090001
```
FLag : <b>PUCC{php_nUm3riC_1s_SucKs}</b>
