pattern = 'abba'
s = 'dog cat cat dog'
s = s.split()
d = {}
for i in range(len(pattern)):
    if pattern[i] not in d and s[i] not in d.values():
        d[pattern[i]] = s[i]
res = ''
for i in pattern:
    if i in d:
        res += d[i]
s = ''.join(s)
if res == s:
