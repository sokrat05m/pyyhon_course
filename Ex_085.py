def order(sentence):
    sentence = sentence.split()
    res = []
    c = 1
    i = 0
    while i < len(sentence):
        if str(c) in sentence[i]:
            res.append(sentence[i])
            c += 1
            i = 0
        else:
            i += 1
    res = ' '.join(res)
    return res

print(order("is2 Thi1s T4est 3a"))