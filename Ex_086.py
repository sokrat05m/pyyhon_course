def tribonacci(signature, n):
    i = 3
    while len(signature) < n:
        signature.append(sum(signature[i - 3:i]))
        i += 1
    return signature

