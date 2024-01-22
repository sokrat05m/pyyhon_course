

def queue_time(customers, n):
    if n == len(customers):
        return max(customers)
    if n == 1:
        return sum(customers)
    dict_1 = {}
    for i in range(1, n + 1):
        dict_1[i] = 0
    i = 0
    while len(customers) > 0:
        for k, v in dict_1.items():
            if v == min(dict_1.values()):
                minim = k
        dict_1[minim] += + customers[i]
        customers.pop(i)

    return max(dict_1.values())

b = queue_time([10,2,3,3], 2)
print(b)

