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