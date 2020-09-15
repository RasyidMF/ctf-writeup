# like1000 - Points: 250
<b>Description : </b>This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.<br>
<b>Hints : </b>Try and script this, it'll save you alot of time
# Solved
Solved using python script
```python
import os

for x in range(1000, 0, -1):
    os.system("tar xf " + str(x) + ".tar")
    f = open("filler.txt", "r")
    if x == 1000:
        DoNothing = None
    else:
        os.system("rm " + str(x) + ".tar")
```
Open the flag.png and read it!<br>
Flag : <b>picoCTF{l0t5_0f_TAR5}</b>
