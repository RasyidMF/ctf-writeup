# Every Bit Counts (70 Points)
My colleague is a senior C developer and he had a bad experience in his job assignment. He was developing applications for a real-time embedded operating system named "Buggy OS™". He had to implement workarounds to avoid using the standard C library in some cases. For instance the memcmp shouldn't be used to test command-line argument because of obscure reason resulting in some bits were not checked. Instead he implemented its own function to check each bit of the command-line and it was working fine.
<br>
To show case how painful it was, he showed me one of its application implementing his new function, but he forgot the supported command-line parameter.
<br>
Note: Solution with cool effects shared in comment.
# Solved
Source
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int result; // eax

  if ( argc == 2 )
  {
    if ( sub_403798(argv[1], argv, envp) == 52 )
    {
      if ( !(argv[1][28] & 0x20)
        && argv[1][36] & 0x10
        && argv[1][47] & 0x20
        && argv[1][32] & 0x20
        && argv[1][43] & 4
        && !(argv[1][50] & 0x80)
        && argv[1][8] & 1
        && argv[1][46] & 4
        && !(argv[1][32] & 0x80)
        && !(argv[1][8] & 4)
        && argv[1][48] & 0x10
        && !(argv[1][16] & 0x80)
        && !(argv[1][19] & 8)
        && argv[1][8] & 0x40
        && argv[1][43] & 0x10
        && argv[1][15] & 4
        && !(*argv[1] & 4)
        && !(argv[1][43] & 8)
        && argv[1][25] & 0x40
        && argv[1][4] & 1
        && !(argv[1][43] & 0x80)
        && !(argv[1][44] & 8)
        && argv[1][33] & 0x20
        && !(argv[1][29] & 0x10)
        && argv[1][33] & 1
        && argv[1][28] & 0x40
        && argv[1][23] & 0x40
        && argv[1][24] & 1
        && argv[1][39] & 0x20
        && !(argv[1][37] & 4)
        && !(argv[1][13] & 0x80)
        && argv[1][49] & 0x20
        && argv[1][9] & 4
        && argv[1][7] & 0x20
        && !(argv[1][48] & 4)
        && !(argv[1][18] & 4)
        && !(argv[1][45] & 4)
        && argv[1][30] & 0x10
        && !(argv[1][7] & 0x10)
        && argv[1][49] & 0x40
        && !(argv[1][2] & 0x80)
        && argv[1][12] & 0x40
        && !(argv[1][37] & 8)
        && !(argv[1][29] & 8)
        && argv[1][29] & 0x20
        && argv[1][50] & 2
        && !(argv[1][45] & 1)
        && argv[1][10] & 0x10
        && !(argv[1][40] & 0x80)
        && !(argv[1][18] & 2)
        && argv[1][43] & 1
        && !(argv[1][26] & 0x80)
        && !(argv[1][51] & 0x80)
        && argv[1][20] & 4
        && argv[1][30] & 8
        && !(argv[1][4] & 0x10)
        && !(argv[1][4] & 0x80)
        && argv[1][21] & 0x40
        && !(argv[1][23] & 0x80)
        && argv[1][12] & 0x10
        && argv[1][41] & 1
        && argv[1][13] & 0x20
        && !(argv[1][36] & 1)
        && !(argv[1][1] & 1)
        && !(argv[1][19] & 0x80)
        && !(argv[1][5] & 0x80)
        && !(argv[1][50] & 0x40)
        && argv[1][8] & 0x10
        && !(argv[1][35] & 8)
        && !(argv[1][9] & 8)
        && *argv[1] & 2
        && !(argv[1][21] & 0x80)
        && !(argv[1][7] & 1)
        && argv[1][41] & 8
        && !(argv[1][3] & 0x80)
        && argv[1][14] & 2
        && argv[1][22] & 2
        && argv[1][23] & 1
        && argv[1][39] & 2
        && !(argv[1][16] & 0x20)
        && !(argv[1][6] & 8)
        && !(argv[1][26] & 1)
        && argv[1][30] & 4
        && argv[1][26] & 2
        && !(argv[1][30] & 0x80)
        && !(argv[1][22] & 0x80)
        && !(argv[1][35] & 0x10)
        && argv[1][48] & 1
        && argv[1][33] & 4
        && argv[1][4] & 4
        && !(argv[1][36] & 0x80)
        && argv[1][31] & 8
        && !(argv[1][1] & 2)
        && argv[1][34] & 4
        && argv[1][16] & 1
        && !(argv[1][3] & 0x10)
        && argv[1][22] & 0x10
        && argv[1][42] & 1
        && argv[1][11] & 1
        && argv[1][1] & 0x10
        && argv[1][2] & 4
        && !(argv[1][10] & 8)
        && argv[1][19] & 1
        && !(argv[1][36] & 8)
        && !(argv[1][4] & 8)
        && !(argv[1][2] & 1)
        && !(argv[1][27] & 0x10)
        && argv[1][9] & 1
        && !(argv[1][13] & 2)
        && argv[1][5] & 0x20
        && !(argv[1][17] & 0x10)
        && argv[1][13] & 0x10
        && argv[1][13] & 0x40
        && argv[1][3] & 4
        && argv[1][7] & 2
        && argv[1][16] & 2
        && !(argv[1][32] & 8)
        && !(argv[1][35] & 2)
        && !(argv[1][49] & 8)
        && argv[1][27] & 4
        && !(argv[1][47] & 0x80)
        && argv[1][13] & 8
        && !(argv[1][1] & 0x80)
        && !(argv[1][38] & 0x80)
        && !(argv[1][36] & 4)
        && argv[1][51] & 0x10
        && !(argv[1][23] & 0x20)
        && argv[1][6] & 2
        && !(argv[1][35] & 0x80)
        && argv[1][20] & 0x20
        && argv[1][9] & 0x20
        && argv[1][45] & 0x20
        && argv[1][12] & 2
        && argv[1][6] & 0x10
        && argv[1][34] & 8
        && argv[1][26] & 0x20
        && !(argv[1][23] & 2)
        && !(argv[1][14] & 0x10)
        && argv[1][12] & 8
        && !(argv[1][34] & 0x80)
        && argv[1][16] & 4
        && !(argv[1][3] & 2)
        && argv[1][49] & 2
        && !(argv[1][22] & 0x20)
        && argv[1][21] & 0x20
        && !(argv[1][41] & 0x20)
        && argv[1][37] & 2
        && !(argv[1][18] & 0x80)
        && argv[1][7] & 4
        && argv[1][47] & 4
        && !(argv[1][10] & 2)
        && !(argv[1][11] & 0x80)
        && !(argv[1][32] & 4)
        && argv[1][38] & 0x40
        && !(*argv[1] & 0x10)
        && argv[1][2] & 0x40
        && !(argv[1][28] & 0x80)
        && argv[1][43] & 0x40
        && argv[1][47] & 8
        && argv[1][44] & 0x20
        && argv[1][24] & 0x20
        && argv[1][9] & 2
        && !(argv[1][6] & 4)
        && !(argv[1][49] & 4)
        && !(*argv[1] & 8)
        && argv[1][11] & 0x40
        && argv[1][5] & 1
        && argv[1][20] & 8
        && argv[1][47] & 0x40
        && argv[1][38] & 8
        && argv[1][25] & 4
        && !(argv[1][33] & 0x80)
        && !(argv[1][5] & 8)
        && !(argv[1][40] & 0x10)
        && argv[1][25] & 0x10
        && argv[1][37] & 1
        && !(argv[1][2] & 8)
        && argv[1][42] & 0x40
        && argv[1][9] & 0x10
        && !(argv[1][46] & 0x80)
        && argv[1][41] & 4
        && argv[1][41] & 0x10
        && !(argv[1][29] & 0x80)
        && !(*argv[1] & 0x20)
        && !(argv[1][37] & 0x40)
        && !(argv[1][25] & 0x80)
        && !(argv[1][23] & 0x10)
        && !(argv[1][27] & 1)
        && argv[1][15] & 0x10
        && argv[1][31] & 0x40
        && !(argv[1][42] & 0x10)
        && argv[1][10] & 0x20
        && !(argv[1][48] & 0x40)
        && !(argv[1][15] & 0x80)
        && !(argv[1][28] & 8)
        && argv[1][39] & 1
        && argv[1][40] & 2
        && !(argv[1][50] & 4)
        && argv[1][39] & 0x10
        && argv[1][42] & 4
        && argv[1][45] & 8
        && !(argv[1][13] & 4)
        && argv[1][51] & 0x20
        && !(argv[1][21] & 8)
        && !(argv[1][32] & 2)
        && argv[1][29] & 4
        && argv[1][30] & 1
        && argv[1][44] & 2
        && argv[1][3] & 8
        && !(argv[1][10] & 0x80)
        && !(argv[1][51] & 2)
        && argv[1][38] & 1
        && argv[1][19] & 0x40
        && argv[1][39] & 0x40
        && argv[1][27] & 0x20
        && argv[1][45] & 0x40
        && argv[1][2] & 2
        && argv[1][27] & 8
        && argv[1][11] & 0x10
        && argv[1][24] & 0x40
        && !(argv[1][5] & 2)
        && argv[1][25] & 2
        && argv[1][26] & 0x40
        && !(argv[1][24] & 4)
        && argv[1][4] & 0x40
        && !(argv[1][47] & 0x10)
        && argv[1][41] & 0x40
        && argv[1][34] & 0x10
        && argv[1][35] & 0x40
        && !(argv[1][5] & 4)
        && !(argv[1][21] & 2)
        && !(argv[1][45] & 0x10)
        && argv[1][36] & 2
        && argv[1][40] & 0x40
        && argv[1][21] & 4
        && argv[1][19] & 4
        && !(argv[1][12] & 0x80)
        && !(argv[1][42] & 2)
        && !(argv[1][1] & 8)
        && argv[1][16] & 0x10
        && !(argv[1][35] & 4)
        && argv[1][13] & 1
        && argv[1][1] & 0x40
        && argv[1][46] & 1
        && argv[1][31] & 0x10
        && argv[1][38] & 4
        && argv[1][47] & 2
        && argv[1][38] & 2
        && !(argv[1][37] & 0x80)
        && !(argv[1][28] & 2)
        && !(argv[1][10] & 0x40)
        && argv[1][46] & 0x10
        && !(argv[1][39] & 0x80)
        && !(argv[1][46] & 0x20)
        && argv[1][31] & 1
        && argv[1][37] & 0x10
        && *argv[1] & 1
        && argv[1][17] & 0x20
        && argv[1][11] & 0x20
        && !(argv[1][49] & 0x80)
        && !(argv[1][18] & 8)
        && argv[1][22] & 0x40
        && !(argv[1][28] & 4)
        && argv[1][14] & 8
        && !(argv[1][48] & 8)
        && argv[1][6] & 0x40
        && !(argv[1][12] & 0x20)
        && argv[1][48] & 0x20
        && !(argv[1][31] & 4)
        && argv[1][46] & 0x40
        && !(argv[1][33] & 8)
        && !(argv[1][42] & 0x80)
        && argv[1][15] & 1
        && !(argv[1][24] & 0x80)
        && argv[1][12] & 4
        && !(argv[1][21] & 0x10)
        && !(argv[1][21] & 1)
        && argv[1][31] & 0x20
        && argv[1][26] & 4
        && argv[1][51] & 0x40
        && argv[1][42] & 0x20
        && argv[1][12] & 1
        && !(argv[1][15] & 8)
        && !(argv[1][27] & 0x80)
        && argv[1][34] & 2
        && argv[1][6] & 0x20
        && argv[1][23] & 8
        && !(argv[1][39] & 4)
        && !(argv[1][18] & 1)
        && argv[1][32] & 0x10
        && !(argv[1][28] & 1)
        && argv[1][46] & 2
        && argv[1][11] & 2
        && !(argv[1][28] & 0x10)
        && argv[1][29] & 2
        && !(argv[1][47] & 1)
        && argv[1][17] & 4
        && argv[1][14] & 0x20
        && !(argv[1][43] & 2)
        && !(argv[1][31] & 0x80)
        && !(argv[1][31] & 2)
        && !(argv[1][35] & 0x20)
        && argv[1][15] & 0x40
        && !(argv[1][30] & 0x20)
        && !(argv[1][45] & 0x80)
        && argv[1][9] & 0x40
        && argv[1][7] & 8
        && !(*argv[1] & 0x80)
        && !(argv[1][38] & 0x20)
        && argv[1][37] & 0x20
        && argv[1][22] & 1
        && argv[1][50] & 0x10
        && argv[1][51] & 4
        && !(argv[1][44] & 0x10)
        && !(argv[1][25] & 0x20)
        && !(argv[1][34] & 0x20)
        && !(argv[1][44] & 0x80)
        && !(argv[1][5] & 0x10)
        && *argv[1] & 0x40
        && !(argv[1][20] & 0x10)
        && argv[1][8] & 8
        && !(argv[1][17] & 0x80)
        && argv[1][35] & 1
        && argv[1][33] & 0x10
        && !(argv[1][32] & 1)
        && !(argv[1][39] & 8)
        && argv[1][4] & 0x20
        && argv[1][22] & 4
        && !(argv[1][14] & 0x80)
        && !(argv[1][20] & 0x80)
        && argv[1][20] & 2
        && argv[1][23] & 4
        && argv[1][43] & 0x20
        && argv[1][34] & 1
        && argv[1][36] & 0x20
        && argv[1][46] & 8
        && argv[1][30] & 2
        && argv[1][8] & 0x20
        && argv[1][17] & 2
        && !(argv[1][27] & 2)
        && !(argv[1][19] & 2)
        && !(argv[1][7] & 0x80)
        && !(argv[1][3] & 1)
        && !(argv[1][1] & 0x20)
        && argv[1][30] & 0x40
        && argv[1][5] & 0x40
        && argv[1][34] & 0x40
        && !(argv[1][26] & 0x10)
        && argv[1][3] & 0x40
        && !(argv[1][41] & 0x80)
        && argv[1][40] & 1
        && !(argv[1][45] & 2)
        && argv[1][1] & 4
        && !(argv[1][26] & 8)
        && !(argv[1][48] & 0x80)
        && argv[1][25] & 8
        && argv[1][17] & 0x40
        && argv[1][29] & 1
        && argv[1][33] & 0x40
        && argv[1][27] & 0x40
        && argv[1][25] & 1
        && !(argv[1][10] & 1)
        && !(argv[1][4] & 2)
        && argv[1][40] & 4
        && argv[1][8] & 2
        && !(argv[1][15] & 2)
        && argv[1][14] & 1
        && !(argv[1][10] & 4)
        && argv[1][42] & 8
        && !(argv[1][50] & 8)
        && argv[1][38] & 0x10
        && argv[1][50] & 1
        && !(argv[1][2] & 0x10)
        && argv[1][51] & 1
        && !(argv[1][44] & 4)
        && argv[1][29] & 0x40
        && argv[1][16] & 0x40
        && argv[1][24] & 0x10
        && argv[1][18] & 0x20
        && !(argv[1][18] & 0x40)
        && argv[1][20] & 0x40
        && !(argv[1][32] & 0x40)
        && argv[1][11] & 4
        && argv[1][3] & 0x20
        && !(argv[1][2] & 0x20)
        && argv[1][7] & 0x40
        && argv[1][41] & 2
        && !(argv[1][49] & 0x10)
        && !(argv[1][9] & 0x80)
        && !(argv[1][48] & 2)
        && !(argv[1][24] & 2)
        && argv[1][36] & 0x40
        && !(argv[1][17] & 1)
        && argv[1][18] & 0x10
        && argv[1][19] & 0x10
        && argv[1][50] & 0x20
        && argv[1][40] & 0x20
        && argv[1][44] & 0x40
        && argv[1][51] & 8
        && argv[1][14] & 4
        && !(argv[1][6] & 0x80)
        && !(argv[1][17] & 8)
        && argv[1][22] & 8
        && !(argv[1][33] & 2)
        && !(argv[1][20] & 1)
        && !(argv[1][6] & 1)
        && argv[1][19] & 0x20
        && !(argv[1][8] & 0x80)
        && argv[1][16] & 8
        && argv[1][15] & 0x20
        && !(argv[1][11] & 8)
        && argv[1][24] & 8
        && argv[1][14] & 0x40
        && argv[1][40] & 8
        && argv[1][49] & 1
        && argv[1][44] & 1 )
      {
        sub_403788(aWowYouFoundMyF);
        result = 0;
      }
      else
      {
        sub_403788(aThisIsNotMyFla);
        result = 1;
      }
    }
    else
    {
      sub_403788(aSFatalErrorFla);
      result = 2;
    }
  }
  else
  {
    sub_403788(aSFatalErrorNoI);
    result = 2;
  }
  return result;
}
```
Pada kasus ini kita disuruh mencari tau flag tersebut, dan diketahui bahwa flag tersebut memiliki besar <b>52</b>, Disini saya menyelesaikan menggunakan <b>z3 Solver</b>
```python
from pwn import *
from z3 import *

