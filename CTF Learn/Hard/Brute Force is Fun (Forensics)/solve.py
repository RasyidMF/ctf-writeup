from zipfile import ZipFile
import itertools
import string

digit = itertools.product(string.digits, repeat=5)

f = ZipFile("./output/zip/00000012.zip")

for x in digit:
    x = ''.join(x)
    res = "ctflag" + x
    # print(res)
    try:
        f.extractall(pwd=bytes(res, 'utf-8'))
        print ("Flag Founded: " + res)
        exit(0)
    except:
        pass