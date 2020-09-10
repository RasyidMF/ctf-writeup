# where are the robots - Points: 100
<b>Description : </b>Can you find the robots? https://2019shell1.picoctf.com/problem/4159/ (link) or http://2019shell1.picoctf.com:4159<br>
<b>Hints : </b>What part of the website could tell you where the creator doesn't want you to look?</b>
# Solved
Try to access <b>https://2019shell1.picoctf.com/problem/4159/robots.txt</b> you will got
```
User-agent: *
Disallow: /a44f7.html
```
Open https://2019shell1.picoctf.com/problem/4159/a44f7.html, and you will got the flag!<br>
Flag : <b>picoCTF{ca1cu1at1ng_Mach1n3s_a44f7}</b>