FLAG_SIZE = 52
argv = [BitVec(i, 16) for i in range(FLAG_SIZE)]
SOLVER = Solver()

update = []

# Add
challenge = ["(argv[28] & 0x20)","argv[36] & 0x10","argv[47] & 0x20","argv[32] & 0x20","argv[43] & 4","!(argv[50] & 0x80)","argv[8] & 1","argv[46] & 4","!(argv[32] & 0x80)","!(argv[8] & 4)","argv[48] & 0x10","!(argv[16] & 0x80)","!(argv[19] & 8)","argv[8] & 0x40","argv[43] & 0x10","argv[15] & 4","!(argv[0] & 4)","!(argv[43] & 8)","argv[25] & 0x40","argv[4] & 1","!(argv[43] & 0x80)","!(argv[44] & 8)","argv[33] & 0x20","!(argv[29] & 0x10)","argv[33] & 1","argv[28] & 0x40","argv[23] & 0x40","argv[24] & 1","argv[39] & 0x20","!(argv[37] & 4)","!(argv[13] & 0x80)","argv[49] & 0x20","argv[9] & 4","argv[7] & 0x20","!(argv[48] & 4)","!(argv[18] & 4)","!(argv[45] & 4)","argv[30] & 0x10","!(argv[7] & 0x10)","argv[49] & 0x40","!(argv[2] & 0x80)","argv[12] & 0x40","!(argv[37] & 8)","!(argv[29] & 8)","argv[29] & 0x20","argv[50] & 2","!(argv[45] & 1)","argv[10] & 0x10","!(argv[40] & 0x80)","!(argv[18] & 2)","argv[43] & 1","!(argv[26] & 0x80)","!(argv[51] & 0x80)","argv[20] & 4","argv[30] & 8","!(argv[4] & 0x10)","!(argv[4] & 0x80)","argv[21] & 0x40","!(argv[23] & 0x80)","argv[12] & 0x10","argv[41] & 1","argv[13] & 0x20","!(argv[36] & 1)","!(argv[1] & 1)","!(argv[19] & 0x80)","!(argv[5] & 0x80)","!(argv[50] & 0x40)","argv[8] & 0x10","!(argv[35] & 8)","!(argv[9] & 8)","argv[0] & 2","!(argv[21] & 0x80)","!(argv[7] & 1)","argv[41] & 8","!(argv[3] & 0x80)","argv[14] & 2","argv[22] & 2","argv[23] & 1","argv[39] & 2","!(argv[16] & 0x20)","!(argv[6] & 8)","!(argv[26] & 1)","argv[30] & 4","argv[26] & 2","!(argv[30] & 0x80)","!(argv[22] & 0x80)","!(argv[35] & 0x10)","argv[48] & 1","argv[33] & 4","argv[4] & 4","!(argv[36] & 0x80)","argv[31] & 8","!(argv[1] & 2)","argv[34] & 4","argv[16] & 1","!(argv[3] & 0x10)","argv[22] & 0x10","argv[42] & 1","argv[11] & 1","argv[1] & 0x10","argv[2] & 4","!(argv[10] & 8)","argv[19] & 1","!(argv[36] & 8)","!(argv[4] & 8)","!(argv[2] & 1)","!(argv[27] & 0x10)","argv[9] & 1","!(argv[13] & 2)","argv[5] & 0x20","!(argv[17] & 0x10)","argv[13] & 0x10","argv[13] & 0x40","argv[3] & 4","argv[7] & 2","argv[16] & 2","!(argv[32] & 8)","!(argv[35] & 2)","!(argv[49] & 8)","argv[27] & 4","!(argv[47] & 0x80)","argv[13] & 8","!(argv[1] & 0x80)","!(argv[38] & 0x80)","!(argv[36] & 4)","argv[51] & 0x10","!(argv[23] & 0x20)","argv[6] & 2","!(argv[35] & 0x80)","argv[20] & 0x20","argv[9] & 0x20","argv[45] & 0x20","argv[12] & 2","argv[6] & 0x10","argv[34] & 8","argv[26] & 0x20","!(argv[23] & 2)","!(argv[14] & 0x10)","argv[12] & 8","!(argv[34] & 0x80)","argv[16] & 4","!(argv[3] & 2)","argv[49] & 2","!(argv[22] & 0x20)","argv[21] & 0x20","!(argv[41] & 0x20)","argv[37] & 2","!(argv[18] & 0x80)","argv[7] & 4","argv[47] & 4","!(argv[10] & 2)","!(argv[11] & 0x80)","!(argv[32] & 4)","argv[38] & 0x40","!(argv[0] & 0x10)","argv[2] & 0x40","!(argv[28] & 0x80)","argv[43] & 0x40","argv[47] & 8","argv[44] & 0x20","argv[24] & 0x20","argv[9] & 2","!(argv[6] & 4)","!(argv[49] & 4)","!(argv[0] & 8)","argv[11] & 0x40","argv[5] & 1","argv[20] & 8","argv[47] & 0x40","argv[38] & 8","argv[25] & 4","!(argv[33] & 0x80)","!(argv[5] & 8)","!(argv[40] & 0x10)","argv[25] & 0x10","argv[37] & 1","!(argv[2] & 8)","argv[42] & 0x40","argv[9] & 0x10","!(argv[46] & 0x80)","argv[41] & 4","argv[41] & 0x10","!(argv[29] & 0x80)","!(argv[0] & 0x20)","!(argv[37] & 0x40)","!(argv[25] & 0x80)","!(argv[23] & 0x10)","!(argv[27] & 1)","argv[15] & 0x10","argv[31] & 0x40","!(argv[42] & 0x10)","argv[10] & 0x20","!(argv[48] & 0x40)","!(argv[15] & 0x80)","!(argv[28] & 8)","argv[39] & 1","argv[40] & 2","!(argv[50] & 4)","argv[39] & 0x10","argv[42] & 4","argv[45] & 8","!(argv[13] & 4)","argv[51] & 0x20","!(argv[21] & 8)","!(argv[32] & 2)","argv[29] & 4","argv[30] & 1","argv[44] & 2","argv[3] & 8","!(argv[10] & 0x80)","!(argv[51] & 2)","argv[38] & 1","argv[19] & 0x40","argv[39] & 0x40","argv[27] & 0x20","argv[45] & 0x40","argv[2] & 2","argv[27] & 8","argv[11] & 0x10","argv[24] & 0x40","!(argv[5] & 2)","argv[25] & 2","argv[26] & 0x40","!(argv[24] & 4)","argv[4] & 0x40","!(argv[47] & 0x10)","argv[41] & 0x40","argv[34] & 0x10","argv[35] & 0x40","!(argv[5] & 4)","!(argv[21] & 2)","!(argv[45] & 0x10)","argv[36] & 2","argv[40] & 0x40","argv[21] & 4","argv[19] & 4","!(argv[12] & 0x80)","!(argv[42] & 2)","!(argv[1] & 8)","argv[16] & 0x10","!(argv[35] & 4)","argv[13] & 1","argv[1] & 0x40","argv[46] & 1","argv[31] & 0x10","argv[38] & 4","argv[47] & 2","argv[38] & 2","!(argv[37] & 0x80)","!(argv[28] & 2)","!(argv[10] & 0x40)","argv[46] & 0x10","!(argv[39] & 0x80)","!(argv[46] & 0x20)","argv[31] & 1","argv[37] & 0x10","argv[0] & 1","argv[17] & 0x20","argv[11] & 0x20","!(argv[49] & 0x80)","!(argv[18] & 8)","argv[22] & 0x40","!(argv[28] & 4)","argv[14] & 8","!(argv[48] & 8)","argv[6] & 0x40","!(argv[12] & 0x20)","argv[48] & 0x20","!(argv[31] & 4)","argv[46] & 0x40","!(argv[33] & 8)","!(argv[42] & 0x80)","argv[15] & 1","!(argv[24] & 0x80)","argv[12] & 4","!(argv[21] & 0x10)","!(argv[21] & 1)","argv[31] & 0x20","argv[26] & 4","argv[51] & 0x40","argv[42] & 0x20","argv[12] & 1","!(argv[15] & 8)","!(argv[27] & 0x80)","argv[34] & 2","argv[6] & 0x20","argv[23] & 8","!(argv[39] & 4)","!(argv[18] & 1)","argv[32] & 0x10","!(argv[28] & 1)","argv[46] & 2","argv[11] & 2","!(argv[28] & 0x10)","argv[29] & 2","!(argv[47] & 1)","argv[17] & 4","argv[14] & 0x20","!(argv[43] & 2)","!(argv[31] & 0x80)","!(argv[31] & 2)","!(argv[35] & 0x20)","argv[15] & 0x40","!(argv[30] & 0x20)","!(argv[45] & 0x80)","argv[9] & 0x40","argv[7] & 8","!(argv[0] & 0x80)","!(argv[38] & 0x20)","argv[37] & 0x20","argv[22] & 1","argv[50] & 0x10","argv[51] & 4","!(argv[44] & 0x10)","!(argv[25] & 0x20)","!(argv[34] & 0x20)","!(argv[44] & 0x80)","!(argv[5] & 0x10)","argv[0] & 0x40","!(argv[20] & 0x10)","argv[8] & 8","!(argv[17] & 0x80)","argv[35] & 1","argv[33] & 0x10","!(argv[32] & 1)","!(argv[39] & 8)","argv[4] & 0x20","argv[22] & 4","!(argv[14] & 0x80)","!(argv[20] & 0x80)","argv[20] & 2","argv[23] & 4","argv[43] & 0x20","argv[34] & 1","argv[36] & 0x20","argv[46] & 8","argv[30] & 2","argv[8] & 0x20","argv[17] & 2","!(argv[27] & 2)","!(argv[19] & 2)","!(argv[7] & 0x80)","!(argv[3] & 1)","!(argv[1] & 0x20)","argv[30] & 0x40","argv[5] & 0x40","argv[34] & 0x40","!(argv[26] & 0x10)","argv[3] & 0x40","!(argv[41] & 0x80)","argv[40] & 1","!(argv[45] & 2)","argv[1] & 4","!(argv[26] & 8)","!(argv[48] & 0x80)","argv[25] & 8","argv[17] & 0x40","argv[29] & 1","argv[33] & 0x40","argv[27] & 0x40","argv[25] & 1","!(argv[10] & 1)","!(argv[4] & 2)","argv[40] & 4","argv[8] & 2","!(argv[15] & 2)","argv[14] & 1","!(argv[10] & 4)","argv[42] & 8","!(argv[50] & 8)","argv[38] & 0x10","argv[50] & 1","!(argv[2] & 0x10)","argv[51] & 1","!(argv[44] & 4)","argv[29] & 0x40","argv[16] & 0x40","argv[24] & 0x10","argv[18] & 0x20","!(argv[18] & 0x40)","argv[20] & 0x40","!(argv[32] & 0x40)","argv[11] & 4","argv[3] & 0x20","!(argv[2] & 0x20)","argv[7] & 0x40","argv[41] & 2","!(argv[49] & 0x10)","!(argv[9] & 0x80)","!(argv[48] & 2)","!(argv[24] & 2)","argv[36] & 0x40","!(argv[17] & 1)","argv[18] & 0x10","argv[19] & 0x10","argv[50] & 0x20","argv[40] & 0x20","argv[44] & 0x40","argv[51] & 8","argv[14] & 4","!(argv[6] & 0x80)","!(argv[17] & 8)","argv[22] & 8","!(argv[33] & 2)","!(argv[20] & 1)","!(argv[6] & 1)","argv[19] & 0x20","!(argv[8] & 0x80)","argv[16] & 8","argv[15] & 0x20","!(argv[11] & 8)","argv[24] & 8","argv[14] & 0x40","argv[40] & 8","argv[49] & 1","argv[44] & 1"]
for x in challenge:
    if x[0] == "!":
        update.append(x[1::] + " == 0")
    else:
        update.append(x + " != 0")

