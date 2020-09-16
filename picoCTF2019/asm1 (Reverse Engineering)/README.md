# asm1 - Points: 200
<b>Description : </b>What does asm1(0x4f3) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm1_6_74dd61bdf487805bf057c71be7941289.<br>
<b>Hints : </b>assembly conditions (https://www.tutorialspoint.com/assembly_programming/assembly_conditions.htm)
# Solved
Lets read instruction here
```asm
<+0>:   push   ebp
<+1>:   mov    ebp,esp
<+3>:   cmp    DWORD PTR [ebp+0x8],0x45d
<+10>:  jg     0x512 <asm1+37>
<+12>:  cmp    DWORD PTR [ebp+0x8],0x430
<+19>:  jne    0x50a <asm1+29>
<+21>:  mov    eax,DWORD PTR [ebp+0x8]
<+24>:  add    eax,0x17
<+27>:  jmp    0x529 <asm1+60>
<+29>:  mov    eax,DWORD PTR [ebp+0x8]
<+32>:  sub    eax,0x17
<+35>:  jmp    0x529 <asm1+60>
<+37>:  cmp    DWORD PTR [ebp+0x8],0x7cd
<+44>:  jne    0x523 <asm1+54>
<+46>:  mov    eax,DWORD PTR [ebp+0x8]
<+49>:  sub    eax,0x17
<+52>:  jmp    0x529 <asm1+60>
<+54>:  mov    eax,DWORD PTR [ebp+0x8]
<+57>:  add    eax,0x17
<+60>:  pop    ebp
<+61>:  ret
```
Lets take 4 instruction first
```asm
<+0>:   push   ebp
<+1>:   mov    ebp,esp
<+3>:   cmp    DWORD PTR [ebp+0x8],0x45d
<+10>:  jg     0x512 <asm1+37>
```
<li><b>ebp</b> was push into registers.</li>
<li>Next create new variable <b>esp</b> and set value of <b>ebp</b></li>
<li>
    Check <b>ebp+0x8</b> is <b>jg ( <= )</b> than 0x45d,
    if <b>TRUE</b> the instruction will continue, <b>ELSE</b> will jumping into <b><asm1+37></b>
</li>
<b>Note: </b> value of <b>ebp</b> = <b>0x4f3</b>. So i the result of this instruction is <b>FALSE</b><hr>
Next, lets take 2 instruction
```asm
<+37>:  cmp    DWORD PTR [ebp+0x8],0x7cd
<+44>:  jne    0x523 <asm1+54>
```
<li>Check <b>ebp+0x8</b> is <b>jne ( == )</b> is equal with 0x7cd</li>
<b>Note: </b> since value <b>ebp+0x8</b> is <b>0x4f3</b>  The answer is <b>FALSE</b><hr>
Next, i know the instruction was jump into <b><asm1+54></b>
```asm
<+54>:  mov    eax,DWORD PTR [ebp+0x8]
<+57>:  add    eax,0x17
<+60>:  pop    ebp
<+61>:  ret
```
<li><b><+54></b> and <b><+57></b> is adding / incerase value <b>ebp</b> with <b>0x17</b>.</li>
```
0x4f3 + 0x17 = 0x50a
```
Flag : <b>0x50a</b>