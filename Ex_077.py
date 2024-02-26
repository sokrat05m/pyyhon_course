def array_diff(a, b):
    res = [i for i in a if i not in b]
    return res


print(array_diff([1,2,2,2,3], [2]))

