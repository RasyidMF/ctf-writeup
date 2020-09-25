# RSA Noob (60 Points)
These numbers were scratched out on a prison wall. Can you help me decode them? https://mega.nz/#!al8iDSYB!s5olEDK5zZmYdx1LZU8s4CmYqnynvU_aOUvdQojJPJQ
# Solved
Pada challenge kali ini, kita harus menggunakan code untuk menyelesaikannya. Saya menggunakan Python untuk solving
```python
from Crypto.Util.number import inverse

e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

p = 416064700201658306196320137931
q = 590872612825179551336102196593

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

m = pow(c, d, n)
print(hex(m))
print(hex(m)[2:-1].decode('hex'))
```
```
$ python solve.py
0x61626374667b6233747465725f75705f793075725f657dL
abctf{b3tter_up_y0ur_e}
```
Flag : <b>abctf{b3tter_up_y0ur_e}</b>