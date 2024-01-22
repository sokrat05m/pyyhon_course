# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = 123123
numberLast = number % 1000
numberFirst = number // 1000
sumFirst = 0
while (numberFirst > 0):
    sumFirst = sumFirst + (numberFirst % 10)
    numberFirst = numberFirst // 10
sumLast = 0
while (numberLast > 0):
    sumLast = sumLast + (numberLast % 10)
    numberLast = numberLast // 10
if (sumFirst == sumLast):
    print ("yes")
else:
    print ("no")
