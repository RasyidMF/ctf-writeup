# PIN (60 Points)
Can you crack my pin?
<br>
https://mega.nz/#!PXYjCKCY!F2gcs83XD6RxjOR-FNWGQZpyvUFvDbuT-PTnqRhBPGQ
# Solved
Mari kita cek source tersebut
```cpp
// .data:0000000000601040 valid           dd 51615h               ; DATA XREF: cek+7↑r
_BOOL8 __fastcall cek(int a1)
{
  return a1 == valid;
}
int __cdecl main(int argc, const char **argv, const char **envp)
{
  unsigned int v4; // [rsp+Ch] [rbp-4h]

  printf("Masukan PIN = ", argv, envp);
  __isoc99_scanf("%d", &v4);
  if ( (unsigned int)cek(v4) )
    puts("PIN benar ! \n");
  else
    puts("PIN salah ! \n");
  return 0;
}
```
Bisa kita lihat bahwa data yang bernama <b>valid</b> memiliki value <b>0x51615</b>, jika saya konversi menjadi decimal adalah <b>333333</b>
```
Masukan PIN = 333333
PIN benar !
```
Flag : <b>333333</b>