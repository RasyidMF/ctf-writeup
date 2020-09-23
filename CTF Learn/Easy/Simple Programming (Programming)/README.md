# Simple Programming (30 Points)
Can you help me? I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2. Please! Here is the file: https://mega.nz/#!7aoVEKhK!BAohJ0tfnP7bISIkbADK3qe1yNEkzjHXLKoJoKmqLys
# Solved
Kali ini kita harus menggunakan code untuk menyelesaikan challenge ini, saya membuat script sederhana untuk menghitung <b>multiple</b>
```python
c = 0
f = open('data.dat', 'r')

for x in f.readlines():
    nol  = x.count("0")
    satu = x.count("1")

    if (nol % 3 == 0) or (satu % 2 == 0):
        c = c + 1

f.close()

print("Jawaban : " + str(c))
```
Flag : <b>6662</b>