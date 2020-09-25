# Riga (20 Points)
Riga is another beginner Reverse Engineering Challenge. Ghidra is a good tool to get started with disassembly and some RE challenges can be solved using Ghidra alone (no gdb required). The sources are included as sources.zip.enc... solve the challenge, get the flag, view the sources used to create the challenge if you are interested. Good Luck!
# Solved
Hint mengatakan bahwa kita tidak perlu <b>GDB</b> untuk mendapatkan flag, maka dari itu saya mencoba decompile file tersebut menggunakan IDA Pro
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  const char *v3; // r12
  char *v4; // rbx
  char v5; // al
  int result; // eax

  __asm { endbr64 }
  memset(buffer, 0, sizeof(buffer));
  StewedSaurkraut0();
  if ( argc == 1 )
  {
    StewedSaurkraut1();
    result = 1;
  }
  else
  {
    v3 = argv[1];
    v4 = buffer;
    sub_10A0(buffer, argv[1], 256LL);
    while ( sub_10C0(v3) > (unsigned __int64)(v4 - buffer) )
    {
      *v4 ^= 0xDEu;
      ++v4;
    }
    BlackRyeBread();
    if ( beerEmbassy )
    {
      if ( beerEmbassy == 1 )
        v5 = HerbalTea0(buffer);
      else
        v5 = HerbalTea2(buffer);
    }
    else
    {
      v5 = HerbalTea1(buffer);
    }
    if ( v5 )
    {
      sub_10F0(1LL, "Congratulations!! You found the flag %s\n", v3);
      result = 0;
    }
    else
    {
      sub_10F0(1LL, "Sorry, you did not find the flag %s\n", v3);
      result = 2;
    }
  }
  return result;
}
```
Kita note dulu ya hasil penelitian
```
sub_10A0 = strcpy()
sub_10F0 = printf()
sub_10C0 = strlen()
sub_10E0 = gettimeofday()
```
Pada fungsi <b>HerbalTea0</b> terdapat fungsi yang berkaitan dengan <b>strlen</b>
```
0x80015ab <_Z10HerbalTea0Pc+75>:     cmp    rax,0x1e
```
Yang menunjukkan flag harus memiliki besar <b>0x1e / 30</b>
```
CTFlearn{....................}
```
Disini saya melihat fungsi (Menggunakan Ghidra)
```cpp
bVar3 = cVar2 + 0x11;
if (bVar3 < 0x7f) {
  if (bVar3 < 0x20) {
    bVar3 = cVar2 + 0x70;
  }
  if ((bVar3 ^ 0xcb) != pickles0[lVar7]) goto LAB_00101620;
}
else {
  if ((byte)(cVar2 + 0xb2U ^ 0xcb) != pickles0[lVar7]) goto LAB_00101620;
}
```
Sebelumnya mari kita ambil data yang berada pada <b>pickles0</b>
```python
pickles0 = [
    0x9F, 0xAE, 0x9C, 0xB6, 0xBD, 0xB9, 0xEF, 0xEB, 0xE6,
    0x9E, 0xB9, 0xEC, 0xB3, 0xB9, 0xE3, 0xB9, 0xBB, 0xA8,
    0x89, 0xE3, 0xBD, 0xEF, 0xBB, 0x96, 0xB9, 0xED, 0xE3,
    0x89, 0xB9, 0xE4
]
```
Pada kode tersebut, setiap karakter akan di tambah <b>0x11 / 17</b> <i>Yang dimaksud di tambah karakter adalah Nomor ASCII nya, contoh <b>a / ord("a") + 17 = r</b></i>, kemudian di encoded menggunakan <b>XOR</b>
```cpp
bVar3 = cVar2 + 0x11;
if ((bVar3 ^ 0xcb) // ....
```
Disini saya menggunakan python untuk mengdecode text tersebut
```python
import string

pickles0 = [
    0x9F, 0xAE, 0x9C, 0xB6, 0xBD, 0xB9, 0xEF, 0xEB, 0xE6,
    0x9E, 0xB9, 0xEC, 0xB3, 0xB9, 0xE3, 0xB9, 0xBB, 0xA8,
    0x89, 0xE3, 0xBD, 0xEF, 0xBB, 0x96, 0xB9, 0xED, 0xE3,
    0x89, 0xB9, 0xE4
]

r = ""

a = string.printable
for x in pickles0:
    t = (x ^ 0xCB) - 17
    r += chr(t)

print(r)
```
```
CTFlea???Da?ga?a_R1?e?_La??1a?
```
Hasilnya, bisa kita lihat bahwa kalkulasi perhitungan saya benar dan ada beberapa karakter yang tidak terdekripsi. Maka dari itu saya mencoba mengambil angka hex tersebut
```python
for x in pickles0:
    t = (x ^ 0xCB) - 17

    if chr(t) in a:
        r += chr(t)
    else: r += " " + hex(t)
print(r)
```
```
CTFlea 0x13  0xf  0x1c Da 0x16 ga 0x17 a_R1 0x17 e 0x13 _La 0x15  0x17 1a 0x1e
```
Saya tau bahwa setelah huruf <b>CTFlea</b> adalah <b>rn{</b>, Saya mencoba kalkulasi menggunakan python
```python
print ord("r") ^ 0x13
=> 97
```
Hasil nya adalah 97, maka dari itu saya mencoba mengkalkulasi dngn script tersebut
```python
a = string.printable
for x in pickles0:
    t = (x ^ 0xCB) - 17

    if chr(t) in a:
        r += chr(t)
    else:
        p = chr(t ^ 97)
        if p in a:
            r += p
        else: r += " " + hex(t) + " "

print(r)
```
```
CTFlearn}Dawgava_R1ver_Latv1a 0x1e
```
Keknya udah lengkap nih flag, tinggal 2 huruf yang tersisa
```
CTFlearn{Dawgava_R1ver_Latv1a}
```
Setelah saya input, ternyata flag nya salah :(. Kemudian saya membaca kata-kata yang tidak jelas lokasinya <b>Dawgava</b>, setelah saya mencari pada google inilah yang saya dapatkan https://www.google.com/search?q=Dawgava
```
Menampilkan hasil untuk Daugava
Atau telusuri Dawgava

Sungai Daugava - Wikipedia bahasa Indonesia, ensiklopedia ...
```
Apa kemungkinan flagnya adalah
```
CTFlearn{Daugava_R1ver_Latv1a}
```
Setelah saya input ternyata benar :D. <i>Jika ada kata-kata yang tidak jelas, Google siap membantu anda</i>.<br>
Flag : <b>CTFlearn{Daugava_R1ver_Latv1a}</b>