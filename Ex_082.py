def find_outlier(integers):
    count_odd = 0
    count_even = 0
    i = 0
    while i < 3:
        if integers[i] % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        i += 1
    if count_even < count_odd:
        res = [x for x in integers if x % 2 == 0]
    else:
        res = [x for x in integers if x % 2 == 1]
    return res[0]


print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))