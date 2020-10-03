# Symbolic Decimals (80 Points)
Did you know that you can hide messages with symbols? For example, !@#$%^&*( is 123456789!<br> Now Try: ^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@% However, this isn't as easy as you might think.
# Solved
Saya menyelesaikan challenge ini menggunakan script
```python
key = {
    "!": 1,
    "@": 2,
    "#": 3,
    "$": 4,
    "%": 5,
    "^": 6,
    "&": 7,
    "*": 8,
    "(": 9,
    ")": 0,
    ",": " "
}

flag = "^&,*$,&),!@#,*#,!!^,(&,!!$,(%,$^,(%,*&,(&,!!$,!!%,(%,$^,(%,&),!!!,!!$,(%,$^,(%,&^,!)%,!)@,!)!,!@%"

res = ""
for x in flag:
    res += str(key[x])

print res
```
```
$ python solve.py
67 84 70 123 83 116 97 114 95 46 95 87 97 114 115 95 46 95 70 111 114 95 46 95 76 105 102 101 125
```
Decode ASCII tersebut
```
CTF{Star_._Wars_._For_._Life}
```
Flag : <b>CTF{Star_._Wars_._For_._Life}</b>