def unique_in_order(sequence):
    list_res = []
    if len(sequence) == 0:
        return list_res
    else:
        list_res.append(sequence[0])
        for i in range(len(sequence) - 1):
            if sequence[i] == sequence[i + 1]:
                pass
            else:
                list_res.append(sequence[i + 1])
        return list_res

result = unique_in_order('')
print(result)



