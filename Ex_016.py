data = [1, 1, 2, 0, 5, 10]
k = 2
length = len(data)
for i in range (k):
    data.insert(i, data [-k + i])
    data.pop(-k + i)
print(data)

