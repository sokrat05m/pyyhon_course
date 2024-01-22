def square_or_square_root(arr):
    list_res = []
    for i in arr:
        if float.is_integer(i ** 0.5):
            list_res.append(int(i ** 0.5))
        else:
            list_res.append(i ** 2)
    return list_res


list_1 = square_or_square_root([4, 3, 9, 7, 2, 1])
print(list_1)
