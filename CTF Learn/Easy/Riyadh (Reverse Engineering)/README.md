# Riyadh (Reverse Engineering)
Another entry level Reversing challenge, if you are new to Reversing you probably want to try my Reyjkavik challenge before attempting this challenge. Good Luck! The flag is hidden inside the Riyadh program. Solve the Challenge, get the flag, and I have included the encrypted sources used to create the challenge in the Riyadh.zip file. If you do to the work of solving the Challenge, I'm providing the Challenge source code (C++ and Python) if you are interested in studying the sources after solving the challenge. I think this is a great way to improve your Reversing skills when learning. Please don't share the sources or flag after you solve the challenge.
# Solved
Mari kita cek source pada file tersebut menggunakan IDA Pro
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  const __m128i *v3; // r13
  __m128i *v4; // rbp
  __m128i v5; // xmm1
  __m128i v6; // xmm2
  __m128i v7; // xmm0
  __m128i v8; // xmm1
  __m128i v9; // xmm2
  __m128i v10; // xmm3
  __m128i v11; // xmm0
  __m128i v12; // xmm0
  int v13; // er12

  __asm { endbr64 }
  memset(buffer, 0, sizeof(buffer));
  Msg1(buffer);
  sub_10F0(buffer);
  if ( argc == 1 )
  {
    v13 = 1;
    Msg2(buffer);
    sub_10F0(buffer);
    return v13;
  }
  CTFLearnHiddenFlag();
  v3 = (const __m128i *)argv[1];
  Msg3(buffer);
  if ( !(unsigned int)sub_10E0(buffer, v3) )
  {
    v13 = 2;
    Msg4(buffer);
    sub_10F0(buffer);
    return v13;
  }
  if ( sub_10C0(v3) != 30 )
  {
    v13 = 3;
    Msg6(buffer);
    sub_10F0(buffer);
    return v13;
  }
  v4 = (__m128i *)sub_10B0(256LL);
  Msg5((char *)v4->m128i_i64);
  v5 = _mm_andnot_si128(_mm_cmpeq_epi8(_mm_loadu_si128(v4), _mm_loadu_si128(v3)), (__m128i)xmmword_3020);
  v6 = _mm_cmpgt_epi8((__m128i)0LL, v5);
  v7 = _mm_unpacklo_epi8(v5, v6);
  v8 = _mm_unpackhi_epi8(v5, v6);
  v9 = _mm_cmpgt_epi16((__m128i)0LL, v8);
  v10 = _mm_cmpgt_epi16((__m128i)0LL, v7);
  v11 = _mm_add_epi32(
          _mm_add_epi32(
            _mm_add_epi32(_mm_unpackhi_epi16(v7, v10), _mm_unpacklo_epi16(v7, v10)),
            _mm_unpacklo_epi16(v8, v9)),
          _mm_unpackhi_epi16(v8, v9));
  v12
// Dan lain-lain
```
Seperti yang kita lihat bahwasannya kita tidak bisa selesaikan challenge ini tanpa <b>GDB</b>, mari kita note dulu apa arti dari <b>Msg1, Msg2, dll</b>
```
Msg1 = Welcome
Msg2 = Argument Not found
Msg3 = CTFlearn{Reversing_Is_Easy} / False Flag
Msg4 = You entered False Flag (CTFlearn{Reversing_Is_Easy})
Msg5 = Success Flag
Msg6 = Wrong Flag
```
Untuk menuju ke instruksi <b>Msg5</b>, kita harus melewati beberapa step yaitu
```
   0x8001169 <main+105>:        call   0x80010c0 <strlen@plt>
=> 0x800116e <main+110>:        cmp    rax,0x1e
   0x8001172 <main+114>:        jne    0x800134a <main+586>
```
Disini kita lihat bahwa flag nya sebesar <b>30</b> huruf dan angka, maka dari itu saya mencoba memperoleh 30 angka kemudian breakpoint lagi pada <b>0x80012df</b>
```
$ Riyadh AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Welcome to CTFlearn Riyadh Reversing Challenge!
[----------------------------------registers-----------------------------------]
RAX: 0x41 ('A')
RBX: 0x0
RCX: 0x13d6f
RDX: 0x8018ec0 ("CTFlearn{Masmak_Fortress_1865}")
RSI: 0x8005160 --> 0x4b7ab17e1180469a
RDI: 0x8005070 --> 0x2508d01b7dc612d9
RBP: 0x8018ec0 ("CTFlearn{Masmak_Fortress_1865}")
RSP: 0x7ffffffedaf0
RIP: 0x80012df --> 0xb60f0000009f840f
R8 : 0x8018ec0 ("CTFlearn{Masmak_Fortress_1865}")
R9 : 0x7c ('|')
R10: 0x7fffff5defa7
R11: 0x7fffff59bbe0 --> 0x8018fc0 --> 0x0
R12: 0x1c
R13: 0x7ffffffede8d
R14: 0x80051c0 ("CTFlearn{Reversing_Is_Easy}")
R15: 0x0
EFLAGS: 0x283 (CARRY parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80012d4 <main+468>:        add    r12d,eax
   0x80012d7 <main+471>:        movzx  eax,BYTE PTR [r13+0x1c]
   0x80012dc <main+476>:        cmp    BYTE PTR [rbp+0x1c],al
=> 0x80012df <main+479>:        je     0x8001384 <main+644>
   0x80012e5 <main+485>:        movzx  eax,BYTE PTR [rbp+0x1d]
   0x80012e9 <main+489>:        cmp    BYTE PTR [r13+0x1d],al
   0x80012ed <main+493>:        je     0x8001447 <main+839>
   0x80012f3 <main+499>:        lea    rdi,[rbp+0x8]
                                                              JUMP is NOT taken
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffedaf0
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 3, 0x00000000080012df in main ()
```
Saya coba input flag <b>CTFlearn{Masmak_Fortress_1865}</b> ternyata berhasil! Saya kira fake :3, tapi sebelum itu saya mencoba menjalankan program dengan flag tersebut
```
$ ./Riyadh CTFlearn{Masmak_Fortress_1865}
Welcome to CTFlearn Riyadh Reversing Challenge!

CONGRATULATIONS!! You found the flag:  CTFlearn{Masmak_Fortress_1865}

All Done!
```
Flag : <b>CTFlearn{Masmak_Fortress_1865}</b>
