# So many 64s (80 Points)
Help! My friend stole my flashdrive that had the flag on it. When he gave it back the flag was changed! Can you help me decrypt it? https://mega.nz/#!OHhUyIqA!H9WxSdG1O7eVcCm0dffggNB0-dBemSpBAXiZ0OXJnLk
# Solved
```python
import base64

f = open("flag.txt", "r")
h = f.read()

while True:
	h = base64.b64decode(h).decode("utf-8")
	if '{' in h:
		print(h)
		break

```
```
ABCTF{pr3tty_b4s1c_r1ght?}
```
Flag : <b>ABCTF{pr3tty_b4s1c_r1ght?}</b>