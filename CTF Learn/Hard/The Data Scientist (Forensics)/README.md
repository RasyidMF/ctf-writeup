# The Data Scientist (70 Points)
My friend is a data-scientist and he spends his days using Excel or cool python libraries like numpy, pandas, or opencv. But this morning he was feeling grumpy and hid my flag in a CSV.<br>
The only thing he told me is that <b>the real hint will be given when you find what the columns mean.</b>
# Solved
Diberikan sebuah file .csv yang harus kita selesaikan, disini saya tidak paham dengan challenge nya akan tetapi saya mencoba mencari tau hint yang di berikan
```
the real hint will be given when you find what the columns mean
```
Saat saya mem-block dari kolumn pertama <b>V0-V52</b> sampai ke <b>257</b> saya menemukan sebuah ASCII teks <i>Pada Kolom AVERAGE</i>
```
V0 = 83
V1 = 69
V2 = 84
V3 = 32
V4 = 65
V5 = 76
V6 = 76
V7 = 32
V8 = 86
V9 = 65

Dan seterusnya
```
Saya menggunakan python untuk menghitung rata-rata tersebut
```python
import pandas

f = pandas.read_csv("the_data_scientist.csv")
res = []

for x in f:
    t = 0
    for s in f[x]:
        t = t + s
    res.append(int(t // 255)) # 255 Column

print(res)
```
Kemudian saya mengkonversi ASCII teks tersebut menjadi teks
```python
hint = [
    83, 69, 84, 32, 65, 76, 76, 32, 86, 65, 76, 85, 69, 83,
    32, 66, 69, 84, 87, 69, 69, 78, 32, 54, 52, 32, 65, 78,
    68, 32, 54, 53, 32, 84, 79, 32, 66, 76, 65, 67, 75, 32,
    65, 78, 68, 32, 83, 67, 65, 78, 32, 73, 84
]
r = ''.join([chr(x) for x in hint])
print r
```
```
SET ALL VALUES BETWEEN 64 AND 65 TO BLACK AND SCAN IT
```
Untuk mewarnai hitam saya menggunakan https://www.ablebits.com/office-addins-blog/2013/10/18/change-background-color-excel-based-on-cell-value/. Bisa kita lihat pada baris ke <b>117 sampai 141</b> terdapat <b>QR Code</b>, kemudian mencoba untuk decode nya
```
CTFlearn{m4ch1n3_l34rn1n9_rul35}
```
Flag : <b>CTFlearn{m4ch1n3_l34rn1n9_rul35}</b>