# logon - Points: 100
<b>Description : </b>The factory is hiding things from all of its users. Can you login as logon and find what they've been looking at? https://2019shell1.picoctf.com/problem/45163/ (link) or http://2019shell1.picoctf.com:45163<br>
<b>Hints : </b>Hmm it doesn't seem to check anyone's password, except for {{name}}'s?
# Solved
Well in the website we can just login without having any account, just example Username with <b>admin</b> and Password with <b>admin</b>.<br>
but still there is no flag appear, instead they just give me the message <b>No flag for you</b>.<br>
I was looking around <b>Where is the vulnerability</b>, and untill i found where it is. It inside of cookies!
```
Cookie: password=admin; username=admin; admin=False
```
Kinda weird right ? why there is "admin" argument. When i change into <b>True</b>
```
Cookie: password=admin; username=admin; admin=True
```
and Re-send the Request, this is what i got
```html
<b>Flag</b>: <code>picoCTF{th3_c0nsp1r4cy_l1v3s_6679fcb5}</code></p>
```
Well that so easy to learn why we need "Looking around".<br>
Flag : <b>picoCTF{th3_c0nsp1r4cy_l1v3s_6679fcb5}</b>
