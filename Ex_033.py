def persistence(n, count=0):
    # Проверяем, если число меньше 10, возвращаем текущее число и количество рекурсивных вызовов
    if n < 10:
        return count

    list_1 = []

    # Разбиваем число на цифры
    while n > 0:
        list_1.append(n % 10)
        n //= 10

    # Умножаем все цифры между собой
    mult = 1
    for i in list_1:
        mult *= i

    # Если результат больше 9, рекурсивно вызываем функцию с новым результатом и увеличиваем счетчик
    return persistence(mult, count + 1)


# Пример использования:
number = 999
result = persistence(number)
print(result)


