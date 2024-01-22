def array_diff(a, b):
    i = 0
    while i < len(b):
        if b[i] in a:
            a = [x for x in a if x != b[i]]
        i += 1
    return a


'''
def array_diff(a, b):
    i, j = 0, 0
    while i < len(b):
        while j < len(a):
            if b[i] == a[j]:
                a.pop(j)
                j = max(0, j - 1)  # Обновляем j после удаления элемента
            else:
                j += 1  # Переходим к следующему элементу в списке a
        j = 0  # Сбросим j до 0 перед следующим циклом i
        i += 1
    return a
'''

result = array_diff([1, 2, 2, 2, 3],[2])
print(result)
