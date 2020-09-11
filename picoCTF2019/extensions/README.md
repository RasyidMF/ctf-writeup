# extensions - Points: 150
<b>Description : </b>This is a really weird text file TXT? Can you find the flag?<br>
<b>Hints : </b>How do operating systems know what kind of file it is? (It's not just the ending!). Make sure to submit the flag as picoCTF{XXXXX}
# Solved
To check file extension im using <b>file</b> command
```
file flag.txt
Result => flag.txt: PNG image data, 1697 x 608, 8-bit/color RGB, non-interlaced
```
Don't tricky by filename!
```
cp flag.txt flag.png
```
Open image flag.png and got the flag!<br>
Flag : <b>picoCTF{now_you_know_about_extensions}</b>
