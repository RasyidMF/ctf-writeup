# Demonstration
import dis

class Demons:
    def func2(c1, c2):
        tmp1 = c2
        tmp2 = c1

        return tmp1 ^ tmp2
    def func():
        fp = open("flag.txt").read()
        cipher = ''
        for i in range(len(fp)):
            temp = func2(ord(fp[i]), 170)
            cipher += chr(func2(temp, i))
        print(cipher)

dis.dis(Demons)
# End

def func2(c1, c2):
    tmp1 = c2
    tmp2 = c1

    return tmp1 ^ tmp2
def func():
    fp = open("flag.txt").read()
    cipher = ''
    for i in range(len(fp)):
        temp = func2(ord(fp[i]), 170)
        cipher += chr(func2(temp, i))
    print(cipher)

func()