# Ngelag (50 Points)
Tower instansi dibikin ngelag nih gara-gara jammer om Apud, jangan lupa import main ya.
# Solved
Saya menggunakan IDA Pro untuk menganalisis file binary tersebut! akan tetapi tidak menemukan hints sama sekali :(. Sebelumnya saya belum mengimport file tersebut, dan setelah saya import saya menemukan pesan ini
```
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'flag', 'sleep', 'sys']
```
Saya coba panggil fungsi
```python
main.flag()
```
Saya mendapatkan pesan
```
Here's Your Flag!
DiskoCTF{
```
Akan tetapi ngestuck di situ-situ aja :(. Sebelumnya saya menyelesaikan challenge yg dimana saya harus mencari tahu document dari fungsi tersebut, maka dari itu saya coba cek 1 per 1 dari 3 fungsi yg ada <b>flag,sleep,sys</b>
```
flag() # Kosong
```
```
sleep(...)
    sleep(seconds)

    Delay execution for a given number of seconds.  The argument may be
    a floating point number for subsecond precision.
```
```
NAME
    sys

MODULE REFERENCE
    https://docs.python.org/3.8/library/sys

    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.
```
Disini saya curiga mengenai <b>sleep</b>. Saya baca ulang challenge nya tadi bahwa ada kata-kata <b>Ngelag</b> :3 well sesuai dengan nama challengenya. Nah dri sini kita mendapatkan akses untuk mengubah script dari <b>sleep(argument)</b>. Ini code nya yg saya coba
```python
def p(x):
    print(x)
main.sleep = p
```
Setelah saya eksekusi saya mendapatkan pesan ini
```
Here's Your Flag!
0.8
D0.8
i0.8
s0.8
k0.8
o0.8
C0.8
T0.8
F0.8
{100000
n0.8
i0.8
c0.8
e0.8
_0.8
o0.8
v0.8
e0.8
r0.8
r0.8
i0.8
d0.8
i0.8
n0.8
g0.8
}
```
<b>Jackpot</b>, sekarang saya parse dari argument tersebut menjadi 1
```python
def p(x):
	global flag
	flag += str(x).replace("0.8", "")

main.sleep = p
```
Anddd Boom! Dapat flag :D<br>
Flag : <b>DiskoCTF{nice_overriding}</b>