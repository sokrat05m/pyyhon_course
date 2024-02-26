numbers = [2, 3, 4]
target = 6
d = {}
for i, j in enumerate(numbers):
    if target - j in d:
        print(d[target - j] + 1, i + 1)
    d[j] = i