# where-is-the-file - Points: 200
<b>Description : </b>I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_0_cc140a3ba634658b98122a1954c1316a.<br>
<b>Hints : </b>What command can see/read files? What's in the manual page of ls?
# Solved
using command
```
ls -al
```
Result :
```
total 80
drwxr-xr-x   2 root       root        4096 Sep 28  2019 .
drwxr-x--x 684 root       root       69632 Oct 10  2019 ..
-rw-rw-r--   1 hacksports hacksports    39 Sep 28  2019 .cant_see_me
```
Flag : <b>picoCTF{w3ll_that_d1dnt_w0RK_b2dab472}</b>
