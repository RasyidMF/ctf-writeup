# The Simpsons (80 Points)
Ya know, I was thinking... wouldn't the Simpsons use octal as a base system? They have 8 fingers... Oh, right! The problem! Ummm, something seems odd about this image... https://mega.nz/#!yfp1nYrQ!LOz_eucuKkjAaDqVvz3GWgbfdKWn8BhussKZbx6bUMg
# Solved
Diberikan sebuah hint yaitu
```python
# Ahh! Realistically the Simpsons would use octal instead of decimal!
encoded = 152 162 152 145 162 167 150 172 153 162 145 170 141 162
key = chr(SolutionToDis(110 157 167 040 155 165 143 150 040 144 151 144 040 115 141 147 147 151 145 040 157 162 151 147 151 156 141 154 154 171 040 143 157 163 164 077 040 050 104 151 166 151 144 145 144 040 142 171 040 070 054 040 164 157 040 164 150 145 040 156 145 141 162 145 163 164 040 151 156 164 145 147 145 162 054 040 141 156 144 040 164 150 145 156 040 160 154 165 163 040 146 157 165 162 051))
key = key + key + chr(ord(key)-4)
print(DecodeDat(key=key,text=encoded))
```
Agak susah dibaca yaa, kemudian saya decode semua hasil dari Octal / Decimal
```python
key = "How much did Maggie originally cost? (Divided by 8, to the nearest integer, and then plus four)"
```
Disini bisa kita pahamin bahwa kita harus mencari tau <b>Berapa banyak Maggie membayar, kemudian di bagi 8 dan mengambil angka terdekat (jika koma)</b>
```python
key = (MaggieCost / 8)
```
Akan tetapi kita tidak tahu berapa banyak yang maggie berikan, <b>Google Siap Membantu</b>, https://www.google.com/search?q=How+much+did+Maggie+originally+cost
```
1. Maggie Money. In the original opening sequence of The Simpsons, the price that appears on the cash register when Maggie is scanned is $847.63. Creator Matt Groening says this was the monthly cost of raising a child in 1989.21 Agu 2014
```
Disana terdapat angka <b>847.63</b> yang menunjukan bahwa angka tersebut disebut sebagai <b>MaggieCost</b>. 
```python
flag = "jrjerwhzkrexar"

key = round(float(847.63 / 8))
key = chr(key + 4)
key = key + key + chr(ord(key) - 4)

print(key)
```
```
nnj
```
Key dari hint tersebut adalah <b>nnj</b>, kemudian ke halaman https://cryptii.com/pipes/vigenere-cipher untuk mengdecode teks tersebut
```
wearenumberone
```
Flag : <b>wearenumberone</b>