# PyDis (40 Points)
You like python don't you, but do you like dis type of python.
<br>
This will be helpful: https://docs.python.org/3/library/dis.html
# Solved
Disini kita diberikan sebuah instruksi
```asm
Disassembly of func2:
  2           0 LOAD_FAST                1 (c2)
              2 STORE_FAST               2 (tmp1)

  3           4 LOAD_FAST                0 (c1)
              6 STORE_FAST               3 (tmp2)

  4           8 LOAD_FAST                2 (tmp1)
             10 LOAD_FAST                3 (tmp2)
             12 BINARY_XOR
             14 RETURN_VALUE

Disassembly of func:
  7           0 LOAD_GLOBAL              0 (open)
              2 LOAD_CONST               1 ('flag.txt')
              4 CALL_FUNCTION            1
              6 LOAD_METHOD              1 (read)
              8 CALL_METHOD              0
             10 STORE_FAST               0 (fp)

  8          12 LOAD_CONST               2 ('')
             14 STORE_FAST               1 (cipher)

  9          16 LOAD_GLOBAL              2 (range)
             18 LOAD_GLOBAL              3 (len)
             20 LOAD_FAST                0 (fp)
             22 CALL_FUNCTION            1
             24 CALL_FUNCTION            1
             26 GET_ITER
        >>   28 FOR_ITER                40 (to 70)
             30 STORE_FAST               2 (i)

  10         32 LOAD_GLOBAL              4 (func2)
             34 LOAD_GLOBAL              5 (ord)
             36 LOAD_FAST                0 (fp)
             38 LOAD_FAST                2 (i)
             40 BINARY_SUBSCR
             42 CALL_FUNCTION            1
             44 LOAD_CONST               3 (170)
             46 CALL_FUNCTION            2
             48 STORE_FAST               3 (temp)

  11         50 LOAD_FAST                1 (cipher)
             52 LOAD_GLOBAL              6 (chr)
             54 LOAD_GLOBAL              4 (func2)
             56 LOAD_FAST                3 (temp)
             58 LOAD_FAST                2 (i)
             60 CALL_FUNCTION            2
             62 CALL_FUNCTION            1
             64 INPLACE_ADD
             66 STORE_FAST               1 (cipher)
             68 JUMP_ABSOLUTE           28

  12    >>   70 LOAD_GLOBAL              7 (print)
             72 LOAD_FAST                1 (cipher)
             74 CALL_FUNCTION            1
             76 POP_TOP

  13         78 LOAD_GLOBAL              0 (open)
             80 LOAD_CONST               4 ('encrypted_flag.txt')
             82 LOAD_CONST               5 ('w')
             84 CALL_FUNCTION            2
             86 SETUP_WITH              16 (to 104)
             88 STORE_FAST               4 (f)

  14         90 LOAD_FAST                4 (f)
             92 LOAD_METHOD              8 (write)
             94 LOAD_FAST                1 (cipher)
             96 CALL_METHOD              1
             98 POP_TOP
            100 POP_BLOCK
            102 BEGIN_FINALLY
        >>  104 WITH_CLEANUP_START
            106 WITH_CLEANUP_FINISH
            108 END_FINALLY
            110 LOAD_CONST               0 (None)
            112 RETURN_VALUE


# output = FLAG
```
Sebelumnya saya tidak paham dengan instruksi dari <b>Python Byte-code</b> tersebut. Kemudian saya memakai <b>dis</b> untuk mencari tahu. Disini saya melihat instruksi dari fungsi <b>func2</b>
```asm
Disassembly of func2:
  2           0 LOAD_FAST                1 (c2)
              2 STORE_FAST               2 (tmp1)

  3           4 LOAD_FAST                0 (c1)
              6 STORE_FAST               3 (tmp2)

  4           8 LOAD_FAST                2 (tmp1)
             10 LOAD_FAST                3 (tmp2)
             12 BINARY_XOR
             14 RETURN_VALUE
```
Melakukan <b>XOR Encrypt</b> pada sebuah teks dan diberikan jumlah angka <b>170</b>. Kemudian saya membuat demonstrasi pada kode tersebut
```python
# Demonstration
import dis

class Demons:
    def func2(c1, c2):
        tmp1 = c2
        tmp2 = c1

        return tmp1 ^ tmp2
    def func():
        fp = open("flag.txt").read()
        cipher = ''
        for i in range(len(fp)):
            temp = func2(ord(fp[i]), 170)
            cipher += chr(func2(temp, i))
        print(cipher)

dis.dis(Demons)
# End
```
<b>Pastikan menggunakan Python3 </b> untuk melakukan hal ini, saat saya mencoba pada python2 tidak berhasil!.
```console
$ python3 solve.py
Disassembly of func:
 11           0 LOAD_GLOBAL              0 (open)
              2 LOAD_CONST               1 ('flag.txt')
              4 CALL_FUNCTION            1
              6 LOAD_METHOD              1 (read)
              8 CALL_METHOD              0
             10 STORE_FAST               0 (fp)

 12          12 LOAD_CONST               2 ('')
             14 STORE_FAST               1 (cipher)

 13          16 LOAD_GLOBAL              2 (range)
             18 LOAD_GLOBAL              3 (len)
             20 LOAD_FAST                0 (fp)
             22 CALL_FUNCTION            1
             24 CALL_FUNCTION            1
             26 GET_ITER
        >>   28 FOR_ITER                40 (to 70)
             30 STORE_FAST               2 (i)

 14          32 LOAD_GLOBAL              4 (func2)
             34 LOAD_GLOBAL              5 (ord)
             36 LOAD_FAST                0 (fp)
             38 LOAD_FAST                2 (i)
             40 BINARY_SUBSCR
             42 CALL_FUNCTION            1
             44 LOAD_CONST               3 (170)
             46 CALL_FUNCTION            2
             48 STORE_FAST               3 (temp)

 15          50 LOAD_FAST                1 (cipher)
             52 LOAD_GLOBAL              6 (chr)
             54 LOAD_GLOBAL              4 (func2)
             56 LOAD_FAST                3 (temp)
             58 LOAD_FAST                2 (i)
             60 CALL_FUNCTION            2
             62 CALL_FUNCTION            1
             64 INPLACE_ADD
             66 STORE_FAST               1 (cipher)
             68 JUMP_ABSOLUTE           28

 16     >>   70 LOAD_GLOBAL              7 (print)
             72 LOAD_FAST                1 (cipher)
             74 CALL_FUNCTION            1
             76 POP_TOP
             78 LOAD_CONST               0 (None)
             80 RETURN_VALUE

Disassembly of func2:
  6           0 LOAD_FAST                1 (c2)
              2 STORE_FAST               2 (tmp1)

  7           4 LOAD_FAST                0 (c1)
              6 STORE_FAST               3 (tmp2)

  9           8 LOAD_FAST                2 (tmp1)
             10 LOAD_FAST                3 (tmp2)
             12 BINARY_XOR
             14 RETURN_VALUE
```
Kemudian saya panggil fungsi <b>func()</b>
```python
def func2(c1, c2):
    tmp1 = c2
    tmp2 = c1

    return tmp1 ^ tmp2
def func():
    fp = open("flag.txt").read()
    cipher = ''
    for i in range(len(fp)):
        temp = func2(ord(fp[i]), 170)
        cipher += chr(func2(temp, i))
    print(cipher)

func()
```
```console
$ python3 solve.py
CTFlearn{Python_Reversing_Is_Pretty_Easy}
```
Flag : <b>CTFlearn{Python_Reversing_Is_Pretty_Easy}</b>