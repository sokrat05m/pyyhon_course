def sum_while(a, b):
    if a == 1 and b == 1:
        return a + b
    if a > 1 and b == 1:
        return 1 + sum_while(a - 1, b)
    if a == 1 and b > 1:
        return 1 + sum_while(a, b - 1)
    return 1 + 1 + sum_while(a - 1, b - 1)


print(sum_while(6, 7))
