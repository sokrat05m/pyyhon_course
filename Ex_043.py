list_1 = [1, 3, 3, 3, 4]

list_res = [min(list_1) if i == max(list_1) else i for i in list_1]
print(list_res)