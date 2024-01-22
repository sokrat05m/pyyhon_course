s = 'SokrAt'
res = ''
for i in range(len(s)):
    if s[i].isupper() and i != 0:
        res = res + '_' + s[i]
    else:
        res = res + s[i]
print(res.lower())