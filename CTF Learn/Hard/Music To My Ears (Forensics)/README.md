# Music To My Ears (70 Points)
This audio file is supposed to say the flag, but it's corrupted! ): <br> https://mega.nz/#!jexRzTzD!Fd3tD8ZcLquXJrsycMFUzozC9MHqaG-srUBfGREtL-0 <br>Can you fix it and input the flag? <br>
# Solved
Disini kita harus memperbaiki corrupted file, saya melihat pada headernya
```
20 20 20 20 66 69 6C 65 74 79 70 65 4D 34 41 20     filetypeM4A
```
Yang seharusnya menjadi
```
00 00 00 20 66 74 79 70 4D 34 41 ftypM4A
```
Maka dari situ saya mengubahnya
```
Result:

$ file hereisyourflag.m4a
hereisyourflag.m4a: ISO Media, Apple iTunes ALAC/AAC-LC (.M4A) Audio
```
Yang dikeluarkan pada audio tersebut ialah
```
Here is your flag : 1_c4n_f1x_it
```
Flag : <b>CTFlearn{1_c4n_f1x_it}</b>