# A CAPture of a Flag (50 Points)
This isn't what I had in mind, when I asked someone to capture a flag... can you help? You should check out WireShark. https://mega.nz/#!3WhAWKwR!1T9cw2srN2CeOQWeuCm0ZVXgwk-E2v-TrPsZ4HUQ_f4
# Solved
Dikarenakan file capture nya sangat besar, saya menggunakan https://packettotal.com/ untuk membaca nya, pada bagian <b>http</b> saya melihat
```
2017-08-04 14:03:25 Z	CbogK8211QbFxrOAw9	10.50.203.75	23253	185.21.216.190
80	1	GET	www.hazzy.co.uk 	/?msg=ZmxhZ3tBRmxhZ0luUENBUH0=	null	...537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36
```
```
ZmxhZ3tBRmxhZ0luUENBUH0=
```
```
$ echo 'ZmxhZ3tBRmxhZ0luUENBUH0=' | base64 -d
flag{AFlagInPCAP}
```
Flag : <b>flag{AFlagInPCAP}</b>