f = open("TheMessage.txt", "r").read()
res = ""

# uniq = []
# for x in f:
#     if not ord(x) in uniq:
#         uniq.append(ord(x))

# print(uniq)

for x in f:
    if len(res) % 9 == 0:
        res += " "
    if ord(x) == 32:
        res += "0"
    else:
        res += "1"

print(res)
