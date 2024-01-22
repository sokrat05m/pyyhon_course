list_1 = [3, 3, 3, 4, 5]
k = 0
low = abs(list_1[0] - k)
low_print = low
i_print = 0
for i in range(len(list_1)):
    low = abs(list_1 [i] - k)
    if low_print > low:
        low_print = low
        i_print = i
print(list_1[i_print])