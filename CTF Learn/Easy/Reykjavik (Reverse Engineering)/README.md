# Reykjavik (10 Points)
Good beginning Reversing challenge - jump into gdb and start looking for the flag!
# Solved
Kita di berikan file .zip yang berisi file binary
```
Reykjavik: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=7279eeb601e0fae531eb3f5414fd8c710731f953, for GNU/Linux 3.2.0, not stripped
```
Sebelum itu saya menggunakan perintah <code>strings Reyjavik</code>
```
CTFlearn{Is_This_A_False_Flag?}
```
Hal tersebut adalah fake flag, maka dari itu saya harus menggunakan IDA Pro untuk membaca source tersebut
```cpp
v23 = 0;
v12 = byte_4020 ^ 0xAB;
v11 = _mm_xor_si128(_mm_load_si128((const __m128i *)&xmmword_20F0), (__m128i)data);
v13 = byte_4021 ^ 0xAB;
v14 = byte_4022 ^ 0xAB;
v15 = byte_4023 ^ 0xAB;
v16 = byte_4024 ^ 0xAB;
v17 = byte_4025 ^ 0xAB;
v18 = byte_4026 ^ 0xAB;
v19 = byte_4027 ^ 0xAB;
v20 = byte_4028 ^ 0xAB;
v21 = byte_4029 ^ 0xAB;
v22 = byte_402A ^ 0xAB;
v9 = sub_10A0(&v11, v3, "CTFlearn{Is_This_A_False_Flag?}", v6);
if ( v9 )
{
    v9 = 4;
    sub_10B0(1LL, "Sorry Dude, '%s' is not the flag :-(\n\n", v3);
}
else
{
    sub_10B0(1LL, "Congratulations, you found the flag!!: '%s'\n\n", &v11);
}
```
Kita bisa lihat disini bahwa flag terenkripsi menggunakan <b>XOR</b> algorithm, maka dari itu saya menggunakan <b>GDB</b> untuk mencari encoded flag tersebut. Saya membuat breakpoint pada address <b>0x00000000080011dd</b> dan membaca address pada <b>data</b>. <i>Address data : <b>0x8004010</b></i>
```
$ x/56bc 0x8004010
0x8004010 <data>:       0xe8    0xff    0xed    0xc7    0xce    0xca    0xd9    0xc5
0x8004018 <data+8>:     0xd0    0xee    0xd2    0xce    0xf4    0xe7    0x9b    0xdd
0x8004020 <data+16>:    0xce    0xf4    0xe2    0xc8    0xce    0xc7    0xca    0xc5
0x8004028 <data+24>:    0xcf    0xf4    0xd6
```
```python
flag = [0xe8, 0xff, 0xed, 0xc7, 0xce, 0xca, 0xd9, 0xc5,
0xd0, 0xee, 0xd2, 0xce, 0xf4, 0xe7, 0x9b, 0xdd,
0xce, 0xf4, 0xe2, 0xc8, 0xce, 0xc7, 0xca, 0xc5,
0xcf, 0xf4, 0xd6]

r = ""
for x in flag:
    r += chr(x ^ 0xAB)
print r
```
```
CTFlearn{Eye_L0ve_Iceland_}
```
Flag : <b>CTFlearn{Eye_L0ve_Iceland_}</b>
