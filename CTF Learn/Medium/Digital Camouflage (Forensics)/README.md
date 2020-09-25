# Digital Camouflage (40 Points)
We need to gain access to some routers. Let's try and see if we can find the password in the captured network data: https://mega.nz/#!XDBDRAQD!4jRcJvAhMkaVaZCOT3z3zkyHre2KHfmkbCN5lYpiEoY Hint 1: It looks like someone logged in with their password earlier. Where would log in data be located in a network capture?<br /> Hint 2: If you think you found the flag, but it doesn't work, consider that the data may be encrypted.
# Solved
Untuk menyelesaikan challenge ini saya menggunakan <b>Wireshark</b>. Disaat saya scrolling-scrolling, saya menemukan request
```
105	123.059179	10.0.0.5	10.0.0.1	HTTP	109	POST /pages/main.html HTTP/1.1  (application/x-www-form-urlencoded)
```
Saya menemukan
```
Form item: "userid" = "hardawayn"
Form item: "pswrd" = "UEFwZHNqUlRhZQ=="
```
```
$ echo 'UEFwZHNqUlRhZQ==' | base64 -d
PApdsjRTae
```
Flag : <b>PApdsjRTae</b>