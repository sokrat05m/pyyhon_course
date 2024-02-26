signature = [1, 1, 1]
n = 10
i = 3
while len(signature) < n:
    signature.append(sum(signature[i-3:i]))
    i += 1

print(signature)