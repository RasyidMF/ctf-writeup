# Simple Steganography (30 Points)
Think the flag is somewhere in there. Would you help me find it? hint-" Steghide Might be Helpfull"
# Solved
Disini kita diharuskan untuk mengekstrak file tersebut menggunakan <b>Steghide</b> akan tetapi di butuhkan password!
```console
$ strings Minions1.jpeg
myadmin
```
Passwordnya adalah <b>myadmin</b>, kemudian jalankan perintah
```console
$ steghide extract -sf Minions1.jpeg
Enter passphrase:
wrote extracted data to "raw.txt".
```
```console
$ cat raw.txt
AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9
```
```console
$ echo 'AEMAVABGAGwAZQBhAHIAbgB7AHQAaABpAHMAXwBpAHMAXwBmAHUAbgB9' | base64 -d
C T F l e a r n { t h i s _ i s _ f u n }
```
Flag : <b>CTFlearn{this_is_fun}</b>
