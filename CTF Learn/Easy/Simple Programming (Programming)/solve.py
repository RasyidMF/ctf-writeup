c = 0
f = open('data.dat', 'r')

for x in f.readlines():
    nol  = x.count("0")
    satu = x.count("1")

    if (nol % 3 == 0) or (satu % 2 == 0):
        c = c + 1

f.close()

print("Jawaban : " + str(c))