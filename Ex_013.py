# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

n = 128
printed = 0
i = 2
k = 0
while printed < n:
    printed = i ** k
    k+=1
    if printed <= n:
        print(printed)