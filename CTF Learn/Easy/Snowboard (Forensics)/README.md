# Snowboard (20 Points)
Find the flag in the jpeg file. Good Luck!
# Solved
Gunakan perintah <code>strings Snowboard.jpg</code>, Disini ada 1 fake flag yaitu
```
CTFlearn{CTFIsEasy!!!}
```
Flag yang sebenarnya terencode base64
```
$ echo 'Q1RGbGVhcm57U2tpQmFuZmZ9Cg==' | base64 -d
CTFlearn{SkiBanff}
```
Flag : <b>CTFlearn{SkiBanff}</b>
