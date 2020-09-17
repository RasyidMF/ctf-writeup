from pwn import *
import string
# Algorithm :
#   String.fromCharCode((c <= "Z" ? 90 : 122) >= (c = c.charCodeAt(0) + 13) ? c : c - 26)

flag = "CHPP{wf_j1gu_e0g13_fgvYY_3m}"
r = ""

for x in flag:

    if x == "{" or x == "}" or x == "_" or x in string.digits:
        r += x
        continue

    c = ord(x)

    if c <= 90:
        d = 90
    else: d = 122

    if d >= (ord(x) + 13):
        r += chr(c + 13)
    else:
        r += chr(c - 13)

log.info(r)