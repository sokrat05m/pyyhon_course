def digital_root(number):
    res = 0
    while number > 0:
        res += number % 10
        number //= 10
    if res < 10:
        return res
    else:
        return digital_root(res)


print(digital_root(493193))