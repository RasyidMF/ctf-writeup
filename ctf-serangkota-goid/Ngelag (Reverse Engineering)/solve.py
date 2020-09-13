import main
import inspect
flag = ""
def p(x):
	global flag
	flag += str(x).replace("0.8", "")

main.sleep = p
main.flag()
print("DiskoCTF{" + flag + "}")