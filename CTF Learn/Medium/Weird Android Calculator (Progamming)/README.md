# Weird Android Calculator (60 Points)
I've found this very weird android application.
<br>
Seems to be some kind of calculator, but there is something strange with it. Can you find out what it is?
<br>
https://mega.nz/#!qXIAgSKZ!u2QBlLV-3G8kmsr6yR0wqpQOFyv89e0WvBt45alBIRY
<br>
Flag is in Format: FLAG{...}
<br>
Note: You don't really need an android device to solve this. But it might be helpful :)
# Solved
Decompile apk tersebut kemudian saya menemukan code
```java
class Solve {
    public static void main(String[] args) {
        for (int i : new int[]{1407, 1397, 1400, 1406, 1346, 1400, 1385, 1394, 1382, 1293, 1367, 1368, 1365, 1344, 1354, 1288, 1354, 1382, 1288, 1354, 1382, 1355, 1293, 1357, 1361, 1290, 1355, 1382, 1290, 1368, 1354, 1344, 1382, 1288, 1354, 1367, 1357, 1382, 1288, 1357, 1348}) {
            System.out.print((char)(i ^ 1337));
        }
    }
}

```
Kemudian saya konversikan menjadi python agar bisa di decode
```python
flag = [
    1407, 1397, 1400, 1406, 1346, 1400, 1385, 1394, 1382, 1293, 1367, 1368, 1365, 1344, 1354, 1288, 1354, 1382, 1288, 1354, 1382, 1355, 1293, 1357, 1361, 1290, 1355, 1382, 1290, 1368, 1354, 1344, 1382, 1288, 1354, 1367, 1357, 1382, 1288, 1357, 1348
]

r = ""

for x in flag:
    r += chr(x ^ 1337)

print r
```
```
$ python solve.py
FLAG{APK_4nalys1s_1s_r4th3r_3asy_1snt_1t}
```
Flag : <b>FLAG{APK_4nalys1s_1s_r4th3r_3asy_1snt_1t}</b>