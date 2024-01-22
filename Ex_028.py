def latest_clock(a, b, c, d):
    list_1 = [a, b, c, d]
    list_res = []
    count = 0
    for i in list_1:
        if i > 5:
            count += 1
    if count >= 2:
        list_res.append(max(filter(lambda x: x <= 1, list_1)))
    else:
        list_res.append(max(filter(lambda x: x <= 2, list_1)))
    list_1.remove(list_res[0])
    if list_res[0] == 0 or list_res[0] == 1:
        list_res.append(max(list_1))
        list_1.remove(list_res[1])
    else:
        list_res.append(max(filter(lambda x: x <= 3, list_1)))
        list_1.remove(list_res[1])
    list_res.append(max(filter(lambda x: x <= 5, list_1)))
    list_1.remove(list_res[2])
    list_res.append(list_1[0])
    list_res = list(map(lambda x: str(x), list_res))
    result = ''
    for i in range(2):
        result += list_res [i]
    result += ':'
    for i in range(2, 4):
        result += list_res[i]
    return result


result = latest_clock(1, 2, 8, 9)
print(result)
