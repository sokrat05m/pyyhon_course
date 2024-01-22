array_a = [1, 2, 3]
array_b = [4, 5, 6]
result = sum(list(map(lambda x: x ** 2, [array_b[i] - array_a[i] for i in range(len(array_b))]))) / len(array_b)
print(result)