# Adding into solver
for x in update:
    SOLVER.add(eval(x))

print(SOLVER.check())
print(SOLVER.model())
```
```
[k!0 = 67,
k!1 = 84,
k!2 = 70,
k!3 = 108,
k!4 = 101,
k!5 = 97,
k!6 = 114,
k!7 = 110,
k!8 = 123,
k!9 = 119,
k!10 = 48,
k!11 = 119,
k!12 = 95,
k!13 = 121,
k!14 = 111,
k!15 = 117,
k!16 = 95,
k!17 = 102,
k!18 = 48,
k!19 = 117,
k!20 = 110,
k!21 = 100,
k!22 = 95,
k!23 = 77,
k!24 = 121,
k!25 = 95,
k!26 = 102,
k!27 = 108,
k!28 = 96,
k!29 = 103,
k!30 = 95,
k!31 = 121,
k!32 = 48,
k!33 = 117,
k!34 = 95,
k!35 = 65,
k!36 = 114,
k!37 = 51,
k!38 = 95,
k!39 = 115,
k!40 = 111,
k!41 = 95,
k!42 = 109,
k!43 = 117,
k!44 = 99,
k!45 = 104,
k!46 = 95,
k!47 = 110,
k!48 = 49,
k!49 = 99,
k!50 = 51,
k!51 = 125]
```
Kemudian ektrak hasil tersebut
```python
k = [x for x in range(52)]

