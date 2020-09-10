# dont-use-client-side - Points: 100
<b>Description : </b>Can you break into this super secure portal? https://2019shell1.picoctf.com/problem/49886/ (link) or http://2019shell1.picoctf.com:49886<br>
<b>Hints : </b>Never trust the client
# Solved
<b>CTRL + U</b> in Browser and you will see the
```javascript
function verify() {
    checkpass = document.getElementById("pass").value;
    split = 4;
    if (checkpass.substring(0, split) == 'pico') {
      if (checkpass.substring(split*6, split*7) == 'e2f2') {
        if (checkpass.substring(split, split*2) == 'CTF{') {
         if (checkpass.substring(split*4, split*5) == 'ts_p') {
          if (checkpass.substring(split*3, split*4) == 'lien') {
            if (checkpass.substring(split*5, split*6) == 'lz_e') {
              if (checkpass.substring(split*2, split*3) == 'no_c') {
                if (checkpass.substring(split*7, split*8) == '4}') {
                  alert("Password Verified")
                  }
                }
              }
      
            }
          }
        }
      }
    }
    else {
      alert("Incorrect password");
    }    
}
```
Flag : <b>picoCTF{no_clients_plz_ee2f24}</b>
