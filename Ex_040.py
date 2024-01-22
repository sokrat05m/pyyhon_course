def diamond(n):
    if n % 2 == 0:
        return None

    s = '*' * n
    i = 1
    while n > 0:
        s = ' ' * i + '*' * (n - 2) + '\n' + s + '\n' + ' ' * i + '*' * (n - 2)
        n -= 2
        i += 1
    return s

a = diamond(7)
print(a)

