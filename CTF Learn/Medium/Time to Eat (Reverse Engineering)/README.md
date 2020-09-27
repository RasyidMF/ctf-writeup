# Time to Eat (50 Points)
My friend sent me some Python code, but something tells me he was hungry when he wrote it. Do you think you can put your reverse engineering skills to use and get it to output the flag?
# Solved
Saya selesai menggunakan debugger pada python, kemudian memahami 1 per 1 dari hasil enkripsi tersebut. Dan inilah history saya
```python
# I wrote and debugged this code with all the convoluted "EAT" variable names.
# Was it confusing? Yes. Was debugging hard? Yes.
# Did I spend more time than I should have on this problem? Yes

EAT = int
eAT = len
EaT = print
ATE = str
AteDigits = ATE.isdigit

def Eating(a1):
    return str(int(a1) * lenInput)

def EAt(eat, eats):
    print(eat, eats)
    eat1 = 0
    eat2 = 0
    eateat = 0
    eAt = ""
    while eat1 < len(eat) and eat2 < len(eats):
        if eateat % lenInput == lenInputMinusOne // lenInputPlusOne:
            eAt += eats[eat2]
            eat2 += 1
        else:
            eAt += eat[eat1]
            eat1 += 1
        eateat += 1
    print("eAt: " + eAt)
    return eAt

def aten(eat):
    # Reverse string
    # 123abc456 => 654cba321
    print ("aten: " + eat[::lenInput-lenInputPlusOne])
    return eat[::lenInput-lenInputPlusOne]

def eaT(eat):
    return Eating(eat[:lenInput]) + aten(eat)

def aTE(eat):
    return eat#*eAT(eat)

def Ate(eat):
    print ("Ate: " + "Eat" + ATE(eAT(eat)) + eat[:lenInput])

    # Len of eat + lenInput
    return "Eat" + str(len(eat)) + eat[:lenInput]

def Eat(eat):
    if len(eat) == 9:
        if AteDigits(eat[:lenInput]) and \
            AteDigits(eat[len(eat) - lenInput + 1:]):
                eateat = EAt(eaT(eat), Ate(aTE(aten(eat))))
                if eateat == "E10a23t9090t9ae0140":
                    flag = "eaten_" + eat
                    print("absolutely EATEN!!! CTFlearn{",flag,"}")
                else:
                    print("thats not the answer. you formatted it fine tho, here's what you got\n>>", eateat)
                    print("Target: E10a23t9090t9ae0140 | ", eateat)
        else:
            print("thats not the answer. bad format :(\
            \n(hint: 123abc456 is an example of good format)")
    else:
        print("thats not the answer. bad length :(")

EaT("what's the answer")
eat = input()
lenInput = len(eat) // 3
lenInputPlusOne = lenInput + 1
lenInputMinusOne = lenInput - 1
Eat(eat)

# Answer
# |E102|3t90|9| 0t |9| ae |01| 40
# |E36a9| 6 |t| 54 |9| cb |6| a3 |5| 21

# 123abc456

# 041eat900
# 441eat009
# 341eat009 => True
```
Flag : <b>CTFlearn{eaten_341eat009}</b>
