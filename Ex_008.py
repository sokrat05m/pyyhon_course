# Сидим в терминале, пока не угадаем число
number = 150
switch = True
while (switch):
    guess = int (input('Введите число: '))
    if (number == guess):
        print('Вы угадали число')
        switch = False
    elif (number > guess):
        print('Ваше число меньше угадываемого')
    elif (number < guess):
        print('Ваше число больше угадываемого')
