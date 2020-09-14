# whats-the-difference - Points: 200
<b>Description : </b>Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server<br>
<b>Hints : </b>How do you find the difference between two files? Dumping the data from a hex editor may make it easier to compare.
# Solved
Im using command <b>diff</b> to solve this challenge
```
cmp -bl kitters.jpg cattos.jpg | awk '{print $5}' | tr -d "\n"
```
Flag : <b>picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j311y_aslkjfdsalkfslkflkjdsfdszmz10548}</b>
