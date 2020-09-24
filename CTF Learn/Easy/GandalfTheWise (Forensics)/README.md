# GandalfTheWise (30 Points)
Extract the flag from the Gandalf.jpg file. You may need to write a quick script to solve this.
# Solved
Gunakan perintah <code>strings Gandalf.jpg</code>, kemudian diberikan 3 Base64 encoded
```
+Q1RGbGVhcm57eG9yX2lzX3lvdXJfZnJpZW5kfQo=
+xD6kfO2UrE5SnLQ6WgESK4kvD/Y/rDJPXNU45k/p
+h2riEIj13iAp29VUPmB+TadtZppdw3AuO7JRiDyU
```
https://cryptii.com/pipes/text-to-base64
```
CTFlearn{xor_is_your_friend}
c4 3e a4 7c ed 94 ac 4e 52 9c b4 3a 5a 01 12 2b 89 2f 0f f6 3f ac 32 4f 5c d5 38 e6 4f e9
87 6a e2 10 88 f5 de 20 29 db d5 54 3e 60 7e 4d a7 6d 66 9a 5d c3 70 2e 3b b2 51 88 3c 94
```
<b>CTFlearn{xor_is_your_friend}</b> adalah fake flag akan tetapi itu adalah sebuah hint yang mengatakan <b>XOR_IS_YOUR_FRIEND</b>, Disini kita harus pahami bahwa kita di berikan 2 Base64 untuk di decrypt menggunakan XOR Algorithm, saya menggunakan XOR Calculator online 
http://xor.pw/
```
4354466c6561726e7b47616e64616c662e42696c626f42616767696e737d
```
http://string-functions.com/hex-string.aspx<br>
Flag : <b>CTFlearn{Gandalf.BilboBaggins}</b>
