def dir_reduc(arr):
    n = 'north'
    s = 'south'
    w = 'west'
    e = 'east'

    i = 0
    while i < len(arr) - 1:
        if (arr[i] == n and arr[i + 1] == s) or (arr[i] == s and arr[i + 1] == n):
            arr.pop(i)
            arr.pop(i)
            i = max(0, i - 1)  # Возвращаемся назад на одну позицию после удаления

        elif (arr[i] == w and arr[i + 1] == e) or (arr[i] == e and arr[i + 1] == w):
            arr.pop(i)
            arr.pop(i)
            i = max(0, i - 1)  # Возвращаемся назад на одну позицию после удаления

        else:
            i += 1  # Переходим к следующей позиции в списке

    return arr


# Пример использования:


result = dir_reduc(["north", "south", "south", "east", "west", "north", "west"])
print(result)
