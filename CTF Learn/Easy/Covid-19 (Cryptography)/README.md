# Covid-19 (30 Points)
In 2019 on the Earth appeard lethal Corona Virus known as Covid-19. Is January 1st 2020. The people have not any information. Somebody interrupt message transfer. He died but let us encrypted note and very important hint. First four characters in decrypted note are: 'Hope'. Are you able to help us and read whole note?
<br>
Note: b"Iqsi88E0b/Ie>=`jmcj\x7fd2y5Eab5:aZy5Cq1dqrqFU\x80nlHls9;).0F"
# Solve
```python
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
```
Flag : <b>c0v1D__19_Wu4An-coomES</b>
