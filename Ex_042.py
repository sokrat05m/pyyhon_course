s = '1234'
rev = ''.join(reversed(s))
list_res = []
i, j = 0, 0
while i < len(s):
    list_res.append(s[i:] + s[:i])
    i += 1
i = 0
while i < len(rev):
    list_res.append(rev[i:] + rev[:i])
    i += 1
print(set(list_res))
