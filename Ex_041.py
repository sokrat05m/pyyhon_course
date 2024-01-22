def last_digit(n1, n2):
    square = n1 ** n2
    if square < 10:
        num = n1
    else:
        num = square % 10
    return num


a = last_digit(9, 7)
print(a)
