number = 10
a = sum(set([i for i in range(2, number) if i % 3 == 0 or i % 5 == 0]))
print(a)