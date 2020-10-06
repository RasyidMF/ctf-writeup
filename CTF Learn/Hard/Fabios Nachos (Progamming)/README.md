# Fabio's Nachos (80 Points)
Fabio runs a very popular nacho restaurant. Every week, he takes his last nacho and adds something new to it. Fabio keeps a collection of his favorite nachos on display, but you suspect that the nachos have a deeper meaning: https://mega.nz/#!yfYyWIyS!M5kT4PCdaqHAYBd2pc0S_Ff-cPc6GT95ib-qq372t_M
# Solved
Disini kita di berikan base64 encoded dan kemudian pas saya decode saya menemukan angka yang sangat panjang yaitu
```
    927372692193078999176, 16641027750620563662096, 83621143489848422977,
    1500520536206896083277, 22698374052006863956975682, 927372692193078999176,
    7778742049, 135301852344706746049, 4807526976, 43566776258854844738105, 32951280099,
    218922995834555169026, 2427893228399975082453, 4807526976, 59425114757512643212875125
```
Saya juga sebelumnya belum pernah melihat angka seperti ini, kemudian setelah searching saya menemukan bahwa angka tersebut adalah <b>Fibonacci</b>, dan ini table nya https://oeis.org/A000045/b000045.txt. Kemudian saya download file tersebut, saya coded dengan python
```python
# Source https://oeis.org/A000045/b000045.txt
# 927372692193078999176 16641027750620563662096 83621143489848422977 1500520536206896083277 22698374052006863956975682 927372692193078999176 7778742049 135301852344706746049 4807526976 43566776258854844738105 32951280099 218922995834555169026 2427893228399975082453 4807526976 59425114757512643212875125
flag = [
    927372692193078999176, 16641027750620563662096, 83621143489848422977,
    1500520536206896083277, 22698374052006863956975682, 927372692193078999176,
    7778742049, 135301852344706746049, 4807526976, 43566776258854844738105, 32951280099,
    218922995834555169026, 2427893228399975082453, 4807526976, 59425114757512643212875125
]
table = open("Fibonacci_Table.txt", "r").read()

res = []

for x in flag:
    p = table.split(str(x) + "\n")[0]
    p = p.split(" ")[len(p.split(" ")) - 2].split("\n")[1]
    res.append(int(p))

string = ""

for x in res:
    string += chr(x)

print string
```
```console
$ python solve.py
flag{f1b0n4ch0}
```
Flag : <b>flag{f1b0n4ch0}</b>