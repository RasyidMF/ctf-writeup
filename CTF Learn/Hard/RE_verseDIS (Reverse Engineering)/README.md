# RE_verseDIS
Could you find the hidden password?
<br>
https://mega.nz/#!XOwVmCSC!ut_5r6b32j2kD6EvlvsvJhmm58pbswusUXF08yI93Zo
# Solved
Diberikan sebuah file dengan source
```cpp
/*
.data:0000000000201080                 public key
.data:0000000000201080 key             db 'IdontKnowWhatsGoingOn',0
.data:0000000000201080                                         ; DATA XREF: main+40↑o
.data:0000000000201020 str             db 8, 3 dup(0), 6, 3 dup(0), 2Ch, 3 dup(0), 3Ah, 3 dup(0)
.data:0000000000201020                                         ; DATA XREF: main+8B↑o
.data:0000000000201020                 db 32h, 3 dup(0), 30h, 3 dup(0), 1Ch, 3 dup(0), 5Ch, 3 dup(0)
.data:0000000000201020                 db 1, 3 dup(0), 32h, 3 dup(0), 1Ah, 3 dup(0), 12h, 3 dup(0)
.data:0000000000201020                 db 45h, 3 dup(0), 1Dh, 3 dup(0), 20h, 3 dup(0), 30h, 3 dup(0)
.data:0000000000201020                 db 0Dh, 3 dup(0), 1Bh, 3 dup(0), 3, 3 dup(0), 7Ch, 3 dup(0)
.data:0000000000201020                 db 13h, 0Fh dup(0)
*/
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int i; // [rsp+8h] [rbp-8h]
  int j; // [rsp+Ch] [rbp-4h]

  printf("Input password: ", argv, envp);
  _isoc99_scanf("%s", input);
  for ( i = 0; i <= 21; ++i )
  {
    key2[i] = key[i];
    msg[i] = str[4 * i] ^ LOBYTE(key2[i]);
  }
  for ( j = 0; j <= 21; ++j )
  {
    if ( input[j] != msg[j] )
      stat = 0;
  }
  if ( stat )
    puts("Good job dude !!!");
  else
    puts("Wrong password");
  return 0;
}
```
Disini tugas kita adalah mengdecode flag tersebut, dan code inilah yang saya gunakan
```python

key = "IdontKnowWhatsGoingOn" # char[21]
str_flag = [
    8, 6, 0x2c, 0x3a, 0x32, 0x30, 0x1c, 0x5c, 1, 0x32, 0x1a, 0x12, 0x45, 0x1d,
    0x20, 0x30, 0x0d, 0x1b, 3, 0x7c, 0x13
]

msg = "" # char[24]
for x in range(len(key)):
    msg += chr(ord(key[x]) ^ str_flag[x])

print msg
```
```
$ python solve.py
AbCTF{r3vers1ng_dud3}
```
Flag : <b>AbCTF{r3vers1ng_dud3}</b>