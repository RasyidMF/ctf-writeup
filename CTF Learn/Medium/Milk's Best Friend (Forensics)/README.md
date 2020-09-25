# Milk's Best Friend (40 Points)
There's nothing I love more than oreos, lions, and winning. https://mega.nz/#!DC5F2KgR!P8UotyST_6n2iW5BS1yYnum8KnU0-2Amw2nq3UoMq0Y Have Fun :)
# Solved
Setelah saya analisi terdapat file .RAR pada file tersebut
```
$ binwalk oreo.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.01
9515          0x252B          RAR archive data, version 4.x, first volume type: MAIN_HEAD
```
```
$ unrar e 252B.rar

UNRAR 5.61 beta 1 freeware      Copyright (c) 1993-2018 Alexander Roshal


Extracting from 252B.rar


Would you like to replace the existing file b.jpg
  6712 bytes, modified on 2017-02-24 21:03
with a new one
  6712 bytes, modified on 2017-02-24 21:03

[Y]es, [N]o, [A]ll, n[E]ver, [R]ename, [Q]uit a

Extracting  b.jpg                                                     OK
Extracting  a                                                         OK
All OK
```
```
$ strings b.jpg
Finally, flag{eat_more_oreos}
```
Flag : <b>flag{eat_more_oreos}</b>