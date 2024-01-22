'''
def f(a, b, n=1):
    if b == 1:
        return n * a
    else:
        n *= a
        return f(a, b - 1, n)
'''

def power_rec(a,b):
    if b == 1:
        return a
    return a * power_rec(a, b - 1)


print(power_rec(3, 5))


