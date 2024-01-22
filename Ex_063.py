digits = [1, 2, 3]
y = 0
for i in range(len(digits)):
    y = y * 10 + digits[i] % 10
y = y + 1
res = []
while y > 0:
    res.insert(0, y % 10)
    y //= 10
print(res)
