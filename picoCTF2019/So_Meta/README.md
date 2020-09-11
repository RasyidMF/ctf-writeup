# So Meta - Points: 150
<b>Description : </b>Find the flag in this picture. You can also find the file in /problems/so-meta_3_6dc950904c3ee41f324ae8d9f142f2b8.<br>
<b>Hints : </b>What does meta mean in the context of files? Ever hear of metadata?
# Solved
using command
```
strings pico_img.png | grep "picoCTF"
```
Flag : <b>picoCTF{s0_m3ta_43f253bb}</b>
