def is_prime (n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'no'
    return 'yes'


n = int(input('Введите число: '))
s = is_prime(n)
print(s)