# Lost In The Binary (80 Points)
I lost a flag inside this binary, please help me to find it. If you trigger certain anti-debugging techniques, you might get false flags…. flag format: FLAG-(str) https://mega.nz/#!ifgzQQCC!E1W0cSOFRvi7bE_v419rzwQB2jAHF0IsIRAWL6H1RNE
# Solved
Diberikan sebuah binary file
```cpp
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  size_t v3; // rax
  size_t v4; // rax
  int i; // [rsp+1Ch] [rbp-24h]
  int m; // [rsp+20h] [rbp-20h]
  int l; // [rsp+24h] [rbp-1Ch]
  int k; // [rsp+28h] [rbp-18h]
  int j; // [rsp+2Ch] [rbp-14h]

  if ( ptrace(PTRACE_TRACEME, 0LL, 0LL, 0LL) == -1 )
    goto LABEL_2;
  if ( a1 > 4 )
  {
    qword_602148 = strtol(a2[1], 0LL, 10);
    if ( qword_602148 )
    {
      qword_602150 = strtol(a2[2], 0LL, 10);
      if ( qword_602150 )
      {
        qword_602158 = strtol(a2[3], 0LL, 10);
        if ( qword_602158 )
        {
          qword_602160 = strtol(a2[4], 0LL, 10);
          if ( qword_602160 )
          {
            if ( -24 * qword_602148 - 18 * qword_602150 - 15 * qword_602158 - 12 * qword_602160 == -18393
              && 9 * qword_602158 + 18 * (qword_602150 + qword_602148) - 9 * qword_602160 == 4419
              && 4 * qword_602158 + 16 * qword_602148 + 12 * qword_602150 + 2 * qword_602160 == 7300
              && -6 * (qword_602150 + qword_602148) - 3 * qword_602158 - 11 * qword_602160 == -8613 )
            {
              qword_602178 = qword_602158 + qword_602150 * qword_602148 - qword_602160;
              sprintf(byte_602141, "%06x", qword_602178);
              v4 = strlen(byte_602141);
              MD5(byte_602141, v4, byte_602110);
              for ( i = 0; i <= 15; ++i )
                sprintf(&byte_602120[2 * i], "%02x", (unsigned __int8)byte_602110[i]);
              printf(off_602080, byte_602120);
              exit(0);
            }
          }
        }
      }
    }
LABEL_2:
    printf("password : ");
    __isoc99_scanf("%s", &s1);
    if ( strlen(&s1) > 0x10 )
    {
      puts("the password must be less than 16 character");
      exit(1);
    }
    for ( j = 0; j < strlen(&s1); ++j )
      *(&s1 + j) ^= 6u;
    if ( !strcmp(&s1, a7yq2hryrn5yJga) )
    {
      v3 = strlen(&s1);
      MD5(&s1, v3, byte_602110);
      for ( k = 0; k <= 15; ++k )
        sprintf(&byte_602120[2 * k], "%02x", (unsigned __int8)byte_602110[k]);
      printf(off_602080, byte_602120);
      exit(0);
    }
    puts("bad password!");
    exit(0);
  }
  printf("password : ");
  __isoc99_scanf("%s", &s1);
  if ( strlen(&s1) > 0x10 )
  {
    puts("the password must be less than 16 character");
    exit(1);
  }
  for ( l = 0; l < strlen(&s1); ++l )
  {
    *(&s1 + l) ^= 2u;
    ++*(&s1 + l);
    *(&s1 + l) = ~*(&s1 + l);
  }
  if ( !memcmp(&s1, &unk_6020B8, 9uLL) )
  {
    for ( m = 0; m < strlen(s); m += 2 )
    {
      s[m] ^= 0x45u;
      s[m + 1] ^= 0x26u;
    }
    puts(s);
  }
  else
  {
    puts("bad password!");
  }
  return 0LL;
}
```
Disini saya menemukan <b>ptrace</b> yang melarang kita untuk melakukan debugging (Anti-Debugger), saya ubah hal tersebut menjadi <b>JMP</b>, Kemudian diberikan lagi 4 instruksi yang harus kita lewati yaitu
```cpp
if ( -24 * qword_602148 - 18 * qword_602150 - 15 * qword_602158 - 12 * qword_602160 == -18393
    && 9 * qword_602158 + 18 * (qword_602150 + qword_602148) - 9 * qword_602160 == 4419
    && 4 * qword_602158 + 16 * qword_602148 + 12 * qword_602150 + 2 * qword_602160 == 7300
    && -6 * (qword_602150 + qword_602148) - 3 * qword_602158 - 11 * qword_602160 == -8613 )
{
    qword_602178 = qword_602158 + qword_602150 * qword_602148 - qword_602160;
    sprintf(byte_602141, "%06x", qword_602178);
    v4 = strlen(byte_602141);
    MD5(byte_602141, v4, byte_602110);
    for ( i = 0; i <= 15; ++i )
    sprintf(&byte_602120[2 * i], "%02x", (unsigned __int8)byte_602110[i]);
    printf(off_602080, byte_602120);
    exit(0);
}
```
Disini saya tidak dapat menyelesaikannya tanpa menggunakan <b>z3 Solver</b> dan inilah code saya
```python
from z3 import *

qword_602148 = Int('0')
qword_602150 = Int('1')
qword_602158 = Int('2')
qword_602160 = Int('3')

SOLVER = Solver()
SOLVER.add(-24 * qword_602148 -18 * qword_602150 -15 * qword_602158 - 12 * qword_602160 == -18393)
SOLVER.add(9 * qword_602158 + 18 * (qword_602150 + qword_602148) - 9 * qword_602160 == 4419)
SOLVER.add(4 * qword_602158 + 16 * qword_602148 + 12 * qword_602150 + 2 * qword_602160 == 7300)
SOLVER.add(-6 * (qword_602150 + qword_602148) - 3 * qword_602158 - 11 * qword_602160 == -8613)

print(SOLVER.check())
print(SOLVER.model())
```
```console
$ python solve.py
sat
[1 = 115, 0 = 227, 2 = 317, 3 = 510]
```
Kemudian jalankan dengan argument tersebut
```console
$ ./lost_in_bin 115 227 317 510
FLAG-21a84f2c7c7fd432edf1686215db05ea
```
Flag : <b>FLAG-21a84f2c7c7fd432edf1686215db05ea</b>