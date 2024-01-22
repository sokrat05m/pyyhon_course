arr = [1, 1, 1, 2, 1, 1]
a = max(set(arr), key=arr.count)
for i in arr:
    if i != a:
        print(i)








