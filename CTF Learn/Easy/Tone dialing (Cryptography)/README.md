# Tone dialing (30 Points)
At 1pm I called my uncle who was 64 years old 10 months ago, but I heard only that. Later I started thinking about the 24 hour clock.
<br>
I hope you will help me solve this problem
# Solved
Dengan menggunakan website ini http://dialabc.com/sound/detect/index.html, dan saya parse menjadi
```python
tone = [67, 84, 70, 108, 101, 97, 110, 123, 67, 82, 89, 80, 84, 79, 71, 82, 65, 80, 72, 89, 125]
res = ""

for x in tone:
    res += chr(x)
print res
```
```console
$ python solve.py
CTFlean{CRYPTOGRAPHY}
```
Flag : <b>CTFlean{CRYPTOGRAPHY}</b>