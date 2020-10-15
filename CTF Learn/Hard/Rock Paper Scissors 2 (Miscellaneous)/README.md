# Rock Paper Scissors 2 (80 Points)
Do you think you can win 30 games of a much more twisted game or Rock Paper Scissors? I'm much less predictable now, there is no way you beat me. nc 138.197.193.132 5002
# Solved
Sebelumnya, kita di beri hint yaitu <b>Twister</b>, https://en.wikipedia.org/wiki/Mersenne_Twister. Disini saya akan menjelaskan cara menyelesaikan challenge nya, saat kita mengkoneksi server tersebut kita diberi 3 pilihan
```
----------- Let's play rock, paper, twister!
----------- Beat me 30 times in a row to win the flag, but this time, im going to be a little less predictable!!

Please choose: R / P / S
>>>
```
<i>Sebelumnya ada challenge tentang ini juga akan tetapi hanya 10 kali yang harus kita kalahkan dan hurufnya tetap, sedangkan ini random</i>. Disini jika kita menginput sebuah 3 dari salah 1 tersebut
```
You didn't win!
I chose R based on 1526179107
Please choose: R / P / S
```
Kita di berikan angka <b>1526179107</b>. Jika saya mengkoneksi ulang lagi
```
You didn't win!
I chose P based on 2655611134
Please choose: R / P / S
```
Hasilnya berbeda, Akan tetapi jika saya mengkoneksi secara berulang-ulang, hasilnya tetap berbeda!. Disini saya memahami kita harus mencari <b>Seed</b> dari random tersebut, jika disingkat exploit <b>PRNG (Pseudorandom Number Generator)</b> https://en.wikipedia.org/wiki/Pseudorandom_number_generator. Untuk mencari tau / bruteforce seed nya saya menggunakan https://github.com/kmyk/mersenne-twister-predictor
```python
# Example
import random
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()
for _ in range(624):
    x = random.getrandbits(32)
    predictor.setrandbits(x, 32)

assert random.getrandbits(32) == predictor.getrandbits(32)
```
Pada kode contohnya kita disuruh untuk melakukan looping sebanyak 624 kali agar mendapatkan prediksi yang tepat, kemudian saya modifikasi kodenya
```python
from pwn import *
from mt19937predictor import MT19937Predictor

cho = { # Maju 1 langkah dari bawah kemudian ke atas kembali
    "R": "P",
    "P": "S",
    "S": "R"
}

r = remote("138.197.193.132", 5002)

predictor = MT19937Predictor()
for x in range(624):
    r.sendlineafter(">>>", "R")
    r.recvuntil("based on ")

    p = r.recvuntil("\n").decode("utf-8").replace("\n", "")
    number = int(p)

    predictor.setrandbits(number, 32)
    log.success(str(x + 1) + ". Based On : " + str(number))

log.info("Sending the specific seed now")
```
Kemudian mengirimkan hasil prediksi tersebut
```python
for x in range(200): # Bruteforce, Jika tidak berhasil ditambahkan aja
    res = predictor.getrandbits(32)
    tse = ["R", "P", "S"][res % 3]
    tse = cho[tse]

    log.info("Sending : " + tse)
    r.sendlineafter(">>>", tse)

    respo = r.recv()
    print(respo)
    if b">>>" in respo:
        res = predictor.getrandbits(32)
        tse = ["R", "P", "S"][res % 3]
        tse = cho[tse]

        log.info("Sending : " + tse)
        r.sendline(tse)
    elif b"30" in respo or b"Consecutive wins: 30" in respo:
        r.interactive()
```
Disini proses agak lama, apalgi Internet indonesia tidak terlalu mendukung. Ditunggu saja sampai mendapatkan pesan
```
You won! Consecutive wins: 30
```
Fullcode :
```python
from pwn import *
from mt19937predictor import MT19937Predictor

cho = { # Maju 1 langkah dari bawah kemudian ke atas kembali
    "R": "P",
    "P": "S",
    "S": "R"
}

r = remote("138.197.193.132", 5002)

predictor = MT19937Predictor()
for x in range(624):
    r.sendlineafter(">>>", "R")
    r.recvuntil("based on ")

    p = r.recvuntil("\n").decode("utf-8").replace("\n", "")
    number = int(p)

    predictor.setrandbits(number, 32)
    log.success(str(x + 1) + ". Based On : " + str(number))

log.info("Sending the specific seed now")

for x in range(200): # Bruteforce, Jika tidak berhasil ditambahkan aja
    res = predictor.getrandbits(32)
    tse = ["R", "P", "S"][res % 3]
    tse = cho[tse]

    log.info("Sending : " + tse)
    r.sendlineafter(">>>", tse)

    respo = r.recv()
    print(respo)
    if b">>>" in respo:
        res = predictor.getrandbits(32)
        tse = ["R", "P", "S"][res % 3]
        tse = cho[tse]

        log.info("Sending : " + tse)
        r.sendline(tse)
    elif b"30" in respo or b"Consecutive wins: 30" in respo:
        r.interactive()


r.interactive()
```
```python
[*] Sending the specific seed now
[*] Sending : R
b'You won! Consecutive wins: 1\n'
[*] Sending : P
b'You won! Consecutive wins: 2\n'
[*] Sending : R
b'You won! Consecutive wins: 3\n'
[*] Sending : P
b'You won! Consecutive wins: 4\n'
[*] Sending : S
b'You won! Consecutive wins: 5\n'
[*] Sending : R
b'You won! Consecutive wins: 6\n'
[*] Sending : R
b'You won! Consecutive wins: 7\n'
[*] Sending : R
b'You won! Consecutive wins: 8\n'
[*] Sending : P
b'You won! Consecutive wins: 9\n'
[*] Sending : P
b'You won! Consecutive wins: 10\n'
[*] Sending : P
b'You won! Consecutive wins: 11\nI chose R based on 860886996\nPlease choose: R / P / S\n>>>'
[*] Sending : S
[*] Sending : S
b'You won! Consecutive wins: 13\n'
[*] Sending : R
b'You won! Consecutive wins: 14\nI chose S based on 4100867882\nPlease choose: R / P / S\n>>>'
[*] Sending : S
[*] Sending : R
b'You won! Consecutive wins: 16\n'
[*] Sending : R
b'You won! Consecutive wins: 17\n'
[*] Sending : S
b'You won! Consecutive wins: 18\n'
[*] Sending : P
b'You won! Consecutive wins: 19\n'
[*] Sending : S
b'You won! Consecutive wins: 20\n'
[*] Sending : S
b'You won! Consecutive wins: 21\n'
[*] Sending : S
b'You won! Consecutive wins: 22\n'
[*] Sending : R
b'You won! Consecutive wins: 23\n'
[*] Sending : R
b'You won! Consecutive wins: 24\n'
[*] Sending : R
b'You won! Consecutive wins: 25\n'
[*] Sending : R
b'You won! Consecutive wins: 26\n'
[*] Sending : S
b'You won! Consecutive wins: 27\n'
[*] Sending : R
b'You won! Consecutive wins: 28\n'
[*] Sending : S
b'You won! Consecutive wins: 29\n'
[*] Sending : R
b"You won! Consecutive wins: 30\nI chose S based on 3055467659\nWow, you're good, here's your flag!\nCTFlearn{m3rs3nn3_kind4_c00l}"
```
Flag : <b>CTFlearn{m3rs3nn3_kind4_c00l}</b>
