# The Numbers - Points: 50
<b>Description : </b>The numbers... what do they mean?<br>
<b>Hints : </b>The flag is in the format PICOCTF{}
# Solved
Number : 
```
[16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]
```
Python Script :
```python
import string

flag = [16, 9, 3, 15, 3, 20, 6, "{", 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, "}"]
a = string.ascii_uppercase
r = ""

for x in flag:
        if x == "{":
                r += "{"
        elif x == "}":
                r += "}"
        else:
                r += a[x - 1]
print r
```
Flag : <b>PICOCTF{THENUMBERSMASON}</b>
