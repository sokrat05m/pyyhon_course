def find_it(seq):
    dict_1 = {}
    for i in seq:
        if i not in dict_1:
            dict_1[i] = 1
        else:
            dict_1[i] += 1
    for k, v in dict_1.items():
        if v % 2 != 0:
            return k


print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))