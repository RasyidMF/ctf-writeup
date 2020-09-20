from pwn import *

flag = "picoCTK\x80k5zsid6q_fb69f6c2}"
resu = ""

def p(x):
    return log.info(x)

for x in range(6):
    resu += flag[x]

for x in range(6, 15):
    resu += chr(ord(flag[x]) - 5)

resu += chr(ord(flag[15]) + 3)

for x in range(16, 26):
    resu += flag[x]


p(resu)
