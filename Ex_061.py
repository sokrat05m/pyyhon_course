list_1 = []
n = 5
a0 = 0
a2 = 1
i = 1
while i <= n:
    ar = a0 + a2
    a0 = a2
    a2 = ar
    i += 1
print(ar)