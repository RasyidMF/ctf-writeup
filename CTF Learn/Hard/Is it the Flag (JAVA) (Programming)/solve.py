import random
import itertools


def hashCode(txt):
    r = 0
    for x in range(len(txt)):
        r = (r * 31) + ord(txt[x])
    return r

def generateText():
    cr = "abcdefghijklmnopqrstuvwxyz0123456789"
    r = ""
    for x in range(6):
        r += cr[random.randint(0, len(cr) - 1)]
    return r

flag = 1472541258 # Lower Case

L1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L3 = ['0','1','2','3','4','5','6','7','8','9']
L4 = L3 + L1

for x in xrange(6): # Flag size = 6
    for pw in itertools.product(L4, repeat=6):
        r = ''.join(pw)
        cd = hashCode(r)
        
        if cd > (1472541258 - 5000) and cd < 1472541258:
            print "Closer : " + r + " | " + str(cd)
        elif cd == flag:
            print "= FLAG : " + r + " | " + str(cd)
            exit(0)

# = FLAG : 0ghzxy | 1472541258
