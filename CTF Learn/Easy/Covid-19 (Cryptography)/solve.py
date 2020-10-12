flag = b"Iqsi88E0b/Ie>=`jmcj\x7fd2y5Eab5:aZy5Cq1dqrqFU\x80nlHls9;).0F"
flag = "d2y5Eab5:aZy5Cq1dqrqFU"

res = ""
c = 0
for x in flag:
    print str(ord(x))
    c += 1
    try:
        if c == 5:
            c = 1
        res += chr(ord(x) - c)
    except:
        pass

print res