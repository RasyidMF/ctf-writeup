# reverse_cipher - Points: 300
We have recovered a binary and a text file. Can you reverse the flag. Its also found in /problems/reverse-cipher_2_d8dc36eefa9dfce00eac3dab8f42513c on the shell server.
# Solved
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  char ptr[23]; // [rsp+0h] [rbp-50h]
  char v5; // [rsp+17h] [rbp-39h]
  int v6; // [rsp+2Ch] [rbp-24h]
  FILE *v7; // [rsp+30h] [rbp-20h]
  FILE *stream; // [rsp+38h] [rbp-18h]
  int j; // [rsp+44h] [rbp-Ch]
  int i; // [rsp+48h] [rbp-8h]
  char v11; // [rsp+4Fh] [rbp-1h]

  stream = fopen("flag.txt", "r");
  v7 = fopen("rev_this", "a");
  if ( !stream )
    puts("No flag found, please make sure this is run on the server");
  if ( !v7 )
    puts("please run this on the server");
  v6 = fread(ptr, 24uLL, 1uLL, stream);
  if ( v6 <= 0 )
    exit(0);
  for ( i = 0; i <= 7; ++i )
  {
    v11 = ptr[i];
    fputc(v11, v7);
  }
  for ( j = 8; j <= 22; ++j )
  {
    v11 = ptr[j];
    if ( j & 1 )
      v11 -= 2;
    else
      v11 += 5;
    fputc(v11, v7);
  }
  v11 = v5;
  fputc(v5, v7);
  fclose(v7);
  return fclose(stream);
}
```
Disini kode yang penting yaitu
```cpp
for ( j = 8; j <= 22; ++j )
{
v11 = ptr[j];
if ( j & 1 )
    v11 -= 2;
else
    v11 += 5;
fputc(v11, v7);
}
```
Saya menggunakan python untuk menyelesaikannya
```python
flag = "picoCTF{w1{1wq83k055j5f}"
ress = ""
for x in range(8, 22):
    k = ord(flag[x])
    if x & 1:
        ress += chr(k + 2)
    else: ress += chr(k - 5)

print "picoCTF{" + ress + "}"
```
```console
$ python solve.py
picoCTF{r3v3rs35f207e7}
```
Flag : <b>picoCTF{r3v3rs35f207e7}</b>