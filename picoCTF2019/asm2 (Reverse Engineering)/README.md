# asm2 - Points: 250
<b>Description : </b>What does asm2(0x9,0x1e) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm2_2_5667a5cd5764b4356121f1d6232ac78c.
<b>Hints : </b>assembly conditions (https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
# Solved
This is same at previous challenge, but there is 2 argument which <b>int</b> and <b>int</b>, Lets take a look the instruction
```asm
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]
	<+9>:	mov    DWORD PTR [ebp-0x4],eax
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]
	<+15>:	mov    DWORD PTR [ebp-0x8],eax
	<+18>:	jmp    0x50c <asm2+31>
	<+20>:	add    DWORD PTR [ebp-0x4],0x1
	<+24>:	add    DWORD PTR [ebp-0x8],0xa9
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x47a6
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]
	<+43>:	leave
	<+44>:	ret
```
If you a beginner to solving this, use https://godbolt.org/ for prototype. <br>
Lets take 6 instruction
```asm
    <+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc] ; Create new integer variable / ebp+0xc = 0x1e
	<+9>:	mov    DWORD PTR [ebp-0x4],eax ; Set value of eax into first argument / ebp-0x4 = 0x1e
	<+12>:	mov    eax,DWORD PTR [ebp+0x8] ; Create new integer variable / ebp+0x8 = 0x9
	<+15>:	mov    DWORD PTR [ebp-0x8],eax ; Set value of eax into second argument / ebp-0x8 = 0x9
```
Okay, lets take some more instruction
```asm
    <+18>:	jmp    0x50c <asm2+31>              ; Jump instruction into <asm2+31> (This is a loop instruction)
	<+20>:	add    DWORD PTR [ebp-0x4],0x1      ; Adding [ebp-0x4] += 1
	<+24>:	add    DWORD PTR [ebp-0x8],0xa9     ; Adding [ebp-0x8] += 169 (0xa9)
	<+31>:	cmp    DWORD PTR [ebp-0x8],0x47a6   ; Check if [ebp-0x8] > 0x47a6
	<+38>:	jle    0x501 <asm2+20>
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]      ; If instruction was finish, getting the value of [ebp-0x4] as return
	<+43>:	leave
	<+44>:	ret
```
Solved with python script
```python

f1 = 0x9
f2 = 0x1e

# Stack
#   ebp+0x4     = ret
#   ebp+0x8     = 0x9
#   ebp+0xc     = 0x1e
#
#   ebp-0x4     = 0x1e
#   ebp-0x8     = 0x9
#

# mov eax,DWORD PTR [ebp+0xc]
eax1 = f2 # mov DWORD PTR [ebp-0x4],eax

# mov eax,DWORD PTR [ebp+0x8]
eax2 = f1 # mov DWORD PTR [ebp-0x8],eax

while True:
    if eax2 > 0x47a6:
        print("EAX-0x8: " + str(hex(eax2) + " | " + str(eax2)))
        print("EAX-0x4: " + str(hex(eax1) + " | " + str(eax1)))
        break
    else:
        eax1 = eax1 + 1
        eax2 = eax2 + 0xa9
```
```
EAX-0x8: 0x47fe | 18430
EAX-0x4: 0x8b | 139
```
Flag : <b>0x8b</b>