# Rock Paper Scissors (40 Points)
Do you think you're lucky enough to win 10 games of Rock Paper Scissors in a row? Connect to the server and find out. nc 138.197.193.132 5001
# Solved
Kita disini diberikan sebuah perintah untuk mengkoneksi ke server
```
nc 138.197.193.132 5001
```
```
----------- Let's play rock, paper, scissors!
----------- Beat me 10 times in a row to win the flag!

Please choose: R / P / S
>>>
```
Kita disini disuruh memilih <b>Batu / Kertas / Gunting</b> untuk memenangkan challenge ini.
```
>>>p
You won! Consecutive wins: 1
I chose R based on 2454155475
Please choose: R / P / S
>>>s
You didn't win!
```
Jika kalah, maka server tersebut mengdisconnectkan saya, maka dari itu saya mencoba koneksi ulang
```
$ nc 138.197.193.132 5001
----------- Let's play rock, paper, scissors!
----------- Beat me 10 times in a row to win the flag!

Please choose: R / P / S
>>>p
You won! Consecutive wins: 1
I chose R based on 2454155475
Please choose: R / P / S
>>>r
You won! Consecutive wins: 2
```
Ada beberapa hal yang saya tidak perhatikan yaitu, <b>Setiap kita koneksi ke server tersebut, jawaban dari pertama sampai terakhir itu tetap sama walaupun harus reconnect</b>. Maksud saya adalah, jika anda kalah pada step ke 2, anda bisa mencoba bruteforce <b>R / P / S</b>, jika benar lanjut ke step 3, dan seterusnya. Dan ini code yang saya pakai untuk solve challenge ini
```python
from pwn import *
step = ["p","r","p","s","p","p","s","p","r","p"]

sh = remote("138.197.193.132", 5001)

for x in step:
    sh.recvuntil("Please choose: R / P / S\n")
    sh.send(x)
    print sh.recvline().replace("\n", "")

log.success("Flag : " + sh.recvall().split("flag!\n")[1])
```
```
$ python solve.py
[+] Opening connection to 138.197.193.132 on port 5001: Done
>>>You won! Consecutive wins: 1
>>>You won! Consecutive wins: 2
>>>You won! Consecutive wins: 3
>>>You won! Consecutive wins: 4
>>>You won! Consecutive wins: 5
>>>You won! Consecutive wins: 6
>>>You won! Consecutive wins: 7
>>>You won! Consecutive wins: 8
>>>You won! Consecutive wins: 9
>>>You won! Consecutive wins: 10
[+] Receiving all data: Done (95B)
[*] Closed connection to 138.197.193.132 port 5001
[+] Flag : CTFlearn{r0ck_p4per_skiss0rs}
```
Flag : <b>CTFlearn{r0ck_p4per_skiss0rs}</b>