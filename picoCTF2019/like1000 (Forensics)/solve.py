import os

for x in range(1000, 0, -1):
    os.system("tar xf " + str(x) + ".tar")
    f = open("filler.txt", "r")
    if x == 1000:
        DoNothing = None
    else:
        os.system("rm " + str(x) + ".tar")