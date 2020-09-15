flag = [
    106 , 85, 53, 116, 95, 52, 95, 98,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    98, 89, 116, 51 , 115, 95, 55 , 97,
    '1' , 'c' , '8' , 'c' , '6' , '6' , '8' , 'b' ,
]
r = ""
for x in flag:
    t = type(x)
    if t == int:
        r += chr(x)
    elif t == str:
        r += x

print ("picoCTF{" + r + "}")