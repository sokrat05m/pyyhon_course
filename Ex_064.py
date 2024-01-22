x = -120
if x < 0:
    x = -x
    y = 0
    while x > 0:
        y = x % 10 + y * 10
        x //= 10
    print(-y)
y = 0
while x > 0:
    y = x % 10 + y * 10
    x //= 10
print(y)


a = 1534236469
b = 2 ** 31 - 1
print(b)