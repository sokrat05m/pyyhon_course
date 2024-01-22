k = 'ноутбук'

# Введите ваше решение ниже
k = k.upper ()
english_1 = "A, E, I, O, U, L, N, S, T, R"
english_2 = "D, G"
english_3 = "B, C, M, P"
english_4 = "F, H, V, W, Y"
english_5 = "K"
english_8 = "J, X"
english_10 = "Q, Z"

russian_1 = "А, В, Е, И, Н, О, Р, С, Т"
russian_2 = "Д, К, Л, М, П, У"
russian_3 = "Б, Г, Ё, Ь, Я"
russian_4 = "Й, Ы"
russian_5 = "Ж, З, Х, Ц, Ч "
russian_8 = "Ш, Э, Ю "
russian_10 = "Ф, Щ, Ъ"

count = 0
for i in k:
    for j in english_1:
        if i == j:
            count += 1
for i in k:
    for j in english_2:
        if i == j:
            count += 2
for i in k:
    for j in english_3:
        if i == j:
            count += 3
for i in k:
    for j in english_4:
        if i == j:
            count += 4
for i in k:
    for j in english_5:
        if i == j:
            count += 5
for i in k:
    for j in english_8:
        if i == j:
            count += 8
for i in k:
    for j in english_10:
        if i == j:
            count += 10
for i in k:
    for j in russian_1:
        if i == j:
            count += 1
for i in k:
    for j in russian_2:
        if i == j:
            count += 2
for i in k:
    for j in russian_3:
        if i == j:
            count += 3
for i in k:
    for j in russian_4:
        if i == j:
            count += 4
for i in k:
    for j in russian_5:
        if i == j:
            count += 5
for i in k:
    for j in russian_8:
        if i == j:
            count += 8
for i in k:
    for j in russian_10:
        if i == j:
            count += 10
print(count)