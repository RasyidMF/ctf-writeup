f = open("whitepages.txt", "r")
r = f.read()

flag = []
bin1 = ' '
bin2 = ' '

for x in r:
        if x == bin1:
                flag.append('0')
        else:
                flag.append('1')

print (''.join(flag))