#!/usr/bin/python -u
import random,string

# flag = "FLAG:"+open("flag", "r").read()[:-1]
flag = "JKRR{iz6h_b8ir1b_k5lb}"
enkripflag = ""
random.seed("random")
for c in flag:
  if c.islower():
    enkripflag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
  elif c.isupper():
    enkripflag += chr((ord(c)-ord('A')-random.randrange(0,25))%25 + ord('A'))
  elif c.isdigit():
    enkripflag += chr((ord(c)-ord('0')-random.randrange(0,15))%15 + ord('0'))
  else:
    enkripflag += c
print "Flag yang telah terenkrip : " + enkripflag

# Flag : Tukk Akhwt eunfze, ptw napuug gttj yucl : JKRR{iz6h_b8ir1b_k5lb}
