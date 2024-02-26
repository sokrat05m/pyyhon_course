def duplicate_count(text):
    text = text.lower()
    dict_1 = {}
    count = 0
    for i in text:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    for i in dict_1.values():
        if i > 1:
            count += 1
    return count


print(duplicate_count('Indivisibilities'))



