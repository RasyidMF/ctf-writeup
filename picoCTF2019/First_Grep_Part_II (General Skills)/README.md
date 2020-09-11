# First Grep: Part II - Points: 200
<b>Description : </b>Can you find the flag in /problems/first-grep--part-ii_3_b4bf3244c2886de1566a28c1b5a465ae/files on the shell server? Remember to use grep.<br>
<b>Hints : </b>grep tutorial https://ryanstutorials.net/linuxtutorial/grep.php
# Solved
When i using <b>dir</b> command there is alot file.
```
files0  files1  files10  files2  files3  files4  files5  files6  files7  files8  files9
```
Of course I don't want to take it 1 by 1, it would take a lot of time to do that. So i decided using this command
```
grep -rni "picoCTF{"
```
and got the flag!<br>
Flag : <b>picoCTF{grep_r_to_find_this_3675d798}</b>
