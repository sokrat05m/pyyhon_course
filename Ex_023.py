def narcissistic(value):
    count = 0
    copy_value = value
    digit_list = []
    while value > 0:
        digit = value % 10
        digit_list.append(digit)
        value //= 10
        count += 1
    digit_list = list(map(lambda x: x ** count, digit_list))
    l_sum = 0
    for i in digit_list:
        l_sum += i
    if l_sum == copy_value:
        return True
    return False  # Code away

p = narcissistic(153)
print(p)
