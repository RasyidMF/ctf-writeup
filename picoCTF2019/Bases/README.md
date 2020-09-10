# Bases - Points: 100
<b>Description : </b>What does this bDNhcm5fdGgzX3IwcDM1 mean? I think it has something to do with bases.<br>
<b>Hints : </b>Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.
# Solved
The challenge is <b>bDNhcm5fdGgzX3IwcDM1</b>, this is a <b>Base64</b> encryption. We can decode Base64 as well
```
echo 'bDNhcm5fdGgzX3IwcDM1' | base64 --decode
```
Flag : <b>picoCTF{l3arn_th3_r0p35}</b>
