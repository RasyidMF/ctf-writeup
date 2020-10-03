# Is it the Flag? (JAVA) (90 Points)
Pedro was disappointed because he didn't speak Python well enough to capture some of the flags on CTFLearn. His plan for revenge was to create one in his native language (Java). The flag is a String of 6 alphanumeric characters. Capture it. https://mega.nz/#!SHp1xCAL!I9-Zy4kwu_JY019MiYZ6CzGey8sJ6UvqE-ML2idmkrs
# Solved
```java
public class IsItTheFlag {

    public static boolean isFlag(String str) {
        return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
    }

    public static void main(String[] args) {
        String flag = "------";
        if (isFlag(flag))
            System.out.println("You found it!");
        else
            System.out.println("Try again :(");
    }
}
```
Diketahui bahwa kita harus mencari hashCode <b>1471587914</b> atau <b>1472541258</b>, dikarenakan tidak bisa di-reverse hal tersebut saya menggunakan Bruteforce pada script python. Dan untungnya kita sudah diberi petunjuk <b>Length Flag</b> tersebut yaitu <b>6</b>
```python
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
```
Bruteforce nya membutuhkan waktu juga untuk mendapatkan HashCode yang cocok ! <br>
Flag : <b>0ghzxy</b>