# Tapping - Points: 200
<b>Description : </b>Theres tapping coming in from the wires. What's it saying nc 2019shell1.picoctf.com 32273.<br>
<b>Hints : </b>What kind of encoding uses dashes and dots? The flag is in the format PICOCTF{}
# Solved
Message of netcat
```
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. .---- -.... --... --... ..--- ..... --... ..--- ---.. --... }
```
This is Cryptography called <b>Morse</b>, I solve this using https://cryptii.com/pipes/morse-code-to-text. And make sure all character is capital<br>
Flag : <b>PICOCTF{M0RS3C0D31SFUN1677257287}</b>	
