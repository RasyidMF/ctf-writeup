# The Credit Card Fraudster (20 Points)
I just arrested someone who is probably the most wanted credit card fraudster in Europe. She is a smart cybercriminal, always a step ahead INTERPOL and she kept unnoticed for years by never buying online, but buying goods with a different card every time and in different stores. My cyber-analysts found out after collecting all evidences she hacked into one the largest payment provider in Europe, reverse-engineered the software present on the server and partly corrupted the card number validation code to accept all her payments. The change enables acceptance of any transaction with a card number multiple of 123457 and the Luhn check digit is valid.
<br><br>
I caught her because every year she bought a bouquet of flowers next to the same cemetery. While handcuffing her at the flower shop's exit, she said the flowers were for her lost father and today it is his death anniversary. She broke down in tears and she did some steps and threw something in the sewers. My female colleague conducted a search on her, but she couldn't find the card she used, only the receipt.
<code>
The little flower shop
======================

European Express Debit
Card Number: 543210******1234
SALE

Please debit my account
Amount: 25.00€
</code>
Can you help me to recover the card number so that I can confirm with the flower merchant's bank the card number was used in that shop and is fraudulent?
<br><br>
Hints : <br>
1/ https://www.youtube.com/watch?v=PNXXqzU4YnM<br>
2/ Flag format is <code>CTFlearn{card_number}</code>
# Solved
Saya tidak paham dengan algoritma yang dijelaskan, saya menggunakan code yang di berikan oleh https://medium.com/@guptaavi352/ctflearn-writeups-9f247c2fe94c
```python
def digits(x):
    num = 2 * x
    return num % 10 + num / 10

def checksum(x):
    sum = 0
    isSecond = 0
    for i in range(len(x) - 1, -1, -1):
        d = int(x[i])
        if isSecond == 1:
            d = d * 2
        sum += d / 10 + d % 10
        isSecond = (isSecond + 1) % 2
    return sum

flag = "5432100000001234"
numb = 123457

for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                for e in range(10):
                    for f in range(10):
                        x = list(flag)
                        if (
                            (digits(a) + b + digits(c) + d + digits(e) + f) % 10 == 1
                        ):
                            res = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                            x[6:12] = list(res)
                            if int(''.join(x)) % numb == 0:
                                print "CTFlearn{" + ''.join(x) + "}"
```
```
CTFlearn{5432103279251234}
```
Flag : <b>CTFlearn{5432103279251234}</b>