k[0] = 67
k[1] = 84
k[2] = 70
k[3] = 108
k[4] = 101
k[5] = 97
k[6] = 114
k[7] = 110
k[8] = 123
k[9] = 119
k[10] = 48
k[11] = 119
k[12] = 95
k[13] = 121
k[14] = 111
k[15] = 117
k[16] = 95
k[17] = 102
k[18] = 48
k[19] = 117
k[20] = 110
k[21] = 100
k[22] = 95
k[23] = 77
k[24] = 121
k[25] = 95
k[26] = 102
k[27] = 108
k[28] = 96
k[29] = 103
k[30] = 95
k[31] = 121
k[32] = 48
k[33] = 117
k[34] = 95
k[35] = 65
k[36] = 114
k[37] = 51
k[38] = 95
k[39] = 115
k[40] = 111
k[41] = 95
k[42] = 109
k[43] = 117
k[44] = 99
k[45] = 104
k[46] = 95
k[47] = 110
k[48] = 49
k[49] = 99
k[50] = 51
k[51] = 125

r = ""
for x in k:
    r += chr(x)

print r
```
```
CTFlearn{w0w_you_f0und_My_fl`g_y0u_Ar3_so_much_n1c3}
```
Disini ada 1 huruf yang kurang, yang jelas pasti huruf <b>A</b> maupun dalam huruf / special character, saya mencoba 1 per 1 dan yang berhasil adalah <b>@</b><br>
Flag : <b>CTFlearn{w0w_you_f0und_My_fl@g_y0u_Ar3_so_much_n1c3}</b>
