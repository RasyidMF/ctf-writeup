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