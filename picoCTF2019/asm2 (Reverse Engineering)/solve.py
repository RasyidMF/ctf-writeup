
f1 = 0x9
f2 = 0x1e

# Stack
#   ebp+0x4     = ret
#   ebp+0x8     = 0x9
#   ebp+0xc     = 0x1e
#
#   ebp-0x4     = 0x1e
#   ebp-0x8     = 0x9
#

# mov eax,DWORD PTR [ebp+0xc]
eax1 = f2 # mov DWORD PTR [ebp-0x4],eax

# mov eax,DWORD PTR [ebp+0x8]
eax2 = f1 # mov DWORD PTR [ebp-0x8],eax

while True:
    if eax2 > 0x47a6:
        print("EAX-0x8: " + str(hex(eax2) + " | " + str(eax2)))
        print("EAX-0x4: " + str(hex(eax1) + " | " + str(eax1)))
        break
    else:
        eax1 = eax1 + 1
        eax2 = eax2 + 0xa9
