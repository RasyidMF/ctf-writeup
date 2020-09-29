import base64
import os

key  = "b18ef1351fc0df641abbe56dcd4928a8bb98452b1b43d8c1c13f1874c8b35056" # SHA256 of CTFlearn 
hint = "TZm1GWpQfUB+7cM2BIng5MCeEgBqxIKunpThaVKemNBmvbis9H0rTAOSIYXsu8vaCK6Z67gNHOQYBPUNl1mY6jWVLfq+5FmUtaW/lnYT71rBlmPcBLymDGFj2BJjZWY4A3aM2Mp0AGDPrK3X4eMu8Q=="

f = open("hint.enc", "wb")
f.write(base64.b64decode(hint))
f.close()

iv = 00000000000000000000000000000000 # Since there is none hint for IV, let it set as 0 * 32
os.system("openssl enc -d -aes-256-cbc -iv " + str(iv) + " -K " + str(key) + " -in hint.enc -out hint.txt -nopad")

