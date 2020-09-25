# POST Practice
This website requires authentication, via POST. However, it seems as if someone has defaced our site. Maybe there is still some way to authenticate? http://165.227.106.113/post.php
# Solved
Cek source tersebut
```html

<h1>This site takes POST data that you have not submitted!</h1><!-- username: admin | password: 71urlkufpsdnlkadsf -->
```
Kita di berikan inputan untuk di kirimkan sebagai method <b>POST</b>
```
$ curl -d 'username=admin&password=71urlkufpsdnlkadsf' http://165.227.106.113/post.php
<h1>flag{p0st_d4t4_4ll_d4y}</h1>
```
Flag : <b>flag{p0st_d4t4_4ll_d4y}</b>