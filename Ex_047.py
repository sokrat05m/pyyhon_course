def move_zeros(lst):
    i = 0
    count = 1
    while i < len(lst):
        if lst[i] == 0:
            lst.pop(i)
            count += 1
            i = max(0, i - 1)
        else:
            i += 1
    for i in range(count):
        lst.append(0)
    return lst
