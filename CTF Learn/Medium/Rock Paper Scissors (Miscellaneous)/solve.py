from pwn import *
step = ["p","r","p","s","p","p","s","p","r","p"]

sh = remote("138.197.193.132", 5001)

for x in step:
    sh.recvuntil("Please choose: R / P / S\n")
    sh.send(x)
    print sh.recvline().replace("\n", "")

log.success("Flag : " + sh.recvall().split("flag!\n")[1])