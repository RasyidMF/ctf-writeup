# Reverse - Nani-the-fuk (50 Points)
aku dimana?
<br>
unrelated: https://www.youtube.com/watch?v=1AhDtMxwnvI
<br>
author: circleous - IPB
<br>
Format Flag: hacktoday{flag}
# Solved
Mari kita lihat source tersebut menggunakan IDA Pro
```cpp
.rodata:0000000000002010	0000000D	C	aku dimana?\n
.rodata:0000000000002020	0000000E	C	(02/20) ???? 
.rodata:0000000000002030	0000000E	C	(01/20) ???? 
.rodata:0000000000002040	0000000E	C	(03/20) ???? 
.rodata:0000000000002050	0000000E	C	(04/20) ???? 
.rodata:0000000000002060	0000000E	C	(05/20) ???? 
.rodata:0000000000002070	0000000E	C	(06/20) ???? 
.rodata:0000000000002080	0000000E	C	(07/20) ???? 
.rodata:0000000000002090	0000000E	C	(08/20) ???? 
.rodata:00000000000020A0	0000000E	C	(09/20) ???? 
.rodata:00000000000020B0	0000000E	C	(10/20) ???? 
.rodata:00000000000020C0	0000000E	C	(11/20) ???? 
.rodata:00000000000020D0	0000000E	C	(12/20) ???? 
.rodata:00000000000020E0	0000000E	C	(13/20) ???? 
.rodata:00000000000020F0	0000000E	C	(14/20) ???? 
.rodata:0000000000002100	0000000E	C	(15/20) ???? 
.rodata:0000000000002110	0000000E	C	(16/20) ???? 
.rodata:0000000000002120	0000000E	C	(17/20) ???? 
.rodata:0000000000002130	0000000E	C	(18/20) ???? 
.rodata:0000000000002140	0000000E	C	(19/20) ???? 
.rodata:0000000000002150	0000000E	C	(20/20) ???? 
```
Kita bisa lihat disini, besar flag tersebut adalah <b>20</b> dengan huruf ataupun angka. Sebelumnya jika kita menjalankan program, kita disuruh input flag nya 1 per 1
```
aku dimana?
 (01/20) ????  s
 (02/20) ????
```
Jika salah satu karakter berhasil, maka lanjut ke karakter berikutnya. Saya menyelesaikan challenge ini menggunakan <b>Bruteforce</b> antara angka dan huruf serta jangan lupa <b>Underscore</b>
```python
from pwn import *
import subprocess
import string

def prnt(x):
    return log.info(x)

char = string.ascii_letters + string.digits + "_"
flag = ""
curr = "01"

FLAG_SIZE = 22


curr = ("0" + str(len(flag) + 1) if len(flag) + 1 <= 9 else str(len(flag)))

for _ in range(FLAG_SIZE):
    for x in char:
        p = subprocess.Popen("./nani-the-fuk", stdout=subprocess.PIPE, stdin=subprocess.PIPE)

        iot = flag + x + "\n"
        val = repr(p.communicate(input=iot)[0])
        sp = val.split("/")
        c = sp[len(sp) - 2].split("(")[1]

        if "hacktoday{" in val:
            flag += x + "\n"
            log.success("Flag: hacktoday{" + flag.replace("\n", "") + "}")
            exit(0)
        if not curr == c:
            flag += x + "\n"
            prnt("Flag: hacktoday{" + flag.replace("\n", "") + "}")
            curr = c
            break
```
Output dari script ini
```
[*] Flag: hacktoday{s}
[*] Flag: hacktoday{s1}
[*] Flag: hacktoday{s1g}
[*] Flag: hacktoday{s1g_}
[*] Flag: hacktoday{s1g_c}
[*] Flag: hacktoday{s1g_c0}
[*] Flag: hacktoday{s1g_c0n}
[*] Flag: hacktoday{s1g_c0nt}
[*] Flag: hacktoday{s1g_c0nto}
[*] Flag: hacktoday{s1g_c0ntor}
[*] Flag: hacktoday{s1g_c0ntorl}
[*] Flag: hacktoday{s1g_c0ntorl_}
[*] Flag: hacktoday{s1g_c0ntorl_f}
[*] Flag: hacktoday{s1g_c0ntorl_fl}
[*] Flag: hacktoday{s1g_c0ntorl_fl0}
[*] Flag: hacktoday{s1g_c0ntorl_fl0w}
[*] Flag: hacktoday{s1g_c0ntorl_fl0w_}
[*] Flag: hacktoday{s1g_c0ntorl_fl0w_x}
[*] Flag: hacktoday{s1g_c0ntorl_fl0w_xD}
[+] Flag: hacktoday{s1g_c0ntorl_fl0w_xD_}
```
Flag : <b>hacktoday{s1g_c0ntorl_fl0w_xD_}</b>