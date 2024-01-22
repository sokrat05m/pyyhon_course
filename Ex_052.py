strs = ["flower", "flow", "flight"]
length = len(strs)

b = min(strs, key=lambda x: len(x))
print(b)
i = 0
a = ''
count = 0
while i < len(b):
    a = a + b[i]
    list_1 = list(filter(lambda x: x.startswith(a), strs))
    i += 1
    if len(list_1) == length:
        count += 1
print(b[:count])