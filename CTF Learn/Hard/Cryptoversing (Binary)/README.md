# Cryptoversing (90 Points)
Hello! My manager sent me a file named xor.bin, and he wants from you to crack this program, and get the flag.
<br>
https://mega.nz/#!neYzjQQS!mKNcdADY8u_V0Iy1a57gQpjNGTni03l7lTKOZVaYNes
# Solved
Cek Source pada file tersebut
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+4h] [rbp-CCh]
  int j; // [rsp+8h] [rbp-C8h]
  int k; // [rsp+Ch] [rbp-C4h]
  int v7; // [rsp+18h] [rbp-B8h]
  int v8; // [rsp+1Ch] [rbp-B4h]
  int v9; // [rsp+20h] [rbp-B0h]
  int v10; // [rsp+24h] [rbp-ACh]
  int v11; // [rsp+28h] [rbp-A8h]
  int v12; // [rsp+2Ch] [rbp-A4h]
  char v13[8]; // [rsp+30h] [rbp-A0h]
  __int64 v14; // [rsp+38h] [rbp-98h]
  int v15; // [rsp+40h] [rbp-90h]
  char v16; // [rsp+44h] [rbp-8Ch]
  char v17[32]; // [rsp+50h] [rbp-80h]
  char s[72]; // [rsp+70h] [rbp-60h]
  unsigned __int64 v19; // [rsp+B8h] [rbp-18h]

  v19 = __readfsqword(0x28u);
  *(_QWORD *)v13 = 'DcE}Ob_h';
  v14 = '(hu)G+RO';
  v15 = 'v,lj';
  v16 = 76;
  printf("[*] Hello! Welcome to our Program!\nEnter the password to contiune:  ", argv);
  __isoc99_scanf("%s", s);
  v7 = 16;
  v8 = 24;
  v9 = strlen(s) >> 1;
  v10 = strlen(s);
  v11 = 0;
  v12 = strlen(s) >> 1;
  for ( i = 0; i <= 1; ++i )
  {
    for ( j = *(&v11 + i); j < *(&v9 + i); ++j )
      v17[j] = *(&v7 + i) ^ s[j];
  }
  for ( k = 0; k < strlen(v13) - 1; ++k )
  {
    if ( v17[k] != v13[k] )
    {
      puts("[-] Wrong Password");
      exit(0);
    }
  }
  puts("[+] Successful Login");
  return 0;
}
```
Disini kita harus me decrypt hasil enkripsi <b>XOR</b> tersebut, dan saya melihat ada 4 integer digunakan untuk mengenkripsi
```python
v7 = 16;
v8 = 24;
v9 = strlen(s) >> 1;
v10 = strlen(s);
```
Maka dari itu saya mencoba 1 per 1 dari 4 integer tersebut menggunakan python
```python
flag = "h_bO}EcDOR+G)uh(jl,vL"
res = ""

for x in flag:
    res += chr(ord(x) ^ 16)

print res
```
```console
$ python solve.py
xOr_mUsT_B;W9ex8z|<f\
```
Disini bisa kita lihat, terdapat teks yang bisa dibaca yaitu <b>xOr_mUsT_B</b>. Simpan dalam note kemudian mencoba brute lagi
```python
flag = "h_bO}EcDOR+G)uh(jl,vL"
res = ""

for x in flag:
    res += chr(ord(x) ^ 24)

print res
```
```console
$ python solve.py
pGzWe]{\WJ3_1mp0rt4nT
```
Final : Gabungkan semua huruf yang masuk akal dan menjadi <b>xOr_mUsT_B</b> + <b>3_1mp0rt4nT</b> : <b>xOr_mUsT_B3_1mp0rt4nT</b><br>
Flag <b>xOr_mUsT_B3_1mp0rt4nT</b>
