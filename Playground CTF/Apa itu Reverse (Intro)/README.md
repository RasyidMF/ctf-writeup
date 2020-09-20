# Apa itu Reverse? (50 Points)
Reverse adalah katgori dimana peserta diberikan sebuah code atau file, lalu peserta dituntut untuk mencoba memahami cara kerja code atau file tersebut, sehingga peserta dapat menemukan flag yang tersembunyi tersebut.<br>
Berikut terlampir contoh file yang memiliki flag tersembunyi. Coba jalankan file tersebut dan cari flagnya!
# Solved
Cek source pada file tersebut menggunakan IDA Pro
```cpp
int __cdecl main(int argc, const char **argv, const char **envp)
{
  int v4; // [rsp+Ch] [rbp-24h]
  __int64 v5; // [rsp+10h] [rbp-20h]

  strcpy((char *)&v5, "PlaygroundCTF{3z_r3veR5e}");
  printf("Masukkan bilangan yang dikali 3 hasilnya 15: ", argv);
  __isoc99_scanf("%d", &v4);
  if ( v4 == 5 )
    printf("Congrats. Flag: %s\n", &v5);
  else
    puts("WRONG ANSWER!");
  return 0;
}
```
Flag : <b>PlaygroundCTF{3z_r3veR5e}</b>
