# Glory of the Garden - Points: 50
<b>Description :</b> This garden contains more than it seems. You can also find the file in /problems/glory-of-the-garden_3_346e50df4a37bcc4aa5f6e5831604e2a on the shell server.
<br><b>Hints :</b> What is a hex editor?
# Solved
Menggunakan command <b>xxd</b> pada Ubuntu. Flag nya berada pada posisi <b>0x00230570</b>: <br>
```
00230570: 636f 4354 467b 6d6f 7265 5f74 6861 6e5f  coCTF{more_than_
00230580: 6d33 3374 735f 7468 655f 3379 3335 6139  m33ts_the_3y35a9
00230590: 3764 3362 427d 220a                      7d3bB}".
```
Atau menggunakan command <b>strings garden.jpg | grep "picoCTF"</b><br>
Flag : <b>picoCTF{more_than_m33ts_the_3y35a97d3bB}</b>
