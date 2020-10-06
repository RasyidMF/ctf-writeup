# RSA Twins! (90 Points)
https://mega.nz/#!2aBwFCKa!NWQKRIbYzSAU2iwCPNppO7SE92W6sne4FKD3sKE2A-k Aww, twins :). Theyâre so cute! They must be (almost) identical because theyâre the same except for the slightest difference. Anyway, see if you can find my flag. Hint: This is just math. You're probably not going to find any sort of specialized attack.
# Solved
Challenge ini sama dengan <b>RSA Beginner</b>, hanya sekedar memfactorize menggunakan <b>factordb.com</b>
```python
from Crypto.Util.number import inverse

n = 14783703403657671882600600446061886156235531325852194800287001788765221084107631153330658325830443132164971084137462046607458019775851952933254941568056899
e = 65537
c = 684151956678815994103733261966890872908254340972007896833477109225858676207046453897176861126186570268646592844185948487733725335274498844684380516667587

p = 121588253559534573498320028934517990374721243335397811413129137253981502291629
q = 121588253559534573498320028934517990374721243335397811413129137253981502291631

phi = ( p - 1 ) * ( q - 1 )

d = inverse(e, phi)
m = pow(c, d, n)

print(hex(m))
```
```console
$ python solve.py
0x666c61677b695f6c3076335f7477314e5f7072316d33737dL
```
```console
$ hexttostr 666c61677b695f6c3076335f7477314e5f7072316d33737d
flag{i_l0v3_tw1N_pr1m3s}
```
Flag : <b>flag{i_l0v3_tw1N_pr1m3s}</b>