# Choose Wisely (50 Points)
Yang seharusnya pertama kali kamu lakukan adalah import wise.
# Solved
Jadi ada beberapa fake flag di dalam file binary tersebut termasuk
```
DiskoCTF{permen_yosan_ngga_dapet_nlag}
DiskoCTF{kalau_pattern_flagnya_sama_berarti_bukan_flag}
DiskoCTF{Kota_Serang_aje_kendor_maju}
```
Setelah saya jalan-jalan pada stack, saya menemukan sesuatu yang mencurigakan yaitu
```
.rodata:0000000000083D60 ; char __pyx_k_FkqimAVDyicow_cpw_qchc_ogorgnchc[62]
.rodata:0000000000083D60 _ZL40__pyx_k_FkqimAVDyicow_cpw_qchc_ogorgnchc db 46h, 6Bh, 71h, 69h, 6Dh, 41h, 56h, 44h, 79h, 69h, 63h
.rodata:0000000000083D60                                         ; DATA XREF: .data:__pyx_string_tab↓o
.rodata:0000000000083D60                 db 6Fh, 77h, 5Dh, 60h, 63h, 70h, 77h, 5Dh, 71h, 63h, 68h
.rodata:0000000000083D60                 db 63h, 5Dh, 6Fh, 67h, 6Fh, 72h, 67h, 6Eh, 63h, 68h, 63h
.rodata:0000000000083D60                 db 70h, 6Bh, 5Dh, 6Bh, 6Ch, 71h, 72h, 67h, 61h, 76h, 5Dh
.rodata:0000000000083D60                 db 66h, 63h, 6Ch, 5Dh, 72h, 6Dh, 6Eh, 7Bh, 6Fh, 6Dh, 70h
.rodata:0000000000083D60                 db 72h, 6Ah, 6Bh, 71h, 6Fh, 7Fh, 0
```
Saya ikuti XREF dari variable tersebut sampai saya menemukan fungsi
```
__pyx_pw_4wise_2001zfdsluoo(_object *,_object *)	.text	000000000004E420	00000ACC	00000078	00000000	R	.	.	S	.	T	.
```
Fungsi yang kita harus pecahkan yaitu
```
wise.zfdsluoo
```
Setelah kita <b>Inspect Document</b> ini yang didapatkan
```
code(argcount, posonlyargcount, kwonlyargcount, nlocals, stacksize,
      flags, codestring, constants, names, varnames, filename, name,
      firstlineno, lnotab[, freevars[, cellvars]])

Create a code object.  Not for the faint of heart.
```
Kita tahu bahwasannya Fungsi tersebut adalah class yg harus kita panggil, jdi ini code nya agar mendapatkan flag!
```python
from wise import zfdsluoo
a = zfdsluoo()
```
Flag : <b>DiskoCTF{kamu_baru_saja_mempelajari_inspect_dan_polymorphism}</b>
