def duplicate_encode(word):
    word = word.lower()
    dict_1 = {}
    for i in word:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    res = ''
    for i in word:
        if dict_1[i] > 1:
            res += ')'
        else:
            res += '('
    return res


print(duplicate_encode('recede'))