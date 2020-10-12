flag = "picoCTF{w1{1wq83k055j5f}"
ress = ""
for x in range(8, 22):
    k = ord(flag[x])
    if x & 1:
        ress += chr(k + 2)
    else: ress += chr(k - 5)

print "picoCTF{" + ress + "}"