import pandas

f = pandas.read_csv("the_data_scientist.csv")
res = []

for x in f:
    t = 0
    for s in f[x]:
        t = t + s
    res.append(int(t // 255)) # 255 Column

print(res)