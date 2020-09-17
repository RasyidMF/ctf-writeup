# Theory of RSA (50 Points)
Bisakah kamu menemukan hasil dari angka dibawah ini menggunakan RSA ?<br>
e = 150815<br>
d = 1941<br>
N = 435979<br>
Format Flag : PUCC{hasilnya}
# Solved
Selesai menggunakan python script
```python
from Crypto.Util.number import inverse

e = 150815
d = 1941
n = 435979

print(pow(e, d, n))
```
Flag : <b>PUCC{133337}</b>

