# Investigative Reversing 0 - Points: 300
<b>Description : </b>We have recovered a binary and an image. See what you can make of it. There should be a flag somewhere. Its also found in /problems/investigative-reversing-0_0_ebc669df876196bdc09a2f54fd5fffed on the shell server.<br>
<b>Hints : </b>Try using some forensics skills on the image. This problem requires both forensics and reversing skills. A hex editor may be helpful
# Solved
Lets take a look at source file, im using IDA Pro
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+4h] [rbp-4Ch]
  int j; // [rsp+8h] [rbp-48h]
  FILE *stream; // [rsp+10h] [rbp-40h]
  FILE *v8; // [rsp+18h] [rbp-38h]
  char ptr; // [rsp+20h] [rbp-30h]
  char v10; // [rsp+21h] [rbp-2Fh]
  char v11; // [rsp+22h] [rbp-2Eh]
  char v12; // [rsp+23h] [rbp-2Dh]
  char v13; // [rsp+24h] [rbp-2Ch]
  char v14; // [rsp+25h] [rbp-2Bh]
  char v15; // [rsp+2Fh] [rbp-21h]
  unsigned __int64 v16; // [rsp+48h] [rbp-8h]

  v16 = __readfsqword(0x28u);
  stream = fopen("flag.txt", "r");
  v8 = fopen("mystery.png", "a");
  if ( !stream )
    puts("No flag found, please make sure this is run on the server");
  if ( !v8 )
    puts("mystery.png is missing, please run this on the server");
  if ( (int)fread(&ptr, 0x1AuLL, 1uLL, stream) <= 0 )
    exit(0);
  puts("at insert");
  fputc(ptr, v8);
  fputc(v10, v8);
  fputc(v11, v8);
  fputc(v12, v8);
  fputc(v13, v8);
  fputc(v14, v8);
  for ( i = 6; i <= 14; ++i )
    fputc((char)(*(&ptr + i) + 5), v8);
  fputc((char)(v15 - 3), v8);
  for ( j = 16; j <= 25; ++j )
    fputc(*(&ptr + j), v8);
  fclose(v8);
  fclose(stream);
  return __readfsqword(0x28u) ^ v16;
}
```
We can read, that flag is inside file <b>mystery.png</b>, so i decided to using <b>xxd</b> (Like hints say) and this what i got
```
0001e860: ed5a 9d38 d01f 5600 0000 0049 454e 44ae  .Z.8..V....IEND.
0001e870: 4260 8270 6963 6f43 544b 806b 357a 7369  B`.picoCTK.k5zsi
0001e880: 6436 715f 6662 3639 6636 6332 7d         d6q_fb69f6c2}
```
Seems like the flag is encrypted, so lets take a look at source again
```cpp
for ( i = 6; i <= 14; ++i )
    fputc((char)(*(&ptr + i) + 5), v8);
fputc((char)(v15 - 3), v8);
  for ( j = 16; j <= 25; ++j )
    fputc(*(&ptr + j), v8);
```
This is easy encryption algorithm, so this is my solve using python script
```python
from pwn import *

flag = "picoCTK\x80k5zsid6q_fb69f6c2}"
resu = ""

def p(x):
    return log.info(x)

for x in range(6):
    resu += flag[x]

for x in range(6, 15):
    resu += chr(ord(flag[x]) - 5)

resu += chr(ord(flag[15]) + 3)

for x in range(16, 26):
    resu += flag[x]


p(resu)
```
Flag : <b>picoCTF{f0und_1t_fb69f6c2}</b>