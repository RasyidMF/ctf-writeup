# XOR Is Friend Not Food (100 Points)
Here: \t\x1b\x11\x00\x16\x0b\x1d\x19\x17\x0b\x05\x1d(\x05\x005\x1b\x1f\t,\r\x00\x18\x1c\x0e
<br>
I think the flag started with: ctflearn{
# Solved
Disini saya harus mencari tau key untuk decode XOR encryption ini, saya menggunakan <b>cribdrag</b> untuk mendapatkan key
```python
data = "091b1100160b1d19170b051d280500351b1f092c0d00181c0e"
```
```
$ python ~/Tools/Python/cribdrag.py 091b1100160b1d19170b051d280500351b1f092c0d00181c0e
Your message is currently:
0       _________________________
Your key is currently:
0       _________________________
Please enter your crib: ctflearn{
*** 0: "jowlsjowl"
```
Saya melihat pada index 0 terdapat kata-kata yang masuk diakal yaitu <b>jowls</b>, saya berpikir bahwa hal tersebut adalah sebuah key, maka dari itu saya ke halaman https://www.dcode.fr/xor-cipher. Kemudian saya masukan data + key nya disana dan ini yang saya dapatkan
```
Data :
091b1100160b1d19170b051d280500351b1f092c0d00181c0e

Key :
JOWLS

Result :
ctflearn{xor_is_the_goop}
```
Flag : <b>ctflearn{xor_is_the_goop}</b>