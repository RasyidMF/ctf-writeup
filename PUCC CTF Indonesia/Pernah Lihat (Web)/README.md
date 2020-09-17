# Pernah Lihat (75 Points)
Sepertinya aku pernah melihatnya, tapi dimana ya ? http://soal.pucc.or.id/seen/
# Solved
Cek source pada website tersbt
```html

<!DOCTYPE Html />
<html>
 <head>
 <meta charset="utf-8">
 <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
 <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
 <style type="text/css">
 .ins {
  padding:auto;
  margin:5rem auto 0 auto;
  text-align:center;
 }
 .btn {
  padding:auto;
  margin:1rem;
 }
 </style>
 <title>Login Bang</title>
 </head>
 <body>
<div class="container text-center">
 <h2>Masukkan Password</h2><small>Keberuntungan mu</small>
 <div class="container ins">
	 <input type="text" name="flag" id="flag" placeholder="Masukkan Flag" /><br>
	 <button class="btn btn-primary" id="login" >Masuk!</button>
 </div>
</div>

 <script type="text/javascript">
 document.getElementById("login").onclick = function () {
 var flag = document.getElementById("flag").value;
 var flags = flag.replace(/[a-zA-Z]/g, function(c){
 return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);});
 if ("CHPP{wf_j1gu_e0g13_fgvYY_3m}" == flags) {
 alert("Yeayyy Bener bro");
 } else {
 alert("Salah Koplok");
 }
 }
 </script>

 </body>
</html>

```
Bisa kita lihat bahwasannya ada password didalam tag <b>script</b>, mari kita pecahkan!
```javascript

 document.getElementById("login").onclick = function () {
 var flag = document.getElementById("flag").value;
 var flags = flag.replace(/[a-zA-Z]/g, function(c){
 return String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26);});
 if ("CHPP{wf_j1gu_e0g13_fgvYY_3m}" == flags) {
 alert("Yeayyy Bener bro");
 } else {
 alert("Salah Koplok");
 }
 }
```
Solved menggunakan python script
```python
from pwn import *
import string
# Algorithm :
#   String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26)

flag = "CHPP{wf_j1gu_e0g13_fgvYY_3m}"
r = ""

for x in flag:

    if x == "{" or x == "}" or x == "_" or x in string.digits:
        r += x
        continue

    c = ord(x)

    if c <= 90:
        d = 90
    else: d = 122

    if d >= (ord(x) + 13):
        r += chr(c + 13)
    else:
        r += chr(c - 13)

log.info(r)
```
Flag : <b>PUCC{js_w1th_r0t13_stiLL_3z}</b>