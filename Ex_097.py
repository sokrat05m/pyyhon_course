s = 'badc'
t = 'baba'
d = {}
# if len(s) != len(t):
#     print('f')
for i in range(len(s)):
    if s[i] not in d and t[i] not in d.values():
        d[s[i]] = t[i]
res = ''
for i in s:
    if i in d:
        res += d[i]
print(res)
