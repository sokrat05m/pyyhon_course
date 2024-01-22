lst = [1, 0, 1, 2, 0, 1, 3]
res = []
for i in lst:
    if i != 0:
        res.append(i)
for i in lst:
    if i == 0:
        res.append(i)
print(res)