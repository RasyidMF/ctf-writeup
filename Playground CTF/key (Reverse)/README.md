# key (50 Points)
Bisakah anda menebak key yang benar?<br>
Format flag: Bootcamp{.*}
# Solved
Mari kita cek source pada program tersebut
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char s; // [rsp+0h] [rbp-90h]
  char s2; // [rsp+70h] [rbp-20h]

  __isoc99_scanf("%100s", &s, envp);
  if ( strlen(&s) != 25 )
  {
    puts("Wrong!");
    exit(0);
  }
  decrypt(&s2, secret);
  if ( !strcmp(&s, &s2) )
    printf("Here your flag: %s\n", &s2);
  return 0;
}
```
Kita bisa lihat, bahwa algoritma yang dipakai oleh program ini tidaklah aman. <b>Kok bisa?</b>, Cek pada code di line ini
```cpp
decrypt(&s2, secret);
  if ( !strcmp(&s, &s2) )
```
Perintah dari decrypt tersebut memberikan output pada <b>&s2</b>, nah otomatis hasil output nya masuk di registers kan!. Jadi kita tidak usah capek-capek baca code dari fungsi <b>decrypt</b>, Jadi disini saya memakai GDB kemudian breakpoint pada address <b>0x000000000040079a</b>
```
   0x0000000000400782 <+103>:   lea    rdx,[rbp-0x20]
   0x0000000000400786 <+107>:   lea    rax,[rbp-0x90]
   0x000000000040078d <+114>:   mov    rsi,rdx
   0x0000000000400790 <+117>:   mov    rdi,rax
   0x0000000000400793 <+120>:   call   0x400560 <strcmp@plt>
   0x0000000000400798 <+125>:   test   eax,eax
=> 0x000000000040079a <+127>:   jne    0x4007b4 <main+153>
```
Kita bisa lihat, string yang telah di decrypt masuk ke registers <b>rbp</b>, mari kita dump
```
(gdb) x/100bc $rbp-0x40
0x7ffffffedb20: 1 '\001'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'
0x7ffffffedb28: 13 '\r' 8 '\b'  64 '@'  0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'
0x7ffffffedb30: -56 '\310'      15 '\017'       121 'y' -1 '\377'       -1 '\377'       127 '\177'      0 '\000'        0 '\000'
0x7ffffffedb38: -64 '\300'      7 '\a'  64 '@'  0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'
0x7ffffffedb40: 66 'B'  111 'o' 111 'o' 116 't' 99 'c'  97 'a'  109 'm' 112 'p'
0x7ffffffedb48: 123 '{' 51 '3'  110 'n' 99 'c'  82 'R'  121 'y' 112 'p' 116 't'
0x7ffffffedb50: 51 '3'  100 'd' 95 '_'  102 'f' 108 'l' 52 '4'  103 'g' 53 '5'
0x7ffffffedb58: 125 '}' 0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'
0x7ffffffedb60: 0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'        0 '\000'
0x7ffffffedb68: -77 '\263'      112 'p' 92 '\\' -1 '\377'       -1 '\377'       127 '\177'      0 '\000'        0 '\000'
0x7ffffffedb70: 32 ' '  -42 '\326'      125 '}' -1 '\377'       -1 '\377'       127 '\177'      0 '\000'        0 '\000'
0x7ffffffedb78: 88 'X'  -36 '\334'      -2 '\376'       -1 '\377'       -1 '\377'       127 '\177'      0 '\000'        0 '\000'
0x7ffffffedb80: 0 '\000'        0 '\000'        0 '\000'        0 '\000'
```
Address pada <b>0x7ffffffedb40</b> terlihat ada format flag nya. Mari kita arahkan address nya kesana
```
(gdb) x/s 0x7ffffffedb40
0x7ffffffedb40: "Bootcamp{3ncRypt3d_fl4g5}"
```
Yep that is the flag!<br>
Flag : <b>Bootcamp{3ncRypt3d_fl4g5}</b>
