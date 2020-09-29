# Image Magic (70 Points)
It looks like someone messed up my picture! Can anyone reorganize the pixels? The python module PIL (Python Imaging Library) might be useful! https://mega.nz/#!OKxByZyT!vaabCJRG5D9zAUp7drTekcA5pszu67r_TbQMtxEzqGE
<br>
Update: I think whoever messed up my image took every column of pixels and put them side by side. Update: I think the width of the image was 304 before they messed with it.
# Solved
```python
from PIL import Image

img 	= Image.open("out copy.jpg")
pixel	= img.load()

flag	= Image.new("RGB", (304, 92), "white")
pixel_f = flag.load()

column = 0

for x in range(flag.size[0]):
	for i in range(flag.size[1]):
		pixel_f[x, i] = pixel[column, 0]
		column = column + 1

flag.save("flag.jpg")
```
Flag : <b>flag{cool_right?}</b>
