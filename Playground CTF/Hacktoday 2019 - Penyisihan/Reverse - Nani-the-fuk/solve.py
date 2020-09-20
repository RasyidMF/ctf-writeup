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