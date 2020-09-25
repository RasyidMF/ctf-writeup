# Rangoon (10 Points)
This is the third in a series of introductory Reversing Challenges; Reyjkavik, Riyadh and Rangoon. These are designed for people new to Reversing. A little gdb, C and Assembler knowledge should be enough to solve this challenge. Good Luck!
<br>
Note that once you solve the challenge, you can use the flag to decrypt the source file used to create the challenge if you are interested in seeing the original C program.
<br>
The LiveOverflow channel on YouTube has some great tutorials on reversing, this video has almost everything you need to solve this challenge: https://www.youtube.com/watch?v=VroEiMOJPm8
# Solved
Mari kita lihat source nya
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v3; // er13
  char *v4; // rbx
  bool v5; // cf
  bool v6; // zf
  const char *v7; // r14
  __int64 v8; // rcx
  const char *v9; // rdi
  const char *v10; // rsi
  __int64 v11; // rax
  __int64 v12; // r15
  __int64 v13; // rdx
  _BOOL4 v14; // er13
  char *v15; // rdi
  __int64 v16; // r12
  __int64 v17; // rax
  __int64 v18; // rax
  __int64 v19; // rax
  __int64 v20; // rax
  __int64 v21; // rax
  __int64 v22; // rdx
  __int64 v23; // rax
  __int64 v25; // [rsp+0h] [rbp-40h]

  __asm { endbr64 }
  v3 = argc;
  v25 = sub_10F0(argc, argv, envp);
  FillInStrings();
  memset(buffer, 0, 0x100uLL);
  v4 = &buffer[256];
  sub_10B0(1LL, "%s\n\n", WelcomeMsg);
  v5 = (unsigned int)argc < 1;
  v6 = argc == 1;
  if ( argc == 1 )
  {
    sub_10B0(1LL, "%s\n\n", UsageMsg);
  }
  else
  {
    v7 = argv[1];
    v8 = 9LL;
    v9 = "CTFlearn{";
    v10 = argv[1];
    do
    {
      if ( !v8 )
        break;
      v5 = *v10 < (unsigned int)*v9;
      v6 = *v10++ == *v9++;
      --v8;
    }
// ===============================================================
	v13 = (unsigned int)(v7[17] == 95) + 2;
        v14 = v7[22] == 95;
        v15 = &buffer[strlen(buffer)];
        *(_QWORD *)v15 = 'nraelFTC';
        v16 = strings;
        v15 += 9;
        *(_WORD *)(v15 - 1) = 123;
        v17 = sub_10D0(v15, *(_QWORD *)(v16 + 8 * v13), v4 - v15);
        v18 = sub_1110(v17, "_", 2LL, &v4[-v17]);
        v19 = sub_10D0(v18 + 1, *(_QWORD *)(v16 + 8LL * (unsigned int)(5 * v14 + 3)), (char *)&unk_41DF - v18);
        v20 = sub_1110(v19, "_", 2LL, &v4[-v19]);
        v21 = sub_10D0(v20 + 1, *(_QWORD *)(v16 + 8 * v12), (char *)&unk_41DF - v20);
        if ( sub_1110(v21, "}", 2LL, &v4[-v21]) + 1LL - (_QWORD)buffer == 28 )
// Dan lain-lain
```
Bisa kita lihat bahwa flag tersebut berformat <b>CTFlearn{</b>, sebelum itu saya mencatat bahwa ada beberapa <b>Exit Code</b> yang harus di note
```
1 = Tidak ada flag yang akan di periksa
2 = Tidak terdapat format CTFlearn{
3 = Mengisi Flag yang salah
4 = Format flag yang salah dan tidak di akhiri dengan huruf }
```
Dan ada terdapat pengecekan pada besar flag yaitu
```cpp
if ( sub_1110(v21, "}", 2LL, &v4[-v21]) + 1LL - (_QWORD)buffer == 28 )
```
Kita harus tahu bahwa flag memiliki huruf dan angka sebanya 28, sebelum itu disaat saya menggunakan breakpoint pada <b>0x80012be</b> saya menemukan fake flag
```
RBP: 0x80040e0 ("CTFlearn{Prince_Princess_Thaketa}")
```
Sebenarnya pada kasus ini terdapat banyak <b>Fake Flag</b> di karenakan penghitungan nya yang saya tidak bisa jelaskan, disini saya mencoba memahami bahwasannya karakter ke <b>17</b> harus <b>_</b>
```cpp
v13 = (unsigned int)(v7[17] == 95) + 2;
```
Dan saya juga merhatikan pada code ini
```cpp
if ( memcpy_chk(v21, "}", 2LL, &v4[-v21]) + '\x01' - (_QWORD)buffer == 28 )
```
Jika saya bisa melewati baris ini, maka saya dapat langsung mendapatkan flag nya didalam registers. Saya mencoba breakpoint pada addr <b>0x80012c2</b>
```
[----------------------------------registers-----------------------------------]
RAX: 0x80040fb --> 0x7d ('}')
RBX: 0xe5
RCX: 0x7d ('}')
RDX: 0x2
RSI: 0x7d ('}')
RDI: 0x80040fb --> 0x7d ('}')
RBP: 0x80040e0 ("CTFlearn{Princess_Maha_Devi}")
RSP: 0x7ffffffedaf0
RIP: 0x80012c2 --> 0xf7894cee89487f75
R8 : 0x0
R9 : 0x80041df --> 0x8016eb000
R10: 0x8002015 --> 0x766f6c2049000a0a ('\n\n')
R11: 0x8002015 --> 0x766f6c2049000a0a ('\n\n')
R12: 0x8016eb0 --> 0x80020c1 --> 0x6c6c4100676e694b ('King')
R13: 0x1c
R14: 0x7ffffffedea7
R15: 0xc ('\x0c')
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80012b6 <main+406>:        call   0x8001110 <__memcpy_chk@plt>
   0x80012bb <main+411>:        add    r13,rax
   0x80012be <main+414>:        cmp    r13,0x1c
=> 0x80012c2 <main+418>:        jne    0x8001343 <main+547>
   0x80012c4 <main+420>:        mov    rsi,rbp
   0x80012c7 <main+423>:        mov    rdi,r14
   0x80012ca <main+426>:        call   0x8001100 <strcmp@plt>
   0x80012cf <main+431>:        mov    r13d,eax
                                                              JUMP is NOT taken
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffedaf0
[------------------------------------------------------------------------------]
```
Input yg saya gunakan adalah
```
CTFlearn{Princess_King.....}
```
<i><b>Note: </b> sebelumnya saya menghabiskan waktu untuk mendapatkan nilai hasil dari <b>R13</b> agar mendapatkan nilai <b>0x1c</b>, dikarenakan saya tidak mengikuti instruksi pada assembly tersebut :(.</i><br>
Jika kita lihat, saya sudah melewati instruksi <b>0x80012c2</b>, maka dari itu kita tidak perlu breakpoint dimana-mana lgi, pada registers sudah di terapkan flagnya disana
```
RBP: 0x80040e0 ("CTFlearn{Princess_Maha_Devi}")
```
Flag : <b>CTFlearn{Princess_Maha_Devi}</b>