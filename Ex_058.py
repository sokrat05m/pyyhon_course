def check(s):
    vowels = 'ёуеыаоэяию'
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count

def same_by(characteristic, object):
    return len(set(list(map(characteristic, object)))) in (0, 1)


stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
list_1 = stroka.split()
if len(list_1) == 1:
    print('Количество фраз должно быть больше одной!')
elif same_by(check, list_1):
    print('Парам пам-пам')
else:
    print('Пам парам')
