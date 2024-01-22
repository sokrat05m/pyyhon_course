def in_array(array1, array2):
    list_res = []
    for i in array1:
        for j in array2:
            if i in j:
                list_res.append(i)
    list_res = list(set(list_res))
    list_res.sort()
    return list_res


result = in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"])
print(result)