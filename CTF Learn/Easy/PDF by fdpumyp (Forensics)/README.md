# PDF by fdpumyp (20 Points)
Hi, just as we talked during a break, you have this file here and check if something is wrong with it. That's the only thing we found strange with this suspect, I hope there will be a password for his external drive
<br>
Bye
# Solved
```console
$ strings dontopen.pdf
== SECRET DATA DONT LOOK AT THIS ==
external:Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==
pin:1234
password:MTIzMVdST05HOWlzamRuUEFTU1dPUkQ=
```
```console
$ echo 'MTIzMVdST05HOWlzamRuUEFTU1dPUkQ=' | base64 -d
1231WRONG9isjdnPASSWORD

$ echo 'Q1RGbGVhcm57KV8xbDB3M3kwVW0wMG15MTIzfQ==' | base64 -d
CTFlearn{)_1l0w3y0Um00my123}
```
Flag : <b>CTFlearn{)_1l0w3y0Um00my123}</b>
