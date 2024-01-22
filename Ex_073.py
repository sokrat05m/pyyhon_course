strng = "56 65 74 100 99 68 86 180 90"
lst = list(map(int, strng.split()))
res = []
r = 0
for num in lst:
    while num > 0:
        r += num % 10
        num //= 10
    res.append(r)
    r = 0
res_str = ''
print(lst)
print(res)
while res:
    index = res.index(min(res))

    res_str = f'{res_str} {str(lst[index])}'
    res.pop(index)
    lst.pop(index)
print(res_str)
