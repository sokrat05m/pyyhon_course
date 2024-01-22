def first_non_repeating_letter(s):
    list_1 = list(s.lower())
    list_res = []
    i = 0
    while i < len(list_1):
        if list_1.count(list_1[i]) == 1:
            list_res.append(list_1[i])
        i += 1
    if len(s) == 0:
        return ''
    if len(list_res) == 0:
        return ''
    elif list_res[0] in s:
        return list_res[0]
    else:
        list_res[0] = list_res[0].upper()
        return list_res[0]


name = first_non_repeating_letter('aaaa')
print(name)



