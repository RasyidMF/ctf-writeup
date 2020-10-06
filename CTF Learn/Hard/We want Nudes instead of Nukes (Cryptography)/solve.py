# {391e95a15847cfd95ecee8f7fe7efd66,8473dcb86bc12c6b6087619c00b6657e}
IV = bytearray.fromhex("391e95a15847cfd95ecee8f7fe7efd66")
C  = bytearray.fromhex("8473dcb86bc12c6b6087619c00b6657e")

# FIRE_NUKES_MELA!
MESSAGE = bytearray.fromhex("464952455f4e554b45535f4d454c4121")

# SEND_NUDES_MELA!
MELANIA = bytearray.fromhex("53454e445f4e554445535f4d454c4121")

RES = bytearray()

for x in range(16): # Length of Message
    RES.append(IV[x] ^ MESSAGE[x] ^ MELANIA[x])

print(RES.hex())