# IFEST-password (231 Points)
https://drive.google.com/open?id=1gsC0mw6r5_390ZO5L1aOobW1q1-9VtqV
# Solved
Pada kasus ini kita disuruh untuk mengdecode, cek pada source nya
```cpp
    if ( s[4] + s[11] * s[8] * s[3] != 482646 )
        v6 = 0;
    if ( s[33] != 57 )
        v6 = 0;
    if ( s[17] - *s - s[38] * s[10] != -2371 )
        v6 = 0;
    if ( s[5] * s[28] + s[34] * s[27] != 5454 )
        v6 = 0;
    if ( s[5] - s[30] + s[16] != 50 )
        v6 = 0;
    if ( s[35] * s[14] - s[42] != 4975 )
        v6 = 0;
    if ( s[14] + s[38] - s[8] - s[25] != 35 )
        v6 = 0;
    if ( s[14] + s[30] * s[41] + s[23] != 5298 )
        v6 = 0;
    if ( s[39] * s[6] != 2640 )
        v6 = 0;
    if ( s[39] + s[16] - s[22] * s[36] != -5374 )
        v6 = 0;
    if ( s[11] * s[32] * s[12] + s[3] != 280991 )
        v6 = 0;
    if ( s[4] + s[40] - s[8] - s[20] != 33 )
        v6 = 0;

// Dan seterusnya
```
Kita note dulu ya, Password nya ada <b>43</b> angka dan huruf. dan setiap 1 angka / huruf itu terdeklarasi oleh <b>if condition</b>. Bisa dibilang ini challenge akan memakan waktu untuk mencari teks nya :(, But <i>we are hacker dont give up</i>. Sebelum itu, bahwa ada <b>Framework python</b> yang dapat menyelesaikan <b>if conditional</b> dan banyak di gunakan saat menjelang CTF yaitu <b>z3 solver</b>. Jadi disini saya menyelesaikan challenge ini menggunakan framework tersebut. Berikut code nya
```python
from pwn import *
from z3 import *

FLAG_SIZE = 43 # strlen(*(const char **)(v5 + 8)) == 43
s = [BitVec(i, 16) for i in range(FLAG_SIZE)]
SOLVER = Solver()

for x in range(FLAG_SIZE):
    # Pastikan character yang di tentukan adalah printable
    SOLVER.add(47 < s[x])
    SOLVER.add(126 > s[x])
    SOLVER.add(64 != s[x],
        96 != s[x],
        ord('[') != s[x],
        ord(']') != s[x],
        ord('<') != s[x],
        ord('>') != s[x],
        ord(':') != s[x],
        ord('^') != s[x],
        ord(';') != s[x],
        ord('=') != s[x],
        ord('\\') != s[x],
        ord('#') != s[x],
        ord('|') != s[x],
        ord('?') != s[x])

# Mistake
#   Sebelumnya tidak berhasil semenjak tidak merhatikan conditional nya (!=)
#   Seharusnya menjadi (==)

SOLVER.add( s[4] + s[11] * s[8] * s[3] == 482646 )
SOLVER.add( s[33] == 57 )
SOLVER.add( s[17] - s[0] - s[38] * s[10] == -2371 )
SOLVER.add( s[5] * s[28] + s[34] * s[27] == 5454 )
SOLVER.add( s[5] - s[30] + s[16] == 50 )
SOLVER.add( s[35] * s[14] - s[42] == 4975 )
SOLVER.add( s[14] + s[38] - s[8] - s[25] == 35 )
SOLVER.add( s[14] + s[30] * s[41] + s[23] == 5298 )
SOLVER.add( s[39] * s[6] == 2640 )
SOLVER.add( s[39] + s[16] - s[22] * s[36] == -5374 )
SOLVER.add( s[11] * s[32] * s[12] + s[3] == 280991 )
SOLVER.add( s[4] + s[40] - s[8] - s[20] == 33 )
SOLVER.add( s[13] + s[6] - s[29] * s[13] == -5608 )
SOLVER.add( s[16] - s[3] - s[38] == -32 )
SOLVER.add( s[31] * (1 - s[12]) + s[28] == -2495 )
SOLVER.add( s[27] - s[29] + s[7] * s[3] == 4017 )
SOLVER.add( s[33] - s[7] - s[11] + s[27] == -42 )
SOLVER.add( s[26] - s[2] * s[40] == -3835 )
SOLVER.add( s[15] - s[25] - s[40] == -15 )
SOLVER.add( s[0] - s[37] - s[21] + s[11] == 21 )
SOLVER.add( s[22] + s[30] - s[39] - s[33] == 85 )
SOLVER.add( s[2] + s[9] * s[28] == 6834 )
SOLVER.add( s[16] + s[25] - s[15] * s[10] == -4595 )
SOLVER.add( s[32] * s[2] + s[3] - s[33] == 3752 )
SOLVER.add( s[31] * s[0] * s[41] - s[23] == 189775 )
SOLVER.add( s[41] + s[27] + s[13] + s[11] == 261 )
SOLVER.add( s[24] * s[16] - s[14] + s[5] == 5550 )
SOLVER.add( s[7] - s[20] - s[38] == -51 )
SOLVER.add( s[13] + s[19] - s[10] - s[0] == 33 )
SOLVER.add( s[38] - s[7] * s[33] - s[33] == -2801 )
SOLVER.add( s[42] + s[15] * s[18] == 5273 )
SOLVER.add( s[1] * s[23] * s[3] == 569380 )
SOLVER.add( s[29] * s[14] + s[22] - s[1] == 10227 )
SOLVER.add( s[32] + s[10] - s[39] - s[17] == -7 )
SOLVER.add( s[22] * s[4] * s[21] == 790356 )
SOLVER.add( s[27] * s[12] + s[19] == 2750 )
SOLVER.add( s[33] * s[2] - s[19] + s[23] == 3933 )
SOLVER.add( s[8] - s[23] + s[40] * s[8] == 3208 )
SOLVER.add( s[42] + s[37] * s[24] == 3317 )
SOLVER.add( s[2] + s[34] + s[23] + s[8] == 276 )
SOLVER.add( s[38] * s[32] == 2646 )
SOLVER.add( s[26] * (s[37] + 1) + s[6] == 5732 )
SOLVER.add( s[18] - s[30] + s[4] == 36 )
SOLVER.add( s[25] + s[28] * s[37] * s[37] == 178752 )
SOLVER.add( s[32] + s[27] + s[0] == 179 )
SOLVER.add( s[34] + s[23] * s[36] == 5638 )
SOLVER.add( s[5] - s[42] * s[33] == -7075 )
SOLVER.add( s[19] * s[38] - s[10] - s[1] == 4684 )
SOLVER.add( s[36] * (s[35] - 1) - s[34] == 2798 )
SOLVER.add( s[40] * s[19] * s[19] - s[15] == 547329 )
SOLVER.add( s[25] * s[14] - s[10] == 5652 )
SOLVER.add( s[19] * s[25] - s[9] + s[36] == 5520 )
SOLVER.add( s[6] + s[21] * s[9] == 11979 )
SOLVER.add( s[42] + s[20] + s[18] == 228 )
SOLVER.add( (s[13] - 1) * s[37] == 3135 )
SOLVER.add( s[4] + s[3] + s[0] == 240 )
SOLVER.add( s[14] * s[6] * s[32] == 259200 )
SOLVER.add( s[28] * s[39] * s[17] == 163350 )
SOLVER.add( s[7] * s[24] - s[16] * s[19] == -7056 )
SOLVER.add( s[37] - s[25] * s[24] + s[0] == -3062 )
SOLVER.add( s[38] + s[26] + s[26] == 245 )
SOLVER.add( s[2] - s[9] - s[40] - s[27] == -163 )
SOLVER.add( s[33] + s[22] - s[21] == 57 )
SOLVER.add( s[10] == 48 )
SOLVER.add( s[9] - s[2] * s[39] * s[33] == -216192 )
SOLVER.add( s[1] * s[35] * s[22] == 346290 )
SOLVER.add( s[0] + s[14] - s[25] * s[3] == -4558 )
SOLVER.add( s[5] * s[39] - s[19] == 2652 )
SOLVER.add( s[8] + s[1] - s[37] == 70 )
SOLVER.add( s[17] - s[26] * s[3] - s[7] == -8129 )
SOLVER.add( s[23] + s[27] + s[19] == 248 )
SOLVER.add( s[2] * s[37] + s[28] == 3988 )
SOLVER.add( s[8] + s[33] - s[25] + s[30] == 157 )
SOLVER.add( s[21] + s[3] * s[1] == 5907 )
SOLVER.add( s[18] + s[31] == 103 )
SOLVER.add( s[16] - s[3] * s[30] + s[9] == -8077 )
SOLVER.add( s[24] * s[26] * s[20] == 279888 )
SOLVER.add( s[19] * (s[39] + 1) - s[28] == 5433 )
SOLVER.add( s[42] + s[8] * s[24] + s[23] == 3415 )
SOLVER.add( s[35] - s[41] - s[21] * s[2] == -6693 )
SOLVER.add( s[2] - s[33] + s[29] == 114 )
SOLVER.add( s[20] - s[13] * s[36] == -3141 )
SOLVER.add( s[28] - s[1] * s[4] == -5825 )
SOLVER.add( s[3] + s[27] * s[17] + s[6] == 2939 )
SOLVER.add( s[17] + s[1] + s[0] == 197 )
SOLVER.add( s[28] * s[22] - s[40] == 5278 )

while True:
    checkSolver = SOLVER.check()
    model = SOLVER.model()
    temp = [0 for x in range(FLAG_SIZE)]
    for x in range(FLAG_SIZE):
        # Mengambil Inputan yang di solve oleh z3
        i = eval(str(
            model[x])[2:]
        )
        temp[i] = eval(str(model[model[x]]))
    prbflag = ''.join(chr(temp[i]) for i in range(FLAG_SIZE))
    if "IFEST" in prbflag:
        log.success("Flag : " + prbflag)
        exit(0)
```
Flag : <b>IFEST2019{0f38dcd64b3aab89b47fd36943991793}</b>
