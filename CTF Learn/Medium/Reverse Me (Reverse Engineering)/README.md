# Reverse Me (50 Points)
A simple reverse engineering challenge.
# Solved
Cek source nya
```cpp
v7 = 87;
v8 = 66;
v9 = 75;
v10 = 69;
v11 = -52;
v12 = -69;
v13 = -127;
v14 = -52;
v15 = 113;
v16 = 122;
v17 = 113;
v18 = 102;
v19 = -33;
v20 = -69;
v21 = -122;
v22 = -51;
v23 = 100;
v24 = 111;
v25 = 110;
v26 = 92;
v27 = -14;
v28 = -83;
v29 = -102;
v30 = -40;
v31 = 126;
v32 = 111;
printf("Enter flag [CTFlearn{ ... }]: ", argv, envp);
__isoc99_scanf("%26s", &v33);
v5 = encrypt(&v33);
v6 = shuffle(v5);
for ( i = 0; i <= 25; ++i )
{
    if ( *(&v7 + i) != *(_BYTE *)(i + v6) )
    {
        puts("Incorrect");
        return 0;
    }
}
puts("Correct!");
```
```cpp
_BYTE *__fastcall encrypt(const char *a1)
{
    size_t v1; // rax
    int i; // [rsp+14h] [rbp-4Ch]
    _BYTE *v4; // [rsp+18h] [rbp-48h]
    int v5; // [rsp+20h] [rbp-40h]
    int v6; // [rsp+24h] [rbp-3Ch]
    int v7; // [rsp+28h] [rbp-38h]
    int v8; // [rsp+2Ch] [rbp-34h]
    int v9; // [rsp+30h] [rbp-30h]
    int v10; // [rsp+34h] [rbp-2Ch]
    int v11; // [rsp+38h] [rbp-28h]
    int v12; // [rsp+3Ch] [rbp-24h]
    unsigned __int64 v13; // [rsp+48h] [rbp-18h]

    v13 = __readfsqword(0x28u);
    v1 = strlen(a1);
    v4 = malloc(v1);
    v5 = 1;
    v6 = 3;
    v7 = 3;
    v8 = 7;
    v9 = 222;
    v10 = 173;
    v11 = 190;
    v12 = 239;
    for ( i = 0; i < strlen(a1); ++i )
        v4[i] = *(&v5 + i % 8) ^ a1[i];
    return v4;
}
```
```cpp
BYTE *__fastcall shuffle(const char *a1)
{
    size_t v1; // rax
    int i; // [rsp+14h] [rbp-1Ch]
    int j; // [rsp+14h] [rbp-1Ch]
    _BYTE *v5; // [rsp+18h] [rbp-18h]

    v1 = strlen(a1);
    v5 = malloc(v1 - 4);
    for ( i = 0; i < strlen(a1); i += 2 )
        v5[i] = a1[i + 1];
    for ( j = 1; j < strlen(a1); j += 2 )
        v5[j] = a1[j - 1];
    return v5;
}
```
Disini dapat kita lihat bahwa enkripsi flag menggunakan fungsi <b>shuffle</b> dan <b>encrypt</b>, dan ini adalah kode yang saya gunakan untuk menyelesaikannya
```cpp
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

char * xorencrypt(char * txt)
{
    int key[8] = {1, 3, 3, 7, 222, 173, 190, 239};
    char * res;
    res = (char*)malloc(strlen(txt));
    
    for (int i = 0; i < (int)strlen(txt); ++i) {
        res[i] = (key[i % 8] ^ txt[i]);
    }
    return res;
}

char * shuffle(char * txt) 
{
    char * res;
    res = (char*)malloc(strlen(txt) - 4);
    for (int i = 0; i < (int)strlen(txt); i += 2 )
    { res[i] = txt[i + 1]; }
    for (int j = 1; j < (int)strlen(txt); j += 2 )
    { res[j] = txt[j - 1]; }
    return res;
}

int main()
{
    char flag[26] = {
        87, 66, 75, 69, -52, -69, -127, -52, 113, 122, 113, 102,
        -33, -69, -122, -51, 100, 111, 110, 92, -14, -83, -102,
        -40, 126, 111
    };
    
    cout << flag << endl;

    char * capture = shuffle(flag);
    
    cout << capture << endl;
    
    capture = xorencrypt(capture);
    
    cout << capture << endl;

    return 0;
}
```
```
CTFLearn{reversing_is_fu0
```
Flagnya agakk rusak, mari saya perbaiki
```
CTFLearn{reversing_is_fun}
```
Flag : <b>CTFLearn{reversing_is_fun}</b>