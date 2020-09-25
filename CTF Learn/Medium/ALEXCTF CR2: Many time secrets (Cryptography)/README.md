# ALEXCTF CR2: Many time secrets (60 Points)
This time Fady learned from his old mistake and decided to use onetime pad as his encryption technique, but he never knew why people call it one time pad! Flag will start with ALEXCTF{.
<br>
https://mega.nz/#!DGxBjaDR!tMWkHf0s0svmkboGd-IASHsS9jACxSYx4zi_ETsyzyQ
# Solved
Diberikan sebuah pesan yang berisi enkripsi XOR
```
0529242a631234122d2b36697f13272c207f2021283a6b0c7908
2f28202a302029142c653f3c7f2a2636273e3f2d653e25217908
322921780c3a235b3c2c3f207f372e21733a3a2b37263b313012
2f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d
283f652c2b31661426292b653a292c372a2f20212a316b283c09
29232178373c270f682c216532263b2d3632353c2c3c2a293504
613c37373531285b3c2a72273a67212a277f373a243c20203d5d
243a202a633d205b3c2d3765342236653a2c7423202f3f652a18
2239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c
263e203d63232f0f20653f207f332065262c3168313722367918
2f2f372133202f142665212637222220733e383f2426386b
```
Untuk menyelesaikannya saya menggunakan https://github.com/SpiderLabs/cribdrag
```
$ python cribdrag.py 0529242a631234122d2b36697f13272c207f2021283a6b0c79082f28202a302029142c653f3c7f2a2636273e3f2d653e25217908322921780c3a235b3c2c3f207f372e21733a3a2b37263b3130122f6c363b2b312b1e64651b6537222e37377f2020242b6b2c2d5d283f652c2b31661426292b653a292c372a2f20212a316b283c0929232178373c270f682c216532263b2d3632353c2c3c2a293504613c37373531285b3c2a72273a67212a277f373a243c20203d5d243a202a633d205b3c2d3765342236653a2c7423202f3f652a182239373d6f740a1e3c651f207f2c212a247f3d2e65262430791c263e203d63232f0f20653f207f332065262c31683137223679182f2f372133202f142665212637222220733e383f2426386b
```
```
Your message is currently:
0       ________________________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
Your key is currently:
0       ________________________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
Please enter your crib: ALEXCTF{
*** 0: "Dear Fri"

Enter the correct position, 'none' for no match, or 'end' to quit: 0
Is this crib part of the message or key? Please enter 'message' or 'key': message
Your message is currently:
0       ALEXCTF{________________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
Your key is currently:
0       Dear Fri________________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
Please enter your crib: Dear Friend
0: "ALEXCTF{HER"

Enter the correct position, 'none' for no match, or 'end' to quit: 0
Is this crib part of the message or key? Please enter 'message' or 'key': key
Your message is currently:
0       ALEXCTF{HER_____________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
Your key is currently:
0       Dear Friend_____________________________
40      ________________________________________
80      ________________________________________
120     ________________________________________
160     ________________________________________
200     ________________________________________
240     ________________________________________
280     ____
```
Dan seterusnya, kalian harus bisa mencocokan kata-kata yang terkait di kepala, Karena disini jika saya jelaskan akan sangat panjang
```
Your message is currently:
0       ALEXCTF{HER_____________Y}ALEXCTF{HERE_G
40      OES_THE_____________________________y}AL
80      EXCTF{HERE_GOES_T_____y}ALEXCTF{HERE_GOE
120     S_T____y}ALEXCTF{HERE_GOES_T_____y}ALEX
160     CTF{HERE_GOES_T_____y}ALEXCTF{HERE_GOES_
200     T_____Y}ALEXCTF{HERE_GOES_THE_KEY}ALEXCT
240     F{HERE_GOES_THE_KEY}ALEXCTF{HERE_GOES_TH
280     E___
Your key is currently:
0       Dear Friend_____________ understood my m
40      istake _____________________________Ion
80      scheme, I heard t_____T is the only encr
120     ypt ____Ethod that is mathema_____Ly pro
160     ven to be not c_____D ever if the key is
200      _____secure, Let Me know if you agree w
240     ith me to use this encryption scheme alw
280     ay__
```
Flag : <b>ALEXCTF{HERE_GOES_THE_KEY}</b>